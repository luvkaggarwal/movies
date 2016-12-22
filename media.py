import webbrowser

class Movie():

    #Adding documentation to any class
    """This class stores the details of a movie and accesses its trailer"""
    
    VALID_RATINGS = ["G","PG","PG-13","R"]
    
    def __init__(self, movie_title, movie_storyline, poster_image, youtube_trailer_url):
        self.title = movie_title
        self.storyline = movie_storyline
        self.image = poster_image
        self.trailer = youtube_trailer_url

    def showTrailer(self):
        webbrowser.open(self.trailer)
