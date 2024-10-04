from model import crearTablas
from model import insertarUsuario


# Prueba de conexión
# conexion = crearTablas.db.conectarBD()  # Intenta conectar a la base de datos
# if conexion is not None:
#     print("Conexión exitosa.")
# else:
#     print("No se pudo conectar a la base de datos.")

# Ejecutar la creación de la tabla
crearTablas.crearTablaUsuario()

# Ejecutar la inserción de usuarios
insertarUsuario.insertarUsuarios()
