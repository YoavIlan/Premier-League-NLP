import os
#
# os.chdir(os.getcwd() + '/Stanford_OpenIE_Python')
# pwd = os.getcwd() + '/corpus'
#
# for f in os.listdir(pwd):
#     print('Processing', f+ '...')
#     os.system('./process_large_corpus.sh corpus/' + f + ' relations/' +f)

from stanfordcorenlp import StanfordCoreNLP
import re

def chunkstring(string, length):
    return (string[0+i:length+i] for i in range(0, len(string), length))

nlp = StanfordCoreNLP('http://localhost', port=9000)

# sentence = "During his eleven year stay at the club, Čech registered 494 senior appearances, making him the club's highest overseas appearance maker, and sixth all-time. He also helped the club win four Premier League titles, four FA Cups, three League Cups, one UEFA Europa League title, and one UEFA Champions League title."
# sentence = "In France, Čech starred in an under-performing team, and soon moved to Premier League side Chelsea for a fee of £7 million (€9.8 million) in 2004, which was then a club record transfer for a goalkeeper."
# pos = nlp.pos_tag(sentence)
# ner = nlp.ner(sentence)
# with open('stanford-corenlp-full-2018-10-05/training.corp', 'w') as f:
#     for i in range(len(pos)):
#         sent = '0\t' + ner[i][1] + '\t' + str(i) + '\tO\t' + pos[i][1] + '\t' + pos[i][0] + '\tO\tO\tO'
#         print(sent)

info = []
with open('Stanford_OpenIE_Python/corpus/Arsenal_F.C.txt') as file:
    file_str = file.read()

    for sentence in chunkstring(file_str, 1000):
        pros = {'annotators': 'relation', 'outputFormat': 'text'}
        relations = nlp.annotate(sentence, properties=pros)
        # print(relations)
        info += re.findall('RelationMention \[type=(is).*\s.*type=PEOPLE.*value="(.*)".*\s.*type=NATIONALITY.*value="(.*)"', relations)
        info += re.findall('RelationMention \[type=(plays_for).*\s.*type=PEOPLE.*value="(.*)".*\s.*type=ORGANIZATION.*value="(.*)"', relations)
with open('Stanford_OpenIE_Python/relations/Arsenal_F.C.txt', 'w') as wf:
    for triple in info:
        wf.write(triple[1] + ' | ' + triple[0] + ' | ' + triple[2] + '\n')
nlp.close() # Do not forget to close! The backend server will consume a lot memery.