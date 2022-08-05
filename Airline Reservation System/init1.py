#Import Flask Library
from flask import Flask, render_template, request, session, url_for, redirect
import pymysql.cursors
import random
import string
from datetime import datetime
from flask_bcrypt import Bcrypt

app = Flask(__name__)
bcrypt = Bcrypt(app)
#Configure MySQL
conn = pymysql.connect(host='localhost',
                       user='root',
					   port = 3306,
                       password='root',
                       db='reserv',
                       charset='utf8mb4',
                       cursorclass=pymysql.cursors.DictCursor)

#Define a route to hello function

@app.route('/')
def hello():
	return render_template('index.html')

#Define route for login
@app.route('/loginCust')
def loginCust():
	return render_template('loginCust.php')

@app.route('/nologinsearchFlights')
def nologinsearchFlights():
	return render_template('nologinsearchFlights.php')

@app.route('/nologinsearchFlightStatus')
def nologinsearchFlightStatus():
	return render_template('nologinsearchFlightStatus.php')

@app.route('/loginStaff')
def loginStaff():
	return render_template('loginStaff.php')

#Define route for register
@app.route('/registerCust')
def registerCust():
	return render_template('registerCust.php')

@app.route('/registerStaff')
def registerStaff():
	return render_template('registerStaff.php')

@app.route('/viewmyFlights')
def viewmyFlights():
	username = session['username']
	return render_template('viewmyFlights.php')

@app.route('/searchforFlights')
def searchforFlights():
	username = session['username']
	return render_template('searchforFlights.php')

@app.route('/cancelTicket')
def cancelTicket():
	username = session['username']
	return render_template('cancelTicket.php', noinput = True)

@app.route('/ratecommentflight')
def ratecommentflight():
	username = session['username']
	return render_template('rateandcomment.php', noinput = True)

@app.route('/checktotalspent')
def checktotalspent():
	username = session['username']
	return render_template('checktotalspent.php')

@app.route('/staffairlineflights')
def staffairlineflights():
	username = session['username']
	airline = session['airline']
	return render_template('staffairlineflights.php')

@app.route('/createnewflight')
def createnewflight():
	username = session['username']
	airline = session['airline']
	return render_template('createnewflight.php')

@app.route('/changestatus')
def changestatus():
	username = session['username']
	airline = session['airline']
	return render_template('changestatus.php')

@app.route('/addairplane')
def addairplane():
	username = session['username']
	airline = session['airline']
	return render_template('addairplane.php')

@app.route('/addairport')
def addairport():
	username = session['username']
	airline = session['airline']
	return render_template('addairport.php')

@app.route('/viewcustomers')
def viewcustomers():
	username = session['username']
	airline = session['airline']
	cursor = conn.cursor()
	q1 = 'SELECT COUNT(ticket_id) as Total, cust_email FROM ticket WHERE airline_name = %s GROUP BY cust_email'
	cursor.execute(q1, (airline))
	data1 = cursor.fetchall()
	if(data1):
		maxnum = 0
		mostfreq = 0
		for i in data1:
			if int(i['Total']) > maxnum:
				maxnum = int(i['Total'])
		for i in data1:
			if int(i['Total']) == maxnum:
				mostfreq = i['cust_email']
		q3 = 'SELECT * FROM customer WHERE cust_email = %s'
		cursor.execute(q3,mostfreq)
		data3 = cursor.fetchone()
		if(q3):
			cursor.close()
			return render_template('viewcustomers.php', recentdate=maxnum, input=data3)
		else:
			error = 'Customer not Found'
			return render_template('viewcustomers.php', error = error)
	else:
		error = 'No Customers Found'
		return render_template('viewcustomers.php', error=error)

#Authenticates the login
@app.route('/loginAuthCust', methods=['GET', 'POST'])
def loginAuthCust():
	#grabs information from the forms
	username = request.form['username']
	password = request.form['password']
	#cursor used to send queries
	cursor = conn.cursor()
	#executes query
	q1 = 'SELECT * FROM login_cust WHERE cust_email = %s'
	cursor.execute(q1, username)
	d1 = cursor.fetchone()
	if(d1):
		if bcrypt.check_password_hash(d1['cust_password'], password) == True:
			cursor.close()
			error = None
				# creates a session for the the user
				# session is a built in
			session['username'] = username
			return redirect(url_for('home'))
		else:
			error = 'Invalid password'
			return render_template('loginCust.php', error=error)
	else:
		error = 'Invalid username'
		return render_template('loginCust.php', error=error)


@app.route('/loginAuthStaff', methods=['GET', 'POST'])
def loginAuthStaff():
	#grabs information from the forms
	username = request.form['username']
	password = request.form['password']
	airline = request.form['airline']
	#cursor used to send queries
	cursor = conn.cursor()
	#executes query
	q1 = 'SELECT * FROM login_staff WHERE staff_username = %s'
	cursor.execute(q1, username)
	d1 = cursor.fetchone()
	if(d1):
		q2 = 'SELECT * FROM airline_staff WHERE staff_username = %s and airline_name = %s'
		cursor.execute(q2, (username, airline))
		d2 = cursor.fetchone()
		if(d2):
			if bcrypt.check_password_hash(d1['staff_password'], password) == True:
				cursor.close()
				error = None
					#creates a session for the the user
					#session is a built in
				session['username'] = username
				session['airline'] = airline
				return redirect(url_for('homeforStaff'))
			else:
				error = 'Invalid password'
				return render_template('loginStaff.php', error=error)
		else:
			error = 'Invalid Input'
			return render_template('loginStaff.php', error=error)
	else:
		error = 'Invalid username'
		return render_template('loginStaff.php', error=error)

