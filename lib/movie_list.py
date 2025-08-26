import requests
from tkinter import messagebox

# ---------------- API CALL ----------------
def fetch_movies():
    """ 
    Fetches the top 100 movies from the IMDb API. If the API call fails,
    
    Returns Json data from a response
    """
    url = "https://imdb-top-100-movies.p.rapidapi.com/"
    headers = {
        "x-rapidapi-key": "113e7daf94mshaf44b20b69465cbp12b3a0jsn7667250440aa",
        "x-rapidapi-host": "imdb-top-100-movies.p.rapidapi.com"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    
    except Exception as e:
        messagebox.showerror("API Error", f"Failed to fetch data:\n{e}")
        return []
