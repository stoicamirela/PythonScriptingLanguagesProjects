#Simple game where the uses guesses the number and we give clues. The user has 3 guesses.

number = 15
def checkNumber():
    your_number = int(input("give number: "))
    if(your_number == number):
        print("true")
    elif(your_number > number):
        print("smaller, do it again")
        your_guess = int(input("give number again: "))
        if(your_guess < your_number):
            print("good, now we have a smaller number")
            if(your_guess == number):
                print("yes, ai ghicit numarul")
            elif(your_guess > number):
                print("nu, inca e mare numarul tau, one more time")
                another_guess = int(input("last try: "))
                if(another_guess == number):
                    print("yes, correct")
                else:
                    print("numarul a fost 15. GAME OVER")
    else:
        print("greater, do it again")
        your_guess = int(input("give number again: "))
        if(your_guess > your_number):
            print("good, now we have a greater number")
            if(your_guess == number):
                print("yes, ai ghicit numarul")
            elif(your_guess < number):
                print("nu, inca e mic numarul tau, one more time")
                another_guess = int(input("last try: "))
                if(another_guess == number):
                    print("yes, correct")
                else:
                    print("numarul a fost 15. GAME OVER")
        

checkNumber()