#Authenticates the register
@app.route('/registerAuthCust', methods=['GET', 'POST'])
def registerAuthCust():
	#grabs information from the forms
	username = request.form['username']
	password = request.form['password']
	login_id = string.digits
	login_id = ''.join(random.choice(login_id) for i in range(80))
	#cursor used to send queries
	cursor = conn.cursor()
	#executes query
	query = 'SELECT * FROM login_cust WHERE cust_email = %s'
	cursor.execute(query, (username))
	#stores the results in a variable
	data = cursor.fetchone()
	#use fetchall() if you are expecting more than 1 data row
	error = None
	if(data):
		#If the previous query returns data, then user exists
		error = "This user already exists"
		return render_template('registerCust.php', error = error)
	else:
		ins = 'INSERT INTO customer VALUES(%s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
		cursor.execute(ins, (username, None, None, None, None,None, None,None, None,None, None))
		ins2 = 'INSERT INTO login_cust VALUES(%s, %s, %s)'
		cursor.execute(ins2, (login_id, username, bcrypt.generate_password_hash(password)))
		conn.commit()
		cursor.close()
		return render_template('index.html')

@app.route('/registerAuthStaff', methods=['GET', 'POST'])
def registerAuthStaff():
	#grabs information from the forms
	username = request.form['username']
	password = request.form['password']
	airline = request.form['airline']
	email = request.form['email']
	login_id = string.digits
	login_id = ''.join(random.choice(login_id) for i in range(80))
	#cursor used to send queries
	cursor = conn.cursor()
	#executes query
	query = 'SELECT * FROM login_staff WHERE staff_username = %s'
	cursor.execute(query, (username))
	#stores the results in a variable
	data = cursor.fetchone()
	#use fetchall() if you are expecting more than 1 data row
	error = None
	if(data):
		#If the previous query returns data, then user exists
		error = "This user already exists"
		return render_template('registerStaff.php', error = error)
	else:
		ins4 = 'SELECT * FROM airline WHERE airline_name = %s'
		cursor.execute(ins4,(airline))
		data2 = cursor.fetchone()
		if not data2:
			ins3 = 'INSERT INTO airline VALUE(%s)'
			cursor.execute(ins3,(airline))
			conn.commit()
		ins = 'INSERT INTO airline_staff VALUES(%s,%s,%s,%s,%s)'
		cursor.execute(ins, (username, None, None,None, airline))
		ins3 = 'INSERT INTO email VALUES(%s)'
		cursor.execute(ins3, (email))
		ins4 = 'INSERT INTO staff_email VALUES(%s,%s)'
		cursor.execute(ins4, (username, email))
		ins2 = 'INSERT INTO login_staff VALUES(%s, %s, %s)'
		cursor.execute(ins2, (login_id, username, bcrypt.generate_password_hash(password)))
		conn.commit()
		cursor.close()
		return render_template('index.html')

@app.route('/NologinsearchFlights', methods=['GET', 'POST'])
def NologinsearchFlights():
	#grabs information from the forms
	departureAirport = request.form['departureAirport']
	arrivalAirport = request.form['arrivalAirport']
	departureDate = request.form['departureDate']
	returnDate = request.form['returnDate']

	#cursor used to send queries
	cursor = conn.cursor()
	#executes query
	error = None
	if (returnDate == ''):
		query = 'SELECT * FROM flight WHERE departure_airport = %s AND arrival_airport = %s AND departure_date = %s AND departure_date > NOW()'
		cursor.execute(query, (departureAirport, arrivalAirport, departureDate))
		#stores the results in a variable
		data1 = cursor.fetchall()
		if (data1):
			cursor.close()
			return render_template('nologinsearchFlights.php', posts=data1)
		else:
			error = "No flights found"
			return render_template('nologinsearchFlights.php', error=error)
	elif (returnDate != ''):
		query = 'SELECT * FROM flight WHERE departure_airport = %s AND arrival_airport = %s AND departure_date = %s AND return_date = %s AND departure_date > NOW()'
		cursor.execute(query, (departureAirport, arrivalAirport, departureDate, returnDate))
		# stores the results in a variable
		data1 = cursor.fetchall()
		if data1:
			cursor.close()
			return render_template('nologinsearchFlights.php', posts=data1, here = 'here')
		else:
			error = "No flights found"
			return render_template('nologinsearchFlights.php', error=error)
	#use fetchall() if you are expecting more than 1 data row

@app.route('/NologinsearchFlightStatus', methods=['GET', 'POST'])
def NologinsearchFlightStatus():
	airline = request.form['airline']
	flightNumber = request.form['flightNumber']
	departureDate = request.form['departureDate']

	# cursor used to send queries
	cursor = conn.cursor()
	# executes query
	error = None
	query = 'SELECT * FROM flight WHERE airline_name = %s AND flight_number = %s AND departure_date = %s'
	cursor.execute(query, (airline, flightNumber, departureDate))
	# stores the results in a variable
	data1 = cursor.fetchone()
	if (data1):
		cursor.close()
		return render_template('nologinsearchFlightStatus.php', status=data1)
	else:
		error = "No flights found"
		return render_template('nologinsearchFlightStatus.php', error=error)

