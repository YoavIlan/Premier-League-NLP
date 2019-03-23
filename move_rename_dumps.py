import os

prem_teams = ["A.F.C._Bournemouth",
              "Brighton_Hove_Albion_F.C.",
              "Liverpool_F.C.",
              "Manchester_City_F.C.",
              "Tottenham_Hotspur_F.C.",
              "Arsenal_F.C.",
              "Manchester_United_F.C.",
              "Chelsea_F.C.",
              "Watford_F.C.",
              "Wolverhampton_Wanderers_F.C.",
              "Everton_F.C.",
              "West_Ham_United_F.C.",
              "Leicester_City_F.C.",
              "Newcastle_United_F.C.",
              "Crystal_Palace_F.C.",
              "Burnley_F.C.",
              "Cardiff_City_F.C.",
              "Southampton_F.C.",
              "Fulham_F.C.",
              "Huddersfield_Town_A.F.C."]

pwd = os.getcwd()
for dir in os.listdir(pwd):
    if os.path.isdir(dir) and (dir in prem_teams or dir == 'league' or dir == 'teams'):
        new_dir = dir.strip('.')
        os.replace(dir+'/AA/wiki_00', 'Stanford_OpenIE_Python/corpus/'+new_dir+'.txt')
        os.rmdir(dir+'/AA')