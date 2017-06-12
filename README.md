# Movie Webpage Generator Tool

### About this project
This project dynamically generates a simple movie webpage from a Python script.
The generated html pages contains the following content for each movie:
  - Movie title
  - Release date, director, cast
  - Short storyline summary
  - Poster art
  - Youtube trailer (when clicked)

### How to run
Before starting make sure the unzipped contents of *movie_site.zip* are still in the same folder.
Run the file *entertainment_center.py* through your console or IDE to generate the HTML webpage.
The page should open in your default browser and will be located in the parent folder under the name **movie_webpage_project.html**.
Clicking on the poster art of a movie will start playback of the trailer.


### Files

The project consists of the following files:

* *media.py*: Python file containing the class definition for the movie class
* *fresh_tomatoes.py*: Python script used to generate the webpage using the bootstrap framework
* *entertainment_center.py*: Python script that initiates movie objects and combines them into a list which it finally uses to generate the webpage through a function *open_movies_page* in *fresh_tomatoes.py*


### Customization
To customize the project you can add movies in *entertainment_center.py*, add movie attributes in *media.py* and change the contents and style of the generated webpage in *fresh_tomatoes.py*. Basic knowledge of Python and/or HTML/CSS required.
