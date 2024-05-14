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
    plt.suptitle("Anazliza statysktyk pokemonów regionu Kanto")

    ###
    plt.subplot(2,2,1)
    aax1=imp['Attack'].mean()
    aax2=imp['Defense'].mean()
    wartosci=[aax1,aax2]
    etykiety=['Attack','Defense']
    c=['orange','blue']
    plt.bar(etykiety,wartosci,color=c)

    ###
    plt.subplot(2, 2, 2)
    aaax1=imp['Type 1'].value_counts()
    aaax2 = aaax1.index
    aaax3 = aaax1.values

    colors = sb.color_palette("pastel")

    plt.pie(aaax3,labels=aaax2,autopct='%1.0f%%',pctdistance=1.15,labeldistance=None, startangle=-90,colors=colors)

    plt.legend(title='Typy pokemonów',loc='center left',bbox_to_anchor=(1,0,0.5,1))

    ###
    plt.subplot(2, 2, 3)
    xx=imp[(imp['Type 1']=='Dragon')|(imp['Type 1']=='Normal')|(imp['Type 1']=='Fire')]

    color={'Dragon':'purple','Normal':'grey','Fire':'red'}

    sb.scatterplot(data=xx,x='Sp. Atk',y='Sp. Def',hue='Type 1', palette=color)

    plt.legend()

    ###
    plt.subplot(2, 2, 4)
    xxx=imp[(imp['Type 1']=='Dragon')|(imp['Type 1']=='Normal')|(imp['Type 1']=='Fire')]

    color = {'Dragon': 'purple', 'Normal': 'grey', 'Fire': 'red'}

    sb.boxplot(data=xxx,x='Type 1',y='Speed',palette=color, hue='Type 1')

    plt.tight_layout()
    plt.savefig('poksy.png')
    plt.show()
wykresy1()