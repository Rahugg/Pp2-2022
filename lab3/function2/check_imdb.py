from list_movies import movies

def checkIMDB(movie):
    for m in movies:
        if(m["name"]==movie and m["imdb"]>5.5):
            print("True")


movie = input()

checkIMDB(movie)