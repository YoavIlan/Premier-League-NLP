import xml.etree.ElementTree as ET
import requests
import re
import os
# from wikiextractor import WikiExtractor as WE


prem_teams = ["A.F.C._Bournemouth",
              "Brighton_%26_Hove_Albion_F.C.",
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

# get main premier league page
params = (
    ('title', 'Special:Export'),
    ('pages', 'Premier_League'),
)

response = requests.get('https://en.wikipedia.org/w/index.php', params=params)
# with open("Premier_League.xml", "w") as f:
#     f.write(response.text)

response = requests.get('https://en.wikipedia.org/w/index.php?title=Special:Export&pages=' + '%0A'.join(prem_teams))
f_name = 'teams.xml'
# with open(f_name, "w") as f:
#     f.write(response.text)

tree = ET.parse(f_name)
root = tree.getroot()
for ch in root:
    try:
        text = ch[3][-2].text
        team = ch[0].text.replace(' ','_')
        if team == 'Brighton_&_Hove_Albion_F.C.':
            team = 'Brighton_Hove_Albion_F.C.'

    except:
        continue
    players = re.findall('player *\|.+name=(?:\[\[)?(\w*) ([\w \']*)', text)
    player_list = ['_'.join(player).replace('\'\'', '').strip() for player in players]
    with open('stanford-corenlp-full-2018-10-05/ner.corp', 'a') as wf:
        for player in player_list:
            wf.write(player.replace('_', '\tPLAYER\n') + '\tPLAYER\n\n')
    response = requests.get('https://en.wikipedia.org/w/index.php?title=Special:Export&pages=' + '%0A'.join(player_list))
    f_name = team + '/players.xml'
    if not os.path.exists(os.path.dirname(f_name)):
        try:
            os.makedirs(os.path.dirname(f_name))
        except OSError as exc: # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise
#     with open(f_name, "w") as f:
#         f.write(response.text)
#     os.system('python wikiextractor/WikiExtractor.py -o ' + team + ' ' + team + '/players.xml')
#
# os.system('python wikiextractor/WikiExtractor.py -o league Premier_League.xml')
# os.system('python wikiextractor/WikiExtractor.py -o teams teams.xml')





