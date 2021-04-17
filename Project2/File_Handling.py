import re
file = open('text1.txt','r')
text = file.read()
print(type(text))

m = re.match(r"(\w+)", text)  # this one searches from the first position only
print(m)

#aici am incercat intr-un regex online sa fac singura formatele
#date1 = (\d+)([ ])([A-Za-z]+)([ ])(\d+)
#date2 = (\d+)([ \.\/])(\w+)([ \.\/])(\d+)

date = re.findall(r"(\d+)([ \.\/])(\w+)([ \.\/])(\d+)", text)  
#findall e pentru tot fisierul/stringul si le intoarce ca lista

print(date)
file.close()