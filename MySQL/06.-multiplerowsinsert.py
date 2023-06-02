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
data = [
    ('Changi International Airport', 'SIN', 'WSSS', 'Singapore', 'Singapore'),
    ('Doha Hamad International Airport', 'DOH', 'OTHH', 'Qatar', 'Doha')
]

# insert multiple rows
cursor.executemany(sql, data)
db.commit()