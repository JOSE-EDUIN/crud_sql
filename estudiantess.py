import pyodbc
import pymysql


class Estudiantesss:

    def __init__(self):
        self.cnn = pyodbc.connect('DRIVER={SQL Server};SERVER=DESKTOP-WIWO\SQLEXPRESS;DATABASE=alumnos;Trusted_Connection=yes;')
        print("conexion correcta")

    def __str__(self):
        datos = self.consulta_estudiante()
        aux = ""
        for row in datos:
            aux = aux + str(row) + "\n"
        return aux

    def consulta_estudiante(self):
        cur = self.cnn.cursor()
        cur.execute("SELECT * FROM estudiantes")
        datos = cur.fetchall()
        cur.close()
        return datos

    def buscar_estudiante(self, Id):
        cur = self.cnn.cursor()
        sql = "SELECT * FROM estudiantes WHERE Id = {}".format(Id)
        cur.execute(sql)
        datos = cur.fetchone()
        cur.close()
        return datos

    def inserta_estudiante(self, nombre, edad, sueldo):
        cur = self.cnn.cursor()
        sql = '''INSERT INTO estudiantes (nombre, edad, sueldo) 
        VALUES('{}', '{}', '{}')'''.format(nombre, edad, sueldo)
        cur.execute(sql)
        n = cur.rowcount
        self.cnn.commit()
        cur.close()
        return n

    def elimina_estudiante(self, Id):
        cur = self.cnn.cursor()
        sql = '''DELETE FROM estudiantes WHERE Id = {}'''.format(Id)
        cur.execute(sql)
        n = cur.rowcount
        self.cnn.commit()
        cur.close()
        return n

    def modifica_estudiante(self, Id, nombre, edad, sueldo):
        cur = self.cnn.cursor()
        sql = '''UPDATE estudiantes SET nombre='{}', edad='{}', sueldo='{}'
         WHERE Id={}'''.format(nombre, edad, sueldo, Id)
        cur.execute(sql)
        n = cur.rowcount
        self.cnn.commit()
        cur.close()
        return n
