import whisper
import recordaudio as ra

print("test")
ra.record_audio()

model = whisper.load_model("base")
result = model.transcribe("output.wav")
print(result['text'])