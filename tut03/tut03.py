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

    # removing NaN values

    # Finally convertring Dataframe to desired output csv file also removing first indexes
    #     Dataframe.to_excel("output_octant_longest_subsequence.xlsx", index=False)

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
    list1 = [1,-1,2,-2,3,-3,4,-4]
    list2 = []
    list3 = []
    for n in list1:
        a = 0
        list = []
        for i in range(z-1):
            if Dataframe.at[i,'Octant'] == n and Dataframe.at[i+1,'Octant'] == n:
                a = a+1
            elif Dataframe.at[i,'Octant'] == n and Dataframe.at[i+1,'Octant'] != n:
                list.append(a+1)
                a=0
    #     print(list)
        largest_count = list[0]
        for counts in list:
            if counts > largest_count:
                largest_count = counts
        list2.append(largest_count)
        list3.append(list.count(largest_count))
    for n in range(8):    
        Dataframe.at[n+1,'     '] = list2[n]
        Dataframe.at[n+1,'      '] = list3[n]
    #     print(largest_count)
    # print(list2)
    # print(list3)


    Dataframe = Dataframe.fillna(' ')
    # just printing first 20 data rows
    Dataframe.head(20)
    Dataframe.to_excel("output_octant_longest_subsequence.xlsx", index=False)


from platform import python_version
ver = python_version()

if ver == "3.8.10":
    print("Correct Version Installed")
else:
    print("Please install 3.8.10. Instruction are present in the GitHub Repo/Webmail. Url: https://pastebin.com/nvibxmjw")

octant_longest_subsequence_count()

end_time = datetime.now()
print('Duration of Program Execution: {}'.format(end_time - start_time))