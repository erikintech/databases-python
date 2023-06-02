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

# insert data into a table
sql = 'INSERT INTO airport (name, iata, icao, country, city) VALUES (%s, %s, %s, %s, %s)'
data = ('Mariscal Sucre International Airport','UIO', 'SEQM', 'Ecuador', 'Quito')
cursor.execute(sql, data)
db.commit()


