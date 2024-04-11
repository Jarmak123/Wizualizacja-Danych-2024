import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')
import matplotlib
import pandas as pd
import numpy as np
import openpyxl

def przyklad1():
    plt.plot([1, 2, 3, 4])
    plt.ylabel('jakies liczby')
    plt.show()

#przyklad1()

def przyklad2():
    plt.plot([1,2,3,4],[1,4,9,16],'ms--')
    plt.axis([0,6,0,20]) #xmin xmax ymin ymax
    plt.show()

#przyklad2()

def przyklad3():
    plt.plot([1,2,3,4],[1,4,9,16],'r')
    plt.plot([1,2,3,4],[1,4,9,16],'o')

    plt.axis([0,6,0,20])
    plt.show()

#przyklad3()

def przyklad4():
    t=np.arange(0.,5.,0.2)

    plt.plot(t,t,'r--',t,t**2,'bs',t,t**3,'g^')
    plt.show()

#przyklad4()

def przyklad5():
    x=np.linspace(0,2,100)

    plt.plot(x,x,label='liniowa')
    plt.plot(x,x**2,label='kwadratowa')
    plt.plot(x,x**3,label='sześcienna')

    plt.xlabel('etykieta x')
    plt.ylabel('etykieta y')

    plt.title('Prosty wykres')
    plt.legend()

    plt.show()

#przyklad5()

def przyklad6():
    x=np.arange(0,10,0.1)
    s=np.sin(x)
    plt.plot(x,s,label='sin(x)')

    plt.xlabel('x')
    plt.ylabel('sin(x)')

    plt.title('Wykres sin(x)')
    plt.legend()

    plt.show()

#przyklad6()

def przyklad7():
    data={'a':np.arange(50),'c':np.random.randint(0,50,50),'d':np.random.randn(50)} #słownik
    data['b']=data['a']+10*np.random.rand(50) #dodanie klucza do slownika
    data['d']=np.abs(data['d'])*100 #nadpisanie wartosi klucza

    plt.scatter('a','b',c='c',s='d',data=data) #c=color s=scale
    plt.xlabel('wartosc a')
    plt.ylabel('wartosc b')

    plt.show()

#przyklad7()

def przyklad8():
    x1=np.arange(0.0,2.0,0.02)
    x2=np.arange(0.0,2.0,0.02)

    y1=np.sin(2*np.pi*x1)
    y2=np.cos(2*np.pi*x2)

    plt.subplot(2,1,1)
    plt.plot(x1,y1,'-')
    plt.title('Dwa podwykresy')
    plt.ylabel('sin(x)')

    plt.subplot(2,1,2)
    plt.plot(x2,y2,'r-')
    plt.xlabel('x')
    plt.ylabel('cos(x)')

    plt.show()

#przyklad8()

def przyklad9():
    x1 = np.arange(0.0, 2.0, 0.02)
    x2 = np.arange(0.0, 2.0, 0.02)
    y1 = np.sin(2 * np.pi * x1)
    y2 = np.cos(2 * np.pi * x2)

    plt.subplot(3,2,1)
    plt.plot(x1,y1,'-')
    plt.title('Dwa podwykresy')
    plt.xlabel('x')
    plt.ylabel('sin(x)')

    plt.subplot(3,2,4)
    plt.plot(x2,y2,'r-')
    plt.xlabel('x')
    plt.ylabel('cos(x)')

    plt.subplot(3,2,5)
    plt.plot(x2, y2, 'r-')
    plt.xlabel('x')
    plt.ylabel('cos(x)')

    plt.show()

#przyklad9()

def przyklad10():
    etykiety=['K','M']
    wartosci=[345,435]
    c=['magenta','black']

    plt.bar(etykiety,wartosci, color=c)
    plt.xticks(rotation=45)
    plt.ylabel('Ilosc narodzin')
    plt.xlabel('Plec')

    plt.show()

#przyklad10()

def przyklad11():
    x=np.random.randn(10000)

    plt.hist(x,bins=50,facecolor='g',alpha=0.75,density=True)
    #bins oznacza ilsoc slupkow, facecolor ich kolor, aplha stopien przezroczystoci wykresu
    #density czy suma zostanie znormalizowana do rokladu prawdopodobienstwa czyli przedzial 0,1
    plt.xlabel('Wartosci')
    plt.ylabel('Prawdopodobienstwo')
    plt.title('Histogram')
    plt.grid(True)

    plt.show()

#przyklad11()

def przyklad12():
    zawodnicy=['Messi','Suarez','Dembele','Coutinho']
    bramki=[48,25,13,11]

    wedges,text,autotext=plt.pie(bramki,labels=zawodnicy,autopct=lambda pct:'{:.1f}%'.format(pct),
    textprops=dict(color='black'))
    plt.setp(autotext,size=14,weight='bold')
    plt.title('Pierwsza wersja wykresu')
    plt.legend(title='Zawodnicy')

    plt.show()

#przyklad12()

def przyklad13():
    zawodnicy = ['Messi', 'Suarez', 'Dembele', 'Coutinho']
    bramki = [48, 25, 13, 11]
    def prepare_label(pct,br):
        absolute=int(np.ceil(pct/100.*np.sum(br)))
        return "{:.1f}% \n({}/{})".format(pct,absolute,sum(bramki))

    wedges,texts,autotexts = plt.pie(bramki,labels=zawodnicy, autopct=lambda pct:prepare_label(pct,bramki),
    textprops=dict(color="black"))
    plt.setp(autotexts,size=14,weight='bold')
    plt.title('Druga wersja wykresu')
    plt.legend(title='Zawodnicy')

    plt.show()

#przyklad13()

def zadanie1():
    x=np.arange(1,21)
    y=np.ones(20)/x
    plot=plt.plot(x,y)

    plt.axis([0,len(x), 0, 1])  # xmin xmax ymin ymax

    plt.show()

#zadanie1()

def zadanie2():
    x=np.arange(1,21)
    y=np.ones(20)/x
    plot=plt.plot(x,y,'g>:',label='f(x)=1/x')

    plt.ylabel('f(x)')
    plt.xlabel('x')
    plt.axis([0,len(x), 0, 1])  # xmin xmax ymin ymax
    plt.legend()

    plt.show()

#zadanie2()

def zadanie3():
    x=np.arange(0,30,0.1)
    y1=np.sin(x)
    y2=np.cos(x)

    plt.plot(x,y1,'r',label='Sin')
    plt.plot(x,y2,'b',label='Cos')
    plt.ylabel('y')
    plt.xlabel('x')
    plt.legend()

    plt.show()

#zadanie3()

def zadanie4():
    x=np.arange(0,30,0.1)
    y1=np.sin(x)
    y2=np.sin(x)+2
    y2=-y2

    plt.plot(x,y1,label='sin(x)')
    plt.plot(x,y2,'y',label='sin(x)')
    plt.ylabel('sin(x)')
    plt.xlabel('x')
    plt.title('Wykres sin(x), sin(x)')
    plt.legend()

    plt.show()

#zadanie4()

def zadanie5():
    imp=pd.read_csv('iris.data', delimiter=',', header=None)

zadanie5()



