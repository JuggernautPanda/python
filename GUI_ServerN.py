#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  GUI_Server.py
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

from easygui import * #Using easygui(tkinter) for creating interactive gui
import hashlib # Used to encrypt the password in md5.
import sys # importing system to make system calls.
import socket # socket programming involved to communicate between server and client.
import _mysql
import MySQLdb as mdb # DB is required so the python uses MySQLdb.
import subprocess as sp
import csv

def UserLogin():
	
	server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server_socket.bind(("", 5000))
	server_socket.listen(5)
	with open('/tmp/test.csv', 'rb') as f:
		reader = csv.reader(f)
		count = 0
		for row in reader:
			
			if count == 0:
				Func = row
				count = count+1
			elif count == 1:
				uname = row
				count = count+1
			elif count == 2:
				passwd == row 
	
	p3=sp.Popen(["rm","-rf","/tmp/test.csv"])
	#msgbox("Hello, please enter your login details.")
	con = mdb.connect('localhost', 'testuser', 'test623', 'testdb');
	cur = con.cursor()
	cur.execute("SELECT * FROM Users WHERE Username = %s"%(uname))
	temp=cur.fetchall()
	con.close()
	for tem in temp:
	#	print row 
		if (tem == passwd):
			#msgbox("Hello"+uname)
			while True:
				client_socket, address = server_socket.accept()
				client_socket.send("Userprofile")
				#print('Server received', repr(data))
				con = mdb.connect('localhost', 'testuser', 'test623', 'Userdb');
				cur = con.cursor()
				cur.execute("SELECT * FROM ListOfFlights") #sends flights and date
				flightDates = cur.fetchall()
				con.commit()
				con.close()
				client_socket.send(flightDates)
		
				UserInsert()
			#Userprofile()
		else:
			msgbox("Wrong username or password!")
	
	
#Note: Register should be present in server. This is for testing purpose only
def Register(uname,passwd):
	#print uname,passwd
	
	print uname, passwd
				
	con = mdb.connect('localhost', 'testuser', 'test623', 'testdb');
	cur = con.cursor()
	#cur.execute("DROP TABLE IF EXISTS Users")
	cur.execute("CREATE TABLE IF NOT EXISTS Users(Id INT PRIMARY KEY AUTO_INCREMENT, Username VARCHAR(25), Password VARCHAR(25))")
	#sql="INSERT INTO Users(Username, Password) VALUES
	cur.execute("INSERT INTO Users(Username, Password) VALUES('%s','%s')"%(uname,passwd))
	cur.execute("SELECT * FROM Users")
	rows = cur.fetchall()
	con.commit()
	con.close()
	#for row in rows:
	#	print row


def Userprofile(): # send a file to the client authenticating it to use a user profile
	server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server_socket.bind(("", 5000))
	server_socket.listen(5)
	while True:
		client_socket, address = server_socket.accept()
		client_socket.send("Userprofile")
		#print('Server received', repr(data))
		con = mdb.connect('localhost', 'testuser', 'test623', 'Userdb');
		cur = con.cursor()
		cur.execute("SELECT * FROM ListOfFlights") #sends flights and date
		flightDates = cur.fetchall()
		con.commit()
		con.close()
		client_socket.send(flightDates)
		
		UserInsert()
	
def UserInsert():
	
	server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server_socket.bind(("", 5000))
	server_socket.listen(5)
	client_socket, address = server_socket.accept()
	while 1:
		
		data = client_socket.recv(1024)
		con = mdb.connect('localhost', 'testuser', 'test623', 'Userdb');
		cur = con.cursor()
		cur.execute("CREATE TABLE IF NOT EXISTS Bookings(Id INT PRIMARY KEY AUTO_INCREMENT, FlightName VARCHAR(25), DOJ VARCHAR(25), Name VARCHAR(25), Address VARCHAR(25) ,Zipcode VARCHAR(25))")
		cur.execute("INSERT INTO Bookings(FlightName,DOJ,Name,Address,Zipcode) VALUES(%s,%s,%s,%s,%s)"%(data[0],data[1],data[2],data[3],data[4]))
		con.commit()
		con.close()
	
def AdminLogin():
	
	with open('/tmp/test.csv', 'rb') as f:
		reader = csv.reader(f)
		count = 0
		for row in reader:
			if count == 0:
				uname = row
				count = 1
			else:
				passwd = row 
	
	#msgbox("Hello, please enter your login details.")
	con = mdb.connect('localhost', 'testuser', 'test623', 'Admindb');
	cur = con.cursor()
	cur.execute("SELECT * FROM Users WHERE Username = %s"%(uname))
	temp=cur.fetchall()
	con.close()
	for tem in temp:
	#	print row 
		if (tem == passwd):
			#msgbox("Hello"+uname)
			AdminProfile()
		else:
			msgbox("Wrong username or password!")
			
def AdminProfile():
	server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server_socket.bind(("", 5000))
	server_socket.listen(5)
	while 1:
    
		client_socket, address = server_socket.accept()
		sql_command = client_socket.recv(1024)
		con = mdb.connect('localhost', 'testuser', 'test623', 'Admindb');
		cur = con.cursor()
		cur.execute(sql_command)
		con.close()
		
while 1:
	msgbox("Welcome to ABC Airlines server! Press ok to continue!")
	p1=sp.Popen(["./S"])
	with open('tmp/test.csv', 'rb') as f:
		reader = csv.reader(f)
		count = 0
	
		for row in reader:
			
			#print row
			if count == 0:
				Func = row
				count = count+1
				print Func
			elif count == 1:
				uname = row
				count = count+1
				print uname
			elif count == 2:
				passwd = row 
				print passwd
		
		if (Func[0] == '1'):
			UserLogin(uname,passwd)
		elif (Func[0] == '2'):
			Register(uname,passwd)
		elif (Func[0] == '3'):
			AdminLogin(uname,passwd)
 	
	msg = "Do you want to continue?"
	title = "Please Confirm"
	
	if ccbox(msg, title):     # show a Continue/Cancel dialog
		pass  # user chose Continue
	else:
		sys.exit(0)           # user chose Cancel
