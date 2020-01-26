from flask import Flask, render_template, request, redirect, url_for, make_response
import motors
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
app = Flask(__name__) #start flask

@app.route('/') #index.html
def index():

	return render_template('index.html')

@app.route('/<changepin>', methods=['POST'])
def reroute(changepin):

	changePin = int(changepin) #changepin to int
	
	if changePin == 1:
		motors.frontleft()
	elif changePin == 2:
		motors.front()
	elif changePin == 3:
		motors.frontright()
	elif changePin == 4:
		motors.left()
	elif changePin == 5:
		motors.stop()
	elif changePin == 6:
		motors.right()
	elif changePin == 7:
		motors.backleft()
	elif changePin == 8:
		motors.back()
	elif changePin == 9:
		motors.backright()
	else:
		motors.stop()

	response = make_response(redirect(url_for('index')))
	return(response)

app.run(debug=True, host='0.0.0.0', port=8090)
