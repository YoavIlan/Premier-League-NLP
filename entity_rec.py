import spacy

nlp = spacy.load('en_core_web_sm')

# Entity recognition for league
# file_name = "league/AA/wiki_00"
# file = open(file_name, "r")
# doc = nlp(file.read())
# for ent in doc.ents:
# 	print(ent.text, ent.start_char, ent.end_char, ent.label_)

# Entity recognition for teams
# file_name = "teams/AA/wiki_00"
# file = open(file_name, "r")
# doc = nlp(file.read())
# for ent in doc.ents:
# 	print(ent.text, ent.start_char, ent.end_char, ent.label_)

# Entity recognition for players
teams = ["A.F.C._Bournemouth", "Arsenal_F.C.", "Burnley_F.C.", "Cardiff_City_F.C.", 
			"Chelsea_F.C.", "Crystal_Palace_F.C.", "Everton_F.C.", "Fulham_F.C.", "Huddersfield_Town_A.F.C.", 
			"Leicester_City_F.C.", "Liverpool_F.C.", "Manchester_City_F.C.", "Manchester_United_F.C.", "Newcastle_United_F.C.",
			"Southampton_F.C.", "Tottenham_Hotspur_F.C.", "Watford_F.C.", "West_Ham_United_F.C.", "Wolverhampton_Wanderers_F.C."]
for team in teams:	
	file_name = team + "/AA/wiki_00"
	file = open(file_name, "r")
	doc = nlp(file.read())
	for ent in doc.ents:
		print(ent.text, ent.start_char, ent.end_char, ent.label_)