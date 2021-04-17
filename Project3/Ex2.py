#Task: get a sentence, display it in reverse and bonus is to display it with "-" between the str characters

input_string = input("Give a sentence: ")
reversed_str = input_string[::-1]
print(reversed_str)
for i in reversed_str:
    print(i, end="-")
    reversed_str.replace(" ", "-")
