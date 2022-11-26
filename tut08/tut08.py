import pandas as pd
import re
from datetime import datetime
start_time = datetime.now()
print(2%6)
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
	df1[" "] = ["Batting Stats" for players in ind_plying_11]
	df1["Batter"] = [players for players in ind_plying_11]
	
	df1["Out By"] = [0 for players in ind_plying_11]
	df1["Run"] = [0 for players in ind_plying_11]
	df1["Balls"] = [0 for players in ind_plying_11]
	df1["fours"] = [0 for players in ind_plying_11]
	df1["Sixes"] = [0 for players in ind_plying_11]
	df1["strike rate"] = [0 for players in ind_plying_11]
	df1["   "] = ["Balling Stats" for players in ind_plying_11]
	df1["Overs Bowled"] = [0 for players in ind_plying_11]
	df1["Wides"] = [0 for players in ind_plying_11]
	df1["Runs Given"] = [0 for players in ind_plying_11]
	df1["Wickets Taken"] = [0 for players in ind_plying_11]
	df1["Economy"] = [0 for players in ind_plying_11]

	df2 = {}
	df2[" "] = ["Batting Stats" for players in pak_plying_11]
	df2["Batter"] = [players for players in pak_plying_11]
	
	df2["Out By"] = [0 for players in pak_plying_11]
	df2["Run"] = [0 for players in pak_plying_11]
	df2["Balls"] = [0 for players in pak_plying_11]
	df2["fours"] = [0 for players in pak_plying_11]
	df2["Sixes"] = [0 for players in pak_plying_11]
	df2["strike rate"] = [0 for players in pak_plying_11]
	df2["   "] = ["Balling Stats" for players in pak_plying_11]
	df2["Overs Bowled"] = [0 for players in pak_plying_11]
	df2["Wides"] = [0 for players in pak_plying_11]
	df2["Runs Given"] = [0 for players in pak_plying_11]
	df2["Wickets Taken"] = [0 for players in pak_plying_11]
	df2["Economy"] = [0 for players in pak_plying_11]

	t = ind_inn.split("\n")
	u = pak_inn.split("\n")
	rajan = ['Rohit','Rahul','Kohli','Suryakumar Yadav','Karthik','Hardik Pandya','Jadeja',"Bhuvneshwar","Avesh Khan","Chahal","Arshdeep Singh"]
	harsa = ['Babar Azam','Rizwan','Fakhar Zaman','Iftikhar Ahmed','Khushdil','Asif Ali','Shadab Khan', 'Mohammad Nawaz', 'Naseem Shah','Haris Rauf','Dahani']
	ind_df = pd.DataFrame(df1)
	pak_df = pd.DataFrame(df2)
	iter = 0
	
	for players in rajan:
		# i = 0
		run_stored = []
		overall_score= 0
		# for players in ind_plying_11:
		Balls = 0
		wides = 0
		runs_made = 0
		runs_given = 0
		wickets_taken=0
		ball_bolw=0
		ball_playd = 0
		four_runs = 0
		six_runs = 0
		for hehe in u:
			
			rem_ball = re.match(f'\d+\.\d\s{players}\sto',hehe)
			
		
			if rem_ball:
				if re.search(r',\s1\srun,',hehe):
					runs_given+=1
				elif re.search(r',\s2\sruns,',hehe):
					runs_given+=2
				elif re.search(r',\s3\sruns,',hehe):
					runs_given+=3
				elif re.search(r',\sSIX,',hehe):
					runs_given+=6
				elif re.search(r',\sFOUR,',hehe):
					runs_given+=4
				elif re.search(r',\sout\s',hehe):
					wickets_taken+=1
				if re.search(r',\swide,',hehe):
					wides+=1
					runs_given+=1
				else:
					ball_bolw+=1

			
		for elem in t:
			rem_bat = re.search(f'\sto\s{players},\s',elem)
			rem_leg = re.search(f',\sleg byes,\s',elem)
			rem_out = re.search(f'({players}\s)(\w+)?(\w\s\w+\s\w+?\s?\w+?\s?\w+?\s?\w+\s(\w+\(\w+\)))',elem)
			if rem_out:
				# print(rem_out)
				ind_df.at[iter,"Out By"]= rem_out.group(3)
			if rem_bat:
				if ind_df.at[iter,"Out By"] == 0:
					ind_df.at[iter,"Out By"]="Not Out"
			
			if rem_bat:
				if rem_leg:
					if re.search(r',\s1\srun,',elem):
						overall_score+=1
					elif re.search(r',\s2\sruns,',elem):
						overall_score+=2
					elif re.search(r',\s3\sruns,',elem):
						overall_score+=3
					elif re.search(r',\sSIX,',elem):
						overall_score+=6
					elif re.search(r',\sFOUR,',elem):
						overall_score+=4
				else:
					if re.search(r',\s1\srun,',elem):
						runs_made+=1
					elif re.search(r',\s2\sruns,',elem):
						runs_made+=2
					elif re.search(r',\s3\sruns,',elem):
						runs_made+=3
					elif re.search(r',\sSIX,',elem):
						runs_made+=6
						six_runs+=1
					elif re.search(r',\sFOUR,',elem):
						runs_made+=4
						four_runs+=1
					# if re.search(r',\swide,',hehe):
				ball_playd+=1
				if re.search(r',\swide|wides,',elem):
					ball_playd-=1

			
		if ball_bolw!=0:
			ind_df.at[iter,'Overs Bowled']= f'{ball_bolw//6}.{ball_bolw%6}'
			ind_df.at[iter,'Wides']= wides
			ind_df.at[iter,'Runs Given']= runs_given
			ind_df.at[iter,'Wickets Taken']= wickets_taken
			ind_df.at[iter,'Economy']= runs_given*6/ball_bolw

		else:	
			ind_df.at[iter,'Overs Bowled']= "DID NOT BALL"

		ind_df.at[iter,'Run'] = runs_made
		ind_df.at[iter,"Balls"]= ball_playd
		ind_df.at[iter,"fours"]= four_runs
		ind_df.at[iter,"Sixes"]= six_runs
		if ball_playd!=0:
			ind_df.at[iter,"strike rate"]= (runs_made/ball_playd)*100

		if rem_out:
			print(rem_out)
			ind_df.at[iter,"Out By"]= rem_out.group()
		if ind_df.at[iter,"Out By"] == 0:
			ind_df.at[iter,"Out By"]="DID NOT BAT"
		iter+=1

		
	
	iter = 0
	for players in harsa:
		# i = 0
		run_stored = []
		overall_score= 0
		# for players in ind_plying_11:
		Balls = 0
		wides = 0
		runs_made = 0
		runs_given = 0
		wickets_taken=0
		ball_bolw=0
		ball_playd = 0
		four_runs = 0
		six_runs = 0
		for hehe in t:
			
			rem_ball = re.match(f'\d+\.\d\s{players}\sto',hehe)
			
		
			if rem_ball:
				if re.search(r',\s1\srun,',hehe):
					runs_given+=1
				elif re.search(r',\s2\sruns,',hehe):
					runs_given+=2
				elif re.search(r',\s3\sruns,',hehe):
					runs_given+=3
				elif re.search(r',\sSIX,',hehe):
					runs_given+=6
				elif re.search(r',\sFOUR,',hehe):
					runs_given+=4
				elif re.search(r',\sout\s',hehe):
					wickets_taken+=1
				if re.search(r',\swide,',hehe):
					wides+=1
					runs_given+=1
				else:
					ball_bolw+=1

			
		for elem in u:
			rem_bat = re.search(f'\sto\s{players},\s',elem)
			rem_leg = re.search(f',\sleg byes,\s',elem)
			rem_out = re.search(f'({players}\s)(\w+)?(\w\s\w+\s\w+?\s?\w+?\s?\w+?\s?\w+\s(\w+\(\w+\)))',elem)
			if rem_out:
				# print(rem_out)
				pak_df.at[iter,"Out By"]= rem_out.group(3)
			if rem_bat:
				if pak_df.at[iter,"Out By"] == 0:
					pak_df.at[iter,"Out By"]="Not Out"
				if rem_leg:
					if re.search(r',\s1\srun,',elem):
						overall_score+=1
					elif re.search(r',\s2\sruns,',elem):
						overall_score+=2
					elif re.search(r',\s3\sruns,',elem):
						overall_score+=3
					elif re.search(r',\sSIX,',elem):
						overall_score+=6
					elif re.search(r',\sFOUR,',elem):
						overall_score+=4
				else:
					if re.search(r',\s1\srun,',elem):
						runs_made+=1
					elif re.search(r',\s2\sruns,',elem):
						runs_made+=2
					elif re.search(r',\s3\sruns,',elem):
						runs_made+=3
					elif re.search(r',\sSIX,',elem):
						runs_made+=6
						six_runs+=1
					elif re.search(r',\sFOUR,',elem):
						runs_made+=4
						four_runs+=1
					# if re.search(r',\swide,',hehe):
				ball_playd+=1
				if re.search(r',\s\w?\swide|wides,',elem):
					ball_playd-=1

			
		if ball_bolw!=0:
			if ball_bolw//6==4 and ball_bolw%6 !=0:
				pak_df.at[iter,'Overs Bowled']= '4'
			else:
				pak_df.at[iter,'Overs Bowled']= f'{ball_bolw//6}.{ball_bolw%6}'
			pak_df.at[iter,'Wides']= wides
			pak_df.at[iter,'Runs Given']= runs_given
			pak_df.at[iter,'Wickets Taken']= wickets_taken
			pak_df.at[iter,'Economy']= runs_given*6/ball_bolw
		else:	
			pak_df.at[iter,'Overs Bowled']= "DID NOT BALL"

		pak_df.at[iter,'Run'] = runs_made
		pak_df.at[iter,"Balls"]= ball_playd
		pak_df.at[iter,"fours"]= four_runs
		pak_df.at[iter,"Sixes"]= six_runs
		if ball_playd!=0:
			pak_df.at[iter,"strike rate"]= (runs_made/ball_playd)*100

		if rem_out:
			print(rem_out)
			pak_df.at[iter,"Out By"]= rem_out.group()
		iter+=1


	ind_df.at[0," "] = "BATTING STATES"
	for hy in range(1,11):
		ind_df.at[hy," "] = "   "
	ind_df.at[0,"   "] = "BALLING STATES"
	for hy in range(1,11):
		ind_df.at[hy,"   "] = "   "

	pak_df.at[0," "] = "BATTING STATES"
	for hj in range(1,11):
		pak_df.at[hj," "] = "   "
	pak_df.at[0,"   "] = "BALLING STATES"
	for hy in range(1,11):
		pak_df.at[hy,"   "] = "   "

	ind_df.to_excel("scorecard_india.xlsx",index = False)
	pak_df.to_excel("scorecard_pakistan.xlsx",index = False)



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
