#simple exercise with dictionary: we have a dictionary with phone numbers and names, and we show first the names and ask user
#what number phone he wants, based on that we show the value of the key name. Bonus things are changing k to value as shown in
#inverted_dict variable. I also sorted the dictionary in a for
#Last task was to count frequencies

my_dictionary = {
    "Robinson": "0756 366 897",
    "Mirela": "0756 322 469",
    "Tom": "932328",
    "Jerry": "7394372",
    "Chloe": "8970798"
}

print(my_dictionary.keys())

name_input = input("name? ")
name = my_dictionary.get(name_input)
print("Number is:", name)
print("\r")

print("Sorted dictionary: ")
for key in sorted(my_dictionary):
    print("%s: %s" % (key, my_dictionary[key]))

print("\r")

inverted_dict = {v: k for k, v in my_dictionary.items()}
print("Inverted dict:", inverted_dict)

print("\r")

file = open('sample.txt', 'r')
text = file.read()
words = text.split()

frequencies = []
for word in words:
    frequencies.append(words.count(word))
print("Frecventele cuvintelor:", dict(list(zip(words, frequencies))))

file.close()
