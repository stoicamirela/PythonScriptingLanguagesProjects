#simple exercise with Lists

import random
my_list = []

input_number = int(input("give a number: "))
for i in range(input_number):
    random_no = random.random()
    my_list.append(random_no)
print(my_list)
