import math
import turtle


def zadanie1a():
    ab=int(input("Podaj bok AB ")) #10
    ac = int(input("Podaj bok AC ")) #6
    bc = int(input("Podaj bok BC ")) #5
    kat = math.degrees(math.acos((ab**2-ac**2-bc**2)/(-2*ac*bc)))

    return kat

#print(zadanie1a())

def zadanie1b():
    ac=int(input("Podaj bok ac "))
    bc=int(input("Podaj bok bc "))
    kat=int(input("Podaj kat pomiedzy nimi "))
    kat=math.cos(kat)
    bok=math.sqrt((ac**2+bc**2)-(2*ac*bc)*kat)
    return math.ceil(bok)

#print(zadanie1b())

def zadanie2():
    win_length=500
    win_height=500

    turtle.screensize(win_length, win_height)
    bob=turtle.Turtle()
    bob.color('red')
    bob.shape('arrow')
    bob.speed(20)

    bob.right(60)
    bob.forward(40)
    bob.left(60)
    for i in range(0,6):
        bob.forward(40)
        bob.left(120)
        bob.forward(40)
        bob.right(60)

    bob.left(120)
    bob.forward(40)
    bob.left(60)

    bob.color('green')
    bob.right(60)
    for i in range(0,6):
        for i in range(0,12):
            bob.forward(50)
            bob.left(30)
        bob.left(60)

    turtle.exitonclick()

zadanie2()