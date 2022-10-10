def octant_transition_count(mod=5000): 
    # importing libraries
    import pandas as pd
    import numpy as np
    import math
    # Trying if input file is there or not and if there is some error then printing that in the except block
    try:
        # reading input file
        Dataframe = pd.read_excel('input_octant_transition_identify.xlsx')
    
    except Exception as e:
        print("File not found or Not relevant file type")
        print(e)
    #if no exeption is found then doing further operation    
    else:
        #trying if mean can be calculated or not like if data is number then "try" will execute otherwise it will go in exception
        try:
            # finding mean and printing them in the avg column
            Dataframe.at[0, 'U Avg'] = Dataframe['U'].mean()
            Dataframe.at[0, 'V Avg'] = Dataframe['V'].mean()
            Dataframe.at[0, 'W Avg'] = Dataframe['W'].mean()
        except Exception as e:
            print(e)
            
        else: 
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
            # getting number of row that will have exact interval as mod value
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
            Dataframe.at[freq + 8,'-2'] = '-2'
            Dataframe.at[freq + 8,'3'] = '+3'
            Dataframe.at[freq + 8,'-3'] = '-3'
            Dataframe.at[freq + 8,'4'] = '+4'
            Dataframe.at[freq + 8,'-4'] = '-4'
        # putting strings in the desired shell of excel sheet according to output file 
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
                    Dataframe.at[freq + 21,'-2'] = '-2'
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
                    Dataframe.at[freq + 21 + 13*r,'-2'] = '-2'
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
            Dataframe.at[freq + 21 + 13*newfreq,'-2'] = '-2'
            Dataframe.at[freq + 21 + 13*newfreq,'3'] = '+3'
            Dataframe.at[freq + 21 + 13*newfreq,'-3'] = '-3'
            Dataframe.at[freq + 21 + 13*newfreq,'4'] = '+4'
            Dataframe.at[freq + 21 + 13*newfreq,'-4'] = '-4'
        # Defining a funtion that will make initial values o in the transition count 
        # here r in matrix number i.e for r = 0 it will go to first matrix in which overall counts has to be placed
        # 13 is the diff between rows of two consecutive matrix so by multipliplying with r we can go to desired rows number
        # column no is same for all the matrix
            def make_zero(r):
                for n in range(8):
                    Dataframe.at[freq + 9 +13*r+n , '1'] = 0 
                    Dataframe.at[freq + 9 +13*r+n , '-1'] = 0
                    Dataframe.at[freq + 9 +13*r+n , '2'] = 0
                    Dataframe.at[freq + 9 +13*r+n , '-2'] = 0
                    Dataframe.at[freq + 9 +13*r+n , '3'] = 0
                    Dataframe.at[freq + 9 +13*r+n , '-3'] = 0
                    Dataframe.at[freq + 9 +13*r+n , '4'] = 0
                    Dataframe.at[freq + 9 +13*r+n , '-4'] = 0
            # calling the function for all matrix except last matrix
            for xt in range(freq+2):       
                make_zero(xt)
        # for last matrix transtition count end will be z-1 
        # Defining a function count_nos that will take r, start , end and count the transition and place it to desired cell
            def count_nos(r,start=0,end = z-1):  
                # creating a list that is containig octant values
                oct_lst=[1,-1,2,-2,3,-3,4,-4]

                for x in range(start,end):
                    fr = Dataframe.at[x,'Octant']
                    to = Dataframe.at[x+1,'Octant']
                    for y in range(len(oct_lst)):
                        if fr == oct_lst[y] and to == 1:
                            Dataframe.iloc[freq + 9+13*r + y , 12+1] += 1
                        elif fr == oct_lst[y] and to == -1:
                            Dataframe.iloc[freq + 9+13*r+ y  , 12+2] += 1
                        elif fr == oct_lst[y] and to == 2:
                            Dataframe.iloc[freq + 9+13*r+ y  , 12+3] += 1
                        elif fr == oct_lst[y]  and to == -2:
                            Dataframe.iloc[freq + 9+13*r+ y  , 12+4] += 1
                        elif fr == oct_lst[y] and to == 3:
                            Dataframe.iloc[freq + 9+13*r+ y  , 12+5] += 1
                        elif fr == oct_lst[y] and to == -3:
                            Dataframe.iloc[freq + 9+13*r+ y  , 12+6] += 1
                        elif fr == oct_lst[y] and to == 4:
                            Dataframe.iloc[freq + 9+13*r+ y  , 12+7] += 1
                        elif fr == oct_lst[y] and to == -4:
                            Dataframe.iloc[freq + 9+13*r+ y  , 12+8] += 1
            # giving r = 0 and default values of start and end will be 0 automatically 
            # This will count overall transition and place to the desired cell 
            count_nos(0)
            # calling function for mod transtion range except last range
            for xy in range(1,freq+1):       
                count_nos(xy,mod*(xy-1),mod*(xy-1) +mod)

            # calling function for last range 
            count_nos(freq+1,mod*freq,z-1)
        # filling NaN value as ' '
            Dataframe = Dataframe.fillna(' ')
        # just for chrecking printing first 60 values of Dataframe
            Dataframe.head(60)
        
        #checking if output file is getting modified or created        
            try:
                Dataframe.to_excel("output_octant_transition_identify.xlsx", index=False)
            except Exception as e:
                print(e)
                print("Maybe Output File is already open somewhere!! To modify it please close that file and try again")


# Checking for Python version version info
from platform import python_version
ver = python_version()

if ver == "3.8.10":
    print("Correct Version Installed")
else:
    print("Please install 3.8.10. Instruction are present in the GitHub Repo/Webmail. Url: https://pastebin.com/nvibxmjw")

mod=5000
# Calling the octant_transition_count fiunction Here we can give mod values
# checking if mode value is of correct type or not
try:
    mod == mod//1
except Exception as e:
    print(e)
    print("Mod value must be an integer")
else:    
    try:
        octant_transition_count(mod)

    except Exception as e:
        print(e)