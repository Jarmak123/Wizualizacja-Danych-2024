import numpy as np

def przyklad1():
    a=np.array([20,30,40,50])
    b=np.arange(4)
    print(b)
    print(a)
    c=a-b
    print(c)
    print(b**2)
    a+=b
    print(a)
    a-=b
    print(a)

#przyklad1()

def przyklad2():
    v=np.arange(12).reshape(3,4)
    print(v)
    print(v.sum())
    print(v.sum(axis=0))
    print(v.min(axis=1))
    print(v.cumsum(axis=1))
#przyklad2()

def przyklad3():
    a=np.arange(3)
    b=np.arange(3)
    print(a.dot(b))
    print(np.dot(a,b))
#przyklad3()

def przyklad4():
    a=np.ones(3,dtype=np.int32)
    print(a,a.dtype)
    b=np.linspace(0,np.pi,3)
    print(b,b.dtype)
    c=a+b
    print(c,c.dtype)
    d=np.exp(c*1j)
    print(d)
#przyklad4()

def zadanie1():
    a=np.ones(3)
    b=np.ones(3)
    c=np.dot(a,b)
    print(a)
    print(b)
    print(c)
    print(a*b)
#zadanie1()

def zadanie2():
    a=np.array([np.random.randint(10,51) for i in range(9)]).reshape((3,3))
    print(a)
    b=np.array([np.random.randint(10,51) for i in range(16)]).reshape((4,4))
    print(b)
    print(a.min(axis=1))#wiersze
    print(a.min(axis=0))#kolumny
    print(b.min(axis=1))
    print(b.min(axis=0))

#zadanie2()


def zadanie4():
    a=np.arange(5)
    b=np.arange(5,7.5,0.5)
    print(a)
    print(b)
    print(a*b)

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
    a=np.arange(6).reshape((2,3))
    print(a)
    b=np.sin(a)
    print(b)

#zadanie5()

def zadanie6():
    a=np.arange(6).reshape((2,3))
    print(a)
    b=np.cos(a)
    print(b)

#zadanie6()

def zadanie7(a,b):
    wynik=np.add(a,b)
    return wynik

#print(zadanie7(np.array([1,2,3]),np.array([2,2,2])))

def przyklad6():
    b=np.arange(6).reshape(3,2)
    print(b)

    for a in b:
        print(a)

    b=b.flat

    for a in b:
        print(a)
#przyklad6()

def zadanie8():
    a=np.arange(9).reshape((3,3))
    for i in a:
        print(i)

#zadanie8()

def zadanie9():
    a=np.arange(9).reshape((3,3))
    for i in a.flat:
        print(i)

#zadanie9()

def przyklad8():
    b=np.arange(6)
    print(b,b.shape)
    a=np.array([np.arange(3),np.arange(3),np.arange(3)])
    print(a,a.shape)
    c=b.reshape((2,3))
    print(c)
    d=c.ravel()
    print(d)
    print(c.T)
#przyklad8()

def zadanie11():
    a=np.arange(12)
    print(a)
    a=a.reshape((3,4))
    print(a)
    a = a.reshape((4,3))
    print(a)
    a = a.reshape((2,6))
    print(a)
    a = a.ravel()
    print(a)

zadanie11()
