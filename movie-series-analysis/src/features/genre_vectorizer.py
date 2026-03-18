import pandas as pd
from src.data.data_cleaning import loadData, copyData,  checkNullValues

df = loadData(r'C:\Users\pedro\OneDrive\Desktop\Reccomendation_System\movie-series-analysis\data\processed\cleaned_titles.csv')

print(df.head(10))