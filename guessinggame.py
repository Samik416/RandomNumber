import random
chances = int(4)
rand = random.randint(0, 30)
number = int(input("Enter a number: "))
while(chances > 0):
    if(number < rand):
        number = int(input("Your number is too small , Guess again: "))
        chances = chances - 1
    elif(number > rand):
        number = int(input("Your number is too big, Guess again: "))
        chances = chances - 1
    elif(number == rand):
        print("You win!!!")
        chances = -1

if(chances == 0):
    print("You lose")
    
    