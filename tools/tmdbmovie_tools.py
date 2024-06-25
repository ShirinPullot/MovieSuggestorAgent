import requests
import os
class SearchTMDBMovies:
    def __init__(self, genre_name):
        """
        Initializes the SearchTMDBMovies object with the provided genre name.

        Parameters:
            genre_name (str): The name of the genre for movie search.

        Returns:
            None
        """
        self.genre_name = genre_name


    def get_movie_details_tool(self):
        """
        Retrieves the genre ID for a given genre name by making a request to the TMDB API.

        Returns:
            int or None: The genre ID if found, None otherwise.
        """
        genre_id = self.get_genre_id()
        if genre_id is None:
            print(f"No movie found for genre: {self.genre_name}")
            return None
        # Get the movie details using the movie ID
        movie_details = self.get_movie_details()
        return movie_details
    

    def get_genre_id(self):
        """
        Retrieves the genre ID for a given genre name by making a request to the TMDB API.

        Returns:
            int or None: The genre ID if found, None otherwise.
        """
        url = 'https://api.themoviedb.org/3/genre/movie/list'
        query = {
            "api_key": os.environ['TMDB_API_KEY'],
            "language": "en-US"
        }

        response = requests.get(url, params=query)
        print('response done')
        if response.status_code != 200:
            print(f"Failed to retrieve genres: {response.status_code}")
            return None

        data = response.json()
        genres = data.get('genres', [])

        for genre in genres:
            if genre['name'].lower() == self.genre_name.lower():
                return genre['id']

        return None
    
    def get_movie_details(self):
        """
        Retrieves the details of a movie.

        Returns:
            dict: A dictionary containing the following details of the movie:
                - title (str): The title of the movie.
                - overview (str): The overview of the movie.
                - cast (list): A list of the names of the top 5 cast members.

        Note:
            - This function makes two API requests to the TMDB (The Movie Database) API to retrieve the movie details.
        """
        genre_id = self.get_genre_id()    
        url = f"https://api.themoviedb.org/3/movie/{genre_id}"
        params = {
            "api_key": os.environ['TMDB_API_KEY'],
        }
        response = requests.get(url, params=params)
        data = response.json()

        # Basic details
        title = data['title']
        overview = data['overview']

        # cast
        cast = [member['name'] for member in data['credits']['cast'][:5]]  

        return {
            "title": title,
            "overview": overview,
            "cast": cast,
        }
   
        
  
    