@app.route('/determinemyFlights', methods=['GET', 'POST'])
def determinemyFlights():
	username = session['username']
	airline = request.form['airline']
	departureAirport = request.form['departureAirport']
	arrivalAirport = request.form['arrivalAirport']
	startingDate = request.form['from']
	toDate = request.form['to']
	cursor = conn.cursor()
	if airline == '' and departureAirport == '' and arrivalAirport == '' and startingDate == '' and toDate == '':
		q1 = 'SELECT * FROM flight NATURAL JOIN ticket WHERE departure_date_time > NOW() AND cust_email = %s'
		cursor.execute(q1, username)
		data1 = cursor.fetchall()
		if (data1):
			cursor.close()
			return render_template('viewmyFlights.php', Input = data1)
		else:
			error = "No future flights"
			return render_template('viewmyFlights.php', error=error)
	else:
		q1 = 'SELECT * FROM flight NATURAL JOIN ticket WHERE airline_name = %s AND departure_airport = %s AND arrival_airport = %s AND cust_email = %s'
		cursor.execute(q1, (airline, departureAirport, arrivalAirport, username))
		data1 = cursor.fetchall()
		data2 = []
		if (data1):
			for line in data1:
				if (line['departure_date'] >= startingDate and line['departure_date'] <= toDate):
					data2.append(line)
			if not data2:
				error = "No flights found"
				return render_template('viewmyFlights.php', error=error)
			cursor.close()
			return render_template('viewmyFlights.php', Input = data2)
		else:
			error = "No flights found"
			return render_template('viewmyFlights.php', error=error)

@app.route('/searchFlightsforCust', methods=['GET', 'POST'])
def searchFlightsforCust():
	username = session['username']
	departureAirport = request.form['departureAirport']
	arrivalAirport = request.form['arrivalAirport']
	departureDate = request.form['from']
	returnDate = request.form['to']
	cursor = conn.cursor()
	if returnDate == '':
		q1 = 'SELECT * FROM flight WHERE departure_date_time > NOW() AND departure_airport = %s AND arrival_airport = %s AND departure_date = %s'
		cursor.execute(q1, (departureAirport, arrivalAirport, departureDate))
		data1 = cursor.fetchall()
		if (data1):
			cursor.close()
			return render_template('searchforFlights.php', Input=data1)
		else:
			error = "No future flights"
			return render_template('searchforFlights.php', error=error)
	else:
		q1 = 'SELECT * FROM flight WHERE departure_date_time > NOW() AND departure_airport = %s AND arrival_airport = %s AND departure_date = %s AND return_date = %s'
		cursor.execute(q1, (departureAirport, arrivalAirport, departureDate, returnDate))
		data1 = cursor.fetchall()
		if (data1):
			cursor.close()
			return render_template('searchforFlights.php', Input=data1)
		else:
			error = "No future flights"
			return render_template('searchforFlights.php', error=error)

@app.route('/purchaseflight', methods=['GET', 'POST'])
def purchaseflight():
	username = session['username']
	airline = request.form['airline']
	flightnumber = request.form['flightnumber']
	cardnum = request.form['cardnum']
	cardname = request.form['cardname']
	expdate = request.form['expdate']
	cardtype = request.form['cardtype']
	cursor = conn.cursor()
	if(cardtype != 'credit') and (cardtype != 'debit'):
		error = 'Card Type is Wrong'
		return render_template('searchforFlights.php', error = error)
	ticketid = string.ascii_letters
	ticketid = ''.join(random.choice(ticketid) for i in range(15))
	m1 = 'SELECT * FROM ticket WHERE cust_email = %s AND airline_name = %s AND flight_number = %s'
	cursor.execute(m1, (username, airline, flightnumber))
	check = cursor.fetchone()
	if(check):
		error = "Ticket has already been purchased"
		return render_template('searchforFlights.php', error=error)
	q1 = 'SELECT * FROM flight WHERE departure_date_time > NOW() AND airline_name = %s AND flight_number = %s'
	cursor.execute(q1, (airline, flightnumber))
	data1 = cursor.fetchone()
	if (data1):
		q2 = 'SELECT COUNT(*) as Total FROM ticket WHERE flight_number = %s'
		cursor.execute(q2, flightnumber)
		data2 = cursor.fetchone()
		q3 = 'SELECT num_seats FROM flight NATURAL JOIN airplane WHERE flight_number = %s'
		cursor.execute(q3, flightnumber)
		data3 = cursor.fetchone()
		if (data3):
			salesprice = data1['base_price']
			seatsleft = data3['num_seats'] - data2['Total']
			ratioseats = 1 - (seatsleft/data3['num_seats'])
			if(seatsleft == 0):
				error = 'Flight is Full'
				return render_template('searchforFlights.php', error = error)
			if (ratioseats >= 0.60):
				salesprice = data1['base_price'] + (data1['base_price'] * 0.20)
			q5 = 'SELECT * FROM flight NATURAL JOIN ticket WHERE airline_name = %s AND flight_number = %s AND cust_email IS NULL AND card_number IS NULL'
			cursor.execute(q5, (airline, flightnumber))
			data4 = cursor.fetchone()
			now = datetime.now()
			dtstring = now.strftime("%Y-%m-%d %H:%M:%S")
			dtstring = dtstring[:10]
			if (data4):
				q6 = 'UPDATE ticket SET cust_email = %s, sold_price = %s, card_number = %s, card_name = %s, exp_date = %s, purchase_date_time = %s, card_type = %s, purchase_date = %s WHERE ticket_id = %s AND airline_name = %s AND flight_number = %s'
				cursor.execute(q6,(username, salesprice, cardnum, cardname, expdate, now, cardtype, dtstring, data4['ticket_id'], airline, flightnumber))
				ins2 = 'INSERT INTO attempt_purchase VALUES(%s,%s,%s,%s,%s,%s)'
				cursor.execute(ins2, (
				username, data4['ticket_id'], cardnum, cardname, expdate,
				datetime.now()))
				conn.commit()
				cursor.close()
				return render_template('afterpurchase.html')
			else:
				ins = 'INSERT INTO ticket VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
				cursor.execute(ins, (ticketid, username, airline, flightnumber, salesprice,cardnum, cardname, expdate, now, cardtype,dtstring))
				ins2 = 'INSERT INTO attempt_purchase VALUES(%s,%s,%s,%s,%s,%s)'
				cursor.execute(ins2, (username, ticketid, cardnum, cardname, expdate, datetime.now()))
				conn.commit()
				cursor.close()
				return render_template('afterpurchase.html')
		else:
			error = "Flight Number is incorrect"
			return render_template('searchforFlights.php', error=error)
	else:
		error = "Airline or Flight Number is incorrect"
		return render_template('searchforFlights.php', error=error)

