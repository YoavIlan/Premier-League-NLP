import spacy 

nlp = spacy.load('en_coref_md')

# Coreferencing for league
file_name = "league.txt"
file = open(file_name, "r")
doc = nlp(file.read())

new_file = open("resolved/league_coref.txt", "w")
new_file.write(doc._.coref_resolved)
new_file.close()

print("finished coreferencing " + file_name)

# Coreferencing for teams
file_name = "teams.txt"
file = open(file_name, "r")
doc = nlp(file.read())

new_file = open("resolved/teams_coref.txt", "w")
new_file.write(doc._.coref_resolved)
new_file.close()

print("finished coreferencing " + file_name)

# Coreferencing for players
teams = ["A.F.C._Bournemouth", "Arsenal_F.C.", "Burnley_F.C.", "Cardiff_City_F.C.", 
			"Chelsea_F.C.", "Crystal_Palace_F.C.", "Everton_F.C.", "Fulham_F.C.", "Huddersfield_Town_A.F.C.", 
			"Leicester_City_F.C.", "Liverpool_F.C.", "Manchester_City_F.C.", "Manchester_United_F.C.", "Newcastle_United_F.C.",
			"Southampton_F.C.", "Tottenham_Hotspur_F.C.", "Watford_F.C.", "West_Ham_United_F.C.", "Wolverhampton_Wanderers_F.C."]

for team in teams:	
	file_name = team + "txt"
	file = open(file_name, "r")
	doc = nlp(file.read())

	new_file = open("resolved/" + team + "_coref.txt", "w")
	new_file.write(doc._.coref_resolved)
	new_file.close()

	print("finished coreferencing " + file_name)


