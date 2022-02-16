from allfunctions import *

request = input("What do you wanna solve?\n").lower()

#TO SOLVE: How many rabbits and how many chickens do we have?
if(request == "chicken rabbit"):
    numlegs,numheads = list(map(int,input("\n").split()))

    solve(numheads=numheads,numlegs=numheads)
#"Guess the number" - game, where the number to be guessed is randomly chosen between 1 and 20.
elif(request == "guess the number"):
    name = input("\nHello! What is your name?\n")
    print(f'\nWell, {name}, I am thinking of a number between 1 and 20.')

    Guess_the_number(name,0,random.randint(1,20))
#that takes a list of integers and prints a histogram to the screen
elif(request == "histogram"):
    numbers=list(map(int,input("\n").split()))

    histogram(numbers,[])
#True if the array contains a 3 next to a 3 somewhere.
elif(request == "has33"):
    numbers = list(map(int,input("\n").split()))

    has_33(numbers,len(numbers),[])
#checks whether a word or phrase is palindrome or not
elif(request == "palindrome"):
    str = input("\n")

    palindrome(str,len(str)-1,"")   
#accepts string from user and print all permutations of that string
elif(request == "permute"):
    string = input("\n")
    a = list(string)

    permute(a, "")
#which will take list of numbers as an agrument and returns only prime numbers from the list
elif(request == "prime number"):
    num__list = list(map(int,input("\n").split()))

    print(*filter__prime(num__list))
#that accepts string from user, return a sentence with the words reversed.
elif(request == "reverse string"):
    str = list(input("\n").split())

    reverse_string(str,len(str)-1,[])
# takes in a list of integers and returns True if it contains 007 in order
elif(request == "spygame"):
    nums = list(map(int,input("\n").split()))

    spygame(nums,[],"007")
# takes a list and returns a new list with unique elements of the first list
elif(request == "unique numbers"):
    numbers=list(map(int,input("\n").split()))

    unique(numbers,[])
#computes the volume of a sphere given its radius
elif(request == "volume of sphere"):
    radius= int(input("\n"))

    volume(radius)

else: print(f'\nOops,there is no such {request} ')
