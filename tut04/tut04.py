from datetime import datetime
start_time = datetime.now()
#Help https://youtu.be/H37f_x4wAC0

def octant_longest_subsequence_count_with_range():
    #importing libraries
    import pandas as pd
    import numpy as np
    # Trying if input file is there or not and if there is some error then printing that in the except block
    try:
        # reading input file
        Dataframe = pd.read_excel('input_octant_longest_subsequence_with_range.xlsx')
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
                    
            # Inserting additional columns and also putting desired strings in that according to output file
            # First of all leaving a blank column after octant column
            # alsp putting +1,-1 ... at there desired cell
            Dataframe.at[0,' '] = ' '
            Dataframe.at[0,'  '] = 'Octant'
            Dataframe.at[0,'     '] = 'Longest Subsquence Length'
            Dataframe.at[0,'      '] = 'Count'

            # creating a list1 that is containing octant values
            list1 = [1,-1,2,-2,3,-3,4,-4]
            list5 = ["+1","-1","+2","-2","+3","-3","+4","-4"]
            for i in range(8):
                Dataframe.at[i+1,'  '] = str(list5[i])

            # Also creating list2 and list3 these lists are used to store largest subsequence count and no of occurance using append 
            list2 = []
            list3 = []
            
            time_end = []
            # Creatind a function that will take a item and a list and give all occurances of that item no matter if it is repeating 
            def find_indices(list_to_check, item_to_find):
                return [idx for idx, value in enumerate(list_to_check) if value == item_to_find]

            for n in list1:
                a = 0
                list = []
                time = []
                for i in range(z-1):
                    
                    if Dataframe.at[i,'Octant'] == n and Dataframe.at[i+1,'Octant'] == n:
                        a = a+1
                        # this a will be keep on adding till the same octant value is getting
                    elif Dataframe.at[i,'Octant'] == n and Dataframe.at[i+1,'Octant'] != n:
                        # Just after we get diff octant value nos of occ is stored in list using append
                        list.append(a+1)
                        time.append(i)#this will keep on adding end time i values 
                        # then again a =  0 for next cycle
                        a=0
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
                occ_list = find_indices(list, largest_count)
                for k in occ_list:
                    time_end.append(time[k])# this will keep on adding the end time of largest occurance 
                
            #     time_end.append(time[ix])
            
                # now finally pribnting them in their desired place

            # print(list2 , end = " ")
            # for i in range(len(time_end)):
            #     time_start[i] = time_end[i]-(list2[i]-1)
                
            # print(time_start,end = " ")
            # print(time_end,end = " ")
            for n in range(8):    
                Dataframe.at[n+1,'     '] = list2[n]
                Dataframe.at[n+1,'      '] = list3[n]
            #putting values in excel sheet as per output file 
            Dataframe.at[0,'        '] = ' '
            Dataframe.at[0,'           '] = 'Octant'
            Dataframe.at[0,'              '] = 'Longest Subsquence Length'
            Dataframe.at[0,'                  '] = 'Count'

            Dataframe.at[1,'           '] = '+1'
            Dataframe.at[2,'           '] = 'Time'
            Dataframe.at[2,'              '] = 'From'
            Dataframe.at[3,'              '] = Dataframe.at[time_end[0]-(list2[0]-1),'Time']

            Dataframe.at[2,'                  '] = 'To'
            Dataframe.at[3,'                  '] = Dataframe.at[time_end[0],'Time']

            Dataframe.at[4,'           '] = '-1'
            Dataframe.at[5,'           '] = 'Time'
            Dataframe.at[5,'              '] = 'From'
            #printing time values 
            Dataframe.at[6,'              '] = Dataframe.at[time_end[1]-(list2[1]-1),'Time']
            Dataframe.at[7,'              '] = Dataframe.at[time_end[2]-(list2[1]-1),'Time']
            Dataframe.at[8,'              '] = Dataframe.at[time_end[3]-(list2[1]-1),'Time']
            Dataframe.at[5,'                  '] = 'To'
            Dataframe.at[6,'                  '] = Dataframe.at[time_end[1],'Time']
            Dataframe.at[7,'                  '] = Dataframe.at[time_end[2],'Time']
            Dataframe.at[8,'                  '] = Dataframe.at[time_end[3],'Time']

            for i in range(6):
                Dataframe.at[9+3*i,'           '] = str(list5[i+2])
                Dataframe.at[10+3*i,'           '] = 'Time'
                Dataframe.at[10+3*i,'              '] = 'From'
                Dataframe.at[10+3*i+1,'              '] = Dataframe.at[time_end[i+4]-(list2[i+2]-1),'Time']
                
                Dataframe.at[10+3*i,'                  '] = 'To'
                Dataframe.at[10+3*i+1,'                  '] = Dataframe.at[time_end[i+4],'Time']

            Dataframe.at[1,'              '] = list2[0]
            Dataframe.at[1,'                  '] = list3[0]
            Dataframe.at[4,'              '] = list2[1]
            Dataframe.at[4,'                  '] = list3[1]

            for n in range(8,25,3):    
                Dataframe.at[n+1,'              '] = list2[n//3]
                Dataframe.at[n+1,'                  '] = list3[n//3]
            #just replcing 1 to +1 and same for others

            for i in range(z):
                if(Dataframe.at[i, "U'=U-U Avg"] >= 0 and Dataframe.at[i, "V'=V-V Avg"] >= 0 and Dataframe.at[i, "W'=W-W Avg"] >= 0):
                    Dataframe.at[i, "Octant"] = "+1"
                if(Dataframe.at[i, "U'=U-U Avg"] >= 0 and Dataframe.at[i, "V'=V-V Avg"] >= 0 and Dataframe.at[i, "W'=W-W Avg"] < 0):
                    Dataframe.at[i, "Octant"] = "-1"
                if(Dataframe.at[i, "U'=U-U Avg"] < 0 and Dataframe.at[i, "V'=V-V Avg"] >= 0 and Dataframe.at[i, "W'=W-W Avg"] >= 0):
                    Dataframe.at[i, "Octant"] = "+2"
                if(Dataframe.at[i, "U'=U-U Avg"] < 0 and Dataframe.at[i, "V'=V-V Avg"] >= 0 and Dataframe.at[i, "W'=W-W Avg"] < 0):
                    Dataframe.at[i, "Octant"] = "-2"
                if(Dataframe.at[i, "U'=U-U Avg"] < 0 and Dataframe.at[i, "V'=V-V Avg"] < 0 and Dataframe.at[i, "W'=W-W Avg"] >= 0):
                    Dataframe.at[i, "Octant"] = "+3"
                if(Dataframe.at[i, "U'=U-U Avg"] < 0 and Dataframe.at[i, "V'=V-V Avg"] < 0 and Dataframe.at[i, "W'=W-W Avg"] < 0):
                    Dataframe.at[i, "Octant"] = "-3"
                if(Dataframe.at[i, "U'=U-U Avg"] >= 0 and Dataframe.at[i, "V'=V-V Avg"] < 0 and Dataframe.at[i, "W'=W-W Avg"] >= 0):
                    Dataframe.at[i, "Octant"] = "+4"
                if(Dataframe.at[i, "U'=U-U Avg"] >= 0 and Dataframe.at[i, "V'=V-V Avg"] < 0 and Dataframe.at[i, "W'=W-W Avg"] < 0):
                    Dataframe.at[i, "Octant"] = "-4"
                
            Dataframe = Dataframe.fillna(' ')
            # just printing first 20 data rows
            Dataframe.head(20)
            #checking if output file is getting modified or created        
            try:
                Dataframe.to_excel("output_octant_longest_subsequence_with_range.xlsx", index=False)
            except Exception as e:
                print(e)
                print("Maybe Output File is already open somewhere!! To modify it please close that file and try again")


from platform import python_version
ver = python_version()

if ver == "3.8.10":
    print("Correct Version Installed")
else:
    print("Please install 3.8.10. Instruction are present in the GitHub Repo/Webmail. Url: https://pastebin.com/nvibxmjw")


try:
    octant_longest_subsequence_count_with_range()

except Exception as e:
    print(e)

#This shall be the last lines of the code.

end_time = datetime.now()
print('Duration of Program Execution: {}'.format(end_time - start_time))
