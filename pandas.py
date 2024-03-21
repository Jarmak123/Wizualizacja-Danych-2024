import pandas as pd
import numpy as np
import xlrd
import openpyxl

def przyklad1(): #Series
    s=pd.Series([1,3,5,np.nan,6,8])
    print(s)

    s=pd.Series([10,12,8,14], index=['Ala','Marek','Wiesiek','Eleonora'])
    print("")
    print(s)
#przyklad1()

def przyklad2(): #dataFrame na podstawie listy
    data=[['Jabłka',9],['Banany',23],['Winogrona',32],['Pomarańcze',12]]
    df=pd.DataFrame(data,columns=['Owoce','Ilość'])
    print(df)
    #inny sposób
    print("")
    df1=pd.DataFrame(data)
    df1.columns='Owoce','Ilość'
    print(df1)
#przyklad2()

def przyklad3(): #tworzenie DataFrame na podstawie słownika
    #slownik={"kraj":"Polska","stolica":"Warszawa","Populacja":3782700}
    data={"Kraj":["Belgia",'Indie','Brazylia'],'Stolica':['Bruksela','New Delhi','Brasilia'],'Populacja':[11190846,1303171035,207847528]}
    df=pd.DataFrame(data,columns=['Kraj','Stolica','Populacja']) #jesli usuniemy populacja to nie pokaze sie cala kolumna
    print(df)
    print(df.dtypes)#sprawdzenie typu dla każdej kolumny

#przyklad3()

def przyklad4():
    daty=pd.date_range('20180401',periods=5)
    print(daty)
    print("")

    df=pd.DataFrame(np.random.randn(5,4),index=daty,columns=list('abcd'))
    print(df)

#przyklad4()

def przyklad5(): #tworzenie dataframe z zewnetrznych źródeł
    df=pd.read_csv('dane.csv', header=None, nrows=2) #odczyt
    #print(df)
    df.to_csv('plik.csv', header=None, index=False)
    #Excel - wymagana biblioteka openpyxl i/lub xlrd
    #importowanie ich nie zawsze ejst konieczne muszą być jendka one zainstalowane

    df=pd.read_excel('imiona.xlsx','Arkusz1')#po przecinku i w '' wybieramy strone w excelu
    print(df)
    df.to_excel('z_indeksami.xlsx', sheet_name='Wytaki z indeksami')

#przyklad5()

def przyklad6(): #pobieranie danych ze struktur
    seria = pd.Series([10, 12, 8, 14], index=['Ala', 'Marek', 'Wiesiek', 'Eleonora'])
    data = {"Kraj": ["Belgia", 'Indie', 'Brazylia'], 'Stolica': ['Bruksela', 'New Delhi', 'Brasilia'],
            'Populacja': [11190846, 1303171035, 207847528]}
    df = pd.DataFrame(data, columns=['Kraj', 'Stolica', 'Populacja'])

    print(seria['Wiesiek']) #dostanie sie do konkretnej wartosci
    print(seria.Wiesiek)
    print("")
    print(df[1:],'\n') #wycinianie
    print(df['Populacja']) #po etykiecie
    print("")
    print(df.iloc[[0],[0]]) #pobranie danych po indeksie wiersza i kolumny
    print(df.loc[[0],['Kraj']]) #Pobieranie po indeksie wiersza i etykiery kolumy
    print(df.at[0,'Kraj'])
    print("")
    print('kraj: ' + df.Kraj) #wywołanie jak w pętli dla każego z jakimś przedrostkiem
    print("")
    print(df.sample()) #losowy element z tablicy
    print(df.sample(2)) #2 losowe elementy
    print(df.sample(frac=0.5)) #ilość elementow procentowo
    print(df.sample(n=10, replace=True))#więcej loswych elementow z powtorzeniami
    print("")
    print(df.head())#wyświetlanie określoną liczbe pierwszych lub ostatnich elementow
    print(df.head(2))
    print(df.tail(1))#ostatnich
    print("")
    print(df.describe())#statystyka dla wartosci
    print(df.T)#transpozycja

#przyklad6()

def przyklad7():
    seria = pd.Series([10, 12, 8, 0], index=['Ala', 'Marek', 'Wiesiek', 'Eleonora'])
    data = {"Kraj": ["Belgia", 'Indie', 'Brazylia'], 'Stolica': ['Bruksela', 'New Delhi', 'Brasilia'],
            'Populacja': [11190846, 1303171035, 207847528]}
    df = pd.DataFrame(data, columns=['Kraj', 'Stolica', 'Populacja'])

    print(seria[(seria>1)]) #wyswietla wartosci gdzie seria jest  wieksza od 1
    print(seria.where(seria>10)) #wyswietla kolekcje w orygialnej liczebnosci ale dla tych ktore nie spelniaja warunkow jest przypisywany NaN
    print(seria.where(seria>10,'za duze')) #mozemy do tego dac wartosc ktora bedzie zastepowala NaN
    print("")
    seria2=seria.copy()
    seria2.where(seria2>10,0,inplace=True) #sprawia ze where modyfikuje tabele
    print(seria2)
    print("")
    print(seria[~(seria>10)]) #wyswietla wartosc gdzie wartosc nie jest wieksza od 10 (negacja)
    print(seria[(seria<13)&(seria>8)]) #można łączyć warunki

    #warunki pobierania danych dla fata frame
    print(df[df['Populacja']>1200000000])
    print(df[((df.Populacja>1000000)&(df.index.isin([0,2])))])
    print("")
    szukaj=['Belgia','Brasilia']
    print(df.isin(szukaj))

#przyklad7()

def przyklad8():
    seria = pd.Series([10, 12, 8, 0], index=['Ala', 'Marek', 'Wiesiek', 'Eleonora'])
    data = {"Kraj": ["Belgia", 'Indie', 'Brazylia'], 'Stolica': ['Bruksela', 'New Delhi', 'Brasilia'],
            'Populacja': [11190846, 1303171035, 207847528]}
    df = pd.DataFrame(data, columns=['Kraj', 'Stolica', 'Populacja'])

    seria['Wiesiek']=15 #aktualizacja wartosci
    print(seria.Wiesiek)

    seria['Alan']=16#dodawanie wartosci
    print(seria)

    df.loc[4]='dodane'
    print(df)
    df.loc[5]=['Polska','Waraszawa',38675467]#dodawanie wartosci
    print(df)

    new_df=df.drop([4]) #robi kopie df z usunietymi wartosciami
    print(new_df)

    df.drop([4], inplace=True) #modyfikuje df tak że usuwa z niego wartosci z indexu 4
    #df.drop('Kraj',axis=1,inplace=True) usunięcie całej kolumny

    df['Kontynet']=['Europa','Azja','Ameryka Południowa','Europa']
    print(df)#dodanie nowej kolumny

    print(df.sort_values(by='Kraj'))#sortowanie po kraju
    grouped=df.groupby(['Kontynet'])#grupowanie po kontynencie
    print("")
    print(grouped.get_group('Europa'))

przyklad8()