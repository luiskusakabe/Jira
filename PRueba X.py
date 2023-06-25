#Datos del primer estudiante 
print('Bienvenido al portal estudiantil, por favor introduzca los datos que seran solicitados a continuacion:')
print("Introduzca los datos del primer alumno")
nombre1=input(str('Nombre del alumno: '))
cedula1=int(input("Numero de cedula: "))
if cedula1>=10000000<=50000000:
    print("")
else:
    print("Por favor ingresar una cedula valida")
edad1=int(input("Edad: "))

if edad1>=18:
    print("El alumno es mayor de edad")
else:
    print("El alumno es menor de edad")
#Calificaciones
Matematica1=float(input("Ingrese la nota de Matematica: "))
variable1=Matematica1%2
if variable1==0:
    print("La nota es par")
else:
    print("La nota es impar")
Biologia1=float(input("Ingrese la nota de biologia: "))
variable2=Biologia1%2
if variable2==0:
    print("La nota es par ")
else:
    print("La nota es impar")
Historia1=float(input("Ingrese la nota de historia: "))
variable3=Historia1%2
if variable3==0:
    print("La nota es par")
else:
    print("La nota es impar")
Arte1=float(input("Ingrese la nota de arte: "))
variable4=Arte1%2
if variable4==0:
    print("La nota es par")
else:
    print("La nota es impar")
promedio=Matematica1+Biologia1+Historia1+Arte1
promedio1=promedio/4
if promedio1>10:
    print("El alumno "+nombre1+" aprobo el curso")
    print("El promedio es: ",promedio1)
else:
    print("El alumno "+nombre1+" reprobo el curso")
    print("El promedio es: ",promedio1)

#Datos del segundo estudiante
print("Introduzca los datos del segundo alumno")
nombre2=input(str('Nombre del alumno: '))
cedula2=int(input("Numero de cedula: "))
if cedula2>=10000000<=50000000:
    print("")
else:
    print("Por favor introduzca una cedula valida")
edad2=int(input("Edad: "))

if edad2>=18:
    print("El alumno es mayor de edad")
else:
    print("El alumno es menor de edad")
#Calificaciones
Geografia1=float(input("Ingrese la nota de Geografia: "))
variable5=Geografia1%2
if variable5==0:
    print("La nota es par")
else:
    print("La nota es impar")
Catedra1=float(input("Ingrese la nota de Catedra: "))
variable6=Catedra1%2
if variable6==0:
    print("La nota es par ")
else:
    print("La nota es impar")
Fisica=float(input("Ingrese la nota de Fisica: "))
variable7=Fisica%2
if variable7==0:
    print("La nota es par")
else:
    print("La nota es impar")
Calculo1=float(input("Ingrese la nota de Calculo I: "))
variable8=Calculo1%2
if variable8==0:
    print("La nota es par")
else:
    print("La nota es impar")
promedio2=Geografia1+Catedra1+Fisica+Calculo1
promedio3=promedio2/4
if promedio3>10:
    print("El alumno "+nombre2+" aprobo el curso")
    print("El promedio es: ",promedio3)
else:
    print("El alumno "+nombre2+" reprobo el curso")
    print("El promedio es: ",promedio3)


print('Bienvenido, a continuacion introduzca los siguientes datos: ')

alumno1,alumno2,alumnoN = 0,0,1

for i in [alumno1,alumno2]:
    nombre = str(input('Nombre del alumno: '))
    apellido = str(input('Apellido del alumno: '))
    Cedula = int(input('Introduce un numero de cedula: '))
    Edad = int(input('Introduce la edad del alumno: '))

    if(Cedula >= 1000000 and Cedula <= 50000000 and Edad > 0 and Edad <= 100):
        print('El alumno '+nombre+' '+apellido+' '+'C.I: '+str(Cedula))
    else:
        print('El alumno ingresado no es valido')
    
    Arte, Biologia, Matematica, Ingles = 0,0,0,0

    print('Ingrese las notas de las siguientes asignaturas: ')
    Arte = int(input('Arte: '))
    Biologia = int(input('Biologia: '))
    Matematica = int(input('Matematica: '))
    Ingles = int(input('Ingles: '))

    if(Arte >= 0 and Arte <= 100):
        None
    else:
        print('Ingrese una nota valida')

    if(Biologia >= 0 and Biologia <=100):
        None
    else:
        print('Ingrese una nota valida')
    
    if(Matematica >= 0 and Matematica <= 100):
        None
    else:
        print('Ingrese una nota valida')
    
    if(Ingles >= 0 and Ingles <= 100):
        None
    else:
        print('Ingrese una nota valida')

    notasS = Arte+Biologia+Matematica+Ingles
    notasT =notasS/4

    print('Promedio: '+str(notasT))

    if (notasT>=50 and notasT<=100):
        print('Aprobado')
    elif(notasT<=50):
        print('Reprobado')

    if(Edad>=18):
        print('Mayor de edad')
    else:
        print('Menor de edad')

    if(Arte%2 == 0):
        print('Arte es par')
    elif(Arte%2 ==1):
        print('Arte es impar')
    if(Biologia%2 == 0):
        print('Biologia es par')
    elif(Biologia%2 ==1):
        print('Biologia es impar')
    if(Ingles%2 == 0):
        print('Ingles es par')
    elif(Ingles%2 ==1):
        print('Ingles es impar')
    if(Matematica%2 == 0):
        print('Matematica es par')
    elif(Matematica%2 ==1):
        print('Matematica es impar')
        