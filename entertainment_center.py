# Udacity IPND: Stage 3 Project by Laurens: Movies Website

# In this file, you can can define instances of the class Movie,
# defined in media.py.

# After you run this code, open the file fresh_tomatoes.html
# see your webpage!

# See the readme for more information.

import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "11/22/1995",
                        "John Lasseter",
                        "Tom Hanks, Tim Allen, Don Rickles",
                        "A story of a boy and his toys that come to life.",
                        "https://goo.gl/48rfto",
                        "https://youtu.be/KYz2wyBy3kc")

avatar = media.Movie("Avatar",
                     "12/18/2009",
                     "James Cameron",
                     "Sam Worthington, Zoe Saldana, Sigourney Weaver",
                     "A marine on an alien planet.",
                     "https://goo.gl/OPWubF",
                     "https://youtu.be/5PSNL1qE6VY")

shawshank_redemption = media.Movie("The Shawshank Redemption",
                                   "11/23/1994",
                                   "Frank Darabont",
                                   "Tim Robbins, Morgan Freeman, Bob Gunton",
                                   "A banker is sentenced to life for the "
                                   "murder of his wife and her lover.",
                                   "https://goo.gl/gbhhZn",
                                   "https://youtu.be/6hB3S9bIaco")

lotr_fotr = media.Movie("The Lord of the Rings: The Fellowship of the Ring",
                        "12/19/2001",
                        "Peter Jackson",
                        "Elijah Wood, Ian McKellen, Liv Tyler",
                        "The Fellowship of the Ring begins its journey to "
                        "Mount Doom.",
                        "https://goo.gl/rbzj5T",
                        "https://youtu.be/V75dMMIW2B4")

lotr_rk = media.Movie("The Lord of the Rings: The Return of the King",
                      "12/17/2003",
                      "Peter Jackson",
                      "Elijah Wood, Ian McKellen, Liv Tyler",
                      "The story's epic conclusion.",
                      "https://goo.gl/nq9obR",
                      "https://youtu.be/r5X-hFf6Bwo")

modern_times = media.Movie("Modern Times",
                           "02/05/1936",
                           "Charlie Chaplin",
                           "Charlie Chaplin, Paulette Goddard, Henry Bergman",
                           "Charlie Chaplin as a factory worker.",
                           "https://goo.gl/HPgvpz",
                           "https://youtu.be/D2AEcUc8tOA")

# create list of movies and pass it to the open_movies_page function
movies = [toy_story, avatar, shawshank_redemption, lotr_fotr, lotr_rk,
          modern_times]

# This function call uses rge list of movie instances as input to generate an 
# HTML file and open it in the browser.
fresh_tomatoes.open_movies_page(movies)
