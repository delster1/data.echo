import nltk
from nltk.corpus import stopwords  # stop words from nltk
from nltk.tokenize import word_tokenize  # tokenizer function

nltk.download("punkt")  #	downloads
nltk.download("stopwords")  #	downloads
nltk.download("averaged_perceptron_tagger")  #	downloads

stoplist = set(
 stopwords.words("english"))  #	initalized stopwords in english from nltk

sentence = input("enter a question\n")  #	sentence to be processed

wordsInSentence = word_tokenize(sentence)  # tokenizing sentence by

taggedSentence = nltk.pos_tag(wordsInSentence)  # tagging sentence by POS

filteredSentence = []
for index,word in enumerate(wordsInSentence):  # iaterate through tokenized sentence
    if word.casefold() not in stoplist or taggedSentence[index][1][0] != "P":
        filteredSentence.append(word)  
        # print(taggedSentence[index])  # detect non-filler words

print(
 f"Filtered Sentence:\n {filteredSentence}\n"
)

with open("cswords.txt", "r") as f:
    for line in f:
        line = line.rstrip()

        # if csword matches word in query
        # TODO: make this work with spaces lol
        # making this work with spaces will become O(n^2) where n is word count

        if line in filteredSentence:
            print("associated topic found: ", line)


