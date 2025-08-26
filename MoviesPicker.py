
import tkinter as tk
from tkinter import ttk
from lib.movie_list import fetch_movies
from lib.SaveData import save_all_movies_to_csv


# ---------------- FILTER FUNCTION ----------------
def filter_movies():
    """ Filters the movies based on user input from the GUI.
    Filters by name, genre, and minimum rating.
    If no filters are applied, it shows all movies.    
    """
    name_filter = name_entry.get().lower()
    genre_filter = genre_entry.get().lower()
    try:
        rating_filter = float(rating_entry.get())
    except ValueError:
        rating_filter = 0.0

    filtered = []
    for movie in movies:
        
        name_match = not name_filter or name_filter.strip().lower() == movie['title'].lower()
        
        if genre_filter:
            if isinstance(movie.get('genre'), list):                
                genre_str = [g.lower() for g in movie.get('genre', [])]
                genre_match = genre_filter.lower() in genre_str
            
            if isinstance(movie.get('genre'), str):
                genre_strs = [g.strip().lower() for g in movie.get('genre', "").split(",")]
                genre_match = genre_filter.lower() in genre_strs
                
        else:
            genre_match = True
            
        rating_match = float(movie['rating']) >= rating_filter
        
        if name_match and genre_match and rating_match:
            filtered.append(movie)

    display_movies(filtered)

# ---------------- DISPLAY FUNCTION ----------------
def display_movies(movie_list):
    """
    display_movies function to populate the GUI table with movie data.
    This function clears the existing rows in the table and inserts new rows
    based on the provided movie_list. Each movie is represented by its title,
    genre, and rating.
    """
    for row in tree.get_children():
        tree.delete(row)

    for movie in movie_list:
        tree.insert("", "end", values=(movie['title'], movie['genre'], movie['rating']))

# ---------------- GUI SETUP ----------------
movies = fetch_movies()

# saving data to csv once fetched using pandas
save_all_movies_to_csv(movies)

root = tk.Tk()
root.title("IMDb Top 100 Movies")
root.geometry("800x500")

# Filters
filter_frame = tk.Frame(root)
filter_frame.pack(pady=10)

tk.Label(filter_frame, text="Name:").grid(row=0, column=0, padx=5)
name_entry = tk.Entry(filter_frame, width=20)
name_entry.grid(row=0, column=1, padx=5)

tk.Label(filter_frame, text="Genre:").grid(row=0, column=2, padx=5)
genre_entry = tk.Entry(filter_frame, width=20)
genre_entry.grid(row=0, column=3, padx=5)

tk.Label(filter_frame, text="Min Rating:").grid(row=0, column=4, padx=5)
rating_entry = tk.Entry(filter_frame, width=5)
rating_entry.grid(row=0, column=5, padx=5)

filter_button = tk.Button(filter_frame, text="Apply Filters", command=filter_movies)
filter_button.grid(row=0, column=6, padx=10)

# Table
columns = ("Title", "Genre", "Rating")
tree = ttk.Treeview(root, columns=columns, show='headings', height=20)
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=200 if col != "Rating" else 100)

tree.pack(fill="both", expand=True)

# Populate with all movies initially
display_movies(movies)

root.mainloop()
