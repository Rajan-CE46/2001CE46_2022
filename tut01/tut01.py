def octant_identification(mod = 5000):
    # importing libraries
    import pandas as pd
    import numpy as np
    # reading input file
    Dataframe = pd.read_csv('octant_input.csv')
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
# printing overall count value at desired places
    Dataframe.at[0, '1'] = oct_1
    Dataframe.at[0, '-1'] = oct_n1
    Dataframe.at[0, '2'] = oct_2
    Dataframe.at[0, '-2'] = oct_n2
    Dataframe.at[0, '3'] = oct_3
    Dataframe.at[0, '-3'] = oct_n3
    Dataframe.at[0, '4'] = oct_4
    Dataframe.at[0, '-4'] = oct_n4
# priniting mod ranges according to mod value
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
# removing NaN values
    Dataframe = Dataframe.fillna(' ')
# just printing first 20 data rows
    Dataframe.head(20)
# Finally convertring Dataframe to desired output csv file also removing first indexes
    Dataframe.to_csv("octant_output.csv", index=False)

# getting input of mod value
mod = 5000
octant_identification(mod)
