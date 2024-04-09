#pip install -r requirements.txt
import numpy as np
def wstep():
    '''
    a=np.arange(30)#utworzenie tablicy jednowymiarowej do 30 pozycji od 0
    #print(a)

    b=np.array([1,2,3,4,5,6,7,8,9,10])#utworzenie tablicy jednowymiarowej o twoich wartosciach
    print(b)

    a=np.arange(30,dtype='float64')#utworzenie tablicy jednowymiarowej do 30 z wlasnym typem danych
    #print(a)

    c=a.astype(int) #skopiowanie tablicy z innym typem znakow
    print(c)
    print(c.shape) #krztałt tablicy
    print(c.ndim)  #wymiar tablicy
    c=np.array([np.arange(4),np.arange(4)]) #utworzenie tablicy dwu wymiarowej
    print(c)
    print(c.ndim)

    zera=np.zeros((5,5)) #utworzenie tablicy z zer
    print(zera)
    jedynki=np.ones((2,2)) #utworzenie tablicy jedynek
    print(jedynki)
    puste=np.empty((2,2)) #utworzenie tablicy z losowymi elementami
    puste=puste.astype(np.int64)
    print(puste)
    x=puste[1,1]
    print(x)
    lin_liczby=np.linspace(1,2,5)
    print(lin_liczby)
    log=np.logspace(1,2,5)
    print(log)
    '''

    macierz, macierz2=np.indices((5,3))
    print(macierz)
    print(macierz2)
    print("$$$$$$$$$$$$$$$$$")
    macierzx,macierzy=np.mgrid[0:5,0:3]
    print(macierzx)
    print(macierzy)
    mat_diag=np.diag([a for a in range(5)])
    print(mat_diag)
    print("$$$$$$$$$$$$$$$$$")
    mat_diag = np.diag([a for a in range(5)],-2)
    print(mat_diag)
    z=np.fromiter(range(5),dtype='int32')
    print(z)

    jan="jan"
    jan_3=np.array(list(jan))
    jan_3=np.array(list(jan),dtype='S1')
    jan_3=np.array(list(b'jan'))
    jan_3=np.fromiter(jan,dtype='S1')
    jan_3 = np.fromiter(jan, dtype='U2')
    print(jan_3)

    mat=np.ones((2,2))
    mat2=np.ones((2,2))
    re=mat+mat2
    re=mat-mat2
    re=mat*mat2
    re=mat/mat2
    print(re)

    y=np.arange(10)
    print(y)
    s=slice(2,7,2)
    print(y[s])
    s=range(2,7,2)
    print(y[s])
    mat=np.arange(25)
    mat=mat.reshape((5,5))
    print(mat)
    print(mat[1:3,2:4])
    print(mat[:,range(2,6,2)])
#wstep()

def zadanie1():
    a=np.arange(2,40,2)
    print(a)

def zadanie2():
    #ndarray to zwykla tablica
    a=np.arange(0,10,0.5)
    print(a, a.dtype)
    b=np.array(a)
    b=b.astype(np.int64)
    print(b, b.dtype)

def zadanie3(n):
    a=np.arange(1,n*n+1)
    a=a.reshape((n,n))
    return a, a.shape

#print(zadanie3(3))

def zadanie4(podstawa, ilosc_poteg):
    a=np.logspace(start=podstawa, stop=False, num=ilosc_poteg, base=podstawa, dtype=int)
    return a

zadanie4()

def zadanie5(dlugosc_wektora):
    a=np.arange(start=dlugosc_wektora,stop=0,step=-1)
    diag=np.diag(a)
    return diag

#print(zadanie5(4))

def zadanie6():
    a=np.array([['m','','','','',''],
                ['a','u','','','',''],
                ['l','i','z','a','k',''],
                ['i','','','y','',''],
                ['n','','','','k',''],
                ['a','d','o','g','a','j']])
    return a

#print(zadanie6())

def zadanie7(n):
    a=np.arange(n*n).reshape((n,n))
    for i in range(n):
        a[i,i]=2
    for i in range(n-1):
        a[i, i+1] = 4
    for i in range(1,n):
        a[i, i -1] = 4
    return a

#print(zadanie7(3))

def zadanie8(tab,kierunek="poziom"):
    if kierunek=="pion":
        try:
            return tab[:,0:2]
        except:
            return "Ilosc wierszy lub kolumn nie pozwala na operacje"
    else:
        try:
            return tab[0:2]
        except:
            return "Ilosc wierszy lub kolumn nie pozwala na operacje"

print(np.arange(4*4).reshape((4,4)))
print(zadanie8(np.arange(4*4).reshape((4,4))))





