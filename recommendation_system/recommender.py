import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

print("Loading Movie Recommendation System...")

# Load dataset
data = pd.read_csv("movies.csv")

# Combine text features
data["features"] = data["Genre"] + " " + data["Description"]

# Convert text into numeric vectors
vectorizer = TfidfVectorizer(stop_words="english")
feature_matrix = vectorizer.fit_transform(data["features"])

# Compute similarity between movies
similarity = cosine_similarity(feature_matrix)

print("\nAvailable Movies:")
print(data["Movie"].to_string(index=False))

movie_name = input("\nEnter a movie you like: ")

# Find movie index
if movie_name not in data["Movie"].values:
    print("Movie not found in dataset")
else:
    index = data[data["Movie"] == movie_name].index[0]

    similarity_scores = list(enumerate(similarity[index]))

    # Sort movies by similarity
    sorted_movies = sorted(similarity_scores, key=lambda x: x[1], reverse=True)

    print("\nRecommended Movies:")

    for movie in sorted_movies[1:6]:
        print(data.iloc[movie[0]]["Movie"])