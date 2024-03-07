import numpy as np

def tablica():
    a=np.arange(2)
    print(a)
    print(type(a))

tablica()

def przyklad1():
    a=np.array([0,1]) #inicjalizacja tablicy
    a=np.arange(2) #inicjalizacja tablicy
    print(a)
    print(type(a))
    print(a.dtype)
    a=np.arange(2,dtype='int64')
    print(a.dtype)
    b=a.astype(float)
    print(a.dtype)
    print(b)
    print(b.dtype)
    print(a.shape)
    print(b.shape)
    print(a.ndim)
    print(b.ndim)
    m=np.array([np.arange(2),np.arange(2)])
    print(m)
    print(type(m))

#przyklad1()

def zadanie1():
    tab=np.arange(2,41,2)
    print(tab)

#zadanie1()

def zadanie2():
    tab1=np.arange(1,10,0.5)
    print(tab1, tab1.dtype)
    tab2=tab1.astype(int)
    print(tab2, tab2.dtype)

#zadanie2()

def zadanie3():
    a=int(input("podaj liczbe naturalna: "))
    def zadanie3a(n):
        array=np.arange(1,n*n+1).reshape((n,n))
        return array
    b=zadanie3a(a)
    print(b)

#zadanie3()

def przykad2():
    zera=np.zeros((5,5))
    jedynki=np.ones((5,5))
    pusta=np.empty((2,2))

    poz_1=pusta[1,1]
    poz_1 = pusta[0, 1]

    liczby = np.arange(1,2,0.1)

    liczby_lin = np.linspace(1,2,5)
    z=np.indices((5,3))

    x,y=np.mgrid[0:5,0:5]

    mat_diag=np.diag([1,2,3,4,5])
    mat_diag_k=np_diag([a for a in range(5)],-2)

    print(mat_diag_k)

przykad2()