import cswiki
import nltktools as nql
from bs4 import BeautifulSoup as bs

sentence = 'what is a web crawler'
args = ['web crawler']
qtype = nql.findType(nql.tagWords(sentence))
#to create output file
outfile = open('out.html', 'w')

# (sentence: str, args: list)
markup = cswiki.search_cswiki(sentence, args) # search wikipedia w/ result

if markup is not None:
    match qtype:
        case "WHAT":
            cleanHTML = cswiki.clean_markup(markup, True, 'wiki').prettify()
            
            myfile = open("whathalfone.txt", "r")
            outfile.writelines(myfile.readlines())
            myfile.close()

            outfile.write(cleanHTML)

            myfile = open("whathalftwo.txt", "r")
            outfile.writelines(myfile.readlines())
            myfile.close()

            soup = bs(cleanHTML, 'html.parser')

            print(soup.contents)


        case _:
            print('default case')

    
