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

cleaned_df['type'] = cleaned_df['type'].astype('category')
cleaned_df['imdb_votes'] = cleaned_df['imdb_votes'].astype('Int64')


# ==========================================================
# 4. TEXT STANDARDIZATION
# ==========================================================

cleaned_df['title'] = cleaned_df['title'].str.strip()


# ==========================================================
# 5. CONSISTENCY CHECKS
# ==========================================================

cleaned_df = cleaned_df[(cleaned_df['imdb_score'] >= 0) & (cleaned_df['imdb_score'] <= 10)]


# ==========================================================
# 6. EXPORT CLEAN DATA
# ==========================================================

cleaned_df.to_csv(
    r'C:\Users\pedro\OneDrive\Desktop\Reccomendation_System\movie-series-analysis\data\processed\clean_titles.csv',
    index=False
)

print("Clean dataset exported")