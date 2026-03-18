# Movie and Series Recommendation System

This project focuses on building a recommendation system for movies and series. The system leverages data analysis, feature engineering, and similarity models to provide personalized recommendations.

## Project Structure

```
movie-series-analysis
├── data
│   ├── raw
│   │   ├── best_movie_by_year_netflix.csv
│   │   └── raw_titles.csv
│   ├── processed
│       └── cleaned_titles.csv
├── notebooks
│   └── 01_data_understanding.ipynb
├── src
│   ├── data
│   │   ├── __init__.py
│   │   └── data_cleaning.py
│   ├── features
│   │   ├── __init__.py
│   │   └── genre_vectorizer.py
│   ├── models
│   │   ├── __init__.py
│   │   └── similarity.py
│   ├── recommender
│       ├── __init__.py
│       └── recommend.py
├── requirements.txt
├── .gitignore
└── README.md
```

### Data

- **data/raw/best_movie_by_year_netflix.csv**: Contains information about the best movies by year on Netflix.
- **data/raw/raw_titles.csv**: Raw dataset of movie and series titles with various attributes.
- **data/processed/cleaned_titles.csv**: Processed dataset after data cleaning and transformation.

### Notebooks

- **notebooks/01_data_understanding.ipynb**: A Jupyter notebook for understanding the dataset, including exploratory data analysis and visualization.

### Source Code

- **src/data/data_cleaning.py**: Functions for cleaning and preprocessing the raw data.
- **src/features/genre_vectorizer.py**: Code for feature engineering, including vectorization of genres.
- **src/models/similarity.py**: Implementation of similarity models for recommendations.
- **src/recommender/recommend.py**: Main logic for generating movie and series recommendations.

### Requirements

- **requirements.txt**: Lists the dependencies required for the project, including libraries such as pandas, numpy, scikit-learn, and Jupyter.

### Git

- **.gitignore**: Specifies files and directories to be ignored by Git, such as data files and virtual environment folders.
