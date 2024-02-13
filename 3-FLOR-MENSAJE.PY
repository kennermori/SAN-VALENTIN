# Código escrito por Kenner Mori
import turtle
import colorsys as cs

turtle.setup(800, 800)
turtle.speed(0)
turtle.tracer(10)
turtle.width(2)
turtle.bgcolor("black")

# Definir la función de mensaje.


def draw_message(message):
    turtle.penup()
    turtle.goto(-285, -320)
    turtle.color("white")
    # Puedes cambiar el tipo de texto
    turtle.write(message, font=("Arial black", 20, "bold"))
    turtle.pendown()


def draw_art():
    for j in range(25):
        for i in range(15):
            turtle.color(cs.hsv_to_rgb(i/15, 1, 1))
            turtle.right(90)
            turtle.circle(200-j*4, 90)
            turtle.left(90)
            turtle.circle(200-j*4, 90)
            turtle.right(180)
            turtle.circle(50, 24)


draw_art()
draw_message("FELIZ SAN VALENTÍN, TE AMO MUCHO")

turtle.hideturtle()
turtle.done()
