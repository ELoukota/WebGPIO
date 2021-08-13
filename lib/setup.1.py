import os, sys, yaml

configPath = os.path.join(sys.path[0], "config.yml")
try:
	with open(configPath, 'r') as ymlfile:
	    cfg = yaml.load(ymlfile)
except Exception:
	print("Config file not found or invalid. Please provide a valid config.yml file. See exampleconfig.yml for reference")
	exit()

try:
	groups = cfg['Groups']
except Exception:
	print("config.yml file is not valid. See exampleconfig.yml for reference")
	exit()

#check for older config file
for i, group in enumerate(groups):
	if 'Accesories' in group:
		groups[i]['Appliances'] = groups[i]['Accesories']
		groups[i].pop('Accesories', None)
		print("Use Appliances instead of Accesories in config.yml")

if 'Settings' in cfg:
	settings = cfg['Settings']
else:
	settings = {}

if 'Host' not in settings:
	settings['Host'] = '0.0.0.0' 

if 'Port' not in settings:
	settings['Port'] = 8000

if 'Threaded' not in settings:
	settings['Threaded'] = False 

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
	#settings['GPIOMode'] = "BOARD"

if 'Make' not in settings:
	settings['Make'] = "RaspberryPi"


if 'Inverted' in settings:
	GlobalActiveState = 1 - int(settings['Inverted'])
else:
	GlobalActiveState = 1

for i, group in enumerate(groups):
	for j, Appliance in enumerate(group['Appliances']):
		if 'Inverted' in Appliance:
			groups[i]['Appliances'][j]['ActiveState'] = 1 - int(Appliance['Inverted'])
		else:
			groups[i]['Appliances'][j]['ActiveState'] = GlobalActiveState