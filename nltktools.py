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

#arrays for terms that determine sentence
questionWords = ["what"]
exWords = ["how","why"]
auxVerbs = ["be","can","could","do","have","would","will","shall","must","might","may"]

def strToLemmatized(inp): # IGNORE
    out = []
    temp = word_tokenize(inp)
    temp = [lemmatizer.lemmatize(word) for word in temp]
    for word in temp:
        if word not in stoplist:
            out.append(word)
    return out

def fixInput(inp): # TOKENIZE AND LEMMAITZE INPUT
    out = []
    temp = word_tokenize(inp)
    temp = [lemmatizer.lemmatize(word) for word in temp]
    temp = out
    return out

def tagWords(inp): #tag words according to aux verb or part of speech for parse
    inp = inp.split(" ")
    out = []

    for index, word in enumerate(inp):
        if word in auxVerbs:
            out.append([word,"VAX"]) # Word is an auxillary verb
        elif word in questionWords:
            out.append([word,"QW"]) # word is a question word
        elif word in exWords:
            out.append([word,"EW"]) # word is an example word
        else:
            out.append(nltk.pos_tag([word]))
        
    return out
            

def findType(inp): #function to sort tagged input by question type (yes or no/what/example)
    out = ""
    for ind,obj in enumerate(inp):
        if ind == 0 and obj[1] == "VAX":
            return "Y/N"
            print("y/n")
        elif obj[1] == "QW":
            return "WHAT"
        elif obj[1] == "EW":
            return "EXAMPLE"
    return out        

# https://www.englishclub.com/vocabulary/wh-question-words.htm USE THIS FOR AUX VERBS
def main():
    sentence = input("enter a question\n")  #	sentence to be processed
    taggedQuestion = tagWords(sentence)
    print(taggedQuestion)
    return findType(taggedQuestion)


if __name__ == '__main__':
    main() 
