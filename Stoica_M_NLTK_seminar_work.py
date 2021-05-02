import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
import matplotlib

file = open("text.txt")
text = file.read()

# ex1 sentence splitting
sentence_tokens = sent_tokenize(text)
print("sentence splitting")
print(sentence_tokens)

# ex2 tokenisation
word_splitting = word_tokenize(text)
print("word splitting")
print(word_splitting)

# ex3 word frequency counting and plotting
text1 = text.split(' ')
word_freq = nltk.FreqDist(text1)
ten_most_common = word_freq.most_common(10)
print(ten_most_common)
print("\r")
word_freq.plot(10, cumulative=False)

# ex4 bigrams counting
bi_grams = list(nltk.ngrams(word_splitting, 2))
print("bigrams:")
print(bi_grams)

# ex5 language identification
tc = nltk.classify.textcat.TextCat()
guess_language = tc.guess_language(text)
print("\r")
print("Language is:", guess_language)

# ex6 sentiment analysis
sid = SentimentIntensityAnalyzer()
scores = sid.polarity_scores(text)

for key in sorted(scores):
    print("{}: {}".format(key, scores[key]), end=" ")

file.close()
