# import os
#
# os.chdir(os.getcwd() + '/Stanford_OpenIE_Python')
# pwd = os.getcwd() + '/corpus'
#
# for f in os.listdir(pwd):
#     print('Processing', f+ '...')
#     os.system('./process_large_corpus.sh corpus/' + f + ' relations/' +f)

from stanfordcorenlp import StanfordCoreNLP

nlp = StanfordCoreNLP('http://localhost', port=9000)

sentence = "Petr Čech (; born 20 May 1982) is a Czech professional footballer who plays as a goalkeeper for club Arsenal."
pos = nlp.pos_tag(sentence)
ner = nlp.ner(sentence)
with open('stanford-corenlp-full-2018-10-05/training.corp', 'w') as f:
    for i in range(len(pos)):
        sent = '0\t' + ner[i][1] + '\t' + str(i) + '\tO\t' + pos[i][1] + '\t' + pos[i][0] + '\tO\tO\tO\n'
        f.write(sent)


# pros = {'annotators': 'ner,relation', 'outputFormat': 'text'}
# print(nlp.annotate(sentence, properties=pros))

nlp.close() # Do not forget to close! The backend server will consume a lot memery.