
    ### This is the file created by me, to use as reference note for Pandas Series
    ## It included how the series is created, indexed, sliced, and how Operations could be done

import numpy as np
import pandas as pd

################################################

  #Create Pandas Series

#Create Empty Pandas Series  
empty=pd.Series()

# In millions , Population
Population = pd.Series([35.467, 63.951, 80.940, 60.665, 127.061, 64.511, 318.523])

#set the name of the series
Population.name="Population of the Countries"

#Displays the Datatype of the series
Population.dtype
# Another Thing  to be noted; is that pandas are backed by numpy arrays and datatypes


#Displays Values of the series
Population.values



 ###############################################

  ## INDEXING

Population #Displays all the series

Population[1] #Displays the second Element of the sereis

# We can also give different index to the series
Population.index = [
    'Canada',
    'France',
    'Germany',
    'Italy',
    'Japan',
    'United Kingdom',
    'United States',

]

# We could have given the name and index differently too

pop1 = pd.Series(
    [35.467, 63.951, 80.94, 60.665, 127.061, 64.511, 318.523],
    index=['Canada', 'France', 'Germany', 'Italy', 'Japan', 'United Kingdom',
       'United States'],
    name='G7 Population in millions')


### then locating

Population['Canada'] #Prints the value of Canada

Population.iloc[0] # It accesed  the value of canada using default integer Indexing

Population.iloc[-1] # It accesed the last element of Series using int index i.e. USA and its value

Population[['Italy', 'France']]  # It accessed the value of Italy and France at once

Population.iloc[[0,1]] # IT accessed the value of 0th and 1st series

Population['Canda': 'Italy'] # It accesed the value of canada to Italy




################################################
#Conditional Selection of Pandas Series

Population > 70 #It doesn't Change the original series, but make temporarily new series and Displays Which one meets True and Which one meets fals

Population[Population>70]
#Now it shows those Countries (Data) only, who have more than 70 (millions)

Population.mean()
#Calculates the mean of all the data from the series

Population[Population > Population.mean()]
#Shows those countries from the series which have higher population than the mean

Population.std()
#show the Standard Deviation of the numerals from the  Series 




######################################################
# Operations and Methods

#    we could do any operation to series , which applies to all elements automatically

Population*1000000 #It makes the every element of the series multiplied by million

#Note Until Population= ....  the original series won't change

Population['France': 'Italy'].mean()
# It calulates the mean betn the datas of France and Italy only

  ##Boolean Arrays

Population[(Population>70) | (Population<40)]
#It displays those whose countries whose population ranges less than 40 or more than 70; it is a "OR" operation

Population[(Population>70) & (Population<40)]
#It displays those whose countries whose population ranges betn 40 to 70; it is a "AND" operation


#######################################################

#Modyfying Series

Population['Canada'] = 40.5 # It changes the orginal value of canda and replace with 40.5

Population.iloc[-1] = 500 # It changes the last Country (USA) data to 500
Population[Population <70] =99.99 #Changes the Data of all the countries having less than 70 (M) to 99.99

print(Population)
print("Bye-Bye")