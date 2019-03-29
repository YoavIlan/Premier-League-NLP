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

# sentence = "Gonzalo Gerardo Higuaín (, born 10 December 1987) is an Argentine professional footballer who plays as a striker for English club Chelsea, on loan from Juventus, and the Argentina national team."
# pos = nlp.pos_tag(sentence)
# ner = nlp.ner(sentence)
# for i in range(len(pos)):
#     sent = '0\t' + ner[i][1] + '\t' + str(i) + '\tO\t' + pos[i][1] + '\t' + pos[i][0] + '\tO\tO\tO'
#     print(sent)
pwd = os.getcwd() + '/Stanford_OpenIE_Python/corpus'

for f in os.listdir(pwd):
    info = []

    with open('Stanford_OpenIE_Python/corpus/'+f) as file:
        file_str = file.read()
        num = len(file_str) // 1000 + 1
        count = 1
        for sentence in chunkstring(file_str, 1000):
            print(f,'part', count, 'of', num)
            count += 1
            pros = {'annotators': 'relation', 'outputFormat': 'text'}
            relations = nlp.annotate(sentence, properties=pros)
            # if re.findall('RelationMention \[type=(plays_for).*\s.*type=PEOPLE.*value="(.*)".*\s.*type=ORGANIZATION.*value="(.*)"', relations):
            # print(relations)
            info += re.findall('RelationMention \[type=(is).*\s.*type=PEOPLE.*value="(.*)".*\s.*type=NATIONALITY.*value="(.*)"', relations)
            info += re.findall('RelationMention \[type=(plays_for).*\s.*type=PEOPLE.*value="(.*)".*\s.*type=ORGANIZATION.*value="(.*)"', relations)
    with open('Stanford_OpenIE_Python/relations/'+f, 'w') as wf:
        for triple in info:
            wf.write(triple[1] + ' | ' + triple[0] + ' | ' + triple[2] + '\n')
nlp.close() # Do not forget to close! The backend server will consume a lot memery.