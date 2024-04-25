import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('TkAgg')

def przyklad1():
    df=pd.read_csv('./zamowienia.csv', sep=';')
    print("\n",df.head(),"\n")
    print(df.describe(),"\n")
    print(df['Utarg'].describe(),"\n")
    print(df.info(),"\n")

    df['Data zamowienia']=pd.to_datetime(df['Data zamowienia'])
    print(df.info(),"\n")
    print(df.head(),"\n")

    df['Data zamowienia']=df['Data zamowienia'].astype(str)
    print(df.info(), "\n")
    print(df.head(), "\n")

    df['Data zamowienia']=pd.to_datetime(df['Data zamowienia'], format='%Y-%m-%d')
    print(df.info(), "\n")
    print(df.head(), "\n")

#przyklad1()

def przyklad2():
    df = pd.read_csv('./zamowienia.csv', sep=';')
    df['Data zamowienia'] = pd.to_datetime(df['Data zamowienia'])

    df['year']=df['Data zamowienia'].dt.year
    df['month']=df['Data zamowienia'].dt.month
    df['day']=df['Data zamowienia'].dt.day

    print("\n",df.head(),"\n")

    print(pd.to_datetime(df[['year','month','day']]), "\n")

    df['Data zamowienia']=df['Data zamowienia'].astype(str)
    df.drop(columns=['year','month','day'], inplace=True)

    print(df.info())

#przyklad2()

def przyklad3():
    df = pd.read_csv('./zamowienia.csv', sep=';')

    df_copy_1=df.copy(deep=True)

    df_copy_1['rok']=df_copy_1['Data zamowienia'].str[:4]
    print("\n",df_copy_1.head(),"\n")

    df_copy_1['Nowa data'] = df_copy_1['Data zamowienia'].str.replace('-', '/')
    print(df_copy_1.head())

    df_copy_1['Jeszcze nowsza data']=df_copy_1['Data zamowienia'].apply(str.replace,args=('-','/'))
    print("\n",df_copy_1.head(),"\n")

#przyklad3()

#Porównywanie wykresów

def przyklad4(): #scatter
    df = pd.read_csv('./zamowienia.csv', sep=';')
    df_copy=df.copy()

    df_copy.sort_values(by=['Data zamowienia'], inplace=True,ignore_index=True)

    print(df_copy.head())

    #inna możliwość

    df['Data zamowienia']=pd.to_datetime(df['Data zamowienia'])
    df.sort_values(by=['Data zamowienia'],inplace=True)
    print(df.head())
    df.reset_index(drop=True,inplace=True)
    print(df.head())

    print(df['Utarg'].cumsum().head())
    #df['Utarg'].cumsum().plot()
    #plt.show()
    #df[['Data zamowienia','Utarg']].set_index('Data zamowienia').cumsum().plot()
    #plt.show() #razem z datami
    sns.lineplot(data=df,x='Data zamowienia',y=np.cumsum(df['Utarg']))
    plt.show()
#przyklad4()

def przyklad5(): #informacja 2 bar
    df = pd.read_csv('./zamowienia.csv', sep=';')

    #df.groupby('Sprzedawca').agg({'Utarg':['sum']}).plot(kind='bar')
    #plt.show()

    ax=sns.barplot(x='Sprzedawca',y='Utarg',data=df,ci=None,estimator=sum)
    plt.xticks(rotation=45)
    plt.show()

#przyklad5()

def przyklad6(): #pie
    df = pd.read_csv('./zamowienia.csv', sep=';')

    df.groupby('Sprzedawca').agg({'Utarg':['sum']}).plot(kind='pie',subplots=True)

    #plt.legend(bbox_to_anchor=(1.3,1.025))
    #plt.show()

    #seaborn

    colors=sns.color_palette('pastel')[0:5]
    dane=df.groupby('Sprzedawca').agg({'Utarg':['sum']})

    plt.pie(dane[('Utarg','sum')], labels=dane.index,colors=colors,autopct='%.0f%%')
    plt.legend(bbox_to_anchor=(1.3,1.025))
    plt.show()
#przyklad6()

def przyklad8():
    df = pd.read_csv('./zamowienia.csv', sep=';')

    dane=df[['Sprzedawca','idZamowienia']].set_index('idZamowienia')
    plt.xticks(rotation=45)

    ax=sns.countplot(x='Sprzedawca',data=dane)

    plt.show()

#przyklad8()

def przyklad9():
    df = pd.read_csv('./zamowienia.csv', sep=';')
    df['Data zamowienia'] = pd.to_datetime(df['Data zamowienia'])

    plt.xticks(rotation=45)
    ax = sns.countplot(x="Sprzedawca", hue=df['Data zamowienia'].dt.year, data=df, palette="Set3")

    for container in ax.containers:
        ax.bar_label(container)

    plt.show()

#przyklad9()

def przyklad10():
    df = pd.read_csv('./zamowienia.csv', sep=';')
    df['Data zamowienia'] = pd.to_datetime(df['Data zamowienia'])
    dane=df.groupby('Sprzedawca').agg({'Utarg':['sum','mean','count']})

    print(dane,'\n')
    print(dane[('Utarg','sum')],'\n')
    print(dane.Utarg['sum'])


przyklad10()



