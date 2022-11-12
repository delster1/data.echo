from bs4 import BeautifulSoup as bs  # import for beautifulsoup

import requests  # this is so i can use a link to get html output
import re  # python regex library (used ln 11)

url = "https://en.wikipedia.org/wiki/Glossary_of_computer_science"  # url to search

response = requests.get(url) # turn url into html


soup = bs(response.content, 'html.parser')  # turn html into soup

# print(soup.prettify())
ptags = soup.find_all(
 re.compile('^dt'))  # array of tags that start with 'h' or 'p'

words = []

with open('cswords,txt','w') as f:
    for i in ptags :  #iterate through array of tags
	  #if text is in tag's NavigableString
        f.write(i.contents[0].contents[0].get_text())
        f.write('\n')