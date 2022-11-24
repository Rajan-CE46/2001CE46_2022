from datetime import datetime
start_time = datetime.now()

def attendance_report():
    from collections import OrderedDict
    from ast import Str
    from cmath import nan
    from itertools import count
    from lib2to3.pytree import type_repr
    import os
    from csv import writer
    from csv import reader
    from traceback import print_tb
    import numpy as np
    import pandas as pd
    from datetime import datetime
    import calendar

    df1 = pd.read_csv('input_registered_students.csv')  
    df2 = pd.read_csv('input_attendance.csv')  
    df2=df2.fillna('2001ce46 rajan')
    days=['2022-07-28','2022-08-01','2022-08-04','2022-08-08','2022-08-12','2022-08-15','2022-08-18','2022-08-22','2022-08-25','2022-08-29','2022-09-01','2022-09-05','2022-09-08','2022-09-12','2022-09-15','2022-09-19','2022-09-22','2022-09-26','2022-09-29']

    df5=pd.DataFrame(columns=['Roll','Name']+days)
    df5.at[0,'Actual Lecture Taken']='Total Mon+Thurs dynamic count'
    df5.at[0,'Total Real']=''
    df5.at[0,"%Attendance"]=''
    print(df5)
    
    for i in range(0,220):

        # break
        roll_no=df1.at[i,'Roll No']
        name=df1.at[i,'Name']
        
        combine=roll_no +' '+name
        
        
        report_date=[]
    
        df3=pd.DataFrame(columns=['dates'])
        k=0
        total_cnt=len(df2['Timestamp'])
        
        for j in range(0,total_cnt):
            if(df2.at[j,'Attendance'].split()[0]==roll_no):
                df3.at[k,'dates']=(df2.at[j,'Timestamp'])
                k=k+1
        
        
        total_submited=len(df3['dates'])
        
        df3['dates'] = pd.to_datetime(df3['dates'],dayfirst=True)
        
        
        valid_days=[]
    
        
        start='14:00:00'
        end='15:00:00'
        for h in range(0,total_submited):
            
            if(((df3.at[h,'dates'].strftime('%A')=='Monday' )|(df3.at[h,'dates'].strftime('%A')=='Thursday'))  ):
                valid_days.append(df3.at[h,'dates'])

        
        
        Total_Attendance_Count=len(valid_days)
        
        
        path="output/{}".format(roll_no)+'.xlsx'
        df4=pd.read_excel(path)
        
        
        df5.at[i+1,'Name']=name
        df5.at[i+1,'Roll']=roll_no
        
        
        real_cnt=0
        
        df4.at[0,'Roll']=roll_no
        df4.at[0,'Name']=name
        
        
        for k in range(0,len(days)):
            s=days[k]
            attend_day=[]
            for h in range(0,len(valid_days)):
                current_date = valid_days[h].strftime("%Y-%m-%d")
                if(current_date==s):
                    
                    attend_day.append(valid_days[h])
            # print(attend_day)
            cnt=0
            for l in range(0,len(attend_day)):
                current_time = attend_day[l].strftime("%H:%M")
                if(((current_time >= start) & (current_time <= end) ) ):
                    cnt+=1 
                
            real=0
            Absent=1
            dublicate=0
            if(cnt>0):
                real=1      
            if(real>0):
                Absent=0
            if(cnt>1):
                dublicate=cnt-1
            real_cnt+=real
            df4.at[k+1,'Date']=s
            df4.at[k+1,'Total Attendance Count']=cnt
            df4.at[k+1,'Real']=real
            df4.at[k+1,'Duplicate']=dublicate
            df4.at[k+1,'Invalid']=len(attend_day)-cnt
            df4.at[k+1,'Absent']=Absent
            
            
            df5.at[i+1,s]='P'
            if(cnt==0):
                df5.at[i+1,s]='A'
            
            
        df5.at[i+1,'Total Real']=real_cnt
        df5.at[i+1,'%Attendance']=round(real_cnt/12*100,2)
        
    
        df4.to_excel(path, index=False)
        
        
        
    hehe = 'attendance_report_consolidated'  
    df5.to_excel(f'output/{hehe}.xlsx',index=False)

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
