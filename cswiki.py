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
def search_cswiki(sentence: str) -> str:
    url = ''
    tagged = tagWords(sentence.casefold())
    taggedQuestion = tagged[0]
    count = tagged[1]
    
    qtype = findType(taggedQuestion)
    args = findArgs(taggedQuestion, qtype, count)
    print(args)

    qtype = findType(tagWords(sentence))

    match qtype:
        case 'WHAT': url = 'https://en.wikipedia.org/wiki/Glossary_of_computer_science'
        case 'EXAMPLE': url = 'https://www.w3schools.com'
        case _:
            print(f'Invalid Question Type: {qtype}')
            url = 'https://www.w3schools.com'


    response = requests.get(url)

    match qtype:
        case 'WHAT':
            only_glossary = strainer(attrs={'class': 'glossary'})
            soup = bs(response.content, 'html.parser', parse_only=only_glossary)  # turn html into soup

            # search for argument in wikipedia
            for topic in soup.find_all('dt'):
                if args[0] == topic.contents[0].contents[0].get_text().rstrip():
                    args[0] = args[0].replace(' ', '_')
                    print('found associated topic: ', args[0])
                    
                    # finding glossary entry from url for topic
                    for tag in soup.find_all(id=args[0]):
                        return tag.find_next('dd')

            # TODO: search w3schools

        case 'EXAMPLE': # w3
            pass

        case _:
            print('More question types haven\'t been implemented yet!')

    return None
