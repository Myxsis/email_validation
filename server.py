from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
mysql = MySQLConnector('emails')
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
app = Flask(__name__)
app.secret_key='blusuhhagherh'


@app.route('/')
def index():
	return render_template('index.html')

@app.route('/email', methods=['POST'])
def new():
	email = request.form['email']
	if not EMAIL_REGEX.match(request.form['email']):
		flash('You must enter a valid email address!')
		return redirect('/')
	else:
		flash('The email you entered is a valid email address! Thank you!')
		query= "INSERT INTO emails (emails, created_at, updated_at) VALUES ('{}', NOW(), NOW())".format(email)
		print query
		mysql.run_mysql_query(query)
		emails = mysql.fetch('SELECT * FROM emails')
		return render_template('success.html', emails=emails)
	# print query
	# mysql.run_mysql_query(query)
	# return redirect('/')


app.run(debug=True)