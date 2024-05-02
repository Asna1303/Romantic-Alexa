import speech_recognition as sr


listener = sr.Recognizer()
try:
        with sr.Microphone() as source:
except:
        pass