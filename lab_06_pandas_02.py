import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def przyklad1():
    y=np.random.randn(100)
    x=pd.date_range('1/1/2015', periods=100)
    ts=pd.Series(y,index=x)
    print(ts)
    ts=ts.cumsum()
    print(ts)
    ts.plot(x=x,y=y)
    plt.show()

#przyklad1()

def przyklad2():
    data={'Kraj':['Polska','Ukraina','USA','Rumunia'],'Stolica':['Warszawa','Kijow','Waszyngton','Rumcajs'],'Populacja':[30,20,10,5],'Kontynent':['Europa','Europa','Ameryka','Ameryka']}
    df=pd.DataFrame(data,columns=['Kraj','Stolica','Populacja','Kontynent'])
    print(df)

    grupa=df.groupby(['Kontynent']).agg({'Populacja':['sum']})
    print(grupa)

    wykres=grupa.plot.bar(rot=0)
    wykres.set_ylabel('Populacja [mld]')
    wykres.set_xlabel('Kontynent')

    wykres.legend()
    plt.title('Populacja z podziałem na kontynenty')
    plt.show()

#przyklad2()

def przyklad3():
    df=pd.read_csv('./wprowadzenie/dane.csv', delimiter=';')
    grupa=df.groupby(['Imię i nazwisko'])['Wartość zamówienia'].sum()

    wykres=grupa.plot.pie(subplots=True, autopct='%.2f %%', fontsize=20, figsize=(6,6))
    plt.title('Suma zamownien dla sprzedawcy')
    plt.show()

#przyklad3()

def przyklad4():
    ts=pd.Series(np.random.randn(1000),index=pd.date_range('1/1/2015',periods=1000))
    print(ts)
    ts=ts.cumsum()
    print(ts)

    df=pd.DataFrame(ts)
    print(df)
    df['Rolling avg']=df.rolling(window=50).mean()
    print(df)
    df.plot()
    plt.show()
#przyklad4()

def zadanie1():
    imp=pd.read_excel('imiona.xlsx')
    df=pd.DataFrame(imp,columns=['Rok','Imie','Liczba','Plec'])
    df=df.groupby('Rok')['Liczba'].sum()
    wykres=df.plot()
    plt.show()

#zadanie1()

def zadanie2():
    imp=pd.read_excel('imiona.xlsx','Arkusz1')
    df=pd.DataFrame(imp,columns=['Rok','Imie','Liczba','Plec'])
    df=df.groupby('Plec')['Liczba'].sum()
    wykres=df.plot.bar()
    plt.show()

#zadanie2()

def zadanie3():
    imp=pd.read_excel('imiona.xlsx','Arkusz1')
    df=pd.DataFrame(imp,columns=['Rok','Imie','Liczba','Plec'])
    df=df[(df['Rok']==2017)|(df['Rok']==2016)|(df['Rok']==2015)|(df['Rok']==2014)|(df['Rok']==2013)]
    df=df.groupby(['Plec'])['Liczba'].sum()
    print(df)
    df.plot.pie(autopct='%.2f %%')
    plt.show()

#zadanie3()

def zadanie4(podstawa, ilosc_poteg):
    a=np.logspace(1,10,num=10,base=2)
    return a

print(zadanie4(2,4))