@app.route('/cancelmyTicket', methods=['GET', 'POST'])
def cancelmyTicket():
	username = session['username']
	airline = request.form['airline']
	flight_number = request.form['flightnumber']
	cursor = conn.cursor()
	q1 = 'SELECT * FROM flight NATURAL JOIN ticket WHERE departure_date_time > DATE_ADD(NOW(), interval 1 day) AND cust_email = %s AND airline_name = %s AND flight_number = %s'
	cursor.execute(q1, (username, airline, flight_number))
	data1 = cursor.fetchall()
	if (data1):
			q3 = 'DELETE FROM attempt_purchase WHERE ticket_id = %s'
			for i in data1:
				cursor.execute(q3, i['ticket_id'])
			conn.commit()
			ins = 'SELECT * FROM ticket WHERE cust_email = %s AND airline_name = %s AND flight_number = %s'
			cursor.execute(ins, (username, airline, flight_number))
			data2 = cursor.fetchone()
			if(data2):
				q2 = 'UPDATE ticket SET cust_email = NULL, sold_price = NULL, card_number = NULL, card_name = NULL, exp_date = NULL, purchase_date_time = NULL, card_type = NULL, purchase_date = NULL WHERE cust_email = %s AND airline_name = %s AND flight_number = %s'
				cursor.execute(q2, (username, airline, flight_number))
				ins2 = 'SELECT * FROM cancel_ticket WHERE cust_email = %s AND ticket_id = %s'
				cursor.execute(ins2, (username, data2['ticket_id']))
				data3 = cursor.fetchone()
				if not (data3):
					q3 = 'INSERT INTO cancel_ticket VALUES(%s,%s)'
					cursor.execute(q3,(data2['ticket_id'], username))
					conn.commit()
				cursor.close()
				return render_template('cancelTicket.php', input=True)
	else:
		error = "Flight not found"
		return render_template('cancelTicket.php', error=error)

@app.route('/ratecommentFlight', methods=['GET', 'POST'])
def ratecommentFlight():
	username = session['username']
	airline = request.form['airline']
	flight_number = request.form['flightnumber']
	departureAirport = request.form['departureAirport']
	arrivalAirport = request.form['arrivalAirport']
	rating = request.form['rating']
	comment = request.form['comment']
	cursor = conn.cursor()
	q1 = 'SELECT * FROM flight NATURAL JOIN ticket WHERE departure_date_time < NOW() AND cust_email = %s AND airline_name = %s AND flight_number = %s AND departure_airport = %s AND arrival_airport = %s'
	cursor.execute(q1, (username, airline, flight_number, departureAirport, arrivalAirport))
	data1 = cursor.fetchone()
	if (data1):
		q2 = 'SELECT * FROM login_cust WHERE cust_email = %s'
		cursor.execute(q2, username)
		data2 = cursor.fetchone()
		if(data2):
			q4 = 'SELECT * FROM create_review WHERE ticket_id = %s AND cust_email = %s'
			cursor.execute(q4,(data1['ticket_id'],username))
			data3 = cursor.fetchone()
			if (data3):
				q5 = 'UPDATE create_review SET cust_comment = %s, cust_rating = %s WHERE ticket_id = %s AND cust_email = %s'
				cursor.execute(q5, (comment, rating, data1['ticket_id'],username))
				conn.commit()
			else:
				q3 = 'INSERT INTO create_review VALUES(%s,%s,%s,%s,%s,%s)'
				cursor.execute(q3, (data1['ticket_id'], username, data2['login_id'], data2['cust_password'], comment, rating))
				conn.commit()
			cursor.close()
			return render_template('rateandcomment.php', input=True)
	else:
		error = "Flight not found"
		return render_template('rateandcomment.php', noinput = True, error=error)

