#importing libraries
import pandas as pd
import numpy as np
# reading input file
Dataframe = pd.read_excel('input_octant_longest_subsequence.xlsx')
# finding mean and printing them in the avg column
mod =5000
Dataframe.at[0, 'U Avg'] = Dataframe['U'].mean()
Dataframe.at[0, 'V Avg'] = Dataframe['V'].mean()
Dataframe.at[0, 'W Avg'] = Dataframe['W'].mean()
z = len(Dataframe)
# creating a function that will print U-U avg
def oct(a, b, c, d):
    for i in range(d):
        Dataframe.at[i, c] = Dataframe.at[i, a] - Dataframe.at[0, b]
# calling oct function that will print U-Uavg and same for V and W
oct("U", "U Avg", "U'=U-U Avg", z)
oct("V", "V Avg", "V'=V-V Avg", z)
oct("W", "W Avg", "W'=W-W Avg", z)
# Getting value of octant based on definition
for i in range(z):
    if(Dataframe.at[i, "U'=U-U Avg"] >= 0 and Dataframe.at[i, "V'=V-V Avg"] >= 0 and Dataframe.at[i, "W'=W-W Avg"] >= 0):
        Dataframe.at[i, "Octant"] = 1
    if(Dataframe.at[i, "U'=U-U Avg"] >= 0 and Dataframe.at[i, "V'=V-V Avg"] >= 0 and Dataframe.at[i, "W'=W-W Avg"] < 0):
        Dataframe.at[i, "Octant"] = -1
    if(Dataframe.at[i, "U'=U-U Avg"] < 0 and Dataframe.at[i, "V'=V-V Avg"] >= 0 and Dataframe.at[i, "W'=W-W Avg"] >= 0):
        Dataframe.at[i, "Octant"] = 2
    if(Dataframe.at[i, "U'=U-U Avg"] < 0 and Dataframe.at[i, "V'=V-V Avg"] >= 0 and Dataframe.at[i, "W'=W-W Avg"] < 0):
        Dataframe.at[i, "Octant"] = -2
    if(Dataframe.at[i, "U'=U-U Avg"] < 0 and Dataframe.at[i, "V'=V-V Avg"] < 0 and Dataframe.at[i, "W'=W-W Avg"] >= 0):
        Dataframe.at[i, "Octant"] = 3
    if(Dataframe.at[i, "U'=U-U Avg"] < 0 and Dataframe.at[i, "V'=V-V Avg"] < 0 and Dataframe.at[i, "W'=W-W Avg"] < 0):
        Dataframe.at[i, "Octant"] = -3
    if(Dataframe.at[i, "U'=U-U Avg"] >= 0 and Dataframe.at[i, "V'=V-V Avg"] < 0 and Dataframe.at[i, "W'=W-W Avg"] >= 0):
        Dataframe.at[i, "Octant"] = 4
    if(Dataframe.at[i, "U'=U-U Avg"] >= 0 and Dataframe.at[i, "V'=V-V Avg"] < 0 and Dataframe.at[i, "W'=W-W Avg"] < 0):
        Dataframe.at[i, "Octant"] = -4

# removing NaN values
Dataframe = Dataframe.fillna(' ')
# just printing first 20 data rows
Dataframe.head(20)
# Finally convertring Dataframe to desired output csv file also removing first indexes
Dataframe.to_excel("output_octant_longest_subsequence.xlsx", index=False)