import turtle

# Ustawienia okna gry
okno = turtle.Screen()
okno.title("Ping Pong")
okno.bgcolor("black")
okno.setup(width=800, height=600)
okno.tracer(0)

# Paletki
paletka_gracz = turtle.Turtle()
paletka_gracz.speed(0)
paletka_gracz.shape("square")
paletka_gracz.color("white")
paletka_gracz.shapesize(stretch_wid=6, stretch_len=1)
paletka_gracz.penup()
paletka_gracz.goto(-350, 0)

paletka_przeciwnik = turtle.Turtle()
paletka_przeciwnik.speed(0)
paletka_przeciwnik.shape("square")
paletka_przeciwnik.color("white")
paletka_przeciwnik.shapesize(stretch_wid=6, stretch_len=1)
paletka_przeciwnik.penup()
paletka_przeciwnik.goto(350, 0)

# Piłka
pilka = turtle.Turtle()
pilka.speed(40)
pilka.shape("square")
pilka.color("white")
pilka.penup()
pilka.goto(0, 0)
pilka.dx = 0.15
pilka.dy = -0.15

# Ruch paletki gracza
def paletka_gracz_gora():
    y = paletka_gracz.ycor()
    if y < 250:
        y += 20
    paletka_gracz.sety(y)

def paletka_gracz_dol():
    y = paletka_gracz.ycor()
    if y > -240:
        y -= 20
    paletka_gracz.sety(y)

# Bindowanie klawiszy
okno.listen()
okno.onkeypress(paletka_gracz_gora, "w")
okno.onkeypress(paletka_gracz_dol, "s")

# Główna pętla gry
while True:
    okno.update()

    # Ruch pilki
    pilka.setx(pilka.xcor() + pilka.dx)
    pilka.sety(pilka.ycor() + pilka.dy)

    # Sprawdzanie kolizji z górną i dolną krawędzią okna
    if pilka.ycor() > 290:
        pilka.sety(290)
        pilka.dy *= -1

    if pilka.ycor() < -290:
        pilka.sety(-290)
        pilka.dy *= -1

    # Sprawdzanie kolizji z bokami planszy i paletkami
    if (pilka.xcor() > 390 or pilka.xcor() < -390):
        pilka.dx *= -1
        
    if (pilka.xcor() > 340 and pilka.xcor() < 350) and (pilka.ycor() < paletka_przeciwnik.ycor() + 50 and pilka.ycor() > paletka_przeciwnik.ycor() - 50):
        pilka.color("blue")
        pilka.setx(340)
        pilka.dx *= -1

    elif (pilka.xcor() < -340 and pilka.xcor() > -350) and (pilka.ycor() < paletka_gracz.ycor() + 50 and pilka.ycor() > paletka_gracz.ycor() - 50):
        pilka.color("red")
        pilka.setx(-340)
        pilka.dx *= -1
