# importing libraries
import pandas as pd
import numpy as np
mod = 5000
# reading input file
Dataframe = pd.read_excel('input_octant_transition_identify.xlsx')
# finding mean and printing them in the avg column
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
# creating another column of user input and also printing string at desired place according to output file 
Dataframe.at[1, ''] = 'User Input'
Dataframe.at[0, 'octant ID'] = 'overall count'
Dataframe.at[1, 'octant ID'] = f"Mod:{mod}"
oct_1 = 0
oct_n1 = 0
oct_2 = 0
oct_n2 = 0
oct_3 = 0
oct_n3 = 0
oct_4 = 0
oct_n4 = 0
# counting octant count in entire data point
for i in range(z):
    if Dataframe.at[i, 'Octant'] == 1:
        oct_1 = (oct_1)+1
    elif Dataframe.at[i, 'Octant'] == -1:
        oct_n1 = (oct_n1)+1
    elif Dataframe.at[i, 'Octant'] == 2:
        oct_2 = (oct_2)+1
    elif Dataframe.at[i, 'Octant'] == -2:
        oct_n2 = (oct_n2)+1
    elif Dataframe.at[i, 'Octant'] == 3:
        oct_3 = (oct_3)+1
    elif Dataframe.at[i, 'Octant'] == -3:
        oct_n3 = (oct_n3)+1
    elif Dataframe.at[i, 'Octant'] == 4:
        oct_4 = (oct_4)+1
    elif Dataframe.at[i, 'Octant'] == -4:
        oct_n4 = (oct_n4)+1
# pinting overall count value at desired places
Dataframe.at[0, '1'] = oct_1
Dataframe.at[0, '-1'] = oct_n1
Dataframe.at[0, '2'] = oct_2
Dataframe.at[0, '-2'] = oct_n2
Dataframe.at[0, '3'] = oct_3
Dataframe.at[0, '-3'] = oct_n3
Dataframe.at[0, '4'] = oct_4
Dataframe.at[0, '-4'] = oct_n4
# piniting mod ranges according to mod value
min_value = 0
# getting number of row that will have exact interval as nod value
freq = z//mod  
for i in range(freq):
    if i == 0:
        Dataframe.at[i+2, 'octant ID'] = f".0000-{mod*i+mod-1}"
    else:
        Dataframe.at[i+2, 'octant ID'] = f"{mod*i}-{mod*i+mod-1}"
Dataframe.at[freq + 2, 'octant ID'] = f"{mod*freq}-{z-1}"
# counting number of octant in each mod ranges(excludong last row)
for k in range(freq):
    oct_1 = 0
    oct_n1 = 0
    oct_2 = 0
    oct_n2 = 0
    oct_3 = 0
    oct_n3 = 0
    oct_4 = 0
    oct_n4 = 0
    for i in range(mod*k, mod*k+mod):
        if Dataframe.at[i, 'Octant'] == 1:
            oct_1 = (oct_1)+1
        elif Dataframe.at[i, 'Octant'] == -1:
            oct_n1 = (oct_n1)+1
        elif Dataframe.at[i, 'Octant'] == 2:
            oct_2 = (oct_2)+1
        elif Dataframe.at[i, 'Octant'] == -2:
            oct_n2 = (oct_n2)+1
        elif Dataframe.at[i, 'Octant'] == 3:
            oct_3 = (oct_3)+1
        elif Dataframe.at[i, 'Octant'] == -3:
            oct_n3 = (oct_n3)+1
        elif Dataframe.at[i, 'Octant'] == 4:
            oct_4 = (oct_4)+1
        elif Dataframe.at[i, 'Octant'] == -4:
            oct_n4 = (oct_n4)+1
    # printing count values
    Dataframe.at[k+2, '1'] = oct_1
    Dataframe.at[k+2, '-1'] = oct_n1
    Dataframe.at[k+2, '2'] = oct_2
    Dataframe.at[k+2, '-2'] = oct_n2
    Dataframe.at[k+2, '3'] = oct_3
    Dataframe.at[k+2, '-3'] = oct_n3
    Dataframe.at[k+2, '4'] = oct_4
    Dataframe.at[k+2, '-4'] = oct_n4
# counting octant values for last row   
oct_1 = 0
oct_n1 = 0
oct_2 = 0
oct_n2 = 0
oct_3 = 0
oct_n3 = 0
oct_4 = 0
oct_n4 = 0
for i in range(mod*freq, z):
    if Dataframe.at[i, 'Octant'] == 1:
        oct_1 = (oct_1)+1
    elif Dataframe.at[i, 'Octant'] == -1:
        oct_n1 = (oct_n1)+1
    elif Dataframe.at[i, 'Octant'] == 2:
        oct_2 = (oct_2)+1
    elif Dataframe.at[i, 'Octant'] == -2:
        oct_n2 = (oct_n2)+1
    elif Dataframe.at[i, 'Octant'] == 3:
        oct_3 = (oct_3)+1
    elif Dataframe.at[i, 'Octant'] == -3:
        oct_n3 = (oct_n3)+1
    elif Dataframe.at[i, 'Octant'] == 4:
        oct_4 = (oct_4)+1
    elif Dataframe.at[i, 'Octant'] == -4:
        oct_n4 = (oct_n4)+1
