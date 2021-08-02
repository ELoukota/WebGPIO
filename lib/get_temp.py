import os,sys
from w1thermsensor import W1ThermSensor


#W1ThermSensor(W1ThermSensor.THERM_SENSOR_DS18B20, "'+ attributes['Status'] + '").get_temperature()


if  len(sys.argv) < 2:
    sensor = W1ThermSensor()
    temperature_in_celsius = sensor.get_temperature()
else:
    sensor_address = sys.argv[1]
    sensor = W1ThermSensor(W1ThermSensor.THERM_SENSOR_DS18B20, sensor_address)
    temperature_in_celsius = sensor.get_temperature()

print(temperature_in_celsius)
 #return temperature_in_celsius
