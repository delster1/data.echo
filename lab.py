import warnings
import whisper
import recordaudio as ra

# ignore warnings caused by model.transcribe()
warnings.filterwarnings(action='ignore', category=UserWarning)

ra.record_audio()

model = whisper.load_model("base.en")
 
result = model.transcribe("input.wav")
print(result['text'])