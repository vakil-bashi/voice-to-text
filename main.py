import speech_recognition as sr

# Initialize recognizer
r = sr.Recognizer()

# Use the microphone as source
with sr.Microphone() as source:
    print("Speak Now:")
    audio = r.listen(source)

try:
    # Recognize speech using Google Web Speech API
    text = r.recognize_google(audio, language='fa-IR')  # 'fa-IR' is the language code for Persian in Iran
    print("You said: " + text)
except sr.UnknownValueError:
    print("Could not understand audio")
except sr.RequestError as e:
    print("Could not request results; {0}".format(e))
