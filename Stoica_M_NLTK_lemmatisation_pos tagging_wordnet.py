from nltk import pos_tag
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer

# task1: pos tagger
file = open("text.txt")
text = file.read()
text_split = text.split()
tokens_tag = pos_tag(text_split)
print("POS TAGS", tokens_tag)

# task2: lemmatisation

lemmatizer = WordNetLemmatizer()
print("books:", lemmatizer.lemmatize("books"))
print("better", lemmatizer.lemmatize("better", pos="a"))
print("lights", lemmatizer.lemmatize("lights"))
print("worse", lemmatizer.lemmatize("worse", pos="a"))

# task3: wordnet synsets
synonyms = wordnet.synsets("booking")
print(synonyms[0].lemmas()[0].name())
print(synonyms[0].examples())

syns =[]
antonyms = []
for syn in wordnet.synsets("good"):
    for l in syn.lemmas():
        syns.append(l.name())
        if l.antonyms():
            antonyms.append(l.antonyms()[0].name())
print(set(syns))
print(set(antonyms))

file.close()