# printing octant values for last row
Dataframe.at[freq + 2, '1'] = oct_1
Dataframe.at[freq + 2, '-1'] = oct_n1
Dataframe.at[freq + 2, '2'] = oct_2
Dataframe.at[freq + 2, '-2'] = oct_n2
Dataframe.at[freq + 2, '3'] = oct_3
Dataframe.at[freq + 2, '-3'] = oct_n3
Dataframe.at[freq + 2, '4'] = oct_4
Dataframe.at[freq + 2, '-4'] = oct_n4
Dataframe.at[freq + 3,'octant ID'] = 'Verified'
Dataframe.at[freq + 3,'1'] = Dataframe.at[0,'1']
Dataframe.at[freq + 3,'-1'] = Dataframe.at[0,'-1']
Dataframe.at[freq + 3,'2'] = Dataframe.at[0,'2']
Dataframe.at[freq + 3,'-2'] = Dataframe.at[0,'-2']
Dataframe.at[freq + 3,'3'] = Dataframe.at[0,'3']
Dataframe.at[freq + 3,'-3'] = Dataframe.at[0,'-3']
Dataframe.at[freq + 3,'4'] = Dataframe.at[0,'4']
Dataframe.at[freq + 3,'-4'] = Dataframe.at[0,'-4']

Dataframe.at[freq + 6,'octant ID'] = 'Overall Transition Count'
Dataframe.at[freq + 7,'1'] = 'To'
Dataframe.at[freq + 9,''] = 'from'
Dataframe.at[freq + 8,'octant ID'] = 'Count'
Dataframe.at[freq + 9,'octant ID'] = '+1'
Dataframe.at[freq + 10,'octant ID'] = '-1'
Dataframe.at[freq + 11,'octant ID'] = '+2'
Dataframe.at[freq + 12,'octant ID'] = '-2'
Dataframe.at[freq + 13,'octant ID'] = '+3'
Dataframe.at[freq + 14,'octant ID'] = '-3'
Dataframe.at[freq + 15,'octant ID'] = '+4'
Dataframe.at[freq + 16,'octant ID'] = '-4'

Dataframe.at[freq + 8,'1'] = '+1'
Dataframe.at[freq + 8,'-1'] = '-1'
Dataframe.at[freq + 8,'2'] = '+2'
Dataframe.at[freq + 8,'-2'] = '+-2'
Dataframe.at[freq + 8,'3'] = '+3'
Dataframe.at[freq + 8,'-3'] = '-3'
Dataframe.at[freq + 8,'4'] = '+4'
Dataframe.at[freq + 8,'-4'] = '-4'

newfreq = z//mod
for r in range(newfreq):
    if r == 0:
        Dataframe.at[freq + 19,'octant ID'] = 'Mod Transition Count'
        Dataframe.at[freq + 20,'1'] = 'To'
        Dataframe.at[freq + 21,'octant ID'] = 'Count'
        Dataframe.at[freq + 22,''] = 'from'
        Dataframe.at[freq + 20,'octant ID'] = f".0000-{mod*r+mod-r}"

        Dataframe.at[freq + 22,'octant ID'] = '+1'
        Dataframe.at[freq + 23,'octant ID'] = '-1'
        Dataframe.at[freq + 24,'octant ID'] = '+2'
        Dataframe.at[freq + 25,'octant ID'] = '-2'
        Dataframe.at[freq + 26,'octant ID'] = '+3'
        Dataframe.at[freq + 27,'octant ID'] = '-3'
        Dataframe.at[freq + 28,'octant ID'] = '+4'
        Dataframe.at[freq + 29,'octant ID'] = '-4'

        Dataframe.at[freq + 21,'1'] = '+1'
        Dataframe.at[freq + 21,'-1'] = '-1'
        Dataframe.at[freq + 21,'2'] = '+2'
        Dataframe.at[freq + 21,'-2'] = '+-2'
        Dataframe.at[freq + 21,'3'] = '+3'
        Dataframe.at[freq + 21,'-3'] = '-3'
        Dataframe.at[freq + 21,'4'] = '+4'
        Dataframe.at[freq + 21,'-4'] = '-4'
    else:
        Dataframe.at[freq + 19 + 13*r,'octant ID'] = 'Mod Transition Count'
        Dataframe.at[freq + 20 + 13*r,'1'] = 'To'
        Dataframe.at[freq + 21 + 13*r,'octant ID'] = 'Count'
        Dataframe.at[freq + 22 + 13*r,''] = 'from'
        Dataframe.at[freq + 20 + 13*r,'octant ID'] = f"{mod*r}-{mod*r+mod-1}"
        Dataframe.at[freq + 22 + 13*r,'octant ID'] = '+1'
        Dataframe.at[freq + 23 + 13*r,'octant ID'] = '-1'
        Dataframe.at[freq + 24 + 13*r,'octant ID'] = '+2'
        Dataframe.at[freq + 25 + 13*r,'octant ID'] = '-2'
        Dataframe.at[freq + 26 + 13*r,'octant ID'] = '+3'
        Dataframe.at[freq + 27 + 13*r,'octant ID'] = '-3'
        Dataframe.at[freq + 28 + 13*r,'octant ID'] = '+4'
        Dataframe.at[freq + 29 + 13*r,'octant ID'] = '-4'

        Dataframe.at[freq + 21 + 13*r,'1'] = '+1'
        Dataframe.at[freq + 21 + 13*r,'-1'] = '-1'
        Dataframe.at[freq + 21 + 13*r,'2'] = '+2'
        Dataframe.at[freq + 21 + 13*r,'-2'] = '+-2'
        Dataframe.at[freq + 21 + 13*r,'3'] = '+3'
        Dataframe.at[freq + 21 + 13*r,'-3'] = '-3'
        Dataframe.at[freq + 21 + 13*r,'4'] = '+4'
        Dataframe.at[freq + 21 + 13*r,'-4'] = '-4'

