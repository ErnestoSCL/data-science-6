import mysql.connector

connection= mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="root",
    database="db_g6"
)

print("¡Conexión exitosa a la base de datos MySQL!")

cursor = connection.cursor()
cursor.execute("select nombre, email from alumno;")
resultados = cursor.fetchall()
for resultado in resultados:
    print('*************')
    print(f'Nombre: {resultado[0]}')
    print(f'Email: {resultado[1]}')

connection.close()