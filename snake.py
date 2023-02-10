import turtle
import time 
import random   

#variables
posponer = 0.1
puntaje = 0
maxPuntaje = 0
mov=0
direc=""

#Configuración
window = turtle.Screen()                
window.title('Snake')                   
window.bgcolor('#353535')               
window.setup(width=600,height=600)      
window.tracer(0)                       

#Cabeza de la serpiente
cabeza = turtle.Turtle()               
cabeza.speed(0)                       
cabeza.shape('square')                  
cabeza.color('#75C46D')              
cabeza.penup()                        
cabeza.goto(0,0)                       
cabeza.direction = 'stop'              

#Comida
comida = turtle.Turtle()
comida.speed(0)
comida.shape('circle')
comida.color('#D12D2D')
comida.penup()
comida.goto(0,100)

#Linea
line = turtle.Turtle()
line.speed(0)
line.shape('circle')
line.color('white')
line.shapesize(stretch_wid=0.07,stretch_len=300)
line.penup()
line.goto(0,240)

#Texto para el puntaje
texto = turtle.Turtle()
texto.speed(0)
texto.color('white')
texto.penup()
texto.hideturtle()
texto.goto(0,260)
texto.write('Puntaje:0     Máximo puntaje: 0', align='center', font=('Courier', 20, 'normal'))

#Cuerpo de la serpiende
cuerpo = []                             #Una lista que almacena cada segmento
colores = [(109,160,104),(104,142,160)]

def printText():

    global  maxPuntaje
    if puntaje>maxPuntaje:
        maxPuntaje = puntaje
    texto.clear()
    texto.write(f'Puntaje:{puntaje}     Máximo puntaje: {maxPuntaje}', align='center', font=('Courier', 20, 'normal'))


#Definir cada movimiento
def arriba():
    global direc
    if mov==0:
        cabeza.direction = 'up'
        direc='up'
def abajo():
    global direc
    if mov==0:
        cabeza.direction = 'down'
        direc='down'
def izquierda():
    global direc
    if mov==0:
        cabeza.direction = 'left'
        direc='left'
def derecha():
    global direc
    if mov==0:
        cabeza.direction = 'right'
        direc='right'
def init_game():
    global direc
    if mov==0:
        cabeza.direction = 'up' 
        direc='up'
def salta():
    if cabeza.direction == 'up':        #Si la direccion es hacia arriba
        y =  cabeza.ycor()              #Obtiene la coordena Y
        x =  cabeza.xcor()              #Obtiene la coordena Y
        cabeza.goto(x,y + 40)             #Actualiza la posición Y

    elif cabeza.direction == 'down':
        y =  cabeza.ycor()              #Obtiene la coordena Y
        x =  cabeza.xcor()              #Obtiene la coordena Y
        cabeza.goto(x,y - 40)

    elif cabeza.direction == 'left':
        x =  cabeza.xcor()              #Obtiene la coordena X
        y =  cabeza.ycor()              #Obtiene la coordena X
        cabeza.goto(x - 40,y)

    elif cabeza.direction == 'right':
        x =  cabeza.xcor()              #Obtiene la coordena X
        y =  cabeza.ycor()              #Obtiene la coordena X
        cabeza.goto(x + 40,y)    
def Space():
    global mov
    global direc
    
    if mov==0:
        mov=1
        cabeza.direction = 'stop'      
    elif mov==1:
        cabeza.direction = direc
        mov=0

#Ejecuta el movimiento
def movimiento():
    if cabeza.direction == 'up':        #Si la direccion es hacia arriba
        y =  cabeza.ycor()              #Obtiene la coordena Y
        cabeza.sety(y + 20)             #Actualiza la posición Y

    elif cabeza.direction == 'down':
        y =  cabeza.ycor()              #Obtiene la coordena Y
        cabeza.sety(y - 20)

    elif cabeza.direction == 'left':
        x =  cabeza.xcor()              #Obtiene la coordena X
        cabeza.setx(x - 20)

    elif cabeza.direction == 'right':
        x =  cabeza.xcor()              #Obtiene la coordena X
        cabeza.setx(x + 20)

#Creacion del cuerpo
def crearSegmento():
    global puntaje
    segmento = turtle.Turtle()
    turtle.colormode(255)
    segmento.speed(0)
    segmento.shape('square')
    segmento.color(random.choice(colores))
    segmento.penup()
    cuerpo.append(segmento)
    puntaje += 1
    printText()

#Colisión con la comida
def colisionComida():
    if cabeza.distance(comida)<20:     
        """   x = random.randint(-280,280)
           y = random.randint(-280, 220) """
        x = random.randrange(-280,280,20)
        y = random.randrange(-280, 220,20)
        comida.goto(x,y)             
        crearSegmento()

#borde
def borde():
    global puntaje
    if cabeza.xcor() <-280 or cabeza.xcor() >280 or cabeza.ycor() <-280 or cabeza.ycor() >220:
        time.sleep(0.5)
        cabeza.goto(0,0)
        cabeza.direction = 'stop'
        for segmento in cuerpo:        
            segmento.goto(1000,1000)
        cuerpo.clear()                  
        puntaje = 0
        printText()

#Mover el cuerpo
def movCuerpo():
    totalSeg = len(cuerpo)

    #Cada elemento sigue al anterior
    #Exepto el primero
    for segmento in range(totalSeg-1,0,-1):     
        x = cuerpo[segmento-1].xcor()          
        y = cuerpo[segmento-1].ycor()
        cuerpo[segmento].goto(x,y)              

    if totalSeg >0:                       
        x = cabeza.xcor()
        y = cabeza.ycor()
        cuerpo[0].goto(x,y)

def mordida():

    global puntaje
    for segmento in cuerpo:
        if cabeza.distance(segmento) < 20:
            time.sleep(0.5)
            cabeza.goto(0, 0)
            cabeza.direction = 'stop'
            for segmento in cuerpo:  # Esconde los segmentos
                segmento.goto(1000, 1000)
            cuerpo.clear()  # Limpia la lista
            puntaje = 0
            printText()

#Conexion con teclado
window.listen()                         #Está pendiente si se oprime una tecla
window.onkeypress(arriba,'Up')          #Ejecuta la función arriba() cuando detecta up
window.onkeypress(abajo,'Down')
window.onkeypress(izquierda,'Left')
window.onkeypress(derecha,'Right')
window.onkeypress(init_game,"Return") 
window.onkeypress(salta,"e") 
window.onkeypress(Space,"p") 


#Ciclo permanente
while True:
    window.update()         

    borde()
    colisionComida()                   
    mordida()
    if mov==0:
        movCuerpo()                         
    movimiento()                        

    time.sleep(posponer)                