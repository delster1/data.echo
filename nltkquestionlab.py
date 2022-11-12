import nltk
from nltk.corpus import stopwords  # stop words from nltk
from nltk.tokenize import word_tokenize  # tokenizer function
from nltk.stem import WordNetLemmatizer

nltk.download("punkt")  #	downloads
nltk.download("stopwords")  #	downloads
nltk.download("averaged_perceptron_tagger")  #	downloads
nltk.download("wordnet")

stoplist = stopwords.words("english")  #	initalized stopwords in english from nltk
lemmatizer = WordNetLemmatizer()

auxVerbs = ["be","can","could","do","have","would","will","shall","must","might","may"]
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

def tagWords(inp): #tag words according to aux verb or part of speech for parse
    inp = inp.split(" ")
    for index, word in enumerate(inp):
        out = []
        auxIndexes = []
        tag = ""
        if word in auxVerbs:
            out.append([word,"VAX"])
        else:
            out.append(nltk.pos_tag([word]))
    return out
            

def findType(inp):
    out = ""
    for ind,obj in enumerate(inp):
        if ind == 0 and obj[1] == "VAX":
            out = "y/n"

def main():
    sentence = input("enter a question\n")  #	sentence to be processed
    taggedQuestion = tagWords(sentence)
    findType(taggedQuestion)


if __name__ == '__main__':
    main() 
