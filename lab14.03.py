import numpy as np

def przyklad1():
    a=np.array([20,30,40,50])
    b=np.arange(4)
    print(f'Tablica B: {b}')
    c=a-b
    print(f'Tablica C: {c}')
    print(f'Tablica C z operacją kwadratu liczby: {c**2}')
    print(f'Tablica A: {a}')
    a+=b
    print(f'Tablica A (zmodyfikowana): {a}')
    a-=b
    print(f'Tablica A (pierwotnie): {a}')

def przyklad2():
    b=np.arange(12).reshape(3,4)
    print(f'Tablica B (w przykladzie 2):\n {b}')
    print(f'Suma całej tablicy B: {b.sum()}')
    print(f'Suma każdej z kolumn tablicy B: {b.sum(axis=0)}')
    print(f'Minimum każdego wiersza tablicy B: {b.min(axis=1)}')
    print(f'Skumulowana suma dla rzędu tablicy B:\n {b.cumsum(axis=1)}')

def przyklad3():
    a=np.arange(3)
    b=np.arange(3)
    print(f'Iloczyn sklarny tablic A i B: {a.dot(b)}')
    print(f'Inny sposób: {np.dot(a,b)}')

def przyklad4():
    a=np.ones(3, dtype=np.int32) #macierz całkowita jedynek
    print(a.dtype.name)
    b=np.linspace(0,np.pi,3) #macierz zmienno przecinkowa ułóżona równo w liniach pod wzgledem dlugosci liczb
    print(b.dtype.name)
    c=a+b
    print(c) #wynikiem jest linspace
    print(c.dtype.name)
    d=np.exp(c*1j) #macierz liczb zespolonych
    print(d)
    print(d.dtype.name)


#przyklad1()
#przyklad2()
#przyklad3()
#przyklad4()

def zadanie1():
    a=np.array([5,4,3])
    b=np.array([3,2,1])
    c=a*b
    print(f'Mnożenie tablicy A:\n{a}\noraz B:\n{b}\nwynik to:\n{c}')

def zadanie2():
    a=np.array([np.random.randint(10,51) for i in range(9)]).reshape(3,3)
    b= np.array([np.random.randint(10, 51) for i in range(16)]).reshape(4, 4)
    print(a)
    print(b)
    print(a.min(axis=0))#kolumny
    print(a.min(axis=1))#wiersze
    print(b.min(axis=0))
    print(b.min(axis=1))

def zadanie3():
    a = np.array([5, 4, 3])
    b = np.array([3, 2, 1])
    c=np.dot(a,b)
    print(f'Iloczyn skalarny a i b to: {c}')

def zadanie4():
    a=np.arange(1,2.5,0.5,dtype='float64')
    b=np.arange(3,dtype='int64')
    print(a)
    print(b)
    c=a*b
    print(c)

#zadanie1()
#zadanie2()
#zadanie3()
#zadanie4()

def przyklad5():
    b=np.arange(3)
    print(b)
    print(np.exp(b))
    print(np.sqrt(b))
    c=np.array([2.,-1.,4.])
    print(np.add(b,c))

#przyklad5()

def zadanie5():
    x=np.array([[1,2,3],[2,4,5]])
    print(x)
    a=np.sin(x)
    print(a)

def zadanie6():
    x = np.array([[94,32,12], [321,5,6]])
    print(x)
    b=np.cos(x)
    print(b)

def zadanie7(a,b):
    return print(np.add(a,b))




#zadanie5()
#zadanie6()
a = b = np.array([1,2])
#zadanie7(a,b)

def przyklad6(): #iteracja po macierzy
    b=np.arange(6).reshape(3,2)
    print(b)
    for a in b:
        print(a)

def przyklad7(): #iteracja po macierzy jakby była płaska
    b=np.arange(6).reshape(3,2)
    print(b)
    for a in b.flat:
        print(a)

#przyklad6()
#przyklad7()

def zadanie8():
    a=np.arange(9).reshape(3,3)
    print(a)
    for i in a:
        print(i)

def zadanie9():
    a=np.arange(9).reshape(3,3)
    print(a)
    for i in a.flat:
        print(i)

#zadanie8()
#zadanie9()

def przyklad8():
    b=np.arange(6)
    print(b)
    print(b.shape)
    c=np.array([np.arange(3), np.arange(3), np.arange(3)])
    print(c)
    print(c.shape)

def przyklad9():
    b=np.arange(6)
    print(b)
    print(b.shape)
    c=b.reshape((2,3))
    print(c)
    print(c.shape)
    d=c.reshape((3,2))
    print(d)
    print(d.shape)
    e=d.ravel() #spłaszczenie macierzy
    print(e)
    print(e.shape)
    f=c.T #transpozycja macierzy
    print(f)
    print(f.shape)

#przyklad8()
#przyklad9()

def zadanie10():
    a=np.arange(81).reshape(9,9)
    print(a)
    x=a.ravel()
    print(x)

def zadanie11():
    a=np.arange(12)
    x=a.reshape((3,4))
    y=a.reshape((4,3))
    z=a.reshape((2,6))
    print(x)
    print(y)
    print(z)
    x = x.ravel()
    y = y.ravel()
    z = z.ravel()
    print(x)
    print(y)
    print(z)

#zadanie10()
zadanie11()
