from list_movies import movies

def imdb():
    sublist=[]
    for m in movies:
        if(m["imdb"]>5.5):
            sublist.append(m["name"])
    print(sublist)

imdb()