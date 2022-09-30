# importing libraries
from datetime import datetime
start_time = datetime.now()
def octant_longest_subsequence_count():
    #importing libraries
    import pandas as pd
    import numpy as np
    # reading input file
    Dataframe = pd.read_excel('input_octant_longest_subsequence.xlsx')
    # finding mean and printing them in the avg column
    # mod =5000
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
# Inserting additional columns and also putting desired strings in that according to output file
# First of all leaving a blank column after octant column
# alsp putting +1,-1 ... at there desired cell
    Dataframe.at[0,' '] = ' '
    Dataframe.at[0,'  '] = 'Count'
    Dataframe.at[0,'     '] = 'Longest Subsquence Length'
    Dataframe.at[0,'      '] = 'Count'
    Dataframe.at[1,'  '] = '+1'
    Dataframe.at[2,'  '] = '-1'
    Dataframe.at[3,'  '] = '+2'
    Dataframe.at[4,'  '] = '-2'
    Dataframe.at[5,'  '] = '+3'
    Dataframe.at[6,'  '] = '-3'
    Dataframe.at[7,'  '] = '+4'
    Dataframe.at[8,'  '] = '-4'
    # Dataframe.iloc[0,0] = '+1'
    # Dataframe.at[1,'n'] = ' '
    # creating a list1 that is containing octant values
    # Also creating list2 and list3 these lists are used to store largest subsequence count and no of occurance using append 
    list1 = [1,-1,2,-2,3,-3,4,-4]
    list2 = []
    list3 = []
    for n in list1:
        a = 0
        list = []
        for i in range(z-1):
            if Dataframe.at[i,'Octant'] == n and Dataframe.at[i+1,'Octant'] == n:
                a = a+1
                # this a will be keep on adding till the sae octant value is getting
            elif Dataframe.at[i,'Octant'] == n and Dataframe.at[i+1,'Octant'] != n:
                # Just after we get diff octant value nos of occ is stored in list using appeng
                list.append(a+1)
                # then again a =  0 for next cycle
                # a=0
                # this list will store number of continuos occurance of octant value w.r.t each octant value
    #     print(list)
    # now finding largest occurance of each octant and appending these values in list 2
    # and count of each largest occurance in list 3
        largest_count = list[0]
        for counts in list:
            if counts > largest_count:
                largest_count = counts
        list2.append(largest_count)
        list3.append(list.count(largest_count))
        # now finally pribnting them in their desired place
    for n in range(8):    
        Dataframe.at[n+1,'     '] = list2[n]
        Dataframe.at[n+1,'      '] = list3[n]
    #     print(largest_count)
    # print(list2)
    # print(list3)


    Dataframe = Dataframe.fillna(' ')
    # just printing first 20 data rows
    Dataframe.head(20)
    # Finally Converting Dataframe to desired output file
    Dataframe.to_excel("output_octant_longest_subsequence.xlsx", index=False)

# Checking for pyuthon version
from platform import python_version
ver = python_version()

if ver == "3.8.10":
    print("Correct Version Installed")
else:
    print("Please install 3.8.10. Instruction are present in the GitHub Repo/Webmail. Url: https://pastebin.com/nvibxmjw")
#  calling octant_longest_subsequence_count() function
octant_longest_subsequence_count()
#   Printing execution time
end_time = datetime.now()
print('Duration of Program Execution: {}'.format(end_time - start_time))