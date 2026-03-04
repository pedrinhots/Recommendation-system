def analyze_data(data):
    # Perform statistical analysis on the dataset
    summary = data.describe()
    return summary

def get_top_n_movies(data, n=10):
    # Get the top N movies based on a specific metric, e.g., rating
    top_movies = data.nlargest(n, 'rating')  # Assuming 'rating' is a column in the dataset
    return top_movies

def get_genre_distribution(data):
    # Analyze the distribution of genres in the dataset
    genre_counts = data['genre'].value_counts()  # Assuming 'genre' is a column in the dataset
    return genre_counts

def analyze_trends_over_time(data):
    # Analyze trends over time, e.g., number of movies released per year
    trends = data['release_year'].value_counts().sort_index()  # Assuming 'release_year' is a column
    return trends