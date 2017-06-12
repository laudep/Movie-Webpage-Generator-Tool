# Movie Website Project: class definitions

import webbrowser

class Movie():
    
    """This class provides a way to store movie related information."""
    
    def __init__(self, movie_title, movie_release_date, movie_director,
                 movie_cast, movie_storyline, poster_image, trailer_youtube):
        """Initialises the instance variables for the Movie class.
        Args:
        movie_title:        string containing movie title
        movie_release_date: string containing movie release date
        movie_director:     string containing name of movie director(s)
        movie_cast:         string containing names of cast members
        movie_storyline:    string containing short story synopsis
        poster_image:       string containing URL to a poster image
        trailer_youtube:    string containing Youtube URL of the trailer
        """
        self.title = movie_title
        self.release_date = movie_release_date
        self.director = movie_director
        self.cast = movie_cast
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        
    def show_trailer(self):
        """Plays the trailer in the web browser."""
        webbrowser.open(self.trailer_youtube_url)
