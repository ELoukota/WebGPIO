import datetime, json
from flask import Flask, render_template, request, redirect, Markup, make_response, url_for
from lib.cors import crossdomain
from lib.setup import zones, settings
from lib.GPIOSetup import GPIO
from lib.appliance import Appliance
from lib import authentication
from w1thermsensor import W1ThermSensor
import w1thermsensor
import mpu6050
from mpu6050 import mpu6050
from time import sleep
# from flask.logging import default_handler
# from logging.config import dictConfig

# dictConfig({
#     'version': 1,
#     'formatters': {'default': {
#         'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
#     }},
#     'handlers': {'wsgi': {
#         'class': 'logging.StreamHandler',
#         'stream': 'ext://flask.logging.wsgi_errors_stream',
#         'formatter': 'default'
#     }},
#     'root': {
#         'level': 'INFO',
#         'handlers': ['wsgi']
#     }
# })

app = Flask(__name__)

if settings['Mods']['EnableMPU6050'] == True:
	ModLevelEnabled = True
else:
	ModLevelEnabled = False

GridEnabled = True
LevelEnabled = True

try:
	acclsensor = mpu6050(0x68)
except:
	acclsensor = []
	LevelEnabled = False

my_scale = 100
samples = 5
deadZoneHi = 0.05
deadZoneLow = -0.05
AccelOffsetX = -575
AccelOffsetY = 25
AccelOffsetZ = 0


def updateLevel():
	loopz = 0
	ax = 0
	ay = 0
	if (LevelEnabled):
		while loopz < samples:
			accel_data = acclsensor.get_accel_data(False, AccelOffsetX, AccelOffsetY, AccelOffsetZ)
			ax = ax + accel_data['x']
			ay = ay + accel_data['y']
			sleep(.1)
			loopz = loopz + 1
		ax = ax / samples
		ay = ay / samples
		ax = round(ax,6)
		ay = round(ay,6)
		if ax < deadZoneHi and ax > deadZoneLow:
			ax = 0
		if ay < deadZoneHi and ay > deadZoneLow:
			ay = 0
		ax = ax * my_scale
		ay = ay * my_scale
		return {'x': ax, 'y': ay}
	else:
		return {'x': 0, 'y': 0}

def btnWatch():
	

def updateStates(zones):
	if (GridEnabled):
		for i, zone in enumerate(zones):
			for j, appliance in enumerate(zone['Appliances']):
				current_appliance = Appliance(appliance)
				zones[i]['Appliances'][j]['State'] = current_appliance.getState()
				if zones[i]['Appliances'][j]['Type'] == 'Temp':
					try: 
						sensor = W1ThermSensor(W1ThermSensor.THERM_SENSOR_DS18B20, zones[i]['Appliances'][j]['Address'])
						zones[i]['Appliances'][j]['Name'] = sensor.get_temperature()
					except:
						zones[i]['Appliances'][j]['Name'] = 'Not Found'
		return zones
	else:
		pass
	
@app.context_processor
def inject_enumerate():
    return dict(enumerate=enumerate)


@app.route("/")
@authentication.login_required
def home():
	now = datetime.datetime.now()
	timeString = now.strftime("%Y-%m-%d %I:%M %p")
	Data = updateLevel()
	Xret = Data['x']
	Yret = Data ['y']
	templateData = {
		'title' : settings['Title'],
		'time': timeString,
		'zones' : updateStates(zones),
		'Xvar' : int(Xret),
		'Yvar' : int(Yret),
		'refresh_rate' : settings['RefreshRate']*1000,
		'ModLevelEnabled' : ModLevelEnabled
	}
	return render_template('home.html', **templateData)

@app.route("/grid/")
@authentication.login_required
@crossdomain(origin='*')
def grid():
	templateData = {
		'title' : settings['Title'],
		'zones' : updateStates(zones)
	}
	return render_template('grid.html', **templateData)

@app.route("/level/")
@authentication.login_required
@crossdomain(origin='*')
def level():
	Data = updateLevel()
	Xret = Data['x']
	Yret = Data ['y']
	templateData = {
		'title' : settings['Title'],
		'Xvar' : int(Xret),
		'Yvar' : int(Yret)
	}
	return render_template('level.html', **templateData)

@app.route("/button/<int:zone_index>/<int:appliance_index>/")
@authentication.login_required
@crossdomain(origin='*')
def button(zone_index, appliance_index):
	appliance = Appliance(zones[zone_index]['Appliances'][appliance_index])
	appliance.executeAction()
	templateData = {
		'title' : settings['Title'],
		'type' : appliance.type,
		'state' : appliance.getState(),
		'zone_index' : zone_index,
		'appliance_index' : appliance_index,
		'name' : appliance.name
	}
	return render_template('button.html', **templateData)

@app.route("/toggle/<int:module>/<int:enabled>/")
@authentication.login_required
@crossdomain(origin='*')
def toggle(module, enabled):
	if module == 0:
		if enabled == 1:
			GridEnabled = True
		else:
			GridEnabled = False
	elif module == 1:
		if enabled == 1:
			LevelEnabled = True
		else:
			LevelEnabled = False
	else:
		pass
	return

@app.route("/login/")
def login():
	return render_template('login.html')

@app.route("/authenticate/", methods=['GET', 'POST'])
def auth():
	if request.method == 'POST':
		password = request.form['password']
		token = authentication.generateToken(password)
		if token:
			expiry_date = datetime.datetime.now() + datetime.timedelta(days=30)
			response = make_response(redirect(url_for('.home')))
			response.set_cookie('token', token, expires=expiry_date)
			return response
	return redirect(url_for('.login'))

@app.route("/logout/")
def logout():
	authentication.removeToken()
	response = make_response(redirect(url_for('.login')))
	response.set_cookie('token', '', expires=0)
	return response

if __name__ == "__main__":
	if settings['SSL']['Enabled']:
		app.run(host = settings['Host'], 
				port = settings['Port'], 
				threaded = settings['Threaded'], 
				debug = settings['Debug'], 
				ssl_context = (settings['cerPath'], settings['keyPath']))
	else:
		app.run(host = settings['Host'], 
				port = settings['Port'], 
				threaded = settings['Threaded'], 
				debug = settings['Debug'])