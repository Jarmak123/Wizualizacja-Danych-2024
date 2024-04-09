import pandas as pd
import numpy as np
import openpyxl
import xlrd

def przyklad1():
    s=pd.Series([1,3,5,np.nan,6,8])
    print(s)
    print("###############")
    s=pd.Series([10,12,8,14], index=['Ala','Marek','Wiesiek','Eleonora'])
    print(s)
#przyklad1()

def przyklad2():
    data=[['Jablka',9],['Banany',23],['Winogrona',32],['Pomarańcze',12]]
    df=pd.DataFrame(data,columns=['Owoce','Ilosc'])
    print(df)

#przyklad2()

def przyklad3():
    data={'kraj':['Belgia','Indie','Brazylia'],'stolica':['Bruksela','New Delhi','Brasilia'],'Populacja':[11190846,1303171035,207847528]}
    df=pd.DataFrame(data,columns=['kraj','stolica','Populacja'])
    print(df, df.dtypes)

#przyklad3()

def przyklad4():
    daty=pd.date_range('2018-04-01',periods=5)
    print(daty)

    df=pd.DataFrame(np.random.randn(5,4), index=daty,columns=["a","b","c","d"])
    print(df)
#przyklad4()

def przyklad5():
    df=pd.read_csv('dane.csv',header=None,nrows=2) #czytanie z csv
    print(df)
    df.to_csv('plik.csv',header=None, index=False) #zapis do csv

    df=pd.read_excel('dane.xlsx','Arkusz1') #odczyt z excel
    print(df)
    df.to_excel('plik.xlsx', sheet_name='Imiona') #zapis do excel

#przyklad5()

def przyklad6():
    seria=pd.Series([10,12,8,14], index=['Juzek','Zientek','Urszula','Jagoda'])
    data={'Kraj':['Polska','Niemcy','Anglia','USA'],'Stolica':['Warszawa','Berlin','Londyn','Waszyngton'],'Populacja':[37000000,83000000,55000000,3330000000]}
    df=pd.DataFrame(data,columns=['Kraj','Stolica','Populacja'])
    print(seria)
    print('')
    print(seria['Juzek'])
    print(seria.Juzek)
    print(seria[1:])
    print('\n')
    print(df)
    print(df['Kraj'])
    print(df.iloc[[2],[0]])
    print(df.loc[[0],['Kraj']])
    print(df.at[0,'Kraj'])
    print('kraj:'+df.Kraj)
    print(df.sample()) #losowy element
    print(df.sample(2))  # losowy element
    print(df.sample(frac=0.25))  # losowy element procentowo
    print(df.sample(n=10,replace=True))  # losowy element z powtarzeniem
    print('##')
    print(df.head(1))#pierwszy element
    print(df.tail(1))  # ostatni element
    print(df.describe())
    print(df.T)
#przyklad6()

