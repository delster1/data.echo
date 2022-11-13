import nltkquestionlab as nql
from bs4 import BeautifulSoup as bs  # import for beautifulsoup
from bs4 import SoupStrainer as strainer # import for soupstrainer
import bs4
import requests  # this is so i can use a link to get html output
import re  # python regex library (used ln 11)

# takes glossary html and fixes hrefs inside to link correctly
# also offers option to clean styles
# sources: wiki, w3
def clean_markup(markup, clean_style=True, source='wiki') -> str:
    if type(markup) == bs4.element.Tag:
        match markup.name:
            case 'a':
                match source:
                    case 'wiki':
                        if markup.attrs['href'][0] == '/':
                            if source == 'wiki':
                                markup.attrs['href'] = 'https://en.wikipedia.org' + markup.attrs['href']
                        else:
                            markup.attrs['href'] = ''
                    case _:
                        # do not modify links in other resources
                        pass
            case 'span':
                match source:
                    case 'wiki':
                        if 'class' in markup.attrs:
                            markup.attrs.pop('class', None)
                        if 'title' in markup.attrs:
                            markup.attrs.pop('title', None)
                    case _:
                        pass
            case _:
                if clean_style:
                    if 'style' in markup.attrs:
                        markup.attrs.pop('style', None)

        if markup.children is not None:
            for i in range(len(markup.contents)):
                markup.contents[i] = clean_markup(markup.contents[i], clean_style=clean_style, source=source)
    
    return markup

# search cs glossary for terms in sentence
def search_cswiki(sentence: str) -> str:
    filteredSentence = nql.strToLemmatized(sentence)

    glossaryURL = 'https://en.wikipedia.org/wiki/Glossary_of_computer_science'

    response = requests.get(glossaryURL) # turn url into html

    only_glossary = strainer(attrs={'class': 'glossary'})
    soup = bs(response.content, 'html.parser', parse_only=only_glossary)  # turn html into soup

    for topic in soup.find_all(re.compile('^dt')):
        topic = topic.contents[0].contents[0].get_text().rstrip().split(' ')

        # if glossary matches term in query
        # since powerset, search is O(n^2) where n is word count
        for set_size in range(len(filteredSentence), 0, -1):
            for i in range(0, len(filteredSentence)):
                term = filteredSentence[i:set_size]

                if term:
                    if term == topic:
                        topic = '_'.join(term)
                        print('Associated CS Wikipedia Topic: ', topic)
                        
                        # finding glossary entry from url for topic
                        contents = soup.find_all(id=topic)

                        for tag in contents:
                            return tag.find_next('dd')

    return None