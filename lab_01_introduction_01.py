import math
import random
def zadanie1():
    wynik = []
    while(True):
        x = input("Podaj liczbe którą chcesz dodać do swojej listy ")
        if x.isdigit():
            wynik.append(x)
            print(wynik)
        elif x=='end':
            break
        else:
            print(wynik)
            continue
    return wynik

#print(zadanie1())

def zadanie2():
    print("zadanie bada monotonicznosc funkcji Y=ax+b \nPodaj zmienne podaj A i B")
    a=int(input("Podaj a: "))
    b=int(input("Podaj b: "))
    print(f'Twoja funkcja: y={a}x+{b}', end='')
    if a>0:
        return " jest rosnąca"
    elif a<0:
        return " jest malejąca"
    elif a==0:
        return " jest stała"

#print(zadanie2())

def zadanie3():
    print("zadanie bada czy dwie proste oznaczone wzorem y=(a1x+b1) i y=(a2x+b2) są do siebie równoległe lub prostopadłe")
    a1 = float(input("Podaj wartosc a1 "))
    b1 = float(input("Podaj wartosc b1 "))
    print(f'PłaszczynaA: y={a1}x+{b1}')
    a2 = float(input("Podaj wartosc a2 "))
    b2 = float(input("Podaj wartosc b2 "))
    print(f'PłaszczynaA: y={a1}x+{b1}\nPłaszczyznaB:y={a2}x+{b2}')
    if a1==a2:
        print("Twoje płaszczyzny są równoległe i ",end='')
    else:
        print("Twoje płaszczyzny nie są równoległe i ",end='')
    if a1*a2==-1:
        return "są prostopadłe"
    else:
        return "nie są prostopadłe"

#print(zadanie3())

def zadanie4(a=2,b=2):
    print("zadanie bada przeciwprostokątną dowolnego trójąta")
    c=a**2+b**2
    c=math.sqrt(c)
    return (f'Przeciwprostokątna trójkąta o bokach {a} i {b} wynosi {c}')

#print(zadanie4())

def zadanie5(a1=1,r=1,ile_elementow=10):
    print("zadanie sumuje ciąg liczb")
    wynik=0
    for i in range(a1,ile_elementow+1,r):
        wynik=wynik+i
    return wynik

#print(zadanie5())

def zadanie6A():
    lista=['ala','ma','kota']
    for i in range(0,len(lista)):
        lista[i]=lista[i]+"!"
    return lista

#print(zadanie6A())

def zadanie6B():
    lista = ['ala', 'ma', 'kota']
    wynik = []
    for i in range(0,len(lista)):
        wynik.append(lista[i]+"!")
    return wynik

#print(zadanie6B())

def guess_the_number_zadanie7():
    liczba_punktow=0
    rundy=0
    print("Zgadnij liczbę od 1 do 10!")
    while(True):
        wylosowana_liczba=random.randint(1,10)
        x=int(input("Wpisz liczbę: "))
        if(wylosowana_liczba==x):
            liczba_punktow=liczba_punktow+10
            print(f'Brawo! Odgadłeś/aś liczbę. Zyskujesz 10 punktow. Suma punktów to: {liczba_punktow}')
            rundy=rundy+1
        else:
            liczba_punktow=liczba_punktow-1
            print(f'Niestety to nie ta liczba. Tracisz punkt. Suma punktów to: {liczba_punktow}')
            rundy = rundy + 1
        if rundy==5:
            return (f'Koniec gry! Twój wynik to {liczba_punktow}')

#print(guess_the_number_zadanie7())

def zadanie8():
    print("zadane bada digital root")
    x=str(input("Podaj liczbe "))
    wynik=0
    for i in x:
        wynik=wynik+int(i)
    return wynik

#print(zadanie8())

def zadanie9():
    print("Gra - tabliczka mnożenia")
    rundy=0
    pop_odp = 0
    while (True):
        a=random.randint(1,9)
        b=random.randint(1,9)
        c=a*b
        print("Podaj odpowiedź:")
        odp=int(input(f'{a}*{b}=? '))
        if odp==c:
            print("Brawo! Prawidłowa odpowiedź")
            rundy=rundy+1
            pop_odp=pop_odp+1
            print(f'{rundy}')
        else:
            print(f'Błędna odpowiedź. Poprawną odpowiedzią jest {c}')
            rundy=rundy+1
            print(f'{rundy}')
        if rundy==10:
            return (f'Koniec gry! Uzyskałeś {pop_odp}/10 punktów')

#print(zadanie9())
'''
    *
   * *
  *****
 *     *
*       *
'''
def zadanie10():
    print("program tworzy litere A o wybranej wielkosci:")
    x=int(input("Podaj wielkosc litery "))
    for i in range(1,x+1):
        print(" "*(x-i)+"*")
        if i==x-4:
            print(" " * (x - i) + ("*"*(x+3)))
    return 0

print(zadanie10())