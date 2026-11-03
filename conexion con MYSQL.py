import pymysql

# 1. Conexión a MySQL
datos_conexion = {
    'host': 'localhost',
    'user': 'root',
    'password': '123456',
    'database': 'Miescuela',
    'port': 3305
}

try:
    # Abrir la conexión
    conexion = pymysql.connect(**datos_conexion)
    print("Conexión Exitosa")

    # Cursor
    cursor = conexion.cursor()

    # Consulta
    sql = "SELECT código, nickname, años, email, fecha_de_registro FROM Estudiantes"
    cursor.execute(sql)

    # Obtener dato
    resultados = cursor.fetchall()

    # Mostrar datos
    print("\n--- LISTA DE ESTUDIANTES ---\n")

    for fila in resultados:
        print(f"código: {fila[0]} | nickname: {fila[1]} | años: {fila[2]} | email: {fila[3]} | fecha_de_registro: {fila[4]}")

    # Cerrar cursor y conexión
    cursor.close()
    conexion.close()

except Exception as e:
    print(f" Ocurrió un error: {e}")
