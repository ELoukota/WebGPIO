import os, sys, yaml

acclData = []

configPath = os.path.join(sys.path[0], "config.yml")
try:
	with open(configPath, 'r') as ymlfile:
	    cfg = yaml.safe_load(ymlfile)
except Exception:
	print("Config file not found or invalid. Please provide a valid config.yml file. See exampleconfig.yml for reference")
	exit()

try:
	zones = cfg['Zones']
except Exception:
	print("config.yml file is not valid. See exampleconfig.yml for reference")
	exit()

#check for older config file
for i, zone in enumerate(zones):
	if 'Accesories' in zone:
		zones[i]['Appliances'] = zones[i]['Accesories']
		zones[i].pop('Accesories', None)
		print("Use Appliances instead of Accesories in config.yml")

if 'Settings' in cfg:
	settings = cfg['Settings']
else:
	settings = {}

if 'Title' not in settings:
	settings['Title'] = 'Default'

if 'Host' not in settings:
	settings['Host'] = '0.0.0.0' 

if 'Port' not in settings:
	settings['Port'] = 8000

if 'Threaded' not in settings:
	settings['Threaded'] = True 

if 'Debug' not in settings:
	settings['Debug'] = False 

if 'SSL' in settings:
	if 'Path' in settings['SSL']:
		if settings['SSL']['Path'] != 'default':
			settings['cerPath']=settings['SSL']['Path'] + settings['SSL']['Certificate']
			settings['keyPath']=settings['SSL']['Path'] + settings['SSL']['Key']
	else:
		settings['cerPath']=os.path.join(sys.path[0], settings['SSL']['Certificate'])
		settings['keyPath']=os.path.join(sys.path[0],  settings['SSL']['Key'])
else:
	settings['SSL']= { 'Enabled': False }

if 'RefreshRate' not in settings:
	settings['RefreshRate'] = 5

if 'GPIOMode' not in settings:
	settings['GPIOMode'] = "BCM"

if 'Make' not in settings:
	settings['Make'] = "RaspberryPi"

if 'Inverted' in settings:
	GlobalActiveState = 1 - int(settings['Inverted'])
else:
	GlobalActiveState = 1

for i, zone in enumerate(zones):
	for j, Appliance in enumerate(zone['Appliances']):
		if 'Inverted' in Appliance:
			zones[i]['Appliances'][j]['ActiveState'] = 1 - int(Appliance['Inverted'])
		else:
			zones[i]['Appliances'][j]['ActiveState'] = GlobalActiveState

if 'Mods' in settings:
	if 'EnableMPU6050' not in settings['Mods']:
		settings['Mods']['EnableMPU6050'] = False
	if 'EnableDallasTempature' not in settings['Mods']:
		settings['Mods']['EnableDallasTempature'] = False
else:
	settings['Mods']['EnableMPU6050'] = False
	settings['Mods']['EnableDallasTempature'] = False