import requests
import nltk
from nltk.corpus import stopwords  # stop words from nltk
from nltk.tokenize import word_tokenize  # tokenizer function
from nltk.stem import WordNetLemmatizer

from bs4 import BeautifulSoup as bs  # import for beautifulsoup

nltk.download("punkt")  #	downloads
nltk.download("stopwords")  #	downloads
nltk.download("averaged_perceptron_tagger")  #	downloads
nltk.download("wordnet")
nltk.download('omw-1.4')

stoplist = stopwords.words("english")  #	initalized stopwords in english from nltk
lemmatizer = WordNetLemmatizer()


url = "https://www.w3schools.com" 

tutorialsArr = []
tutorialsLinksArr = []
def tutorialGlossary():

    w3treeHtml = open("w3tree.html","r")
    soup = bs(w3treeHtml,'html.parser') 

    for a in soup.find_all("a"):
        tutorialsLinksArr.append(url+a["href"])
        temp = a.get_text().casefold()
        temp = temp.replace("learn", "")
        temp = temp.replace(" ","")
        tutorialsArr.append(temp)
    print(tutorialsLinksArr)
    
    return tutorialsArr

def topicsGlossary(arr):

    myFile = open('topics.txt', 'w')

    for ind,obj in enumerate(tutorialsLinksArr):
        response = requests.get(obj) # turn url into html
        soup = bs(response.content, 'html.parser')
        topicsList = soup.find("div",id="leftmenuinnerinner")
        soup = bs(str(topicsList),"html.parser")
        for o in soup.find_all("a"):
            
            text = o.get_text()
            text = text.replace("Learn ", "").casefold()
            myFile.write(text+'\n')
    myFile.close()
        
#arrays for terms that determine sentence
questionWords = ["what"]
exWords = ["how","why"]
# auxVerbs = ["be","can","could","do","have","would","will","shall","must","might","may"]

def strToLemmatized(inp): # IGNORE
    out = []
    temp = word_tokenize(inp)
    temp = [lemmatizer.lemmatize(word) for word in temp]
    for word in temp:
        if word not in stoplist:
            out.append(word)
    return out

def tagWords(inp: str): #tag words according to aux verb or part of speech for parse
    inp = inp.split(" ")
    out = []

    for index, word in enumerate(inp):
        # if word in auxVerbs:
        #     out.append([word,"VAX"]) # Word is an auxillary verb
        if word in questionWords:
            out.append([word,"QW"]) # word is a question word
        elif word in tutorialsArr:
            out.append([word,"TUT"])
        elif word in exWords:
            out.append([word,"EW"]) # word is an example word
        else:
            out.append(nltk.pos_tag([word]))
        
    return out
            

def findType(inp: list): #function to sort tagged input by question type (yes or no/what/example)
    out = ""
    for ind,obj in enumerate(inp):
        # if ind == 0 and obj[1] == "VAX":
        #     return "Y/N"
        #     print("y/n")
        if obj[1] == "QW":
            return "WHAT"
        elif obj[1] == "EW":
            return "EXAMPLE"
    return out        

# https://www.englishclub.com/vocabulary/wh-question-words.htm USE THIS FOR AUX VERBS
def main():
    sentence = "how can i iterate over an array in python"  #	sentence to be processed
    taggedQuestion = tagWords(sentence)
    # print(taggedQuestion)
    tutorials = tutorialGlossary()
    # topicsGlossary(tutorialsLinksArr) 
    return findType(taggedQuestion)


if __name__ == '__main__':
    main() 
