import subprocess, time, datetime
from lib.GPIOSetup import GPIO
from lib.setup import settings
from w1thermsensor import W1ThermSensor

class Appliance:

	def __init__(self, attributes):
		self.attributes = attributes
		self.name = attributes['Name']
		self.type = attributes['Type']
		if self.type == 'GPIO':
			self.pin = attributes['Pin']
			self.active = attributes['ActiveState']
		if self.type == 'BTN':
			self.pin = attributes['Pin']
			self.active = attributes['ActiveState']
			self.duration = attributes['Duration']
			self.trigertime = datetime.now(tzinfo=None)
		if self.type == 'Script':
			if 'Timeout' in attributes:
				self.timeout = "timeout "+str(attributes['Timeout'])+" "
			else:
				self.timeout = "timeout 0.2 "
			self.status_cmd = self.timeout + attributes['Status']
			if 'Action' in attributes:
				self.action = True
				self.on_cmd = attributes['Action'][True]
				self.off_cmd = attributes['Action'][False]
			else:
				self.action = False
		if self.type == 'Temp':
			if 'Timeout' in attributes:
				self.timeout = int(attributes['Timeout'])
			else:
				self.timeout = 1
			self.address = attributes['Address']

	def getState(self):
		if self.type == 'GPIO':
			if GPIO.input(self.pin) is self.active:
				return 1
			else:
				return 0
		elif self.type == 'BTN':
			if GPIO.input(self.pin) is self.active:
				self.triggered = 1
				self.trigertime = datetime.timedelta(seconds=self.duration) datetime.now(tzinfo=None)
				return 1
			elif self.triggered == 1:
				return 1
			else:
				return 0
		elif self.type == 'Temp':
			try: 
				sensor = W1ThermSensor(W1ThermSensor.THERM_SENSOR_DS18B20, self.address)
				return 1
			except:
				return 0
		else:
			returnCode = subprocess.call([self.status_cmd], shell=True)
			if returnCode == 0:
				return 1
			return 0

	def setState(self, state):
		if self.type == 'GPIO':
			if state > 1:
				original_state= GPIO.input(self.pin)
				new_state = 1 - original_state
			else:
				new_state = 1 - self.active - state
			GPIO.output(self.pin, new_state)
		if GPIO.input(self.pin) is self.active:
			return 1
		else:
			return 0

	def executeAction(self):
		if self.type == 'GPIO':
			original_state= GPIO.input(self.pin)
			new_state = 1 - original_state
			GPIO.output(self.pin, new_state)
			if 'Duration' in self.attributes:
				time.sleep(self.attributes['Duration'])
				GPIO.output(self.pin, original_state)
		if self.type == 'BTN':
			self.triggered = False
		if self.type == 'Script' and self.action:
			if self.getState():
				subprocess.call([self.off_cmd], shell=True)
			else:
				subprocess.call([self.on_cmd], shell=True)
		if self.type == 'Temp':
			sensor = W1ThermSensor(W1ThermSensor.THERM_SENSOR_DS18B20, self.address)
			self.name = sensor.get_temperature()
