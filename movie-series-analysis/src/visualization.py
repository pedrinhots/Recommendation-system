import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def plot_rating_distribution(data):
    plt.figure(figsize=(10, 6))
    sns.histplot(data['rating'], bins=20, kde=True)
    plt.title('Rating Distribution')
    plt.xlabel('Rating')
    plt.ylabel('Frequency')
    plt.show()

def plot_genre_distribution(data):
    genre_counts = data['genre'].value_counts()
    plt.figure(figsize=(12, 6))
    sns.barplot(x=genre_counts.index, y=genre_counts.values)
    plt.title('Genre Distribution')
    plt.xlabel('Genre')
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    plt.show()

def plot_top_n_movies(data, n=10):
    top_movies = data.nlargest(n, 'rating')
    plt.figure(figsize=(12, 6))
    sns.barplot(x='rating', y='title', data=top_movies)
    plt.title(f'Top {n} Movies by Rating')
    plt.xlabel('Rating')
    plt.ylabel('Movie Title')
    plt.show()