@app.route('/checkTotalSpent', methods=['GET', 'POST'])
def checkTotalSpent():
	username = session['username']
	start = request.form['start']
	to = request.form['to']
	cursor = conn.cursor()
	if start == '' and to == '':
		q1 = 'SELECT SUM(sold_price) as Total FROM ticket WHERE purchase_date_time >= DATE_SUB(NOW(), INTERVAL 1 YEAR) AND cust_email = %s'
		cursor.execute(q1,(username))
		data1 = cursor.fetchone()
		if(data1):
			dicofdics = {}
			for i in range((int(datetime.today().year))-1, int(datetime.today().year) + 1):
				dic = {}
				q2 = 'SELECT MONTH(purchase_date) as Month,SUM(sold_price) as Total from ticket WHERE cust_email = %s AND purchase_date >= date_sub(NOW(), INTERVAL 6 MONTH) AND SUBSTRING(purchase_date,1,4) = %s group by MONTH(purchase_date)'
				cursor.execute(q2, (username, i))
				data2 = cursor.fetchall()
				if(data2):
					months = {1: 'Jan', 2: 'Feb', 3: 'Mar',4:'Apr', 5: 'May', 6: 'June', 7: 'July',8:'Aug',9: 'Sep', 10: 'Oct', 11: 'Nov',12:'Dec'}
					for j in data2:
						j['Month'] = months[j['Month']]
						dic[j['Month']] = j['Total']
					dicofdics[i] = dic
			if len(dicofdics) == 0:
				error = "No Flights Found: Total is $0"
				return render_template('checktotalspent.php', error=error)
			else:
				cursor.close()
				return render_template('checktotalspent.php', firstinput = data1, secondinput = True, fourthinput = dicofdics)
		else:
			error = "No Flights Found: Total is $0"
			return render_template('checktotalspent.php', error=error)
	else:
		q1 = 'SELECT SUM(sold_price) as Total FROM ticket WHERE purchase_date >= %s AND purchase_date <= %s GROUP BY cust_email HAVING cust_email = %s'
		cursor.execute(q1, (start, to, username))
		data1 = cursor.fetchone()
		startyear = str(start)[:4]
		endyear = str(to)[:4]
		if (data1):
			dicofdics = {}
			for i in range(int(startyear), int(endyear) + 1):
				dic = {}
				q2 = 'SELECT MONTH(purchase_date) as Month,sum(sold_price) as Total from ticket WHERE cust_email = %s AND purchase_date >= %s AND purchase_date <= %s AND SUBSTRING(purchase_date,1,4) = %s group by MONTH(purchase_date)'
				cursor.execute(q2, (username, start, to, i))
				data2 = cursor.fetchall()
				if (data2):
					months = {1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'June', 7: 'July', 8: 'Aug', 9: 'Sep',
							  10: 'Oct', 11: 'Nov', 12: 'Dec'}
					for j in data2:
						j['Month'] = months[j['Month']]
						dic[j['Month']] = j['Total']
					dicofdics[i] = dic
			if len(dicofdics) == 0:
				error = 'No Flights Found: Total is $0'
				return render_template('checktotalspent.php', error=error)
			else:
				cursor.close()  # 2000: {April:3,Sep:4}
				return render_template('checktotalspent.php', fifthinput=data1, thirdinput=True, fourthinput=dicofdics)
		else:
			error = "No Flights Found: Total is $0"
			return render_template('checktotalspent.php', error=error)

@app.route('/staffairlineFlights', methods=['GET', 'POST'])
def staffairlineFlights():
	username = session['username']
	airline = session['airline']
	departureAirport = request.form['departureAirport']
	arrivalAirport = request.form['arrivalAirport']
	start = request.form['from']
	to = request.form['to']
	cursor = conn.cursor()
	if departureAirport == '' and arrivalAirport == '' and start == '' and to == '':
		q1 = 'SELECT * FROM flight WHERE departure_date_time >= NOW() AND departure_date_time <= DATE_ADD(NOW(), INTERVAL 30 DAY) AND airline_name = %s'
		cursor.execute(q1, airline)
		data1 = cursor.fetchall()
		if(data1):
			q2 = 'SELECT * FROM flight NATURAL JOIN ticket NATURAL JOIN customer WHERE departure_date_time >= NOW() AND departure_date_time <= DATE_ADD(NOW(), INTERVAL 30 DAY) AND airline_name = %s'
			cursor.execute(q2, airline)
			data2 = cursor.fetchall()
			if(q2):
				cursor.close()
				return render_template('staffairlineflights.php', customerlist = data2, input=data1)
			else:
				error = 'No Customers'
				return render_template('staffairlineflights.php', error = error)
		else:
			error = "No Future Flights found"
			return render_template('staffairlineflights.php', error=error)
	else:
		q1 = 'SELECT * FROM flight WHERE departure_date >= %s AND departure_date <= %s AND airline_name = %s AND departure_airport = %s AND arrival_airport = %s'
		cursor.execute(q1, (start, to, airline, departureAirport, arrivalAirport))
		data1 = cursor.fetchall()
		if (data1):
			q2 = 'SELECT * FROM flight NATURAL JOIN ticket NATURAL JOIN customer WHERE departure_date_time >= %s AND departure_date_time <= %s AND airline_name = %s AND departure_airport = %s AND arrival_airport = %s'
			cursor.execute(q2, (start, to, airline, departureAirport, arrivalAirport))
			data2 = cursor.fetchall()
			if (q2):
				cursor.close()
				return render_template('staffairlineflights.php', customerlist=data2, input=data1)
			else:
				error = 'No Customers'
				return render_template('staffairlineflights.php', error=error)
		else:
			error = "No Future Flights found"
			return render_template('staffairlineflights.php', error=error)

