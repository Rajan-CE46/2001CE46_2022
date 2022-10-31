from datetime import datetime
start_time = datetime.now()

def attendance_report():
    import pandas as pd
    import numpy as np
    import os
    import glob
    import re
    import datetime
    # reading input file
    Dataframe = pd.read_csv('input_attendance.csv')
    Dataframe1 = pd.read_csv("input_registered_students.csv")

    df_cons = pd.read_csv(r"output\attendance_report_consolidated.csv")
    rollcount = Dataframe['Attendance'].tolist()
    rollcount1 = [str(x) for x in rollcount]
    rollcount2 = [y.upper() for y in rollcount1]

    # for z in range(len(Dataframe)):
    dates = Dataframe['Timestamp'].tolist()
    list_times = []
    for z in range(len(dates)):
        l5= re.findall(r"[\w']+",dates[z])
        list_times.append(l5)
        
    # print(list_times)

    lect = 1
    for p in range(1,len(list_times)):  
        if(int(list_times[p-1][0]) != int(list_times[p][0]) or int(list_times[p-1][1]) != int(list_times[p][1]) ):
            if(datetime.datetime(int(list_times[p][2]),int(list_times[p][1]),int(list_times[p][0])).weekday() == 0 or datetime.datetime(int(list_times[p][2]),int(list_times[p][1]),int(list_times[p][0])).weekday()== 3):
                lect+=1
    lect = lect -1
    print(lect)


    path ='output'
    all_files = glob.glob(path + "/*.csv")
    a = 0    
    for i in range(222):
        if a == 221:
            break
        else:
            df2 = pd.read_csv(f"""{all_files[i]}""")
            df2.at[0,'Roll'] = f"""{Dataframe1.at[i,'Roll No']}"""
            df2.at[0,'Name'] = f"""{Dataframe1.at[i,'Name']}"""
            df2.at[0,'total_lecture_taken'] = lect
            df_cons.at[i,'total_lecture_taken'] = lect
            df_cons.at[i,'Roll'] = f"""{Dataframe1.at[i,'Roll No']}"""
            df_cons.at[i,'Name'] = f"""{Dataframe1.at[i,'Name']}"""
            l2 = 0
            for k in range(len(Dataframe)):
                l1= re.findall(r"[\w']+",Dataframe.at[k,"Timestamp"])
    #             print(l1)
                if(f"{Dataframe.at[k,'Attendance']}".upper() == f"{Dataframe1.at[i,'Roll No']} {Dataframe1.at[i,'Name']}"):
                    if(datetime.datetime(int(l1[2]),int(l1[1]),int(l1[0])).weekday() == 0 or datetime.datetime(int(l1[2]),int(l1[1]),int(l1[0])).weekday() == 3):
                        if(int(l1[3])==14 or (int(l1[3])==15 and int(l1[4]) == 0 and int(l1[5])==0)):
                            l2+=1
                
    #         print(l2) 
            df2.at[0,'attendance_count_actual'] = int(l2)
            df2.at[0,'attendance_count_fake'] = int(rollcount2.count(f"{Dataframe1.at[i,'Roll No']} {Dataframe1.at[i,'Name']}"))-int(l2)
            df2.at[0,'attendance_count_absent'] = int(lect) - int(df2.at[0,'attendance_count_actual'])
            
            df_cons.at[i,'attendance_count_actual'] = int(l2)
            df_cons.at[i,'attendance_count_absent'] = int(lect) - int(df2.at[0,'attendance_count_actual'])
            df_cons.at[i,'attendance_count_fake'] = int(rollcount2.count(f"{Dataframe1.at[i,'Roll No']} {Dataframe1.at[i,'Name']}"))-int(l2)
    #         if(int(df2.at[0,'total_lecture_taken'])!=0):
            df_cons.at[i,'Percentage (attendance_count_actual/total_lecture_taken) 2 digit decimal '] = round(int(df2.at[0,'attendance_count_actual'])*100/int(lect),2)
            df2.at[0,'Percentage (attendance_count_actual/total_lecture_taken) 2 digit decimal '] = round(int(df2.at[0,'attendance_count_actual'])*100/int(lect),2)
            a = a+1
        df2.to_csv(f"""{all_files[i]}""",index = False)
    df_cons.to_csv(f"""{all_files[221]}""",index = False)
    df_cons.head(20)

from platform import python_version
ver = python_version()

if ver == "3.8.10":
    print("Correct Version Installed")
else:
    print("Please install 3.8.10. Instruction are present in the GitHub Repo/Webmail. Url: https://pastebin.com/nvibxmjw")


attendance_report()




#This shall be the last lines of the code.
end_time = datetime.now()
print('Duration of Program Execution: {}'.format(end_time - start_time))
