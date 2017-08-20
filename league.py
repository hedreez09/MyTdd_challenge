	
filename = "football-league-results.txt" 
def leagueResult():
	with open(filename) as result:        #this is to display the content of filename 
		result.next()                     #this removes the first roll of the table since is not needed 
		scoreDiff = []
		clubNamesList = []
		for team in result:
			team = team.split()       #to split the content of the file one by one 
			clubNames = []
			clubData = []

			for data in team:                 #this  function try to check the data in data cast them to integer then except the string as error hen cast them to string 

				try:
					data = int(data)                     
					clubData.append(data)
				except ValueError:
					stringData = str(data)
					if stringData != "-":
						clubNames.append(stringData)
					pass
			if len(clubData) > 0:             #this is to check if this content of clubdata is not emtpy
				scoreFor = int(clubData[4])   #this cast the content of column 5 which is th score for to integer
				scoreAgainst = int(clubData[5]) #this cast the content of column 6 which is th score for to integer
				del clubNames[:1]
				clubNames = ' '.join(clubNames)  #the .join(clubName join the names of clubs with two name)
				clubNamesList.append(clubNames)
				scoreDiff.append(scoreFor - scoreAgainst)

		teamGoalPerformance = dict(zip(clubNamesList,scoreDiff))
		lowestDiffTeam = min(sorted(teamGoalPerformance.keys()))
		lowestDiffScore = min(sorted(teamGoalPerformance.values()))

		print ("The team with the smallest difference in 'for' and 'against' goals is: " + str(lowestDiffTeam) + ':' + str(lowestDiffScore))

leagueResult()
