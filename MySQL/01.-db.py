import mysql.connector

# connection creation
db = mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	password = 'narutoRamen.95',
	port = '3306'
)

# cursor creation
cursor = db.cursor()

# create a database
cursor.execute( 'CREATE DATABASE airportdb' )



