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
all_sentences = []

sentence = "Petr Čech (; born 20 May 1982) is a Czech professional footballer who plays as a goalkeeper for club Arsenal."
pos = nlp.pos_tag(sentence)
ner = nlp.ner(sentence)
for i in range(len(pos)):
    sent = '0\t' + ner[i][1] + '\t' + str(i) + '\tO\t' + pos[i][1] + '\t' + pos[i][0] + '\tO\tO\tO\n'
all_sentences.append(sent)

sentence = "Héctor Bellerín Moruno (, born 19 March 1995) is a Spanish professional footballer who plays as a right back or wing back for club Arsenal and the Spain national team."
pos = nlp.pos_tag(sentence)
ner = nlp.ner(sentence)
for i in range(len(pos)):
    sent = '0\t' + ner[i][1] + '\t' + str(i) + '\tO\t' + pos[i][1] + '\t' + pos[i][0] + '\tO\tO\tO\n'
all_sentences.append(sent)

sentence = "Mohamed Naser Elsayed Elneny ( , ; born 11 July 1992) simply known as Mohamed Elneny, is an Egyptian professional footballer who plays as a midfielder for club Arsenal and the Egypt national team."
pos = nlp.pos_tag(sentence)
ner = nlp.ner(sentence)
for i in range(len(pos)):
    sent = '0\t' + ner[i][1] + '\t' + str(i) + '\tO\t' + pos[i][3] + '\t' + pos[i][0] + '\tO\tO\tO\n'
all_sentences.append(sent)

sentence = "Sokratis Papastathopoulos (, ; born 9 June 1988), commonly known by the singular name Sokratis, is a Greek professional footballer who plays as a centre back for club Arsenal and the Greece national team."
pos = nlp.pos_tag(sentence)
ner = nlp.ner(sentence)
for i in range(len(pos)):
    sent = '0\t' + ner[i][1] + '\t' + str(i) + '\tO\t' + pos[i][1] + '\t' + pos[i][0] + '\tO\tO\tO\n'
all_sentences.append(sent)

sentence = "Laurent Koscielny (; , ; born 10 September 1985) is a French professional footballer who plays as a centre back for club Arsenal, where he is club captain."
pos = nlp.pos_tag(sentence)
ner = nlp.ner(sentence)
for i in range(len(pos)):
    sent = '0\t' + ner[i][1] + '\t' + str(i) + '\tO\t' + pos[i][1] + '\t' + pos[i][0] + '\tO\tO\tO\n'
all_sentences.append(sent)

sentence = "Henrikh Mkhitaryan (, ; born 21 January 1989) is an Armenian professional footballer who plays for club Arsenal and captains the Armenian national team."
pos = nlp.pos_tag(sentence)
ner = nlp.ner(sentence)
for i in range(len(pos)):
    sent = '0\t' + ner[i][1] + '\t' + str(i) + '\tO\t' + pos[i][1] + '\t' + pos[i][0] + '\tO\tO\tO\n'
all_sentences.append(sent)

sentence = "Aaron James Ramsey (born 26 December 1990) is a Welsh professional footballer who plays as a midfielder for club Arsenal and the Wales national team."
pos = nlp.pos_tag(sentence)
ner = nlp.ner(sentence)
for i in range(len(pos)):
    sent = '0\t' + ner[i][1] + '\t' + str(i) + '\tO\t' + pos[i][2] + '\t' + pos[i][0] + '\tO\tO\tO\n'
all_sentences.append(sent)

sentence = "Alexandre Lacazette (; born 28 May 1991) is a French professional footballer who plays as a forward for club Arsenal and the France national team."
pos = nlp.pos_tag(sentence)
ner = nlp.ner(sentence)
for i in range(len(pos)):
    sent = '0\t' + ner[i][1] + '\t' + str(i) + '\tO\t' + pos[i][1] + '\t' + pos[i][0] + '\tO\tO\tO\n'
