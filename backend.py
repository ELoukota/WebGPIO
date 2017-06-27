from flask import Flask, render_template, redirect, Markup
import RPi.GPIO as GPIO
import subprocess, os, datetime, time
app = Flask(__name__)


roomName = ['Bed Room', 'Server Room']
accName= [['Fan', 'Front Light', 'Back Light', 'Bright Light'], ['Champ']]
outPin = [[6, 13, 19, 26],[]]

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

for i in range(len(outPin)):
	GPIO.setup(outPin[i], GPIO.OUT, initial=GPIO.HIGH)

def accState(roomNumber, accNumber):
	if roomNumber == 0:
		if GPIO.input(outPin[roomNumber][accNumber]) is 1:
			return 'containerOff'
		else:
			return 'containerOn'
	elif roomNumber > 0:
		#get the state of other accesories in other rooms
		return 'containerOff'

@app.route("/")
def main():
	now = datetime.datetime.now()
	timeString = now.strftime("%Y-%m-%d %I:%M %p")

	passer = ''
	for i in range(len(roomName)):
		passer = passer + "<p class='roomtitle'>%s</p>" % (roomName[i])
		for j in range(len(accName[i])):
			buttonHtmlName = accName[i][j].replace(" ", "<br>")
			passer = passer + "<span id='button%d%d'><button class='%s' onclick='toggle(%d,%d)'>%s</button></span>" % (i, j, accState(i,j), i, j, buttonHtmlName)

	buttonGrid = Markup(passer)
	templateData = {
		'title' : 'WebGPIO',
		'time': timeString,
		'buttons' : buttonGrid
	}
	return render_template('main.html', **templateData)

@app.route("/button/<int:roomNumber>/<int:accNumber>/")
def toggle(roomNumber, accNumber):
	if len(outPin[roomNumber]) != 0:
		state= not GPIO.input(outPin[roomNumber][accNumber])
		GPIO.output(outPin[roomNumber][accNumber],state)
		#subprocess.call(['./echo.sh'], shell=True)
	else:
		#action for other rooms
		subprocess.call(['./echo.sh'], shell=True)
	#print(roomNumber, accNumber)
	buttonHtmlName = accName[roomNumber][accNumber].replace(" ", "<br>")
	passer="<button class='%s' onclick='toggle(%d,%d)'>%s</button>" % (accState(roomNumber,accNumber), roomNumber, accNumber, buttonHtmlName)
	return passer


if __name__ == "__main__":
   app.run(host='0.0.0.0', port=8000, debug=True)
