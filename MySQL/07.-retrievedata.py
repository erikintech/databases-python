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

# insert multiple rows
cursor.execute('SELECT id, name, iata, icao, country, city FROM airport')
airports = cursor.fetchall()
for airport in airports:
    print(airport)