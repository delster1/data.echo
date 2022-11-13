import cswiki
import nltktools as nql
from bs4 import BeautifulSoup as bs

sentence = 'what is a web crawler'
args = ['web crawler']
qtype = nql.findType(nql.tagWords(sentence))

# (sentence: str, args: list)
markup = cswiki.search_cswiki(sentence, args) # search wikipedia w/ result

if markup is not None:
    match qtype:
        case "WHAT":
            cleanHTML = cswiki.clean_markup(markup, True, 'wiki').prettify()
            
            print(cleanHTML)
            
            soup = bs(cleanHTML, 'html.parser')
            
        case _:
            print('default case')

    