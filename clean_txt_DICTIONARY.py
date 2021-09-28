import os
import io
import pandas as pd

#stabilisce il path locale in cui sit rova il file
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def clean(file_txt, freq = False):
    
    file = io.open(file_txt, mode="r", encoding="utf-8")  #apre il file
    lines = file.read().splitlines()    # separa righe del file

    lista = []
    for l in lines:   
        tokens = l.split()
        lista.append(tokens)   #mette elementi di goni riga in liste
    
    return list(lista)

    #PROBLEM: numero non va bene come key univoca
    #freq_dict = dict(lista) 
    #return freq_dict

    file.close()

#print(len(clean("German.txt", freq = True)))
freq_lang = clean("German_freq.txt", freq = True)
#if freq_lang == None:
#print('hi')


#print(type(freq_lang))

def transcriptions(file_text):

    transcr =  pd.read_csv(file_text, sep=' ', header=None , engine='python', index_col=False)

    # Splitta il file in colonne solo una volta, quindi la trascrizione risulta come seconda colonna 
    clean_transcr = transcr[1] #metto in variabile tutte le trascrizioni
    lista = [el for el in clean_transcr] #creo una lista
    print(lista)   ####NON FUNZIONA PIU
    

var = transcriptions("provaa_lex.txt")


for el in freq_lang:
    #print(el[1])
    if el[1] in var:
        print('ok')
    else:
        pass






    