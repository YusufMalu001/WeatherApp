import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init()

def talk(text):
    """Speaks the provided text aloud."""
    engine.say(text)
    engine.runAndWait()

def take_command():
    """Captures voice input and converts it to text."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎙️ Listening...")
        audio = recognizer.listen(source)

    try:
        city = recognizer.recognize_google(audio)
        print(f"📍 You said: {city}")
        return city
    except sr.UnknownValueError:
        print("❌ Sorry, I could not understand.")
        return None
    except sr.RequestError as e:
        print(f"⚠️ Could not request results: {e}")
        return None
