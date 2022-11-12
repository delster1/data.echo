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
<<<<<<< HEAD
for line in cswordslines:
    for word in wordsInSentence:
        if word in stoplist:
            wordsInSentence.remove(word)
        elif word in line:
            toResearch.append([word,line])
=======
for index,word in enumerate(wordsInSentence):  # iaterate through tokenized sentence
    if word.casefold() not in stoplist or taggedSentence[index][1][0] != "P":
        filteredSentence.append(word)  
        print(taggedSentence[index])  # detect non-filler words
>>>>>>> 0ad88099105343e1438aa287605ab2a4c4aef018


# print(cswords)

print("toResearch: ", toResearch)
