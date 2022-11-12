import nltk
from nltk.corpus import stopwords  # stop words from nltk
from nltk.tokenize import word_tokenize  # tokenizer function
from nltk.stem import WordNetLemmatizer

nltk.download("punkt")  #	downloads
nltk.download("stopwords")  #	downloads
nltk.download("averaged_perceptron_tagger")  #	downloads
nltk.download("wordnet")
nltk.download('omw-1.4')

stoplist = stopwords.words("english")  #	initalized stopwords in english from nltk
lemmatizer = WordNetLemmatizer()

def strToLemmatized(inp):
    out = []
    temp = word_tokenize(inp)
    temp = [lemmatizer.lemmatize(word) for word in temp]
    for word in temp:
        if word not in stoplist:
            out.append(word)
    return out

def fixInput(inp):
    out = []
    temp = word_tokenize(inp)
    temp = [lemmatizer.lemmatize(word) for word in temp]
    for word in temp:
        if word not in stoplist:
            out.append(word)
    return out


# print(cswords)
def main():
    print("toResearch: ", toResearch)
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

if __name__ == '__main__':
    main() 
