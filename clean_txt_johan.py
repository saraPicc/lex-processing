# Import dependencies
import os
import io
import pandas as pd

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
    print(df_transcr.head())
    return df_transcr


# Load as a pandas dataframe and clean frequency file
freq_lang = clean(".\data\German_freq.txt")
cleaned_transc = transcriptions(".\data\German_clph.txt")

# Join datasets
joined_df = cleaned_transc.join(freq_lang.set_index('word'), on='word', how='left')
# Remove when no frequency exist
joined_df = joined_df.dropna()
# Sort
joined_df=joined_df.sort_values(by=['freq'],ascending=False)

# Print transcriptions as a list
print(joined_df['transcription'].tolist())
# Get all word with freq greater than X
#high_freq_df  = joined_df[joined_df['freq']<=30]