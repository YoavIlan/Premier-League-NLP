import os

os.chdir(os.getcwd() + '/Stanford_OpenIE_Python')
pwd = os.getcwd() + '/corpus'

for f in os.listdir(pwd):
    print('Processing', f+ '...')
    os.system('./process_large_corpus.sh corpus/' + f + ' relations/' +f)