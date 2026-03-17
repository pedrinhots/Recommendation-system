import pandas as pd

# ==========================================================
# 1. LOAD DATA
# ==========================================================

df = pd.read_csv(r'C:\Users\pedro\OneDrive\Desktop\Reccomendation_System\movie-series-analysis\data\raw\raw_titles.csv')

cleaned_df = df.copy()

print("Dataset loaded")
print(cleaned_df.shape)


# ==========================================================
# 2. NULL VALUES TREATMENT
# ==========================================================

print("Null values per column:")
print(cleaned_df.isnull().sum())


# ==========================================================
# 3. DATA TYPE CORRECTION
# ==========================================================
print("Rodei aqui")
cleaned_df['type'] = cleaned_df['type'].astype('category')
cleaned_df['imdb_votes'] = cleaned_df['imdb_votes'].astype('Int64')
print("Rodei aqui 2")

# ==========================================================
# 4. TEXT STANDARDIZATION
# ==========================================================
print("Rodei aqui 3")
cleaned_df['title'] = cleaned_df['title'].str.strip()
print("Rodei aqui 4")

# ==========================================================
# 5. AGE STANDARDIZATION
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
print("Rodei aqui 5")
cleaned_df["age_certification_num"] = cleaned_df["age_certification"].map(age_map)
cleaned_df["age_certification_num"] = cleaned_df["age_certification_num"].fillna(0) ##Unkown age certifications are assigned a value of 0, indicating that they do not fit into any of the defined age categories. This allows us to retain these entries in the dataset while acknowledging that their age certification is unknown or not applicable.
#We will aply the following pipeline to the age_certification column:
#Kids mode → remove Unknown
#Normal mode → allow Unknown
print("Rodei aqui 6")


# ==========================================================
# 6. SEASON STANDARDIZATION
# ==========================================================

cleaned_df['seasons'] = cleaned_df['seasons'].fillna(0)
cleaned_df['seasons'] = cleaned_df['seasons'].astype('Int64')

# ==========================================================
# 7. CONSISTENCY CHECKS
# ==========================================================
print("Rodei aqui 7")
vote_threshold = cleaned_df['imdb_votes'].quantile(0.70)

cleaned_df = cleaned_df[cleaned_df['imdb_votes'] >= vote_threshold] # Filter out movies/series with votes below the 70th percentile
#This means excluding 70% of the entries with the lowest number of votes, which are likely to be less popular or have less reliable ratings.
print("Rodei aqui 8")
cleaned_df = cleaned_df[(cleaned_df['imdb_score'] >= 0) & (cleaned_df['imdb_score'] <= 10)]

# ==========================================================
# 8. WEIGHTED RATING
# ==========================================================



# ==========================================================
# 9. EXPORT CLEAN DATA
# ==========================================================
print("Rodei aqui 9")
cleaned_df.to_csv(
    'C:\\Users\\pedro\\OneDrive\\Desktop\\Reccomendation_System\\movie-series-analysis\\data\\processed\\clean_titles.csv',
    index=False
)

print(cleaned_df.head())
print(cleaned_df.shape)

print("Null values per column:")
print(cleaned_df.isnull().sum())

print("Fim do codigo")