def przyklad7():
    seria = pd.Series([10, 12, 8, 14], index=['Juzek', 'Zientek', 'Urszula', 'Jagoda'])
    data = {'Kraj': ['Polska', 'Niemcy', 'Anglia', 'USA'], 'Stolica': ['Warszawa', 'Berlin', 'Londyn', 'Waszyngton'],
            'Populacja': [37000000, 83000000, 55000000, 3330000000]}
    df = pd.DataFrame(data, columns=['Kraj', 'Stolica', 'Populacja'])

    print(seria[(seria>10)])
    print(seria.where(seria>10))#to zamo co wyżej tylko wstawia nan
    print(seria.where(seria>10,'za duze')) #podstawia za duze za nan
    seria2=seria.copy()
    #seria2.where(seria>10,'za duze',inplace=True)
    print(seria2)
    print(seria[~(seria>10)])
    print(seria[(seria<13)&(seria>8)])
    print("\n")
    #warunki pobierania danych dla dataframe
    print(df[df['Populacja']<120000000])
    print(df[((df['Populacja']>100000)&(df.index.isin([0,2])))])
    print("####")
    szukaj=['USA','Polska']
    print(df.isin(szukaj))

    seria['Juzek']=69
    print(seria)
    seria['Aleksander']=1 #dodanie wartosci
    print(seria)
    new_seria=seria.drop(['Zientek'])
    print(new_seria)

    print("####")

    print(df)
    df.loc[4]='dodane'
    print(df)
    df.loc[5]=['Urugwaj','Ketrzyn',123456789]
    print(df)
    new_df=df.drop(4)
    print(new_df)
    df.drop(4,inplace=True)
    print(df)
    df['Kontynent']=['Europa','Europa','Europa','Dupa','Europa']
    print(df)
    print(df.sort_values(by='Kraj'))#SORTOWANIE
    grouped=df.groupby(['Kontynent'])#grupowanie
    print("##")
    print(grouped.get_group(('Europa',)))
    print("##")
    print(df.groupby(['Kontynent']).agg({'Populacja':['sum']}))
    print("Sumy cześciowe")
    tabela=pd.pivot_table(df,values=['Populacja'],index=['Kontynent'],columns=['Kraj'], aggfunc=np.sum,margins=True)
    print(tabela.stack('Kraj'))
#przyklad7()

def zadanie1():
    a=pd.read_excel('imiona.xlsx','Arkusz1')
    df=pd.DataFrame(a,columns=['Rok','Imie','Liczba','Plec'])
    print(df)

#zadanie1()

def zadanie2a():
    a = pd.read_excel('imiona.xlsx', 'Arkusz1')
    df = pd.DataFrame(a, columns=['Rok', 'Imie', 'Liczba', 'Plec'])

    print(df[df['Liczba']>1000])
    print(df.where(df['Liczba']>1000))

#zadanie2()

def zadanie2b():
    a = pd.read_excel('imiona.xlsx', 'Arkusz1')
    df = pd.DataFrame(a, columns=['Rok', 'Imie', 'Liczba', 'Plec'])

    print(df[(df['Imie']=='JAKUB')|(df['Imie']=='KUBA')])

#zadanie2b()

def zadanie2c():
    a = pd.read_excel('imiona.xlsx', 'Arkusz1')
    df = pd.DataFrame(a, columns=['Rok', 'Imie', 'Liczba', 'Plec'])

    print(df['Liczba'].sum())

#zadanie2c()

def zadanie2d():
    a=pd.read_excel('imiona.xlsx','Arkusz1')
    df=pd.DataFrame(a,columns=['Rok','Imie','Liczba','Plec'])

    group=df.groupby(['Rok'])
    print(group.sum({'Liczba':['sum']}))

#zadanie2d()

def zadanie2e():
    a = pd.read_excel('imiona.xlsx', 'Arkusz1')
    df = pd.DataFrame(a, columns=['Rok', 'Imie', 'Liczba', 'Plec'])
    where=df[(df['Rok']>=2000)&(df['Rok']<=2005)]
    wynik=where['Liczba'].sum()
    print(wynik)

#zadanie2e()

def zadanie2f():
    a = pd.read_excel('imiona.xlsx', 'Arkusz1')
    df = pd.DataFrame(a, columns=['Rok', 'Imie', 'Liczba', 'Plec'])
    dziewczyny=df[(df['Plec']=='K')]
    dziewczyny=dziewczyny['Liczba'].sum()
    chlopcy = df[(df['Plec'] == 'M')]
    chlopcy = chlopcy['Liczba'].sum()
    print(f'Dziewczyny:{dziewczyny}\n Chlopcy:{chlopcy}')

#zadanie2f()

