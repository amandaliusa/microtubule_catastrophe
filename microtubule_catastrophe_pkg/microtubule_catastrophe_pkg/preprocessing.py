import numpy as np
import pandas as pd

import bebi103 

def process_labeled_unlabeled(filename):
    '''Processes csv file with microtubule catastrophe times 
    for labeled and unlabeled tubulin and returns tidy dataframe'''
    
    df = pd.read_csv(filename)
    df = df.drop('Unnamed: 0', axis=1)
    df['labeled'] = df['labeled'].apply(lambda x: 'labeled' if x else 'unlabeled')
    
    return df

def extract_labeled(df):
    '''Extracts microtubule catastrophe times for labeled tubulin 
    from provided dataframe'''
    
    labeled = df.loc[df['labeled']=='labeled']['time to catastrophe (s)']
    return labeled

def extract_labeled(df):
    '''Extracts microtubule catastrophe times for unlabeled tubulin 
    from provided dataframe'''
    
    unlabeled = df.loc[df['labeled']=='unlabeled']['time to catastrophe (s)']
    return unlabeled