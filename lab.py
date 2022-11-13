import warnings
import whisper
import recordaudio as ra
import cswiki

# Transcribing Audio

# ignore warnings caused by model.transcribe()
# warnings.filterwarnings(action='ignore', category=UserWarning)

# ra.record_audio()

# model = whisper.load_model("base.en")

# result = str(model.transcribe("input.wav")['text'])
result = 'what is a web crawler'

print(result)

markup = cswiki.search_cswiki(result, ['web crawler']) # search wikipedia w/ result

if markup is not None:
    print(cswiki.clean_markup(markup, True, 'wiki').prettify())