import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import openpyxl
import openpyxl
matplotlib.use("TkAgg")

def przyklad1():
    y = np.random.randn(100)
    x = pd.date_range('1/1/2015',periods=100)
    ts = pd.Series(y,index=x)
    print(ts)
    print("###############")
    ts = ts.cumsum()
    print(ts)
    ts.plot(x=x,y=y)
    plt.show()
#przyklad1()

def przyklad2():
    data={'Kraj':['Belgia','Indie','Brazylia','Polska'],'Stolica':['Bruksela','New Delhi','Brasilia','Warszawa'],
    'Kontynent':['Europa','Azja','Ameryka Południowa','Europa'],
    'Populacja':[11190846,1303171035,207847528,38675467]}
    df = pd.DataFrame(data,columns=['Kraj','Stolica','Kontynent','Populacja'])
    print(df)

    print("##############################################################################")

    grupa = df.groupby(['Kontynent']).agg({'Populacja':['sum']})
    print(grupa)

    wykres=grupa.plot.bar(rot=0)
    wykres.set_ylabel('Populacja [mld]')
    wykres.set_xlabel('Kontynent')

    wykres.legend()
    plt.title('Populacja z podziałem na kontynenty')
    plt.show()

#przyklad2()

def przyklad3():
    df=pd.read_csv('dane.csv', delimiter=";")
    grupa=df.groupby(['Imię i nazwisko'])["Wartość zamówienia"].sum()
    #wykres kołowy
    #figsize ustawia wiwlkosc wykresu w calach
    wykres=grupa.plot.pie(subplots=True,autopct='%.2f %%', fontsize=20, figsize=(6,6))
    plt.title('Suma zamowien dla sprzedawcy')
    plt.show()

#przyklad3()

def przyklad4():
    ts=pd.Series(np.random.randn(1000),index=pd.date_range("1/1/2015",periods=1000))
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
    csv=pd.read_excel('imiona.xlsx')
    grupa=csv.groupby('Rok')['Liczba'].sum()
    grupa.plot(ylabel="Liczba urodzeń", xlabel=grupa.index, figsize=(6,6), rot=90)
    plt.title("Liczba urodzonych dzieci w danym roku")
    plt.show()
#zadanie1()

def zadanie2():
    excel=pd.read_excel('imiona.xlsx')
    grupa=excel.groupby('Plec')['Liczba'].sum()
    grupa=grupa.plot.bar(ylabel="Liczba urodzeń", xlabel=grupa.index, figsize=(6, 6), rot=90)
    grupa=grupa.reset_index()
    plt.show()
    print(grupa)
zadanie2()
