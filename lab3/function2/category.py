from list_movies import movies

def find_category(category):
    for m in movies:
        if(m["category"]==category):
            print(m["name"])

category = input()
find_category(category)
