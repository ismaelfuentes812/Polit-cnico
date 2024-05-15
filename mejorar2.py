#print("hola mundo")sirve para imprimir por consola
#
#-int: Numero enteros
#-float: N°decimales
#-string:Letras
#-bool:v o f


"""
#creando primera variable
saludo = "hola mundo desde variable"
#imprimir variable
print (saludo)
#imrimir por consola hola +nombre
nombre ="ismael"
#para concatenar se puede usar , o + 
print ("hola",nombre)
"""
#actividad 4

"""#entrada
#ingresa stringy conviertea cadena de texto y convierte n° entero (int) a decimales (float)
n1 = int (input( "ingrese n1: "))
n2 = float(input( "ingrese n2: "))

#procesos
suma = n1+n2

#salidas
print ( "resultado",suma)"""

#Activad 5

"""n1 = int (input( "ingrese n1: "))
n2 = int(input( "ingrese n2: "))
#proceso
producto = n1*n2
#salida
print ("resultado",producto)"""

#actividad 6
"""
l1 = float(input("ingrese l1"))

#proceso
perimetro = l1 * 4
#salida
print ("resultado",perimetro)"""

#actividad 7
"""
a = 5
b = 3
#Proceso
proceso = a + b, a-b,a*b
#salida
print("-"*50)
print("resultado",proceso)
print("-"*50) """

#atividad 8
"""
cant1= int(input("producto art 1: "))
pre1= float(input("precio art 1: "))
cant2= int(input("producto art 2: "))
pre2= float(input("precio art 2: "))
cant3= int(input("producto art 3: "))
pre3= float(input("precio art 3: "))
#Procesos
total_art1 =cant1*pre1
total_art2 =cant2*pre2
total_art3 =cant3*pre3
total_articulos = total_art1 + total_art2 + total_art3
#salida
print("-"*50)
print(total_art1)
print("-"*50)
print(total_art2)
print("-"*50)
print(total_art3)
print("-"*50)
print(total_articulos)"""

#Atividad 9
"""
kml= float(input("kml: "))
pr= float(input("pr: "))
km= int(input("km: "))

#Proceso
kml= km/kml
km= kml*pr

#salida
print("-"*50)
print("cantidad_consumido",kml)
print("-"*50)
print("precio_consumido",km)
print("-"*50)"""

#Actividad 10
"""
t1=int(input("temperatura1: "))
t2=int(input("temperatura2: "))
t3=int(input("temperatura3: "))

#Proceso
promedio= (t1+t2+t3)//3

#salida
print("-"*50)
print("Promedio",promedio)
print("-"*50) """

#Actividad 11
"""
cand01=int(input("votos01: "))
cand02=int(input("votos02: "))

#proceso
votos_totales=(cand01+cand02)
votos01=(cand01*100)/100
votos02=(cand02*100)/100
#salida
print("-"*50)
print("Candidato01",votos01,"%","|")
print("-"*50)
print("Candidato02",votos02,"%","|")
print("-"*50)
print("Votos totales",cand01+cand02,"%","|")
"""
#Clase 2------------------------------------
"""
a= 10
b= 5
#suma
print("suma =", a+b)
#resta
print("suma =", a-b)
#Produto/multiplicacion
print("suma =", a*b)
#Divisiondecomaflotante
print("suma =", a/b)
#Division entera
print("suma =", a//b)
#resto de na dvision
print("suma =", a%b)
#potencia
print("suma =", a**b)
"""
#Actividad 17
"""
a=10/5+3
b=50/5+10-10*1
c=50-3*10+4*1
print("Resultado de C es",a)
print("Resultado de C es",b)
#Actividad 18
"""
"""
#a)
print("respuesta1 es el entero: ",int(9/4))
print("respuesta1 es el entero: ",round(17/3))

#b)
print("el residiuo de 9 dividido entre 4 es: ",(9%4))
print("el residiuo de 17 dividido entre 3 es: ",(17%3))
"""
"""

#Actividad 19


a= 10
b= 7

c= 10+10-5*7+4

d=3*10+1-7//4+10%2

e=2*10+7-1+10**2

print("-"*50)
print("Resultado de C es",c)
print("-"*50)
print("Resultado de D es",d)
print("-"*50)
print("Resultado de E es",e)
print("-"*50)
"""
#Actividad 21
"""
p= (c1+c2+c3)/3

s= (n+(n+1))/2

h=(a2+b2)**0.5

p=((y2-y1)/(x2-x1))
"""
#Actividad 22
"""
#entrada
name = input("Nombre: ")
last = input("Apellido: ")
print("°"*30)
print(last.lower()+"_"+name.lower()+"@tdf.edu.ar")
print("°"*30)
"""
#Actividad 23
"""

cor=400
ros=122

tiempo= cor/ros
print("°"*30)
print("el tiempo es de: ",round(cor/ros))
print("°"*30)
"""
#Actividad 24
"""
last= input("Apellido: ")
name= input ("Nombre: ")
dni= int(input("DNI: "))
age= int(input("Edad: "))
tel= int(input("Telefono: "))
ciu= input("Ciudad: ")
print("°"*55)
print("Bienvenido",last.upper(),",",name.capitalize(),"al Curso de Diseño Web!")
print("°"*55)
print("Tus datos son:")
print("DNI :",dni)
print("Edad :",age)
print("Telefono:",tel)
print("Ciudad:",ciu.capitalize())
print("°"*55)
"""
#Actividad 26
"""
n1=int(input("ingrese N1: "))
n2=int(input("ingrese N2: "))

if n1>n2:
   print(n2,n1)
elif n2==n1:
   print("son iguales")
else:
    print(n1,n2)
    """
