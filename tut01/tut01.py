 def octant_identification(mod=5000):

    import pandas as pd
    DataFrame = pd.read_csv(r'C:\Users\rajan\Documents\GitHub\2001CE46_2022\tut01\octant_input.csv')

    DataFrame.at[0, "U Avg"] = DataFrame["U"].mean()
    DataFrame.at[0, "V Avg"] = DataFrame["V"].mean()
    DataFrame.at[0, "W Avg"] = DataFrame["W"].mean()

    Data_lenght = len(DataFrame)

    def oct(a, b, c, Data_lenght):
        for i in range(Data_lenght):
            DataFrame.at[i, c] = DataFrame.at[i, a] - DataFrame.at[0, b]

    oct("U", "U Avg", "U", Data_lenght)
    oct("V", "V Avg", "V", Data_lenght)
    oct("W", "W Avg", "W", Data_lenght)

    for i in range(Data_lenght):
        if(DataFrame.at[i, "U"] >= 0 and DataFrame.at[i, "V"] >= 0 and DataFrame.at[i, "W"] >= 0):
            DataFrame.at[i, "Octant"] = 1
        if(DataFrame.at[i, "U"] >= 0 and DataFrame.at[i, "V"] >= 0 and DataFrame.at[i, "W"] < 0):
            DataFrame.at[i, "Octant"] = -1
        if(DataFrame.at[i, "U"] < 0 and DataFrame.at[i, "V"] >= 0 and DataFrame.at[i, "W"] >= 0):
            DataFrame.at[i, "Octant"] = 2
        if(DataFrame.at[i, "U"] < 0 and DataFrame.at[i, "V"] >= 0 and DataFrame.at[i, "W"] < 0):
            DataFrame.at[i, "Octant"] = -2
        if(DataFrame.at[i, "U"] < 0 and DataFrame.at[i, "V"] < 0 and DataFrame.at[i, "W"] >= 0):
            DataFrame.at[i, "Octant"] = 3
        if(DataFrame.at[i, "U"] < 0 and DataFrame.at[i, "V"] < 0 and DataFrame.at[i, "W"] < 0):
            DataFrame.at[i, "Octant"] = -3
        if(DataFrame.at[i, "U"] >= 0 and DataFrame.at[i, "V"] < 0 and DataFrame.at[i, "W"] >= 0):
            DataFrame.at[i, "Octant"] = 4
        if(DataFrame.at[i, "U"] >= 0 and DataFrame.at[i, "V"] < 0 and DataFrame.at[i, "W"] < 0):
            DataFrame.at[i, "Octant"] = -4


    DataFrame["Octant ID"] = ''
    DataFrame.at[1, "Octant ID"] = "Overall Count"
    DataFrame.at[2, "Octant ID"] = f"mod: {mod}"

    min_data = 5000
    max_data = 9999

    for i in range(3, 9):
        if(i == 3):
            DataFrame.at[i, "Octant ID"] = "0000-4999"
        else:
            DataFrame.at[i, "Octant ID"] = f" {min_data} - {max_data}"
            min_data = min_data + 5000
            max_data = max_data + 5000


    for row in range(3, 9):
        freq = {}
        if(row == 3):
            min_data=0
            max_data = mod
        for i in range(min_data, max_data):
            if(i >= 29745):
                break
            if(DataFrame.at[i, "Octant"] in freq):
                freq[DataFrame.at[i, "Octant"]]=freq[DataFrame.at[i, "Octant"]] + 1
            else:
                freq[DataFrame.at[i, "Octant"]] = 1
        for key, value in freq.items():
            DataFrame.at[row, key]=value
            if(DataFrame.at[1, key] ==''):
                DataFrame.at[1, key]=0
            DataFrame.at[1, key]=DataFrame.at[1, key] + value
        if(row== 3):
            min_data = mod + 1
            max_data = 2*mod
        if(row>3):
            min_data = min_data + mod
            max_data = max_data + mod
    DataFrame = DataFrame.fillna('')
    print(DataFrame.head(9))


mod=5000
octant_identification(mod)

#DataFrame.to_csv("octant_output.csv",index = False)