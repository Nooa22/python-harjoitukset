import mysql.connector

yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='1234',
    autocommit=True
)

maakoodi = input("Anna maakoodi: ")

kursori = yhteys.cursor()

sql = """
    SELECT type, COUNT(*)
    FROM airport
    WHERE iso_country = %s
    GROUP BY type
"""

kursori.execute(sql, (maakoodi,))

tulokset = kursori.fetchall()

for tyyppi, maara in tulokset:
    print(tyyppi, maara)

kursori.close()
yhteys.close()
