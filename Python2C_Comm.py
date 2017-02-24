#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Python2C_Comm.py
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
#  '\xdcd~\xb6^g\x11\xe1U7R\x18!+9d')
#  

import subprocess as sp
import MySQLdb as mdb

uname='graja'
hi='hello'
p=sp.Popen(["./ex", hi]).wait()
print p

##con = mdb.connect('localhost', 'testuser', 'test623', 'testdb');
##cur = con.cursor()
#DBS ="SELECT * FROM Users WHERE Username = "
#cur.execute("SELECT * FROM Users WHERE Username = 'graja'")
##cur.execute("SELECT * FROM Users WHERE Username = '%s'"%(uname))
##rows=cur.fetchall()
##con.close()
##for row in rows:
	##print row 

