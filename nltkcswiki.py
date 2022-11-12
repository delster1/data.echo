import nltkquestionlab as nql
from bs4 import BeautifulSoup as bs  # import for beautifulsoup

import requests  # this is so i can use a link to get html output
import re  # python regex library (used ln 11)

sentence = "what is a web crawler"

filteredSentence = nql.strToLemmatized(sentence)

print(f"Filtered Sentence:\n {filteredSentence}\n")

glossaryURL = "https://en.wikipedia.org/wiki/Glossary_of_computer_science"

response = requests.get(glossaryURL) # turn url into html
soup = bs(response.content, 'html.parser')  # turn html into soup

for topic in soup.find_all(re.compile('^dt')):
    topic = topic.contents[0].contents[0].get_text().rstrip().split(" ")

    # if csword matches term in query
    # making this work with spaces is O(n^2) where n is word count
    for set_size in range(len(filteredSentence), 0, -1):
        for i in range(0, len(filteredSentence)):
            term = filteredSentence[i:set_size]

            # simple powerset of filteredSentence
            # if term makes sure the term isnt empty

            if term:
                if term == topic:
                    topic = "_".join(term)
                    print("associated topic: ", topic)

                    ptags = soup.find_all(id=topic)

                    for i in ptags:
                        print(i.text)
