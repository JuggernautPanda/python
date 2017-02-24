#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  BookingServer.py
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

while 1:
	msgbox("Welcome to ABC Airlines server! Press ok to continue!")
	p1=sp.Popen(["./S"]).wait()
	
	msg = "Do you want to continue?"
	title = "Please Confirm"
	
	if ccbox(msg, title):     # show a Continue/Cancel dialog
		pass  # user chose Continue
	else:
		sys.exit(0)           # user chose Cancel
