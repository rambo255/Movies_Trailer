import fresh_tomatoes
import media

'''Here we are creating different instance
   of class Movie with filename media'''


toilet = media.Movie("Toilet",
                     "A movie about sanitation problems in india",
                     "https://upload.wikimedia.org/wikipedia/en/thumb/1/12/"
                     "Toilet_Ek_Prem_Katha.jpg/220px-Toilet_Ek_Prem_Katha.jpg",
                     "https://www.youtube.com/watch?v=ym4EJQ7XORk")

judwaa2 = media.Movie("Judwaa2",
                      "A comedy about twin brothers",
                      "https://upload.wikimedia.org/wikipedia/en/thumb/9/91"
                      "/Judwaa_2_Poster.jpg/220px-Judwaa_2_Poster.jpg",
                      "https://www.youtube.com/watch?v=DDwbjWCgxVM")

baahubali2 = media.Movie("Baahubali2",
                         "A humongous fight for the throne ",
                         "https://upload.wikimedia.org/wikipedia/en/"
                         "thumb/f/f9/Baahubali_the_Conclusion.jpg/"
                         "220px-Baahubali_the_Conclusion.jpg",
                         "https://www.youtube.com/watch?v=G62HrubdD6o")

tiger = media.Movie("Tiger Zinda Hai",
                    "A raw agent saving lives of"
                    " nurses in Iraq",
                    "https://upload.wikimedia.org/wikipedia/commons/thumb"
                    "/3/33/Tiger_Zinda_Hai_Official_Film_Poster.jpg/"
                    "220px-Tiger_Zinda_Hai_Official_Film_Poster.jpg",
                    "https://www.youtube.com/watch?v=ePO5M5DE01I")

golmaal = media.Movie("Golmaal Again",
                      "A group of 4 friends with lots of madness",
                      "https://upload.wikimedia.org/wikipedia/en/thumb/4/49/"
                      "Ajay_Devgn%27s_Golmaal_Again_poster.jpg/"
                      "220px-Ajay_Devgn%27s_Golmaal_Again_poster.jpg",
                      "https://www.youtube.com/watch?v=VgQUwsUHdqc")

padmavati = media.Movie("Padmavati",
                        "A movie based on rajput queen",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/4/47/"
                        "Padmavati_Poster.jpg/220px-Padmavati_Poster.jpg",
                        "https://www.youtube.com/watch?v=X_5_BLt76c0")

'''A list named movies is created
   which stores these instances'''

movies = [toilet, judwaa2, baahubali2, tiger, golmaal, padmavati]

''''the list is paased in the open_movies_page()
    of file fresh_tomatoes'''

fresh_tomatoes.open_movies_page(movies)
