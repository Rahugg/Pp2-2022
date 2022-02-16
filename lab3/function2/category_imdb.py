from list_movies import movies

def average_imdb(movie):
    imdbs,ans = [],0
    for m in movies:
            if(m["category"]==movie):
                imdbs.append(m["imdb"])#appending the imdb score of given element
    for i in range(len(imdbs)):
            ans += imdbs[i]#calculating the sum of given movies' imdb
    print(ans/len(imdbs))#printing the avg imdb

category = input()
average_imdb(category)
