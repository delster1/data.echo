import warnings
import whisper
import recordaudio as ra
import cswiki

# ignore warnings caused by model.transcribe()
warnings.filterwarnings(action='ignore', category=UserWarning)

ra.record_audio()

model = whisper.load_model("base.en")

result = str(model.transcribe("input.wav")['text'])

print(result)

markup = cswiki.search_cswiki(result)

if markup is not None:
    print(cswiki.clean_markup(markup, True, 'wiki').prettify())