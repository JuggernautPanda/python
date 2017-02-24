#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Login.py
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

from easygui import *
import hashlib

def Login(uname,passwd):
	p2=sp.Popen(["./C_Booking",uname,passwd])
	p3=sp.Popen(["./fileTransferReceive","5000"])
	

while 1:
	
	msgbox("Welcome to ABC Airlines! Press ok to continue!")
	DB_Con()
	msg ="Please make a choice."
	title = "Login/Register"
	choices = ["Booking", "AdminLogin","Register/Sign Up"]
	choice = choicebox(msg, title, choices)
	# note that we convert choice to string, in case
	# the user cancelled the choice, and we got None.
	msgbox("You chose: " + str(choice), "Redirecting...")
	
	# if - else statements go here according to the choice
	if choice=="Booking" :
		
		msgbox("Please Login!")
		msg = "Enter your User Name and Password"
		title = "Login Page"
		fieldNames = ["UserName","Password"]
		fieldValues = []  # we start with blanks for the values
		fieldValues = multpasswordbox(msg,title, fieldNames)
		md5_object = hashlib.md5()
		md5_object.update(fieldNames[1].encode('utf-8'))
		PWD = md5_object.hexdigest() # This is the md5 encrypted password.
		#msgbox("Hello, please enter your login details.")
		while 1:
			if fieldValues == None: break
			errmsg = ""
			for i in range(len(fieldNames)):
				if fieldValues[i].strip() == "":
					errmsg = errmsg + ('"%s" is a required field.\n\n' % fieldNames[i])
			if errmsg == "": break # no problems found
			fieldValues = multpasswordbox(errmsg, title, fieldNames, fieldValues)
		msg = "Make a choice"
		title = "Welcome to Flight Selection!"
		FlightChoice = multchoicebox(msg,title,FlightData)
		print FlightChoice
		Login(fieldValues[0],PWD,FlightChoice)	
	
	
	msg = "Do you want to continue?"
	title = "Please Confirm"
	if ccbox(msg, title):     # show a Continue/Cancel dialog
		pass  # user chose Continue
	else:
		sys.exit(0)           # user chose Cancel
