import turtle
import random

turtle.bgpic("ruleta2.gif") # import the bg photo

lineas = 7
alumno = 0
grados = 90
speed = 28

turtle.hideturtle() 
s = turtle.getscreen()
t = turtle.Turtle()
t.penup()
# t.hideturtle()
turtle.title("Ruleta de la fortuna")

t.color('yellow')

clase = [
"name","name","name","name","name","name","name","name",
"name","name","name","name","name","name","name","name",
"name","name","name","name","name","name","name","name"
]

t.hideturtle()
# clono la tortuga, esta tortuga va a actuar como la pelota, se va a llamar C
t.pendown()
c = t.clone()
x = t.clone()
t.penup()

c.hideturtle()
c.penup()
c.forward(360)
c.left(90)

turtle.tracer(0) # disable the animation

t.forward(440)
t.left(90)
t.forward(-40)
t.showturtle()
t.color('white')

t.write("name", font=("Cooper Black", 10, "italic"))  # pinto el primer nombre


# Bucle para pintar todos los nombres, he creado un circulo de 450 grados, cada 15 grados pintara un
# nombre, hasta los 24 nombres que hay, mas el primero que lo pinto fuera del bucle
t.showturtle()
for i in range(23):
    t.circle(450, 15)
    alumno += 1
    t.write(clase[alumno], font=("Cooper Black", 10, "italic"))
t.hideturtle()
c.showturtle()
c.shape("circle")

turtle.tracer(1) # activa la animacion, para que se vea la bola dar vueltas

# Bucle que decide con un numero random la posicion de donde va a caer la pelota,
# el rango 43, 51 es para que de mas de 1 vuelta
answer = turtle.textinput('Quieres tirar de la ruleta?', 'si / no')
while answer == ('si'):
    rand = random.randint(43,51)
    for i in range(rand):  
        c.circle(360, 15)
        c.speed(rand - i)
    answer = turtle.textinput('Quieres tirar de la ruleta?', 'si / no')
