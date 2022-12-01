import os, sys
import warnings
import whisper
import tools.recordaudio as ra

<<<<<<< HEAD
# Local modules
import cswiki
from nltktools import *
=======
# local modules
from tools.cswiki import search_cswiki
from tools.htmlinsert import insertHTML
>>>>>>> 8b1c1a084090a0e4d5432edbbff9ee83249e3b30

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

    # # ignore warnings caused by model.transcribe()
    # warnings.filterwarnings(action='ignore', category=UserWarning)

    # # record audio
    # print()
    # ra.record_audio(seconds=seconds)

    # model = whisper.load_model('base.en')

    # # transcribe audio
    # sentence = str(model.transcribe('input.wav')['text']).casefold()
    # os.remove('input.wav')

    # test sentence
    sentence = ' what is a boolean expression?'

    print(f'\n----------------\n\nTranscribed audio: {sentence}\n')

    markup, qtype = search_cswiki(sentence) # search wikipedia w/ result
    print(f'markup: {markup}')

    if markup is not None:
        insertHTML(markup, qtype)

if __name__ == '__main__':
    main() 
    
