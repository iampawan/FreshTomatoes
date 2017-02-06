import fresh_tomatoes
import media

badri = media.Movie("Badrinath Ki Dulhania","Badrinath Ki Dulhania is an upcoming Indian romantic comedy film",
                    "https://upload.wikimedia.org/wikipedia/en/8/88/Badrinath_ki_Dulhania.jpg","https://www.youtube.com/watch?v=ztX-iGlZ_Ug")

print badri.storyline

movies = [badri]

fresh_tomatoes.open_movies_page(movies)