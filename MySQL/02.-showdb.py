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

# verify if a database exists
cursor.execute('SHOW DATABASES')
dbs = cursor.fetchall()
for db in dbs:
    print(db)