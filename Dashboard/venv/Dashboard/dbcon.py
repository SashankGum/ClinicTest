hostname = 'localhost'
username = 'postgres'
password = 'pass@123'
database = 'Test'

import psycopg2

def getCon():
	myConnection = psycopg2.connect( host=hostname, user=username, password=password, dbname=database )
	return myConnection

def closeCon(cur):
	cur.close()
