import pandas as pd
import re
from datetime import datetime
start_time = datetime.now()

#Help
def scorecard():

	with open('india_inns2.txt') as f:
		ind_inn = f.read()
	with open('pak_inns1.txt') as f:
		pak_inn = f.read()
	with open('teams.txt') as f:
		playing = f.read()

	# print(pak_inn)

	a= playing.split("\n")

	pak_list = a[0].split(":")
	pak_plying_11 = pak_list[1].split(",")
	# print(pak_plying_11)

	ind_list = a[2].split(":")
	ind_plying_11 = ind_list[1].split(",")
	# print(ind_plying_11)


	df1 = {}

	df1["Batter"] = [players for players in ind_plying_11]
	df1["Details"] = [0 for players in ind_plying_11]
	df1["Run"] = [0 for players in ind_plying_11]
	df1["Balls"] = [0 for players in ind_plying_11]
	df1["fours"] = [0 for players in ind_plying_11]
	df1["Sixes"] = [0 for players in ind_plying_11]
	df1["strike rate"] = [0 for players in ind_plying_11]

	df2= {}

	df2["Batter"] = [players for players in pak_plying_11]
	df2["Details"] = [0 for players in pak_plying_11]
	df2["Run"] = [0 for players in pak_plying_11]
	df2["Balls"] = [0 for players in pak_plying_11]
	df2["fours"] = [0 for players in pak_plying_11]
	df2["Sixes"] = [0 for players in pak_plying_11]
	df2["strike rate"] = [0 for players in pak_plying_11]
	t = ind_inn.split("\n")
	u = pak_inn.split("\n")
	rajan = ['Rohit','Rahul','Kohli','Suryakumar Yadav','Karthik','Hardik Pandya','Jadeja',"Bhuvneshwar","Avesh Khan","Chahal","Arshdeep Singh"]
	harsa = ['Babar Azam','Rizwan','Fakhar Zaman','Iftikhar Ahmed','Khushdil','Asif Ali','Shadab Khan', 'Mohammad Nawaz', 'Naseem Shah','Haris Rauf','Dahani']
	ind_df = pd.DataFrame(df1)
	pak_df = pd.DataFrame(df2)
	# listee =[]
	iter = 0

	for players in rajan:
		# i = 0
		run_stored = []
		# for players in ind_plying_11:
		Balls = 0
		four_runs = 0
		six_runs = 0
		for elem in t:
			remark = re.search(f'{players},\s\w*\s*\w*(,)?((1|2|3|FOUR|SIX)|no\srun|out)',elem)
			rem_out = re.search(f'{players}\s\w\s\w+\s\w+?\s?\w+?\s?\w+?\s?\w+\s\w+\(\w+\)',elem)
			if rem_out:
				print(rem_out)
				ind_df.at[iter,"Details"]= rem_out.group(0)
			if remark:
				# print(remark)
				rem = (remark[0])
				# print(rem)
				rem = rem.split(', ')
				bats = rem[0]; run = rem[1]
				# print(bats)
				# print(run)
				# Balls+=1

				if run == 'FOUR':
					# print(type(run))
					run_stored.append(4)
					four_runs+=1
					# Balls+=1
				elif run == 'SIX':
					# print(type(run))
					run_stored.append(6)
					six_runs+=1
					# Balls+=1
				else:
					if run != 'no run' and run!= 'out':
						# print(type(run))
						run_stored.append(run)
					# Balls+=1
				Balls+=1
				
				
			
		# print(run_stored)
		int_run = [int(i) for i in run_stored]
		# print(sum(int_run))
		# print(Balls)
		ind_df.at[iter,"Run"]= sum(int_run)
		ind_df.at[iter,"Balls"]= Balls
		ind_df.at[iter,"fours"]= four_runs
		ind_df.at[iter,"Sixes"]= six_runs
		if ind_df.at[iter,"Details"] == 0:
			ind_df.at[iter,"Details"] = "NOT OUT/ DNB"

		
		if Balls!=0:
			ind_df.at[iter,"strike rate"]= sum(int_run)/Balls*100
		else:
			ind_df.at[iter,"strike rate"]= 0
		iter+=1


	iter = 0
	for players in harsa:
		# i = 0
		run_stored = []
		# for players in ind_plying_11:
		Balls = 0
		four_runs = 0
		six_runs = 0
		for elem in u:
			remark = re.search(f'{players},\s\w*\s*\w*(,)?((1|2|3|FOUR|SIX)|no\srun|out)',elem)
			rem_out = re.search(f'{players}\s\w\s\w+\s\w+?\s?\w+?\s?\w+?\s?\w+\s\w+\(\w+\)',elem)
			if rem_out:
				print(rem_out)
				pak_df.at[iter,"Details"]= rem_out.group(0)
			if remark:
				# print(remark)
				rem = (remark[0])
				# print(rem)
				rem = rem.split(', ')
				bats = rem[0]; run = rem[1]
				# print(bats)
				# print(run)
				# Balls+=1

				if run == 'FOUR':
					# print(type(run))
					run_stored.append(4)
					four_runs+=1
					# Balls+=1
				elif run == 'SIX':
					# print(type(run))
					run_stored.append(6)
					six_runs+=1
					# Balls+=1
				else:
					if run != 'no run' and run!= 'out':
						# print(type(run))
						run_stored.append(run)
					# Balls+=1
				Balls+=1
				
				
			
		# print(run_stored)
		int_run = [int(i) for i in run_stored]
		# print(sum(int_run))
		# print(Balls)
		pak_df.at[iter,"Run"]= sum(int_run)
		pak_df.at[iter,"Balls"]= Balls
		pak_df.at[iter,"fours"]= four_runs
		pak_df.at[iter,"Sixes"]= six_runs
		if pak_df.at[iter,"Details"] == 0:
			pak_df.at[iter,"Details"] = "NOT OUT/ DNB"
		if Balls!=0:
			pak_df.at[iter,"strike rate"]= sum(int_run)/Balls*100
		else:
			pak_df.at[iter,"strike rate"]= 0
		iter+=1


	ind_df.to_excel("score_ind.xlsx",index = False)
	pak_df.to_excel("score_pak.xlsx",index = False)



###Code

from platform import python_version
ver = python_version()

if ver == "3.8.10":
	print("Correct Version Installed")
else:
	print("Please install 3.8.10. Instruction are present in the GitHub Repo/Webmail. Url: https://pastebin.com/nvibxmjw")


scorecard()






#This shall be the last lines of the code.
end_time = datetime.now()
print('Duration of Program Execution: {}'.format(end_time - start_time))
