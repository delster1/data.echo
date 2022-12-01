from tools.nltktools import *
from tools.w3tools import *
from bs4 import BeautifulSoup as bs  # import for beautifulsoup\
from bs4 import SoupStrainer as strainer
import requests  # this is so i can use a link to get html output

# creates a powerset of search terms given from args
# yoinked this from online lol
def build_topics(args: list):
    # detect what kind of arguments are input
    # recursive array traversal to un-nest
    # print(f'args: {args}')
    # this while loop might need to be reimplemented later
    while any(isinstance(i, list) for i in args) and len(args) == 1:
        args = args[0]

    # print(f'final args: {args}')

    out = [[]]
    for topic in args:
        term = topic[0][0]
        
        for i in range(len(out)):
            out.append([" ".join(out[i] + [term])])
    
    out.pop(0)

    for i in range(len(out)):
        out[i] = out[i][0]
    
    return out
        

# search website for info to answer question
def search_cswiki(sentence: str):
    sentence = sentence.rstrip().lstrip().casefold()

    if sentence[-1] in ['!', '.', '?']:
        sentence = sentence[:-1]

    tagged = tagWords(sentence)
    taggedQuestion = tagged[0]
    count = tagged[1]
    
    qtype = findType(taggedQuestion)

    # TODO: fix findArgs for smaller inputs like 'what is coding'
    args = findArgs(taggedQuestion, qtype, count)

    # creating powerset of topics
    topics = build_topics(args[1])

    print(f'topics: {topics}')

    match qtype:
        case 'WHAT':
            url = 'https://en.wikipedia.org/wiki/Glossary_of_computer_science'
            response = requests.get(url)

            only_glossary = strainer(attrs={'class': 'glossary'})
            soup = bs(response.content, 'html.parser', parse_only=only_glossary)  # turn html into soup

            # search for argument in wikipedia
            for dt in soup.find_all('dt'):
                content = dt.contents[0].contents[0].text.rstrip().casefold()
                if content in topics:
                    topic = content.replace(' ', '_')
                    
                    # finding glossary entry from url for topic
                    for tag in soup.find_all(id=topic):
                        return tag.find_next('dd'), qtype

            # TODO: search w3schools

        case 'EXAMPLE': # w3
            # unnecessary bc dellie has w3 like a goat
            # url = 'https://www.w3schools.com'
            # response = requests.get(url)

            tutorial = "javascript"
            topic = "loop"

            getW3HomepageSoup()

            tutorialsDict = getTutorialsDict()
            topicLinks = getTopicsSoup(tutorialsDict, tutorial, topic)
            out = getExamples(topicLinks)

            return out, qtype

        case _:
            print(f'Invalid question type: {qtype}')

    return "", qtype
