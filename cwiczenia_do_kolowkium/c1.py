import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def przyklad1():
    df=pd.read_csv('zamowienia.csv', delimiter=';')
    print(df.head())
    print(df.describe())
    print(df['Utarg'].describe())
    print(df.info())
    df['Data zamowienia']=pd.to_datetime(df['Data zamowienia'])
    print(df.info())
    df['Data zamowienia']=df['Data zamowienia'].astype(str)
    print(df.info())
#przyklad1()


def zadanie1():
    imp=pd.read_csv('Pokemon.csv',delimiter=',', encoding='latin')
    imp=imp[imp['Type 2'].isnull()]
    x=sns.scatterplot(data=imp,hue='Stage',y='Defense',x='Attack',)
    print(imp)

    sns.move_legend(x,loc="upper right",bbox_to_anchor=(1.15,1))
    plt.grid(True)
    plt.show()

#zadanie1()

def zadanie2():
    imp=pd.read_csv('Pokemon.csv',delimiter=',', encoding='latin')

    where=imp[(imp['Type 1']=='Fire')|(imp['Type 1']=='Grass')|(imp['Type 1']=='Water')]
    grp=where['Type 1'].value_counts().reset_index()
    grp.columns=['Type 1','count']

    #print(grp)

    sns.barplot(data=grp,x='Type 1',y='count',palette=['#6890F0','#78C850','#F08030'],hue='Type 1', legend=False)
    plt.show()
#zadanie2()

def zadanie3():
    imp = pd.read_csv('Pokemon.csv', delimiter=',', encoding='latin')
    imp['Legendary']=imp['Legendary'].astype(str)
    imp.loc[(imp['Legendary']=='False'), 'Legendary']='Zwykly'
    imp.loc[(imp['Legendary'] =='True'), 'Legendary'] = 'Legendarny'

    cnt=imp['Legendary'].value_counts().reset_index()
    cnt.columns=['Leg','count']

    color=sns.color_palette()

    plt.pie(cnt['count'],labels=cnt['Leg'],autopct='%1.1f%%',colors=color)
    plt.show()

#zadanie3()

def zadanie4():
    imp = pd.read_csv('Pokemon.csv', delimiter=',', encoding='latin')
    imp=imp[['HP','Defense','Attack']]
    imp.columns=['HP','Obrona','Atak']

    print(imp)

    sns.boxplot(data=imp)
    plt.show()

#zadanie4()

def zadanie5():
    imp = pd.read_csv('Pokemon.csv', delimiter=',', encoding='latin')
    imp=imp[['Legendary','Defense','Attack']]

    sns.jointplot(data=imp,x='Defense',y='Attack',hue='Legendary')

    plt.show()

#zadanie5()

def zadanie6():
    imp = pd.read_csv('Pokemon.csv', delimiter=',', encoding='latin')

    imp=imp[['Attack','Defense','Speed']]

    print(imp)

    sns.pairplot(imp)

    plt.show()
#zadanie6()

def zadanie6_1():
    imp = pd.read_csv('Pokemon.csv', delimiter=',', encoding='latin')

    loc=imp.loc[:,['Attack','Defense','Speed']]

    #print(loc)
    plt.show()
zadanie6_1()