@app.route('/createnewFlight', methods=['GET', 'POST'])
def createnewFlight():
	username = session['username']
	airline = session['airline']
	flight_number = request.form['flightNumber']
	departuredatetime = request.form['departuredatetime']
	departureAirport = request.form['departureAirport']
	arrivalAirport = request.form['arrivalAirport']
	arrivaldatetime = request.form['arrivaldatetime']
	airplaneid = request.form['airplaneid']
	baseprice = request.form['baseprice']
	status = request.form['status']
	departdate = request.form['departdate']
	returndate = request.form['returndate']
	cursor = conn.cursor()
	if flight_number == '' and departureAirport == '' and arrivalAirport == '' and departuredatetime == '' and arrivaldatetime == '' and baseprice == '' and status == '' and departdate == '' and returndate == '':
		q1 = 'SELECT * FROM flight WHERE departure_date_time >= NOW() AND departure_date_time <= DATE_ADD(NOW(), INTERVAL 30 DAY) AND airline_name = %s'
		cursor.execute(q1, airline)
		data1 = cursor.fetchall()
		if(data1):
			cursor.close()
			return render_template('createnewflight.php', input=data1)
		else:
			error = "No Future Flights found"
			return render_template('createnewflight.php', error=error)
	else:
		if(returndate == ''):
			returndate = None
		q5 = 'SELECT * FROM airplane WHERE id_num = %s'
		cursor.execute(q5,(airplaneid))
		idcheck = cursor.fetchone()
		if(idcheck):
			q3 = 'SELECT * FROM airport WHERE airport_name = %s'
			cursor.execute(q3, (departureAirport))
			data3 = cursor.fetchone()
			q4 = 'SELECT * FROM airport WHERE airport_name = %s'
			cursor.execute(q4, (arrivalAirport))
			data4 = cursor.fetchone()
			if (data3) and (data4):
				ins = 'SELECT * FROM login_staff WHERE staff_username = %s'
				cursor.execute(ins, username)
				login = cursor.fetchone()
				if (login):
					q1 = 'SELECT * FROM flight WHERE airline_name = %s AND flight_number = %s'
					cursor.execute(q1, (airline, flight_number))
					data1 = cursor.fetchone()
					if (data1):
						error = 'Flight already exists'
						return render_template('createnewflight.php', error=error)
					q2 = 'INSERT INTO flight VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
					cursor.execute(q2, (
					airline, flight_number, departuredatetime, departureAirport, arrivalAirport, arrivaldatetime, baseprice,
					airplaneid, status, departdate, returndate))
					conn.commit()
					q2 = 'INSERT INTO create_set_price VALUES(%s,%s,%s,%s,%s,%s,%s)'
					cursor.execute(q2, (login['login_id'],login['staff_password'], username,flight_number, airline, departuredatetime, baseprice))
					conn.commit()
					cursor.close()
					return render_template('createnewflight.php',success = True)
				else:
					error = 'Login Error'
					return render_template('createnewflight.php', error=error)
			else:
				error = 'Airports are not registered'
				return render_template('createnewflight.php', error=error)

		else:
			error = 'Airplane ID is incorrect'
			return render_template('createnewflight.php', error=error)

@app.route('/changeflightstatus', methods=['GET', 'POST'])
def changeflightstatus():
	username = session['username']
	airline = session['airline']
	flight_number = request.form['flightNumber']
	departuredate = request.form['departuredate']
	departureAirport = request.form['departureAirport']
	arrivalAirport = request.form['arrivalAirport']
	newstatus = request.form['newstatus']
	newstatus = newstatus.lower()
	if newstatus != 'on-time' and newstatus != 'delayed' and newstatus != 'cancelled':
		error = 'Input is not a Valid Status'
		return render_template('changestatus.php', error=error)
	cursor = conn.cursor()
	ins = 'SELECT * FROM login_staff WHERE staff_username = %s'
	cursor.execute(ins, username)
	login = cursor.fetchone()
	if (login):
		q1 = 'SELECT * FROM flight WHERE departure_date = %s AND flight_number = %s AND departure_airport = %s AND arrival_airport = %s'
		cursor.execute(q1, (departuredate, flight_number, departureAirport, arrivalAirport))
		data1 = cursor.fetchone()
		if (data1):
			q3 = 'SELECT * FROM set_flight_status WHERE staff_username = %s AND flight_number = %s AND airline_name = %s'
			cursor.execute(q3, (username, flight_number, airline))
			data3 = cursor.fetchone()
			if (data3):
				q2 = 'UPDATE set_flight_status SET new_status = %s WHERE staff_username = %s AND flight_number = %s AND airline_name = %s'
				cursor.execute(q2, (newstatus, username, flight_number, airline))
				conn.commit()
			else:
				q2 = 'INSERT INTO set_flight_status VALUES(%s,%s,%s,%s,%s,%s,%s)'
				cursor.execute(q2, (login['login_id'], username, login['staff_password'], flight_number, airline, data1['departure_date_time'], newstatus))
				conn.commit()
			q2 = 'UPDATE flight SET flight_status = %s WHERE departure_date = %s AND flight_number = %s AND departure_airport = %s AND arrival_airport = %s'
			cursor.execute(q2, (newstatus, departuredate, flight_number, departureAirport, arrivalAirport))
			conn.commit()
			cursor.close()
			return render_template('changestatus.php', success = True)
		else:
			error = "No Flight found"
			return render_template('changestatus.php', error=error)
	else:
		error = 'Login error'
		return render_template('changestatus.php', error=error)

@app.route('/addAirplane', methods=['GET', 'POST'])
def addAirplane():
	username = session['username']
	airline = session['airline']
	idnum = request.form['idnum']
	numseats = request.form['numseats']
	comp = request.form['comp']
	age = request.form['age']
	cursor = conn.cursor()
	ins = 'SELECT * FROM login_staff WHERE staff_username = %s'
	cursor.execute(ins, username)
	login = cursor.fetchone()
	if (login):
		q1 = 'SELECT * FROM airplane WHERE (id_num = %s AND airline_name = %s) OR id_num = %s'
		cursor.execute(q1, (idnum, airline,idnum))
		data1 = cursor.fetchone()
		if (data1):
			error = "Airplane already exists"
			return render_template('addairplane.php', error=error)
		q2 = 'INSERT INTO airplane VALUES(%s,%s,%s,%s,%s)'
		cursor.execute(q2, (airline, idnum, numseats, comp, age))
		conn.commit()
		ins2 = 'INSERT INTO add_airplane VALUES(%s, %s, %s, %s, %s)'
		cursor.execute(ins2, (login['login_id'], username, login['staff_password'], airline, idnum))
		conn.commit()
		q3 = 'SELECT * FROM airplane WHERE airline_name = %s'
		cursor.execute(q3,(airline))
		data2 = cursor.fetchall()
		if(q3):
			cursor.close()
			return render_template('addairplane.php', input = data2, success = True)
		else:
			error = 'No Airplanes in the System'
			return render_template('addairplane.php', error=error)
	else:
		error = 'Login error'
		return render_template('addairplane.php', error=error)