#Actividad 27
"""
a=int(input("ingrese N°: "))
b=int(input("ingrese N°: "))
c=int(input("ingrese N°: "))

suma=(a+b+c)
cubo=suma**3
if suma>10:
        print("el resultadoes:",suma//2)

else:
     print("el resultado es:",cubo)
"""
#Actividad 28
"""
tt= int(input("ingrese n° de turno:"))
hs= int(input("ingrese hs trabajadas:"))
pr1=5234
pr2=8057.75
diurno=1
nocturno=2
print("°"*35)
if tt==diurno:
    print("Sueldo diurno")
    print("hs trabajadas",hs,"hs")
    print("°"*35)
    print("Su sueldo es","$",hs*pr1)
    print("°"*35)
elif tt>2:
    print("seleccione turno: 1 diurno 2 Nocturno")
    print("°"*35)
else:
    print("Sueldo Nocturno")
    print("hs trabajadas",hs,"hs")
    print("°"*35)
    print("Su sueldo es","$",hs*pr2)
    print("°"*55)
 """
#Ejercicio de practica
"""
edad= int(input("ingrese su edad: "))

if edad>=18:
    print(" Es mayor de edad")

else:
    print("No Es mayor de edad")
 """
#2
"""
pasw= input("ingrese contraseña: ").upper()

passw="89880A"

if pasw==passw:
    print("contraseña correcta")
else:
    print("contraseña incorrecta")
    """
#3  Si el divisor es 0 el programa debe mostrar un error
"""
n1=int(input("ingrese 1 N°: "))
n2=int(input("ingrese 2 N°: "))

if n1==0:
    print("Error, no se puede dividir por 0")
elif n2==0:
    print("Error, no se puede dividir por 0")
else:
    print((n1/n2),"se puede dividir")
  """  
#4
"""
num= int(input("Ingrese N°: "))
         
if num%2 == 0:
         print("es par")
else:
     print("es impar")
"""

#5
#Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y nombre.
#elgrupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con nombre anterior a la N y el grupo B por el resto.
#preguntar nombre y sexo y mostrar n pantalla el grupo que corresponde.        
         
name= input("ingrese nombre: ")
gen= input("ingrese genero: ")


#6
"""
rent= int(input("Ingrese monto: "))

if rent <= 10000:
    print("Le corresponde 5%","$",rent*5/100)
elif rent > 10000 and rent <20000:
    print("Le corresponde 15%","$",rent*15/100)
elif rent >= 20000 and rent <35000:
    print("Le corresponde 20%","$",rent*20/100)
elif rent >= 35000 and rent < 60000:
    print("Le corresponde 30%","$",rent*30/100)
else:
    print("Le corresponde 45%","$",rent*45/100)
"""
#7
"""
pizz= int(input("seleccione una variedad 1_Pizza veg & 2_Pizza no veg: "))


if pizz==1:
    print("_Pizza vegana_ seleccione un ingrediente")
    print("°"*55)
    ingr= int(input("1_Pimiento\t2_Tofu: "))
    if ingr==1:
        print("°"*55)
        print("Pimiento")
        print("°"*55)
        print("Pizza vegana:Salsa de tomate\t mozzarella \t Pimiento")
        print("°"*55)
    elif ingr==2:
        print("°"*55)
        print("tofu")
        print("°"*55)
        print("Pizza vegana:Salsa de tomate\t mozzarella \t Tofu")
        print("°"*55)
else:
    print("°"*55)
    print("_Pizza No vegana_ seleccione un ingrediente")
    print("°"*55)
    ingr= int(input("1_Peperoni\t2_Jamon \t3_Salmon: "))
    if ingr==1:
        print("°"*55)
        print("Peperoni")
        print("°"*55)
        print("Pizza No vegana:Salsa de tomate\tmozzarella\tPeperoni")
        print("°"*55)
    elif ingr==2:
        print("°"*55)
        print("Jamon")
        print("°"*55)
        print("Pizza No vegana:Salsa de tomate\t mozzarella \t Jamon")
        print("°"*55)
    elif ingr==3:
        print("°"*55)
        print("Salmon")
        print("°"*55)
        print("Pizza No vegana:Salsa de tomate\t mozzarella \t Salmon")
        print("°"*55)
"""      
#8
