import requests
import nltk
from nltk.corpus import stopwords  # stop words from nltk
from nltk.tokenize import word_tokenize  # tokenizer function
from nltk.stem import WordNetLemmatizer
from bs4 import BeautifulSoup as bs  # import for beautifulsoup

nltk.download("punkt", quiet=True)  #	downloads
nltk.download("stopwords", quiet=True)  #	downloads
nltk.download("averaged_perceptron_tagger", quiet=True)  #	downloads
nltk.download("wordnet", quiet=True)
nltk.download('omw-1.4', quiet=True)

stoplist = stopwords.words("english")  #	initalized stopwords in english from nltk
lemmatizer = WordNetLemmatizer()


url = "https://www.w3schools.com" 

tutorialsArr = []
tutorialsLinksArr = []
def tutorialGlossary():

    w3treeHtml = open("resources/w3tree.html","r")
    soup = bs(w3treeHtml,'html.parser') 

    for a in soup.find_all("a"):
        tutorialsLinksArr.append(url+a["href"])
        temp = a.get_text().casefold()
        temp = temp.replace("learn", "")
        temp = temp.replace(" ","")
        tutorialsArr.append(temp)
    # print(tutorialsLinksArr)
    
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
            temp = text.split(" ")
            if temp[0] in tutorialsArr:
                # print("FOUND " ,temp[0])
                text = text.replace(temp[0],"")
            
            myFile.write(text+'\n')

    myFile.close()
        
#arrays for terms that determine sentence
questionWords = ["what"]
exWords = ["how","why"]
# auxVerbs = ["be","can","could","do","have","would","will","shall","must","might","may"]
qw = ["an","be","can","could","do","have","would","will","shall","must","might","may","what","how","why","which","whom","work","with"]
def strToLemmatized(inp): # IGNORE
    out = []
    temp = word_tokenize(inp)
    temp = [lemmatizer.lemmatize(word) for word in temp]
    for word in temp:
        if word not in stoplist:
            out.append(word)
    return out

# tag words according to aux verb or part of speech for parse
def tagWords(inp: str):
    ct = 0

    arr = inp.split(" ")
    out = []
    with open("resources/topics.txt", "r") as f:
        contents = f.read()
        for index, word in enumerate(arr):
            # if word in auxVerbs:
            #     out.append([word,"VAX"]) # Word is an auxillary verb
            if word in questionWords:
                out.append([(word,"QW")]) # word is a question word
            elif word in contents and word not in qw and word not in stoplist and word not in tutorialsArr: 
                # print(word)
                ct +=1
                out.append([(word,"TPC")]) # TPC = topic
            elif word in tutorialsArr:
                ct+=1
                out.append([(word,"TUT")])
            elif word in exWords:
                out.append([(word,"EW")]) # word is an example word
            else:
                out.append(nltk.pos_tag([word]))

        f.close() 
        return out, ct
            

def findType(inp: list): #function to sort tagged input by question type (yes or no/what/example)
    out = ""
    
    for ind, obj in enumerate(inp):
        # if ind == 0 and obj[1] == "VAX":
        #     return "Y/N"
        #     print("y/n")
        next_a = inp[1][0][1]
        next_b = inp[2][0][1]

        match obj[0][1]:
            case 'QW':
                if ind == 0 and next_a == 'VBZ'and next_b == 'DT':
                    return 'WHAT'
                # if(ind == 0 and inp[1][0][1] == "VBZ" and inp[2][0][1] == "DT"):
                #     return "WHAT"
                
                return "WHAT"
            case 'EW':
                return "EXAMPLE"
            case _:
                return ''

    return out        

def findArgs(arr, qType, ct):
    args = []
    tagsArr = [i[0][1] for i in arr]
    # print(arr)
    if ct > 1:
        if qType == "WHAT":
            if(arr[1][0][1] == "VBZ" and arr[2][0][1] == "DT"):
                args.append(arr[3:len(arr)])
            else:
                for ind,obj in enumerate(tagsArr):
                    if obj == "TUT" or obj == "TPC":
                        args.append(arr[ind])
        elif qType == "EXAMPLE":
            for ind,obj in enumerate(tagsArr):
                if obj == "TUT" or obj == "TPC":
                    args.append(arr[ind])
    else:
        if qType == "WHAT":
            if(len(arr)-1>3 and arr[1][0][1] == "VBZ" and arr[2][0][1] == "DT"):
                args.append(arr[3:len(arr)])
            else:
                for ind,obj in enumerate(tagsArr):
                    if obj == "TUT" or obj == "TPC":
                        args.append(arr[ind])            
        elif qType == "WHAT":
            for ind,obj in enumerate(tagsArr):
                if obj == "TUT" or obj == "TPC":
                    args.append(arr[ind])            
                    
    return qType,args
        

# https://www.englishclub.com/vocabulary/wh-question-words.htm USE THIS FOR AUX VERBS
def main():
    sentence = "what is a boolean expression"  #	sentence to be processed

    tutorials = tutorialGlossary()
    # print(tutorialsArr,"\n\n")
    tagged = tagWords(sentence)
    taggedQuestion = tagged[0]
    count = tagged[1]

    # topicsGlossary(tutorialsLinksArr) 
    questionType = findType(taggedQuestion)
    print(findArgs(taggedQuestion,questionType,count))


if __name__ == '__main__':
    main() 
