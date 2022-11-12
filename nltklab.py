import nltk
from nltk.corpus import stopwords  # stop words from nltk
from nltk.tokenize import word_tokenize  # tokenizer function
from nltk.stem import WordNetLemmatizer

nltk.download("punkt")  #	downloads
nltk.download("stopwords")  #	downloads
nltk.download("averaged_perceptron_tagger")  #	downloads
lemmatizer = WordNetLemmatizer()

stoplist = stopwords.words("english")  #	initalized stopwords in english from nltk

sentence = input("enter a question\n")  #	sentence to be processed

wordsInSentence = word_tokenize(sentence)  # tokenizing sentence by
wordsInSentence = [lemmatizer.lemmatize(word) for word in wordsInSentence]
taggedSentence = nltk.pos_tag(wordsInSentence)  # tagging sentence by POS
print(taggedSentence)
cswords = open('cswords.txt', 'r')
cswordslines = cswords.readlines()

toResearch = []

filteredSentence = []
for line in cswordslines:
    for word in wordsInSentence:
        if word in stoplist:
            wordsInSentence.remove(word)
        elif word in line:
            toResearch.append([word,line])


# print(cswords)

print("toResearch: ", toResearch)
