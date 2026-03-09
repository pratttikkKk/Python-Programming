from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

ps=PorterStemmer()
text="you'r doing very foolish things by crying everytime everywhere continously badly and jumping "
words=word_tokenize(text)

print("original sentence:",text)
print("original words:",words)
print("stemmed words:")

for i in words:
 print(i,"->",ps.stem(i))




