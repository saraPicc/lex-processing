# Import dependencies
import os
import io
import pandas as pd
import Levenshtein as lv
import numpy as np
import sys
import getopt 

#stabilisce il path locale in cui sit rova il file
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Create functions to clean and load transcriptions
def clean(file_txt):
    # load dataframe and ignoring initial spaces
    df_file =  pd.read_csv(file_txt, sep=' ', skipinitialspace=True, header=None , engine='python', index_col=False)
    df_file = df_file.dropna(axis = 1, how = 'all')
    # Rename columns
    df_file = df_file.rename(columns={0:'freq', 1:'word'})
    #print(df_file.head())
    return df_file

def transcriptions(file_text):
    # load dataframe and ignoring initial spaces
    df_transcr =  pd.read_csv(file_text, sep='|', header=None , engine='python', index_col=False)
    # Split only on first space
    aux0 = df_transcr[0].str.split(' ',1, expand = True)
    # Store back to df
    df_transcr[0] = aux0[0]   
    df_transcr[1] = aux0[1] 
    # Remove single quotes
    df_transcr[0] = df_transcr[0].str.replace("'", '', regex=False)
    # Rename columns
    df_transcr = df_transcr.rename(columns={0:'word', 1:'transcription'})
    #print(df_transcr.head())
    return df_transcr

#####farlo per tutte le lingue e append to one dF

############################################

# chunk to run the script on linux - to be finished

# Get all arguments
#argv = sys.argv[1:]
# Access by flag
#opts, args = getopt.getopt(argv, 'f:')
# Filename
#filename = opts[0]

###############################################

# Load as a pandas dataframe and clean frequency file
freq_lang = clean(".\data\Spanish_freq.txt")
cleaned_transc = transcriptions(".\data\Spanish_db_vow_appr.txt")

# Join datasets
joined_df = cleaned_transc.join(freq_lang.set_index('word'), on='word', how='left')
# Remove when no frequency exist
joined_df = joined_df.dropna()
# Sort
joined_df=joined_df.sort_values(by=['freq'], ascending=False)

print(joined_df)

# Print transcriptions as a list
transcr_list = joined_df['transcription'].tolist()

#prints number of elements in the list 
#print(len(transcr_list))


#calculates LV

def LV(lista):
    l_lv_dis = [lv.distance(lista[i], lista[j]) for i in range(len(lista)) for j in range(i + 1, len(lista)) ]
    val = np.average(l_lv_dis)
    return val
    

print(LV(transcr_list))

############

#print(our_calc(filename[1], filename[2]))

############