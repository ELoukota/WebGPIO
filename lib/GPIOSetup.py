from lib.setup import zones, settings

if settings['Make'] == 'OrangePi':
	import OPi.GPIO as GPIO
else:
	import RPi.GPIO as GPIO

if settings['GPIOMode'] == 'BOARD':
	GPIO.setmode(GPIO.BOARD)
else:
	GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

def initialState(active_value):
	if active_value == 0:
		return GPIO.HIGH
	else:
		return GPIO.LOW

for zone in zones:
	for Appliance in zone['Appliances']:
		if Appliance['Type'] == 'GPIO':
			initial_state = initialState(Appliance['ActiveState'])
			GPIO.setup(Appliance['Pin'],
					   GPIO.OUT, 
					   initial= initial_state)