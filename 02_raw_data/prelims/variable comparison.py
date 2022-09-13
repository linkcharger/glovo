#%%
import glob
from os import read
from numpy import ndarray
import pandas as pd
import numpy as np
from pprint import pprint

dataPath = 'raw'



#%%
fileColumns = {}
missedFiles = []

for file in glob.glob(f'{dataPath}/*.csv', recursive=False):
    
    name = file[file.find('\\')+2:-4]
    print(f'doing file {name}')

    try:
        df = pd.read_csv(
            file, 
            nrows=10,
            )

        fileColumns[name] = list(df.columns)

    except UnicodeDecodeError:
        missedFiles.append(name)
        pass


print(f'missed files: {missedFiles}')
# pprint(columns)


#%%
locations = {}
count = -1
reorganisedAll = {}


for file, cols in fileColumns.items():
    reorganisedOne = [None] * 60

    for element in cols:
        if element not in locations.keys():
            count += 1
            locations[element] = count

        reorganisedOne[locations[element]] = element


    reorganisedAll[file] = reorganisedOne


# pprint(reorganisedAll)




comparisonDF = pd.DataFrame(reorganisedAll)

comparisonDF


#%%
comparisonDF.to_excel('variable comparison.xlsx')

