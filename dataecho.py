import os, sys
import warnings
import whisper
import tools.recordaudio as ra

# local modules
from tools.cswiki import search_cswiki
from tools.htmlinsert import insertHTML

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
    