@app.route('/addAirport', methods=['GET', 'POST'])
def addAirport():
	username = session['username']
	airline = session['airline']
	airport = request.form['airportname']
	city = request.form['city']
	country = request.form['country']
	type = request.form['type']
	type = type.lower()
	if type != 'domestic' and type != 'international' and type != 'domestic/international':
		error = 'Input is not a Valid Type'
		return render_template('addairport.php', error=error)
	cursor = conn.cursor()
	ins = 'SELECT * FROM login_staff WHERE staff_username = %s'
	cursor.execute(ins, username)
	login = cursor.fetchone()
	if (login):
		q1 = 'SELECT * FROM airport WHERE airport_name = %s'
		cursor.execute(q1, airport)
		data1 = cursor.fetchone()
		if (data1):
			error = "Airport already exists"
			return render_template('addairport.php', error=error)
		q2 = 'INSERT INTO airport VALUES(%s,%s,%s,%s)'
		cursor.execute(q2, (airport, city, country, type))
		conn.commit()
		ins2 = 'INSERT INTO add_airport VALUES(%s, %s, %s, %s)'
		cursor.execute(ins2, (login['login_id'], username, login['staff_password'], airport))
		conn.commit()
		cursor.close()
		return render_template('addairport.php', success = True)
	else:
		error = 'Login error'
		return render_template('addairport.php', error=error)

@app.route('/viewRatings', methods=['GET', 'POST'])
def viewRatings():
	username = session['username']
	airline = session['airline']
	cursor = conn.cursor()
	q1 = 'SELECT flight_number, SUM(cust_rating) / COUNT(cust_rating) as Average FROM ticket NATURAL JOIN create_review WHERE airline_name = %s GROUP BY flight_number'
	cursor.execute(q1, airline)
	data1 = cursor.fetchall()
	if(data1):
		q2 = 'SELECT flight_number, ticket_id, cust_email, cust_comment, cust_rating FROM ticket NATURAL JOIN create_review WHERE airline_name = %s'
		cursor.execute(q2, airline)
		data2 = cursor.fetchall()
		return render_template('viewratings.html', input = data1, input2 = data2)
	else:
		error = "No Reviews Found"
		return render_template('viewratings.html', error=error)

@app.route('/viewCustomers', methods=['GET', 'POST'])
def viewCustomers():
	username = session['username']
	airline = session['airline']
	custemail = request.form['custemail']
	cursor = conn.cursor()
	q1 = 'SELECT * FROM ticket NATURAL JOIN flight NATURAL JOIN customer WHERE cust_email = %s and airline_name = %s and departure_date_time < NOW()'
	cursor.execute(q1, (custemail, airline))
	data1 = cursor.fetchall()
	if (data1):
		cursor.close()
		return render_template('viewcustomers.php', custemail = custemail, customerlist = data1)
	else:
		error = "No Flights found"
		return render_template('viewcustomers.php', error=error)

@app.route('/viewReports', methods=['GET', 'POST'])
def viewReports():
	username = session['username']
	airline = session['airline']
	start = request.form['start']
	to = request.form['to']
	cursor = conn.cursor()
	q1 = 'SELECT COUNT(ticket_id) as Total FROM ticket WHERE airline_name = %s AND purchase_date >= %s AND purchase_date <= %s'
	cursor.execute(q1, (airline, start, to))
	data1 = cursor.fetchone()
	startyear = str(start)[:4]
	endyear = str(to)[:4]
	if (data1):
		dicofdics = {}
		for i in range(int(startyear), int(endyear) + 1):
			dic = {}
			q2 = 'SELECT MONTH(purchase_date) as Month,count(ticket_id) as Total FROM ticket WHERE airline_name = %s AND purchase_date >= %s AND purchase_date <= %s AND SUBSTRING(purchase_date,1,4) = %s group by MONTH(purchase_date)'
			cursor.execute(q2, (airline, start, to, i))
			data2 = cursor.fetchall()
			if (data2):
				months = {1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'June', 7: 'July', 8: 'Aug', 9: 'Sep',
						  10: 'Oct', 11: 'Nov', 12: 'Dec'}
				for j in data2:
					j['Month'] = months[j['Month']]
					dic[j['Month']] = j['Total']
				dicofdics[i] = dic
		if len(dicofdics) == 0:
			error = 'No Tickets Found. $0'
			return render_template('viewreports.php', error = error)
		else:
			cursor.close() #2000: {April:3,Sep:4}
			return render_template('viewreports.php', input = data1, input2 = dicofdics)
	else:
		error = "No Tickets found. $0"
		return render_template('viewreports.php', error=error)

@app.route('/home')
def home():
	username = session['username']
	return render_template('home.html')

@app.route('/addemail')
def addemail():
	username = session['username']
	airline = session['airline']
	return render_template('addemail.php')

@app.route('/addnumber')
def addnumber():
	username = session['username']
	airline = session['airline']
	return render_template('addnumber.php')

@app.route('/homeforStaff')
def homeforStaff():
	username = session['username']
	airline = session['airline']
	return render_template('homeforStaff.html')

@app.route('/viewreports')
def viewreports():
	username = session['username']
	airline = session['airline']
	return render_template('viewreports.php')

@app.route('/changeBasePrice')
def changeBasePrice():
	username = session['username']
	airline = session['airline']
	return render_template('changebaseprice.php', input = True)

@app.route('/flightstatuscount')
def flightstatuscount():
	username = session['username']
	airline = session['airline']
	return render_template('flightstatuscount.php')

