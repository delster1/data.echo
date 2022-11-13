import os, sys
import warnings
import whisper
import recordaudio as ra
from bs4 import BeautifulSoup as bs

# Local modules
import cswiki
import nltktools as nql

def main():
    cmd_argc = len(sys.argv)
    match cmd_argc:
        case _:
            print(cmd_argc)

    # ignore warnings caused by model.transcribe()
    warnings.filterwarnings(action='ignore', category=UserWarning)

    # record audio
    ra.record_audio()

    model = whisper.load_model('base.en')

    # transcribe audio
    sentence = str(model.transcribe('input.wav')['text'])

    print(f'\n----------------\nTranscribed audio: {sentence}')

    os.remove('input.wav')

    qtype, args = nql.findType(nql.tagWords(sentence))
    print(qtype, args)

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

if __name__ == '__main__':
    main() 
    
