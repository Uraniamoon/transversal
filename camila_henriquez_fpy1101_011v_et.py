
import random

trabajadores=['Juan Perez','Maria Garcia','Carlos Lopez','Ana Martinez','Pedro Rodriguez','Laura Hernandez','Miguel Sanchez','Isabel Gomez','Francisco Diaz','Elena Fernandez']

def asignar_sueldos(trabajadores):
 
  nombre_trabajador=input("ingrese nombre del trabajador :")
  print(nombre_trabajador)

  sueldo_asignado=random.randint(300000,2500000)
  print( "sueldo",sueldo_asignado) 


def clasificar_sueldos(trabajadores):
  for trabajador in trabajadores:

    sueldo=random.randint(300000,2500000)
    print("nombre", trabajador,", ", 'Sueldo Asignado', sueldo)

def ver_estadisticas(trabajadores):
  
  sueldo_max=2500000
  sueldo_min=300000
  promedio= sueldo_max*sueldo_min/2 
  
  print(trabajadores,promedio)

def reporte_sueldos(trabajadores):
  sueldo_base= random.randint(300000,2500000)
  descto_salud= sueldo_base *0.07
  descto_afp= sueldo_base *0.12
  sueldo_liquido=sueldo_base - descto_afp - descto_salud
  print(sueldo_liquido)

def salir_programa():
 if trabajadores == 5 :
   print("finalizando programa" ) 
 


while True:
  print("1- Asignar sueldos")
  print("2- Clasificar sueldos")
  print("3- Ver estadisticas")
  print("4- Reporte de sueldos")
  print("5- Salir del Programa")

  opcion= int(input("Ingrese una opcion : " ))


  if opcion == 1 :
   asignar_sueldos(trabajadores)
  if opcion == 2:
   clasificar_sueldos(trabajadores)
  if opcion == 3 :
   ver_estadisticas(trabajadores) 
  if opcion == 4 :
   reporte_sueldos(trabajadores) 
  if opcion == 5:
   print("fin del programa ")
  break   