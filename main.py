import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
import numpy as np

def pandas1():
    imp=pd.read_csv('Pokemon.csv', delimiter=',', encoding='latin')
    print(imp.head(4))

#pandas1()

def pandas2():
    imp = pd.read_csv('Pokemon.csv', delimiter=',', encoding='latin')

    where=imp[imp['Total']>300]

    print(where)
    print('Nie jesteśmy w stanie stwierdzic ile jest dokładnie kolumn większych od 300 w tym przypadku,'
          'ponieważ kolumny są nie posortowane.')

#pandas2()

def pandas3():
    imp = pd.read_csv('Pokemon.csv', delimiter=',', encoding='latin')
    print(imp.describe())

#pandas3()

def pandas4():
    imp = pd.read_csv('Pokemon.csv', delimiter=',', encoding='latin')

    grouped=imp.groupby(imp['Type 1'])['Defense'].mean()
    grouped1 = imp.groupby(imp['Type 1'])['Defense'].transform('mean')

    print(grouped)
    print(grouped1)

    #a

    imp['Średnia obrona wg. Typu 1']=grouped1

    print(imp)

    #b

    imp['Ulubiony']='Nie'

    imp.loc[(imp['Type 1']=='Rock') | (imp['Type 2']=='Rock'), 'Ulubiony']='Tak'

    print(imp)

#pandas4()

def pandas5():
    imp = pd.read_csv('Pokemon.csv', delimiter=',', encoding='latin')

    imp['Dwa typy']=imp['Type 1']+"-"+imp['Type 2']
    imp.loc[(imp['Dwa typy'].isna()), 'Dwa typy']=imp['Type 1']


    print(imp)

#pandas5()

def pandas6():
    imp = pd.read_csv('Pokemon.csv', delimiter=',', encoding='latin')

    cnt=imp['Name'].count()

    where=imp[imp['Legendary']==False]

    cnt2=where['Name'].count()

    print(cnt)
    print(cnt2)

#pandas6()

def pandas7():
    imp = pd.read_csv('Pokemon.csv', delimiter=',', encoding='latin')
    where=imp[imp['Type 2'].isna()]

    print(where)

#pandas7()

def pandas8():
    imp = pd.read_csv('Pokemon.csv', delimiter=',', encoding='latin')

    grouped=imp.groupby(imp['Type 1'])['Defense'].mean()
    grouped1 = imp.groupby(imp['Type 1'])['Defense'].transform('mean')

    print(grouped)
    print(grouped1)

    #a

    imp['Średnia obrona wg. Typu 1']=grouped1

    print(imp)

    #b

    imp['Ulubiony']='Nie'

    imp.loc[(imp['Type 1']=='Rock') | (imp['Type 2']=='Rock'), 'Ulubiony']='Tak'

    print(imp)

    imp['Dwa typy'] = imp['Type 1'] + "-" + imp['Type 2']
    imp.loc[(imp['Dwa typy'].isna()), 'Dwa typy'] = imp['Type 1']

    dwld=imp.to_csv('Zmodyfikowany_plik.csv')

#pandas8()

def wykresy1():
    imp = pd.read_csv('Pokemon.csv', delimiter=',', encoding='latin')

    fig=plt.figure(figsize=(14,10))
    ax=fig.add_subplot


    plt.title('Analiza statystyk pokemonów regionu Kanto')
    plt.show()

wykresy1()