all_sentences.append(sent)

sentence = "Mesut Özil (, ; born 15 October 1988) is a German professional footballer who plays for club Arsenal. He is considered to be one of the best players in the world."
pos = nlp.pos_tag(sentence)
ner = nlp.ner(sentence)
for i in range(len(pos)):
    sent = '0\t' + ner[i][1] + '\t' + str(i) + '\tO\t' + pos[i][1] + '\t' + pos[i][0] + '\tO\tO\tO\n'
all_sentences.append(sent)

sentence = "Lucas Sebastián Torreira Di Pascua (; born 11 February 1996) is a Uruguayan professional footballer who plays as a midfielder for club Arsenal and the Uruguay national team."
pos = nlp.pos_tag(sentence)
ner = nlp.ner(sentence)
for i in range(len(pos)):
    sent = '0\t' + ner[i][1] + '\t' + str(i) + '\tO\t' + pos[i][4] + '\t' + pos[i][2] + '\tO\tO\tO\n'
all_sentences.append(sent)

sentence = "Stephan Lichtsteiner (; born 16 January 1984) is a Swiss professional footballer who plays for club Arsenal and captains the Switzerland national team."
pos = nlp.pos_tag(sentence)
ner = nlp.ner(sentence)
for i in range(len(pos)):
    sent = '0\t' + ner[i][1] + '\t' + str(i) + '\tO\t' + pos[i][1] + '\t' + pos[i][0] + '\tO\tO\tO\n'
all_sentences.append(sent)

sentence = "Alexander Chuka Iwobi ( ; born 3 May 1996) is a Nigerian professional footballer who plays as a forward for club Arsenal and the Nigeria national team."
pos = nlp.pos_tag(sentence)
ner = nlp.ner(sentence)
for i in range(len(pos)):
    sent = '0\t' + ner[i][1] + '\t' + str(i) + '\tO\t' + pos[i][2] + '\t' + pos[i][0] + '\tO\tO\tO\n'
all_sentences.append(sent)

sentence = "Ignacio \"Nacho\" Monreal Eraso (; born 26 February 1986) is a Spanish professional footballer who plays as a left back or centre back for club Arsenal and the Spain national team."
pos = nlp.pos_tag(sentence)
ner = nlp.ner(sentence)
for i in range(len(pos)):
    sent = '0\t' + ner[i][1] + '\t' + str(i) + '\tO\t' + pos[i][2] + '\t' + pos[i][1] + '\tO\tO\tO\n'
all_sentences.append(sent)

sentence = "Bernd Leno (born 4 March 1992) is a German professional footballer who plays as a goalkeeper for club Arsenal and the German national team."
pos = nlp.pos_tag(sentence)
ner = nlp.ner(sentence)
for i in range(len(pos)):
    sent = '0\t' + ner[i][1] + '\t' + str(i) + '\tO\t' + pos[i][1] + '\t' + pos[i][0] + '\tO\tO\tO\n'
all_sentences.append(sent)

sentence = "Shkodran Mustafi (; born 17 April 1992) is a German professional footballer who plays as a centre back for club Arsenal and the German national team."
pos = nlp.pos_tag(sentence)
ner = nlp.ner(sentence)
for i in range(len(pos)):
    sent = '0\t' + ner[i][1] + '\t' + str(i) + '\tO\t' + pos[i][1] + '\t' + pos[i][0] + '\tO\tO\tO\n'
all_sentences.append(sent)

def write2file():
    with open('stanford-corenlp-full-2018-10-05/training.corp', 'w') as f:
        for index in range(all_sentences):
                f.write(all_sentences[index])

def main():
    write2file(send2file)

if __name__== "__main__":
  main()



# pros = {'annotators': 'ner,relation', 'outputFormat': 'text'}
# print(nlp.annotate(sentence, properties=pros))

nlp.close() # Do not forget to close! The backend server will consume a lot memery.
