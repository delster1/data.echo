from bs4 import element
from bs4 import BeautifulSoup as bs

# takes glossary html and fixes hrefs inside to link correctly
# also offers option to clean styles
# sources: wiki, w3
def clean_markup(markup, clean_style=True, source='wiki') -> bs:
    if type(markup) == element.Tag:
        match markup.name:
            case 'a':
                match source:
                    case 'wiki':
                        if markup.attrs['href'][0] == '/':
                            if source == 'wiki':
                                markup.attrs['href'] = 'https://en.wikipedia.org' + markup.attrs['href']
                        else:
                            # TODO: remove other <a> elements and put text back
                            pass
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

# sandwich markup between halfone.txt and halftwo.txt
def insertHTML(markup: str, qtype: str, clean_style=True, site='wiki'):
    outfile = open('out.html', 'w')

    myfile = open("resources/halfone.txt", "r")
    outfile.writelines(myfile.readlines())
    myfile.close()

    markup = str(clean_markup(markup, clean_style=clean_style, source=site))
    
    match qtype:
        case 'WHAT':
            pass

        case 'EXAMPLE':
           pass

        case _:
            print('default case')
    
    outfile.write(markup)

    myfile = open("resources/halftwo.txt", "r")
    outfile.writelines(myfile.readlines())
    myfile.close()

    outfile.close()