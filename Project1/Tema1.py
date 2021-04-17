#s = "A", str(12*3)
#print(s)
my_string = "Alabama is here"

#vrem sa vedem daca incepe sau se sfarseste printr-un string
def startsOrEndsWith():
    if(my_string.startswith("...")):
        print("string begins with 3 dotted points")
    elif(my_string.endswith("...")):
        print("string ends with 3 dotted points")
    else:
        print("string doesn't contain 3 dotted points at the beginning or at the end")

#inlocuim cuvantul Alabama cu Bucharest, dar fiind salvata aceasta
#schimbare intr-o variabila, stringul original este inca pastrat
def replaceString():
    replaced_string = my_string.replace("Alabama","Bucharest")
    print("original string is replaced into",replaced_string)

#cateva metoda de prelucrare a stringului nostru orginal
def printingStringsInFormats():
    print("index of here",my_string.index("here"))
    print("rindex of is",my_string.rindex("is"))
    print("lowered string",my_string.lower())
    print("upper case string",my_string.upper())
    print("splitted string",my_string.split())
    print("stripped string of 'Ala' is", my_string.strip("Ala"))
    print("rstrip strips the string 'is here':", my_string.rstrip('is here'))
    print("lstrip strips the string 'Alabama':", my_string.lstrip('Alabama'))

#facem o formatare intr-un anumit mod a unui string
def formattingStrings():
    #first way
    txt1 = "My name is {fname}, I'm {age}".format(fname = "Stoica", age = 23)
    print(txt1)
    
    #second way
    txt2 = "My name is {0}, I'm {1}".format("Mirela", 23)
    print(txt2)
    
    #third way, shortest version of the second way
    txt3 = "My name is {}, I'm {}".format("Estera", 23)
    print(txt3)

    #lucrand cu numere de tip float
    pret = 78
    print("Pentru pretul de {:.2f} lei!".format(pret))

def checkingStrings():
    print("alpha or not?",my_string.isalpha())
    print(my_string.isupper())
    print(my_string.islower())
    print(my_string.find("Alabama"))
    print(my_string.count("is"))

print("original string is", my_string)
startsOrEndsWith()
print("\r") #printing a blank row between the results of the functions
replaceString()
print("\r")
printingStringsInFormats()
print("\r")
formattingStrings()
print("\r")
checkingStrings()