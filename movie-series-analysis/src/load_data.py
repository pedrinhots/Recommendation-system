import pandas as pd
from sklearn.preprocessing import MultiLabelBinarizer

csv_path = 'C:/Users/pedro/OneDrive/Desktop/Getting Started/movie-series-analysis/data/raw/raw_titles.csv'
dataframe = pd.read_csv(csv_path)

'''
encoded_genres = pd.get_dummies(dataframe['genres'], 'genre')

dataframe = pd.concat([dataframe, encoded_genres], axis = 1)

print(dataframe)
''' #This will not work because each movie has more than one genre.

#The genres already are inside lists.

#MultiLabelBinarizer to encode genres:

mlb = MultiLabelBinarizer()

encoded_genres = pd.DataFrame(mlb.fit_transform(dataframe['genres']), 
                                  columns=mlb.classes_,
                                  index=dataframe.index)

#Combining with the original dataframe:

dataframe = pd.concat([dataframe, encoded_genres], axis=1)

print(dataframe)