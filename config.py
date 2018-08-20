import mysql.connector

conn = mysql.connector.connect(
         user='root',
         password='N0rm4.p1a',
         host='127.0.0.1',
         database='clientes')

cur = conn.cursor()

query = ("SELECT * FROM Persona")

cur.execute(query)

for (id, nombre, apellido, direcion, ciudad) in cur:
    print("{}, {}, {}, {}".format(id, nombre,apellido,ciudad))

cur.close()
conn.close()
