from . import conexionBD as db


def insertarUsuarios():
    conexion = db.conectarBD()  # Usar la función conectar del módulo db
    cursor = conexion.cursor()

    insertar_usuarios_query = """
    INSERT INTO Usuarios (nombre, email, fecha_de_registro)
    VALUES (%s, %s, %s);
    """

    usuarios = [
        ('Alan Bastida', 'alan@example.com', '2024-10-03'),
        ('Maria Lopez', 'maria@example.com', '2024-10-02'),
        ('Juan Perez', 'juan@example.com', '2024-10-01')
    ]

    cursor.executemany(insertar_usuarios_query, usuarios)

    conexion.commit()

    print("Usuarios insertados con éxito.")

    cursor.close()
    conexion.close()
