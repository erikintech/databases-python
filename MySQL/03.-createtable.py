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

# create table
cursor.execute("""CREATE TABLE airport(
    id int AUTO_INCREMENT NOT NULL,
    name VARCHAR(60),
    iata VARCHAR(3),
    icao VARCHAR(8),
    country VARCHAR(35),
    city VARCHAR(35),
    PRIMARY KEY (id)
)
""")
