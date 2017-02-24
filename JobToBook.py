#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  JobToBook.py
#  
#  Copyright 2016 raja <raja@raja-Inspiron-N5110>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

# edit this file with your gmail id and password


import csv
import MySQLdb as mdb 
import smtplib

def Booking(uname,passwd,flightDate,flightName):
	
	sender = 'grajasumant@gmail.com'
	receivers = ['grajasumant@gmail.com']
	print "You are in Booking"
	con = mdb.connect('localhost', 'testuser', 'test623', 'testdb');
	cur = con.cursor()
	#cur.execute("DROP TABLE IF EXISTS Users")
	cur.execute("SELECT * FROM Users WHERE Username='%s'"%(uname))
	pwd = cur.fetchall()
	if (pwd == passwd):
		 
		cur.execute("CREATE TABLE IF NOT EXISTS Bookings(Id INT PRIMARY KEY AUTO_INCREMENT, Username VARCHAR(25), FlightName VARCHAR(512), FlightDate VARCHAR(512))")
		#sql="INSERT INTO Users(Username, Password) VALUES
		cur.execute("INSERT INTO Bookings(Username, FlightName, FlightDate) VALUES('%s','%s','%s')"%(uname,flightName,flightDate))
		cur.execute("SELECT * FROM Bookings WHERE Username='%s'"%(uname))
		rows = cur.fetchall()
		for row in rows:
			message ="Booked Flight with details"+flightDate
			fromaddr = 'fromadddrs@gmail.com'
			toaddrs  = 'toaddrs@gmail.com'
		
			username = 'username@gmail.com'
			password = 'xyz'
			server = smtplib.SMTP('smtp.gmail.com:587')
			server.ehlo()
			server.starttls()
			server.login(username,password)
			server.sendmail(fromaddr, toaddrs, message)
			server.quit()

		
	con.commit()
	con.close()

with open('/tmp/test.csv', 'rb') as f:
		reader = csv.reader(f)
		count = 0
		
	
		for row in reader:
			
			#print row
			if count == 0:
				uname = row
				count = count+1
				#print Func[0]
				#print type(Func)
			elif count == 1:
				PWD = row
				count = count+1
				#print uname
			elif count == 2:
				FDate = row
				count = count + 1
			elif count == 3:
				FName =row
				count = count + 1
			
			
		Booking(uname[0],PWD[0],FDate[0],FName[0])
