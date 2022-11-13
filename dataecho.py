import os
import warnings
import whisper
import recordaudio as ra
from bs4 import BeautifulSoup as bs

# Local modules
import cswiki
import nltktools as nql

# Transcribing Audio

# ignore warnings caused by model.transcribe()
warnings.filterwarnings(action='ignore', category=UserWarning)

ra.record_audio()

model = whisper.load_model('base.en')

result = str(model.transcribe('input.wav')['text'])

os.remove('input.wav')

# args = ['web crawler']

qtype, args = nql.findType(nql.tagWords(result))
print(qtype, args)

#to create output file
outfile = open('out.html', 'w')

# (sentence: str, args: list)
markup = cswiki.search_cswiki(result, args) # search wikipedia w/ result

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

    
