import mysql.connector
# connection creation
db = mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	password = 'narutoRamen.95',
    database = 'airportdb',
	port = '3306'
)
# cursor creation
cursor = db.cursor()

# verify if a table exists
cursor.execute('SHOW TABLES')
tables = cursor.fetchall()

for table in tables:
    print(table)