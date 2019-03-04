import xml.etree.ElementTree as ET
import requests
import re

# top5_dict = {
# "Premier_League" : ["A.F.C._Bournemouth",
#                     "Brighton_%26_Hove_Albion_F.C.",
#                     "Liverpool_F.C.",
#                     "Manchester_City_F.C.",
#                     "Tottenham_Hotspur_F.C.",
#                     "Arsenal_F.C.",
#                     "Manchester_United_F.C.",
#                     "Chelsea_F.C.",
#                     "Watford_F.C.",
#                     "Wolverhampton_Wanderers_F.C.",
#                     "Everton_F.C.",
#                     "West_Ham_United_F.C.",
#                     "Leicester_City_F.C.",
#                     "Newcastle_United_F.C.",
#                     "Crystal_Palace_F.C.",
#                     "Burnley_F.C.",
#                     "Cardiff_City_F.C.",
#                     "Southampton_F.C.",
#                     "Fulham_F.C.",
#                     "Huddersfield_Town_A.F.C."],
# "Ligue_1" :        ["Paris_Saint-Germain_F.C.",
#                     "Lille_OSC",
#                     "Olympique_Lyonnais",
#                     "AS_Saint-Étienne",
#                     "Olympique_de_Marseille",
#                     "Stade_de_Reims",
#                     "Montpellier_HSC",
#                     "Racing_Club_de_Strasbourg_Alsace",
#                     "Stade_Rennais_F.C.",
#                     "OGC_Nice",
#                     "Nîmes_Olympique",
#                     "Angers_SCO",
#                     "FC_Girondins_de_Bordeaux",
#                     "FC_Nantes",
#                     "Toulouse_FC",
#                     "AS_Monaco_FC",
#                     "Amiens_SC",
#                     "Stade_Malherbe_Caen",
#                     "Dijon_FCO",
#                     "En_Avant_de_Guingamp"],
# "Bundesliga" :     ["Borussia_Dortmund",
#                     "FC_Bayern_Munich",
#                     "Borussia_Mönchengladbach",
#                     "RB_Leipzig",
#                     "VfL_Wolfsburg",
#                     "Eintracht_Frankfurt",
#                     "Bayer_04_Leverkusen",
#                     "TSG_1899_Hoffenheim",
#                     "SV_Werder_Bremen",
#                     "Hertha_BSC",
#                     "1._FSV_Mainz_05",
#                     "Fortuna_Düsseldorf",
#                     "SC_Freiburg",
#                     "FC_Schalke_04",
#                     "FC_Augsburg",
#                     "VfB_Stuttgart",
#                     "Hannover_96",
#                     "1._FC_Nürnberg"],
# "La_Liga" :        ["FC_Barcelona",
#                     "Atlético_Madrid",
#                     "Real_Madrid_CF",
#                     "Getafe_CF",
#                     "Sevilla_FC",
#                     "Deportivo_Alavés",
#                     "Real_Betis",
#                     "Real_Sociedad",
#                     "Valencia_CF",
#                     "Athletic_Bilbao",
#                     "SD_Eibar",
#                     "CD_Leganés"]
#
# }

prem_teams = ["A.F.C._Bournemouth",
              "Brighton_&_Hove_Albion_F.C.",
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

get main premier league page
params = (
    ('title', 'Special:Export'),
    ('pages', 'Premier_League'),
)

response = requests.get('https://en.wikipedia.org/w/index.php', params=params)
with open("Premier_League.xml", "w") as f:
    f.write(response.text)

#get all team pages and player
for team in prem_teams:
    params = (
        ('title', 'Special:Export'),
        ('pages', team),
    )
    response = requests.get('https://en.wikipedia.org/w/index.php', params=params)
    f_name = 'teams/'+ team + '.xml'
    with open(f_name, "w") as f:
        f.write(response.text)
    tree = ET.parse(f_name)
    root = tree.getroot()

    text = root[1][3][-2].text
    players = re.findall('player\|.+name=(?:\[\[)?(\w*) ([\w \']*)', text)
    for player in players:
        p_name = ' '.join(player).replace('\'\'', '').strip()
        params = (
            ('title', 'Special:Export'),
            ('pages', p_name),
        )
        response = requests.get('https://en.wikipedia.org/w/index.php', params=params)
        f_name = 'players/'+ p_name + '.xml'
        with open(f_name, "w") as f:
            f.write(response.text)


