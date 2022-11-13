from nltktools import *
from bs4 import BeautifulSoup as bs  # import for beautifulsoup\
from bs4 import SoupStrainer as strainer
import bs4
import requests  # this is so i can use a link to get html output

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
                            print(markup.parent)
                            print('Current Child: ', markup.name)
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
                pass
        
        if clean_style:
            if 'style' in markup.attrs:
                markup.attrs.pop('style', None)

        if markup.children is not None:
            for i in range(len(markup.contents)):
                markup.contents[i] = clean_markup(markup.contents[i], clean_style=clean_style, source=source)
    
    return markup

# search website for info to answer question
def search_cswiki(sentence: str, qtype: str, args: list) -> str:
    url = ''
    match qtype:
        case 'WHAT': url = 'https://en.wikipedia.org/wiki/Glossary_of_computer_science'
        case 'EXAMPLE': url = 'https://www.w3schools.com'
        case _:
            print(f'Invalid Question Type: {qtype}')
            url = 'https://www.w3schools.com'

    response = requests.get(url)

    match qtype:
        case 'EXAMPLE': # w3
            pass

        case 'WHAT':
            sentence = strToLemmatized(sentence.casefold())
            only_glossary = strainer(attrs={'class': 'glossary'})
            soup = bs(response.content, 'html.parser', parse_only=only_glossary)  # turn html into soup

            # search for argument in wikipedia
            for topic in soup.find_all('dt'):
                content = topic.contents[0].contents[0].get_text().rstrip().casefold().split(' ')
                # print(f'{type(sentence)} | {content}')
                if sentence == content:
                    topic = '_'.join(sentence)
                    
                    # finding glossary entry from url for topic
                    for tag in soup.find_all(id=topic):
                        return tag.find_next('dd')

            # TODO: search w3schools

        case _:
            print('More question types haven\'t been implemented yet!')

    return None
