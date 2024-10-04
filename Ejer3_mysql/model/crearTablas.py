from . import conexionBD as db

def crearTablaUsuario():
    # Obtener la conexión a la base de datos
    conexion = db.conectarBD()  
    
    if conexion is None:
        print("No se pudo establecer la conexión a la base de datos.")
        return 

    cursor = conexion.cursor()  # Crear un cursor para ejecutar la consulta

    # Consulta SQL para crear la tabla
    query = """
        CREATE TABLE IF NOT EXISTS Usuarios (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nombre VARCHAR(100),
            email VARCHAR(100),
            fecha_de_registro DATE
        );
    """
    
    try:
        cursor.execute(query)  
        print("Tabla 'Usuarios' creada con éxito.")
    except Exception as e:
        print(f"Ocurrió un error al crear la tabla: {e}") 

    finally:
        cursor.close()  
        conexion.close() 
