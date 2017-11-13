import webbrowser

'''A class Movie is created under the filename media'''


class Movie():
    '''this function creates the object of class Movie
    and also stores the needed arguments in object '''
    def __init__(self, title, storyline, poster_url, trailer):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_url
        self.trailer_youtube_url = trailer
    '''this function helps to open the trailer in the browser'''
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
