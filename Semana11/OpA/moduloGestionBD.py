import mysql.connector


config = {
    'user': 'root',
    'password': '1234',
    'host': '127.0.0.1',
    'port': '3306',
    'database': 'cuscatlan'
}

miConexion = mysql.connector.connect(**config)

def registrarCliente(oCliente):
    cursorDB = miConexion.cursor()
    sentenciaSQL = ("INSERT INTO cuscatlan.clientes "+
                    "(`idCliente`,"+
                    "`IdeCliente`,"+
                    "`nomCliente`,"+
                    "`ape1Cliente`,"+
                    "`ape2Cliente`,"+
                    "`generoClien`,"+
                    "`CantViajes`,"+
                    "`Salario`)"+
                    "VALUES (%s,%s,%s,%s,%s,%s,%s,%s)")
    valores = (oCliente.idCliente,oCliente.ideCliente,oCliente.nomCliente,
               oCliente.ape1Cliente,oCliente.ape2Cliente,
               oCliente.generoClien,oCliente.cantViajes,oCliente.salario)
    
    cursorDB.execute(sentenciaSQL,valores)
    miConexion.commit() #Sin esto no quedaria guardado en base datos, esto es obligatorio

def modificarCliente(oCliente):
    cursorDB = miConexion.cursor()
    sentenciaSQL = ("UPDATE cuscatlan.clientes "+                    
                    "set nomCliente = %s,"+
                    "    ape1Cliente = %s,"+
                    "    ape2Cliente = %s,"+
                    "    generoClien = %s,"+
                    "    CantViajes = %s,"+
                    "    Salario = %s "+
                    "WHERE IdeCliente = %s")
    valores = (oCliente.nomCliente,oCliente.ape1Cliente,oCliente.ape2Cliente,
               oCliente.generoClien,oCliente.cantViajes,oCliente.salario,oCliente.ideCliente)
    
    cursorDB.execute(sentenciaSQL,valores)
    miConexion.commit()

def consultarClientes() -> dict:
    cursorDB = miConexion.cursor()
    sentenciaSQL = "Select * from cuscatlan.clientes"
    cursorDB.execute(sentenciaSQL)
    rs = cursorDB.fetchall()
    return rs

def buscarCliente(identificacion) -> dict:
    cursorDB = miConexion.cursor()
    sentenciaSQL = "Select * from cuscatlan.clientes Where IdeCliente = %s"    
    valores = (identificacion,)
    cursorDB.execute(sentenciaSQL,valores)
    rs = cursorDB.fetchone()
    return rs

def eliminarCliente(identificacion):
    cursorDB = miConexion.cursor()
    sentenciaSQL = ("Delete from cuscatlan.clientes Where IdeCliente = %s")                    
    valores = (identificacion,)    
    cursorDB.execute(sentenciaSQL,valores)
    miConexion.commit()