#Import pandas
import pandas as pd

#Establish data
data = {'Price': [1, 2, 3, 4, 5, 6, 6.5, 7, 8, 9, 10],
        'Quantity': [100, 90, 80, 70, 60, 50, 45, 40, 30, 20, 10]}

#Create pandas Dataframe
df = pd.DataFrame(data)

#Print Dataframe
print(df)

#Export as csv file
df.to_csv(r'/Users/chicken/Documents/GitHub/ManagerialEconomics/DemandAnalysis/HW2_AAE625.csv')