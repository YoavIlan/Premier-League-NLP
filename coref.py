import spacy 

nlp = spacy.load('en_coref_md')

""" Practice code from tutorial """

doc = nlp(u'My sister has a dog. She loves him.')

"""
# print(doc._.has_coref)
# print(doc._.coref_clusters) # prints out all the clusters

# print(doc._.coref_clusters[1].mentions)
# print(doc._.coref_clusters[1].mentions[-1])
# print(doc._.coref_clusters[1].mentions[-1]._.coref_cluster.main)

# token = doc[-1]
# print(doc[-1])
# print(token._.in_coref)
# print(token._.coref_clusters)

# span = doc[-1:]
# print(doc[-1:])
# print(span._.is_coref)
# if span._.is_coref:
# 	print(span._.coref_cluster.main)
# 	print(span._.coref_cluster.main._.coref_cluster)

"""



# Coreferencing for league
# file_name = "league/AA/wiki_00"
# file = open(file_name, "r")
# doc = nlp(file.read())

# Coreferencing for teams
# file_name = "teams/AA/wiki_00"
# file = open(file_name, "r")
# doc = nlp(file.read())

# Coreferencing for players
teams = ["A.F.C._Bournemouth", "Arsenal_F.C.", "Burnley_F.C.", "Cardiff_City_F.C.", 
			"Chelsea_F.C.", "Crystal_Palace_F.C.", "Everton_F.C.", "Fulham_F.C.", "Huddersfield_Town_A.F.C.", 
			"Leicester_City_F.C.", "Liverpool_F.C.", "Manchester_City_F.C.", "Manchester_United_F.C.", "Newcastle_United_F.C.",
			"Southampton_F.C.", "Tottenham_Hotspur_F.C.", "Watford_F.C.", "West_Ham_United_F.C.", "Wolverhampton_Wanderers_F.C."]
# for team in teams:	
# 	file_name = team + "/AA/wiki_00"
# 	file = open(file_name, "r")
# 	doc = nlp(file.read())


file_name = teams[0] + "/AA/wiki_00"
file = open(file_name, "r")
doc = nlp(file.read())

# print(doc._.has_coref)
print(doc._.coref_clusters) # prints out all the clusters



