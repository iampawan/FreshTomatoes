import urllib


def read_file():
    myfile = open("/Users/pawankumar/Downloads/movie_quotes.txt")
    movie_file = myfile.read()
    print movie_file
    myfile.close()
    check_profanity(movie_file)

def check_profanity(text_to_search) :
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text_to_search)
    output = connection.read()
    print output
    connection.close()

read_file()
