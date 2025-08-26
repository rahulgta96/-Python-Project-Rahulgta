import pandas as pd

    # Flatten lists in dictionaries
def save_all_movies_to_csv(movies):
    """Saves all movies to a CSV file.
    Args:
        movies (json data like dict): save the movies data to csv file
    """
    
    for movie in movies:
        for key, value in movie.items():
            if isinstance(value, list):
                movie[key] = ", ".join(map(str, value))

    # Convert to DataFrame
    df = pd.DataFrame(movies)

    # Export to CSV
    df.to_csv("movies.csv", index=False)