def zadanie2g():
    a = pd.read_excel('imiona.xlsx', 'Arkusz1')
    df = pd.DataFrame(a, columns=['Rok', 'Imie', 'Liczba', 'Plec'])

    dziewczyny=df[(df['Plec']=='K')]
    dziewczyny=dziewczyny[dziewczyny['Liczba']==dziewczyny['Liczba'].max()]
    chlopacy=df[(df['Plec']=='M')]
    chlopacy=chlopacy[(chlopacy['Liczba']==chlopacy['Liczba'].max())]
    print(dziewczyny)
    print(chlopacy)

#zadanie2g()

def zadanie2h():
    a=pd.read_excel('imiona.xlsx','Arkusz1')
    df=pd.DataFrame(a,columns=['Rok','Imie','Liczba','Plec'])

    for i in range(2000,2018):
        dziewczyny=df[(df['Plec']=='K')&(df['Rok']==i)]
        dziewczyny=dziewczyny[dziewczyny['Liczba']==dziewczyny['Liczba'].max()]
        chlopak=df[(df['Plec']=='M')&(df['Rok']==i)]
        chlopak=chlopak[chlopak['Liczba']==chlopak['Liczba'].max()]
        print(f'Dziewczyna i Chłopak na rok: {i}')
        print(dziewczyny)
        print(chlopak)

#zadanie2h()

def zadanie3a():
    imp=pd.read_csv('zamowienia.csv',delimiter=';')
    df=pd.DataFrame(imp,columns=['Kraj','Sprzedawca','Data zamowienia','idZamowienia','Utarg'])
    print(df['Sprzedawca'].unique())

#zadanie3a()


def zadanie3b():
    imp=pd.read_csv('zamowienia.csv', delimiter=';')
    df=pd.DataFrame(imp,columns=['Kraj','Sprzedawca','Data zamowienia','idZamowienia','Utarg'])
    print(df.sort_values(by='Utarg').tail(5))

#zadanie3b()

def zadanie3c():
    imp = pd.read_csv('zamowienia.csv', delimiter=';')
    df = pd.DataFrame(imp, columns=['Kraj', 'Sprzedawca', 'Data zamowienia', 'idZamowienia', 'Utarg'])
    ilosc_zamowien_sprzedawcy=df['Sprzedawca'].value_counts()
    print(ilosc_zamowien_sprzedawcy)

#zadanie3c()

def zadanie3d():
    imp = pd.read_csv('zamowienia.csv', delimiter=';')
    df = pd.DataFrame(imp, columns=['Kraj', 'Sprzedawca', 'Data zamowienia', 'idZamowienia', 'Utarg'])

    suma_zamowien=df.groupby('Kraj')['Utarg'].sum()
    print(suma_zamowien)

#zadanie3d()

def zadanie3e():
    imp = pd.read_csv('zamowienia.csv', delimiter=';')
    df = pd.DataFrame(imp, columns=['Kraj', 'Sprzedawca', 'Data zamowienia', 'idZamowienia', 'Utarg'])

    df=df[(df['Kraj']=='Polska')&(df['Data zamowienia'].str.contains('2005'))]
    df=df['Utarg'].sum()
    print(df)

#zadanie3e()

def zadanie3f():
    imp = pd.read_csv('zamowienia.csv', delimiter=';')
    df = pd.DataFrame(imp, columns=['Kraj', 'Sprzedawca', 'Data zamowienia', 'idZamowienia', 'Utarg'])

    df=df[(df['Data zamowienia'].str.contains('2004'))]['Utarg'].mean()

    print(df)

#zadanie3f()

def zadanie3g():
    imp = pd.read_csv('zamowienia.csv', delimiter=';')
    df = pd.DataFrame(imp, columns=['Kraj', 'Sprzedawca', 'Data zamowienia', 'idZamowienia', 'Utarg'])

    dane_2004=df[(df['Data zamowienia'].str.contains('2004'))]

    dane_2004.to_csv('dane_2004.csv', index=False)

    dane_2005 = df[(df['Data zamowienia'].str.contains('2005'))]

    dane_2005.to_csv('dane_2005.csv', index=False)

zadanie3g()





