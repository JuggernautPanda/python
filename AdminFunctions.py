#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  AdminFunctions.py
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

import csv
import hashlib # Used to encrypt the password in md5.


	
print "Enter admin credentials"
username=raw_input("username:")
passwd=raw_input("password:")

md5_object = hashlib.md5()
md5_object.update(passwd.encode('utf-8'))
PWD = md5_object.hexdigest()

with open('/tmp/AdminAuth.csv', 'rb') as f:
	reader = csv.reader(f)
	count = 0
	for row in reader:
		if count == 0:
			un=row
			count = count+1
		elif count == 1:
			pwd=row
			count = count + 1
	
	if (username==un[0]):
		if(passwd==pwd[0]): # if(PWD==pwd): should be present because password should be encrypted. Testing purpose
			print "Welcome admin. What do you want to do?"
			print "If you want to Add Flight, enter Add"
			print "If you want to Delete Flight, enter Delete"
			func_whatToDo = raw_input("Add\Delete")
			if (func_whatToDo == "Add"):
				flightName = raw_input("Enter Flight Name")
				flightDate = raw_input("Enter Flight Date")
				MYSQLquery = "INSERT INTO FlightsData(FlightName,Date) VALUES('"+flightName+','+"'"+flightDate+"'"+')'
				#print MYSQLquery 
				
				p2=sp.Popen(["./C_AdminFunctions",MYSQLquery])
				
			elif (func_whatToDo == "Delete"):
				flightName = raw_input("Enter Flight Name")
				flightDate = raw_input("Enter Flight Date")
				MYSQLquery = "DELETE FROM FlightsData WHERE FlightName='"+flightName+"'"+" AND Date='"+flightDate
				#print MYSQLquery 
				p3=sp.Popen(["./C_AdminFunctions",MYSQLquery])
				
			
				
	
	
	


