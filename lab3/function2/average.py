from list_movies import movies

def average_imdb(movie):
    imdbs,ans = [],0
    for i in range(len(movie)):
        for m in movies:
            if(m["name"]==movie[i]):
                imdbs.append(m["imdb"])#appending the imdb score of given element
    for i in range(len(imdbs)):
            ans += imdbs[i]#calculating the sum of given movies' imdb
    print(ans/len(imdbs))#printing the avg imdb

n,movie = int(input()),[]
for i in range(n):
    att = input()
    movie.append(att)#creating a list of movies
average_imdb(movie)