Dataframe.at[freq + 19 + 13*newfreq,'octant ID'] = 'Mod Transition Count'
Dataframe.at[freq + 20 + 13*newfreq,'1'] = 'To'
Dataframe.at[freq + 21 + 13*newfreq,'octant ID'] = 'Count'
Dataframe.at[freq + 22 + 13*newfreq,''] = 'from'
Dataframe.at[freq + 20 + 13*newfreq,'octant ID'] = f"{mod*newfreq}-{z-1}"
Dataframe.at[freq + 22 + 13*newfreq,'octant ID'] = '+1'
Dataframe.at[freq + 23 + 13*newfreq,'octant ID'] = '-1'
Dataframe.at[freq + 24 + 13*newfreq,'octant ID'] = '+2'
Dataframe.at[freq + 25 + 13*newfreq,'octant ID'] = '-2'
Dataframe.at[freq + 26 + 13*newfreq,'octant ID'] = '+3'
Dataframe.at[freq + 27 + 13*newfreq,'octant ID'] = '-3'
Dataframe.at[freq + 28 + 13*newfreq,'octant ID'] = '+4'
Dataframe.at[freq + 29 + 13*newfreq,'octant ID'] = '-4'
Dataframe.at[freq + 21 + 13*newfreq,'1'] = '+1'
Dataframe.at[freq + 21 + 13*newfreq,'-1'] = '-1'
Dataframe.at[freq + 21 + 13*newfreq,'2'] = '+2'
Dataframe.at[freq + 21 + 13*newfreq,'-2'] = '+-2'
Dataframe.at[freq + 21 + 13*newfreq,'3'] = '+3'
Dataframe.at[freq + 21 + 13*newfreq,'-3'] = '-3'
Dataframe.at[freq + 21 + 13*newfreq,'4'] = '+4'
Dataframe.at[freq + 21 + 13*newfreq,'-4'] = '-4'

# list = []
# for h in range(64):
#     list.append(0)
# for p in range(z):
#     if Dataframe.at[p,'Octant'] == 1 and Dataframe.at[p,'Octant'] == 1:
#         list[0] = list[0] + 1
#     elif Dataframe.at[p,'Octant'] == 1 and Dataframe.at[p,'Octant'] == -1:
#         list[1] = list[1] + 1
#     elif Dataframe.at[p,'Octant'] == 1 and Dataframe.at[p,'Octant'] == 2:
#         list[2] = list[2] + 1
#     elif Dataframe.at[p,'Octant'] == 1 and Dataframe.at[p,'Octant'] == -2:
#         list[3] = list[3] + 1
#     elif Dataframe.at[p,'Octant'] == 1 and Dataframe.at[p,'Octant'] == 3:
#         list[4] = list[4] + 1
#     elif Dataframe.at[p,'Octant'] == 1 and Dataframe.at[p,'Octant'] == -3:
#         list[5] = list[5] + 1
#     elif Dataframe.at[p,'Octant'] == 1 and Dataframe.at[p,'Octant'] == 4:
#         list[6] = list[6] + 1
#     elif Dataframe.at[p,'Octant'] == 1 and Dataframe.at[p,'Octant'] == -4:
#         list[7] = list[7] + 1
# #     for x in range(1,5):
# #         for y in range(1,5):
# #             if Dataframe.at[p,'Octant'] == x and Dataframe.at[p+1,'Octant'] == y:
# #                 for w in range(17):
# #                     list[w] = list[w]+1
    
# print(list[0])
    
#     if Dataframe.at[p,'Octant'] & Dataframe.at[p+1,'Octant'] == 1:
#         count_11 = count_11+1
#     elif 
# removing NaN values
Dataframe = Dataframe.fillna(' ')
# just printing first 20 data rows
Dataframe.head(60)
# Finally convertring Dataframe to desired output excel file also removing first indexes
Dataframe.to_excel("output_octant_transition_identify.xlsx", index=False)
