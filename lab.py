import warnings
import whisper
import recordaudio as ra

# ignore warning caused by model.transcribe()
warnings.filterwarnings('ignore')

ra.record_audio()

model = whisper.load_model("base.en")
 
result = model.transcribe("input.wav")
print(result['text'])