import os, sys
import warnings
import whisper
import recordaudio as ra
from bs4 import BeautifulSoup as bs

# Local modules
import cswiki
from nltktools import *

def main():
    seconds = 4
    cmd_argc = len(sys.argv)
    match cmd_argc:
        case 2:
            try:
                seconds = int(sys.argv[1])
            except:
                print('Usage: py dataecho.py <recording_seconds>')
        case _:
            pass

    # ignore warnings caused by model.transcribe()
    # warnings.filterwarnings(action='ignore', category=UserWarning)

    # # record audio
    # ra.record_audio(seconds=seconds)

    # model = whisper.load_model('base.en')

    # # transcribe audio
    # sentence = str(model.transcribe('input.wav')['text']).casefold()
    # os.remove('input.wav')

    sentence = 'what is a boolean expression'

    print(f'\n----------------\n\nTranscribed audio: {sentence}')

    #to create output file
    outfile = open('out.html', 'w')

    # (sentence: str, args: list)
    markup = cswiki.search_cswiki(sentence) # search wikipedia w/ result

    if markup is not None:
        tagged = tagWords(sentence)
        taggedQuestion = tagged[0]
        count = tagged[1]
        
        qtype = findType(taggedQuestion)
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

if __name__ == '__main__':
    main() 
    
