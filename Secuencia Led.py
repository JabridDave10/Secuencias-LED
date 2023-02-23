from machine import Pin as pin
from utime import sleep as pausi,sleep_ms as pausita

puertos = [2, 16, 5, 19, 3, 1, 22, 23]
todos = []
centro1=[]
centro2=[]
shooter1=[]
shooter2=[]
velocidad=50
velocidadr=50
velocidad2=velocidad*7
velocidad3=velocidad//2
Val_inicial=1
Val_final=1
mitadlist=(len(puertos)//2)
# asigna valores a las listas
for i in puertos:
    shooter1.append (pin(i,pin.OUT))

for i in puertos:
    todos.append (pin(i,pin.OUT))

for i in puertos[:mitadlist]:
    centro1.append (pin(i,pin.OUT))

for i in puertos[mitadlist:]:
    centro2.append (pin(i,pin.OUT))

# funcion 1
def derecha():
    for elemento in todos:
        for j in range (2):
            elemento.value(not elemento.value())
            pausita(velocidad)

def izquierda():
    for elemento in reversed(todos):
        for j in range (2):
            elemento.value(not elemento.value())
            pausita(velocidad)

# funcion 2

def shoter_izquierda():
    todos[0].value(1)
    
    for elemento in todos[Val_inicial:]:
        for j in range (2):
            elemento.value(not elemento.value())
            pausita(velocidad)
            
    todos[0].value(0)
    
      
def shoter_derecha():
    
    for elemento in reversed (todos):
        todos[7].value(1)
        for j in range (2):
            elemento.value(not elemento.value())
            pausita(velocidad)
        todos[7].value(0)

#funciones de division central
def mitad1 ():
    for elemento in centro1:
        elemento.value(1)

    pausita(velocidad2) 

    for elemento in centro1:
        elemento.value(0)
def mitad2 ():
    for elemento in centro2:
        elemento.value(1)

    pausita(velocidad2) 

    for elemento in centro2:
        elemento.value(0)

#vel 100
def extremos_centro():
    for i,k in zip(centro1,reversed(centro2)):
        for elemento2 in centro2:
            
            (i.value(not i.value()),k.value(not k.value()))
            pausita(velocidad)

def everyone():
    for elemento in todos:
        elemento.value(1)
    pausita(velocidad*10)   
    for elemento in todos:
        elemento.value(0) 
    pausita(velocidad) 

#vel 100
def centro_extremos():
    for i,k in zip(reversed(centro1),centro2):
        for elemento2 in centro2:
            
            (i.value(not i.value()),k.value(not k.value()))
            pausita(velocidad)
#hhdfgh
def volumen():
    for i,k in zip(reversed(centro1),centro2):
        for elemento2 in centro2:           
            (i.value(1),k.value(1))
            pausita(velocidad)
    for i,k in zip(centro1,reversed(centro2)):
        for elemento2 in centro2:
            (i.value(0),k.value(0))
            pausita(velocidad)
#inicio del patron led
while True:
    
    contador=0
    while contador<10:
        derecha()
        izquierda()
        contador+=1
        if contador>4:
            velocidad=velocidad3
    velocidad=velocidadr
    contador=0
    while contador<5:
        shoter_derecha()
        contador+=1
    while contador<10:
        shoter_izquierda()
        contador+=1
    
    contador=0
    while contador<5:
        mitad1()
        mitad2() 
        contador+=1
    
    contador=0
    while contador<5:
        extremos_centro() 
        contador+=1
     
    contador=0
    while contador<5:
        everyone() 
        contador+=1
    
    contador=0
    while contador<5:
        centro_extremos() 
        contador+=1

    contador=0
    while contador<5:
        everyone() 
        contador+=1

    contador=0
    while contador<5:
        volumen()
        contador+=1
        
    contador=0
    while contador<5:
        extremos_centro() 
        centro_extremos()
        contador+=1

    contador=0
    while contador<5:
        everyone() 
        contador+=1