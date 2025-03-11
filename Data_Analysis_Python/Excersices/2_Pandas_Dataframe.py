 ### This is the file created by me, to use as reference note for Pandas Series
    ## It included how the Dataframe in pandas is created, indexed, sliced, and how Operations could be done

import numpy as np
import pandas as pd


df = pd.DataFrame({
    'Population': [35.467, 63.951, 80.94 , 60.665, 127.061, 64.511, 318.523],
    'GDP': [
        1785387,
        2833687,
        3874437,
        2167744,
        4602367,
        2950039,
        17348075
    ],
    'Surface Area': [
        9984670,
        640679,
        357114,
        301336,
        377930,
        242495,
        9525067
    ],
    'HDI': [
        0.913,
        0.888,
        0.916,
        0.873,
        0.891,
        0.907,
        0.915
    ],
    'Continent': [
        'America',
        'Europe',
        'Europe',
        'Europe',
        'Asia',
        'Europe',
        'America'
    ]
}, columns=['Population', 'GDP', 'Surface Area', 'HDI', 'Continent'])


#Dataframe uploaded, these dataframes are the combination of series


df.index = [
    'Canada',
    'France',
    'Germany',
    'Italy',
    'Japan',
    'United Kingdom',
    'United States',
]

# It indexes Dataframe rows...


df.columns #Displays the columns' index

df.index # Displays the index of df (Rows)

df.info() # Gives the data information of the column
#It displays that the all the columns have what data type and no_of_NULL_COUNT separately..

df.size #gives the size of the dataframe

df.describe() #gives thes statistical info about the numeral data of the dataframe
#It Shows the  each columns' : count, mean, std, min, 25%, 50%, 75%, max

df.dtypes #gives the which columns contains which type of data

df.dtypes.value_counts()
#It gives the count of datatype used of the overall all columns(table) has...



##############################################################
#Indexing, Selection and Slicing

df.loc['Canada']
#just like previous, it gives all the values of canada; pop, GDP, HDI, etc

df.iloc[-1]
#just acess the last row of the table

df['Population']
# It displays all the countries populations' value

df['Population'].to_frame()
#It converts the selected series to separate dataframe

df[['Population', 'GDP']]
#It converts two selected Coloumns to separate dataframe

df[1:3]
#It access the rows from 1 to 2 i.e.  1, 2

df.loc['France':'Italy']
#It access the data of rows from france to italy

df.loc['France': 'Italy', 'Population']
#prints the population of the rows from france to italy

df.loc['France': 'Italy', ['Population','GDP']]
#prints the population & GDP of the rows from France to italy

df.iloc[[0,1,-1]]
#prints the value of 1st, 2nd and last data

df.iloc[1:3, 3]
#prints 4th Columns' data of 1st and 2nd position countries


########################################################

#Conditional Selection

df['population']>70
#Displays True or false which rows has population greater than 70 or not

df.loc[df['population']>70]
#Displays those countries only which are true for the condn

df.loc[df['Population']>70 , 'Population']
#Displays those countries population only...

df.loc[df['Population']>70, 'Population']

###############################################################

#Dropping Stuff

df.drop['Canada']

df.drop(['Canada','Japan'])

###Drops the whole rows (stated)

df.drop(columns=['Population', 'HDI'])
#Drops the whole respective columns

df.drop(['Italy', 'Canada'], axis=0)
## Axis = 0 states rows

df.drop(['Population', 'HDI'], axis=1)
## Axis = 1 states coloumns

df.drop(['Population'], axis='columns')
## Could state directly columns

##############################################################

#Operations

df[['Population', 'GDP']]/100
#Divide those columns by 100

langs = pd.series(
    ['French','German', 'Italian'],
    index=['France', 'Germany', 'Italy'],
    name ='Language'
)#Language Series defined with some indexes

df['Language']=langs #Those value of langs series would be attached with the respective indexes and other would get NaN

df['Language']='English' #make all the values of Langauage rows as "ENGLISH"


#################################################################

##Renaming Columns

df.rename(
 columns={
     'HDI': 'Human Development Index', 
     'Annual Popcorn Consumtion': 'APC',
 }, index={
     'United States': 'USA',
     'United Kingdom': 'UK',
     'Argentina': 'AR'
 })

# it renames the columns or rows

df.rename(index=str.upper)

#########################################################
# appending new row in df

new_row = pd.Series(
    {
        'Population': 3,
        'GDP': 5,
    }, name='china'
)
df=pd.concat([df, new_row.to_frame().T])
##First converting Column matrix to row matrix using transpose
# ... (cuz series is column matrix)


##Creating Columns from other columns
df['GDP_per_capita']=df['GDP']/df['Population']

#statistical info and function could also be used ...

df.head()
#Shows data of first five rows

df.describe()
# describe all the columns statistcal info : mean, count, std.....

#Also could be getting info by converting dataframe to single series
population=df['Population']
population.min()
population.max()
population.sum()

#......And several more