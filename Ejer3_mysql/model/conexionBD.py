import mysql.connector


"""
    Conecta a la base de datos EmpleadosBD en localhost

    Returns:
        mysql.connector.connection.MySQLConnection: Conexión a la base de datos
            o None si la conexión falló
"""


def conectarBD():

    mydb = None

    try:
        mydb = mysql.connector.connect(
            host="localhost",       
            user="root",           
            password="",           
            database="EmpleadosBD" 
        )

        if mydb.is_connected():
            print("Conexión establecida con éxito")
            return mydb  # Retorna la conexión si es exitosa
        else:
            print("Conexión fallida")

    except mysql.connector.Error as error:
        print("Conexión fallida: {}".format(error))

    # finally:
    #     if mydb is not None and mydb.is_connected():
    #         mydb.close()
    #         print("Conexión finalizada")

    return None  # Retorna None si la conexión falló
