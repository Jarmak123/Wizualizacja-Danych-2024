import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')
import matplotlib
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import pandas as pd
import numpy as np
import openpyxl

def przyklad1():
    fig = plt.figure()
    ax=fig.add_subplot(projection='3d')

    t=np.linspace(0,2*np.pi,100)
    z=t
    x=np.sin(t)*np.cos(t)
    y=np.tan(t)
    ax.plot(x,y,z, label='zadanie1')

    ax.legend()
    plt.show()

#przyklad1()

def przyklad2():
    np.random.seed(19680801) #przez seed zawsze bedzie wygladalo tak samo

    def randrange(n, vmin, vmax):
        return (vmax - vmin)*np.random.rand(n)+vmin

    fig=plt.figure()
    ax=fig.add_subplot(111,projection='3d')

    n=100

    for c,m,zlow,zhigh in [('r','o',-50,-25),('b','^',-30,-5)]:
        xs=randrange(n,23,32)
        ys=randrange(n,0,100)
        zs=randrange(n,zlow,zhigh)
        ax.scatter(xs,ys,zs,c=c,marker=m)

    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')
    plt.show()

#przyklad2()

def przyklad3():
    fig=plt.figure()
    ax=fig.add_subplot(projection='3d')

    #generowanie danch
    x=np.arange(-5,5,0.25)
    y=np.arange(-5,5,0.25)
    x,y=np.meshgrid(x,y) #tworzenie punktow lokalizacji
    r=np.sqrt(x**2+y**2)
    z=np.sin(r)

    #rysowanie powierzchni
    surf=ax.plot_surface(x,y,z, cmap=cm.coolwarm, linewidth=0, antialiased=False)
    ax.set_zlim(-1.01,1.01) #ustawia limit na osi z
    ax.zaxis.set_major_locator(LinearLocator(10)) #ile kratek na osi z
    ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f')) #zaokrąglenie wyswietlanej liczby na osi do 2 miejsc

    #dodanie paska kolorow
    fig.colorbar(surf, shrink=0.5, aspect=5)
    plt.show()

#przyklad3()

def przyklad4():
    fig=plt.figure(figsize=(8,3)) #wielkosc wykresu w calach
    ax1=fig.add_subplot(1,2,1, projection='3d')
    ax2=fig.add_subplot(1,2,2, projection='3d')

    _x=np.arange(4)
    _y=np.arange(5)
    _xx,_yy=np.meshgrid(_x,_y)
    x,y=_xx.ravel(),_yy.ravel()
    top=x+y
    bottom=np.zeros_like(top)
    width=depth=1
    ax1.bar3d(x,y,bottom,width,depth,top,shade=True)
    ax1.set_title('Wykres zacieniony')
    ax2.bar3d(x,y,bottom,width,depth,top,shade=False)
    ax2.set_title('Wykres nie zacieniony')
    plt.show()

#przyklad4()

def zadanie1():
    z=np.arange(0,2*np.pi)
    x=np.sin(z)
    y=2*np.cos(z)

    fig=plt.figure()
    ax=fig.add_subplot(projection='3d')

    ax.plot(x,y,z, label='zadanie1')
    plt.legend()
    plt.show()

#zadanie1()

def zadanie2():
    np.random.seed(1) #przez seed zawsze bedzie wygladalo tak samo

    def randrange(n, vmin, vmax):
        return (vmax - vmin)*np.random.rand(n)+vmin

    fig=plt.figure()
    ax=fig.add_subplot(111,projection='3d')

    n=100

    for c,m,zlow,zhigh in [('r','o',-50,-25),('b','^',-30,-5),('r','o',-50,-25),('m','s',-2,-25),('g','r',-1,-3)]:
        xs=randrange(n,23,32)
        ys=randrange(n,0,100)
        zs=randrange(n,zlow,zhigh)
        ax.scatter(xs,ys,zs,c=c,marker=m)

    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')
    plt.show()

zadanie2()