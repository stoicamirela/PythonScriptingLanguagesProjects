#same game as in Project1, but using while this time

import random

number = random.randint(0,10)
print(number)
your_number = int(input("Give a number:"))
i = 0
while your_number != number and i<2:
    if(your_number < number):
        print("Too small, try again")
        old_number = your_number
        your_number = int(input("Give again a number:"))
        if(your_number > old_number):
            pass
        else:
            print("number still small")
            # your_number = int(input("Give again a number:"))
       
    else:
        print("Too big, try again")
        old_number = your_number
        your_number = int(input("Give again a number:"))
        if(your_number < old_number):
            pass
        else:
            print("number still big")
            # your_number = int(input("Give again a number:"))
    i += 1
    print(i)
if(your_number == number):
    print("YOU WON THE GAME")
else:
    print("GAME OVER")