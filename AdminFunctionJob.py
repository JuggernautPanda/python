#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  AdminFunctionJob.py
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
import _mysql
import MySQLdb as mdb # DB is required so the python uses MySQLdb.

def AdminExecute(query):
	con = mdb.connect('localhost', 'testuser', 'test623', 'Admindb');
	cur = con.cursor()
	cur.execute("%s"%(query))

with open('/tmp/AdminFunctions.csv', 'rb') as f:
		reader = csv.reader(f)
		count = 0
		
	
		for row in reader:
			
			#print row
			if count == 0:
				query = row
				count = count+1
		
		AdminExecutable(query)




