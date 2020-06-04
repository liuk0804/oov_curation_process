from flask import render_template, request
from app import app
import curation
import wtforms


@app.route('/') 
def homepage():
	name = request.args.get('name') 
	return render_template('homepage.html', name=name)


@app.route('/app') 
def run_msg():
	message = request.args.get('message') 
	return render_template('app.html', name=message)


@app.route('/usertest', methods=['GET', 'POST']) 
def msg_view():
# the methods that handle requests are called views, in flask msg = ''
# form is a dictionary like attribute that holds the form data if request.method == 'POST':
	msg = request.form["message"]
	return render_template('index.html', message=msg)