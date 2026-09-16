import mysql.connector

yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='1234',
    autocommit=True
)

icao = input("Anna lentoaseman ICAO-koodi: ")

kursori = yhteys.cursor()

sql = """
    SELECT name, municipality
    FROM airport
    WHERE ident = %s
"""

kursori.execute(sql, (icao,))

tulos = kursori.fetchone()

if tulos:
    print("Lentoasema:", tulos[0])
    print("Sijaintikunta:", tulos[1])
else:
    print("Lentoasemaa ei löytynyt.")

kursori.close()
yhteys.close()