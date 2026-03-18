import pandas as pd

def exportCleanData(df, path):
    if df is not None:
        if path is not None:
            df.to_csv(
                path,
                index=False
            )

def checkNullValues(df):
    if df is not None:
        print("Null values per column:")
        print((df.isnull().sum() / len(df)) * 100)

def loadData(path):
    if path is not None:
        df = pd.read_csv(path)
        print("Dataset loaded")
        print(df.shape)
        return df
    else:
        print("Path is None. Cannot load data.")
        return None

def copyData(df):
    if df is not None:
        return df.copy()
    else:
        print("DataFrame is None. Cannot copy data.")
        return None
    
# ==========================================================
# 1. LOAD DATA
# ==========================================================

df = loadData(r'C:\Users\pedro\OneDrive\Desktop\Reccomendation_System\movie-series-analysis\data\raw\raw_titles.csv')

cleaned_df = copyData(df)

# ==========================================================
# 2. DATA TYPE CORRECTION
# ==========================================================

cleaned_df['type'] = cleaned_df['type'].astype('category')
cleaned_df['imdb_votes'] = cleaned_df['imdb_votes'].astype('Int64')

# ==========================================================
# 3. TEXT STANDARDIZATION
# ==========================================================

cleaned_df['title'] = cleaned_df['title'].str.strip()

# ==========================================================
# 4. AGE STANDARDIZATION
# ==========================================================

age_map = {
    "G": 1,
    "TV-Y": 1,
    "TV-G": 1,

    "TV-Y7": 2,
    "PG": 2,

    "TV-PG": 3,
    "PG-13": 3,

    "TV-14": 4,

    "R": 5,
    "TV-MA": 5,

    "NC-17": 6
}

cleaned_df["age_certification_num"] = cleaned_df["age_certification"].map(age_map)
cleaned_df["age_certification_num"] = cleaned_df["age_certification_num"].fillna(0) ##Unkown age certifications are assigned a value of 0, indicating that they do not fit into any of the defined age categories. This allows us to retain these entries in the dataset while acknowledging that their age certification is unknown or not applicable.
#We will aply the following pipeline to the age_certification column:
#Kids mode → remove Unknown
#Normal mode → allow Unknown

# ==========================================================
# 5. SEASON STANDARDIZATION
# ==========================================================

cleaned_df['seasons'] = cleaned_df['seasons'].fillna(0)
cleaned_df['seasons'] = cleaned_df['seasons'].astype('Int64')

# ==========================================================
# 6. CONSISTENCY CHECKS
# ==========================================================

vote_threshold = cleaned_df['imdb_votes'].quantile(0.70)

cleaned_df = cleaned_df[cleaned_df['imdb_votes'] >= vote_threshold] # Filter out movies/series with votes below the 70th percentile
#This means excluding 70% of the entries with the lowest number of votes, which are likely to be less popular or have less reliable ratings.

cleaned_df = cleaned_df[(cleaned_df['imdb_score'] >= 0) & (cleaned_df['imdb_score'] <= 10)]

# ====================================================================================================================
# 7. WEIGHTED RATING
# ====================================================================================================================

nulls = cleaned_df[['imdb_votes', 'imdb_score']].isna().sum()

if nulls.sum() > 0:
    print("Warning: There are null values in 'imdb_votes' or 'imdb_score'. Weighted rating cannot be calculated for these entries.")
else: 
    print("No null values in 'imdb_votes' or 'imdb_score'. Proceeding with weighted rating calculation.")
    #Média Global do score:
    C = cleaned_df['imdb_score'].mean()
    #Minimo de votos:
    m = cleaned_df['imdb_votes'].min()
    #Criando o Weighted Rating:
    cleaned_df['weighted_rating'] = (
        (cleaned_df['imdb_votes'] / (cleaned_df['imdb_votes'] + m)) 
        * cleaned_df['imdb_score'] + (m / (cleaned_df['imdb_votes'] + m) * C)
    )
    cleaned_df['weighted_rating'] = cleaned_df['weighted_rating'].round(3)
    #Verificando se a coluna criada faz sentido:
    print(cleaned_df[['title', 'imdb_score', 'imdb_votes', 'weighted_rating']].head(10))
    print(cleaned_df.sort_values('weighted_rating', ascending=False).head(10))
    
    #PERCEBA QUE WEIGHTED RATING NUNCA MAIOR QUE IMDB SCORE, POIS O PESO DO IMDB SCORE É MAIOR QUE O PESO DA MEDIA GLOBAL, ENTÃO O WEIGHTED RATING VAI SER SEMPRE INFERIOR
    #poucos votos, WR se aproxima da média global, muitos votos, WR se aproxima do imdb_score.
    #O score final deve seguir uma lógica mais ou menos assim: final_score = similarity * weighted_rating
    #O similarity será calculado indivudlamente para cada usuário, e o weighted_rating é um score geral de qualidade do filme/serie, que leva em consideração tanto a nota média quanto a quantidade de votos, para evitar que filmes com poucas avaliações tenham uma nota muito alta apenas por causa de algumas avaliações positivas. 
# ====================================================================================================================
# 8. EXPORT CLEAN DATA
# ====================================================================================================================

#checkNullValues(cleaned_df)
exportCleanData(cleaned_df, r'C:\Users\pedro\OneDrive\Desktop\Reccomendation_System\movie-series-analysis\data\processed\cleaned_titles.csv')

print("Fim do codigo")
