#we're reading a file text and we want to find the words that are bigger than n, for example here i ask user for a number and i show the words with the length bigger than the input_number

file = open('sampletxt.txt', 'r')
text = file.read()
words = text.split()  # words este lista

input_number = int(input("give a number from 0 to 10, integer: "))

for word in words:
    if len(word) > input_number:
        print(word)
file.close()