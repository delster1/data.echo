# import nltkquestionlab
from bs4 import BeautifulSoup as bs  # import for beautifulsoup

import requests  # this is so i can use a link to get html output
import re  # python regex library (used ln 11)

filteredSentence = ['what', 'is', 'string']
glossaryURL = "https://en.wikipedia.org/wiki/Glossary_of_computer_science"

print(
 f"Filtered Sentence:\n {filteredSentence}\n"
)

with open("cswords.txt", "r") as f:
    for line in f:
        line = line.rstrip().split(" ")

        # if csword matches word in query
        # TODO: make this work with spaces lol
        # making this work with spaces will become O(n^2) where n is word count

        for set_size in range(len(filteredSentence), 0, -1):
            for i in range(0, len(filteredSentence)):
                term = filteredSentence[i:set_size]

                # simple powerset of filteredSentence
                # if term makes sure the term isnt empty
                if term:
                    if term in line or term == line:
                        topic = "_".join(term)
                        print("associated topic: ", topic)
                        
                        response = requests.get(glossaryURL) # turn url into html
                        soup = bs(response.content, 'html.parser')  # turn html into soup

                        paragraphs = soup.find_all('p')

                        print(paragraphs[1].text)

