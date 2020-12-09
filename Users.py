'''
Created on 8/12/2020

@author: User
'''

from src import ArrayList

ar = ArrayList.ArrayLinerList(10)

class Registro():
    def __init__(self,id:int,satOxi:int,fCardi:int,hora:str,fecha:str):
        self.id = id
        self.satOxi = satOxi
        self.fCardi = fCardi
        self.hora = hora
        self.fecha = fecha 
    
    def __str__(self):
        return self.hora
        
class Registros():
    def __init__(self, listaRegistros:ar):
        self.ListaRegistros = listaRegistros
        self.PromedioOx = 0
        self.PromedioFCar = 0

class User():
    def __init__(self,id : int, username : str,password:str,name : str ,fecha:str,region:str, prioridad:int,registros:ar):
        self.id = id
        self.username = username
        self.password = password
        self.name = name
        self.fecha = fecha
        self.region = region
        self.prioridad = prioridad
        self.registros = registros

    def __str__(self):
        return self.name
    
    def __eq__(self, other):
        return self.prioridad == other.prioridad
    
    def __lt__(self, other):
        return self.prioridad < other.prioridad
    

class Medic():
    def __init__(self,id:int,nombre:str,disponible:bool):
        self.id = id
        self.nombre = nombre
        self.disponible = disponible
        
class cita():
    def __init__(self, user: User,medic : Medic ):
        self.user = user
        self.medic = medic
                

reg1 = Registro(10,11,2,' asd',' rew')
arr = ArrayList.ArrayLinerList(10)
arr.add(0, reg1)
reg  = Registros(ar)

u = User(1,'a','a','Lopez','a','a',4,reg)
u2 = User(1,'a','a','Lopez','a','a',4,reg)
print()