@app.route('/changebaseprice', methods=['GET', 'POST'])
def changebaseprice():
	username = session['username']
	airline = session['airline']
	flight_number = request.form['flightNumber']
	newprice = request.form['newprice']
	cursor = conn.cursor()
	ins = 'SELECT * FROM login_staff WHERE staff_username = %s'
	cursor.execute(ins, username)
	login = cursor.fetchone()
	if (login):
		q1 = 'SELECT * FROM flight WHERE airline_name = %s AND flight_number = %s'
		cursor.execute(q1, (airline, flight_number))
		data1 = cursor.fetchone()
		if not (data1):
			error = 'Flight doesnt exist'
			return render_template('changebaseprice.php', error=error)
		q2 = 'UPDATE flight SET base_price = %s WHERE flight_number = %s AND airline_name = %s'
		cursor.execute(q2, (newprice, flight_number, airline))
		conn.commit()
		q3 = 'SELECT * FROM create_set_price WHERE staff_username = %s AND flight_number = %s AND airline_name = %s'
		cursor.execute(q3, (username, flight_number, airline))
		data3 = cursor.fetchone()
		if not (data3):
			q4 = 'INSERT INTO create_set_price VALUES(%s,%s,%s,%s,%s,%s,%s)'
			cursor.execute(q4, (
			login['login_id'], login['staff_password'], username, flight_number, airline, data1['departure_date_time'], newprice))
			conn.commit()
		else:
			q4 = 'UPDATE create_set_price SET base_price = %s WHERE staff_username = %s AND flight_number = %s AND airline_name = %s'
			cursor.execute(q4, (newprice, username, flight_number, airline))
			conn.commit()
		cursor.close()
		return render_template('changebaseprice.php', success = True)
	else:
		error = 'Login error'
		return render_template('changebaseprice.php', error=error)
@app.route('/viewrevenue')
def viewrevenue():
	username = session['username']
	airline = session['airline']
	cursor = conn.cursor()
	q1 = 'SELECT SUM(sold_price) as TotalMonth FROM ticket WHERE airline_name = %s AND purchase_date_time >= DATE_SUB(NOW(), INTERVAL 1 MONTH)'
	cursor.execute(q1, airline)
	data1 = cursor.fetchone()
	if(data1):
		q2 = 'SELECT SUM(sold_price) as TotalYear FROM ticket WHERE airline_name = %s AND purchase_date_time >= DATE_SUB(NOW(), INTERVAL 1 YEAR)'
		cursor.execute(q2, airline)
		data2 = cursor.fetchone()
		if(data2):
			cursor.close()
			return render_template('viewrevenue.html',input = data1, input2 = data2)
		else:
			cursor.close()
			return render_template('viewrevenue.html', input=data1)
	else:
		q2 = 'SELECT SUM(sold_price) as TotalYear FROM ticket WHERE airline_name = %s AND purchase_date_time >= DATE_SUB(NOW(), INTERVAL 1 YEAR)'
		cursor.execute(q2, airline)
		data2 = cursor.fetchone()
		if (data2):
			cursor.close()
			return render_template('viewrevenue.html', input2=data2)
		else:
			cursor.close()
			return render_template('viewrevenue.html')

@app.route('/addEmail', methods=['GET', 'POST'])
def addEmail():
	username = session['username']
	airline = session['airline']
	newemail = request.form['newemail']
	cursor = conn.cursor()
	q1 = 'SELECT * FROM email WHERE email_staff = %s'
	cursor.execute(q1, (newemail))
	data1 = cursor.fetchone()
	if(data1):
		error = "Email already registered"
		return render_template('addemail.php', error=error)
	else:
		ins = 'INSERT INTO email VALUES(%s)'
		cursor.execute(ins, newemail)
		ins4 = 'INSERT INTO staff_email VALUES(%s,%s)'
		cursor.execute(ins4, (username, newemail))
		conn.commit()
		cursor.close()
		return render_template('addemail.php', Input=True)

@app.route('/addNumber', methods=['GET', 'POST'])
def addNumber():
	username = session['username']
	airline = session['airline']
	newnumber = request.form['newnumber']
	cursor = conn.cursor()
	q1 = 'SELECT * FROM phone_number WHERE staff_phone_num = %s'
	cursor.execute(q1, (newnumber))
	data1 = cursor.fetchone()
	if(data1):
		error = "Number already registered"
		return render_template('addnumber.php', error=error)
	else:
		ins = 'INSERT INTO phone_number VALUES(%s)'
		cursor.execute(ins, newnumber)
		ins4 = 'INSERT INTO staff_phone VALUES(%s,%s)'
		cursor.execute(ins4, (username, newnumber))
		conn.commit()
		cursor.close()
		return render_template('addnumber.php', Input=True)

@app.route('/flightstatusCount', methods=['GET', 'POST'])
def flightstatusCount():
	username = session['username']
	airline = session['airline']
	status = request.form['status']
	cursor = conn.cursor()
	if status != 'on-time' and status != 'delayed' and status != 'cancelled' and status != 'on time':
		error = 'Status is invalid'
		return render_template('flightstatuscount.php', error = error)
	q1 = 'SELECT COUNT(*) as Total, flight_status FROM flight WHERE airline_name = %s and flight_status = %s'
	cursor.execute(q1, (airline, status))
	data1 = cursor.fetchone()
	if data1['Total'] != 0:
		cursor.close()
		return render_template('flightstatuscount.php', Input = data1)
	else:
		error = 'No Flights With That Status Found'
		return render_template('flightstatuscount.php', error = error)

@app.route('/logout')
def logout():
	session.pop('username')
	return redirect('/')

@app.route('/logoutStaff')
def logoutStaff():
	session.pop('username')
	session.pop('airline')
	return redirect('/')
		
app.secret_key = 'some key that you will never guess'

if __name__ == "__main__":
	app.run('127.0.0.1', 5000, debug = True)
