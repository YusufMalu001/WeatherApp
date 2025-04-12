import speech_recognition as sr
import pyttsx3

# Initialize text-to-speech
engine = pyttsx3.init()
engine.say("Say the name of the city.")
engine.runAndWait()

# Initialize recognizer
recognizer = sr.Recognizer()

# Use microphone to capture audio
with sr.Microphone() as source:
    print("🎙️ Listening... (Please speak clearly)")
    recognizer.adjust_for_ambient_noise(source, duration=1)  # improves accuracy
    audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)

# Try to recognize speech
try:
    city = recognizer.recognize_google(audio)
    print(f"📍 You said: {city}")
except sr.UnknownValueError:
    print("❌ Sorry, I could not understand the audio.")
except sr.RequestError as e:
    print(f"⚠️ API request error: {e}")
except Exception as e:
    print(f"🚨 Unexpected error: {e}")

