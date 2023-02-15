import pyttsx3 as pytts
import speech_recognition
import time

# --------------------->> Functions <<---------------------
 
def speak(audio):
    print("-------------------------------------->>> ~~~~~~~ <<<--------------------------------------")
    text_to_speech_engine.say(audio)
    print(f": {audio}")
    text_to_speech_engine.runAndWait()
    print("-------------------------------------->>> ~~~~~~~ <<<--------------------------------------")

    
def listenAndRecognizeSpeech():
    with speech_recognition.Microphone() as source:
        print("Listening...")
        audio = listener.listen(source)
        try:
            print("Recognizing...")
            recognized_speech = listener.recognize_google(audio, language='en-in')
            print(f": {recognized_speech}")
        except Exception as error:
            print(error)
            return "none"
        return recognized_speech.lower()
    

def executeTask():
    while True:
        command = listenAndRecognizeSpeech()
        if 'jarvis' in command:
            speak("Yes Sir. I am alive and ready to follow...")
            speak("How may I help you today.")
        elif 'how are you' in command:
            speak("I am fine sir! Is there Anything I can do for you?")




# --------------------->> Driver Code <<---------------------
    
listener = speech_recognition.Recognizer()
print("Setting up...")
with speech_recognition.Microphone() as source:
    listener.adjust_for_ambient_noise(source, duration=1) # In this line system will take 1 sec to adjust itself for environment noise  
listener.pause_threshold = 0.7 # number of seconds the system will take to recognize the voice once the user has stopped speaking

text_to_speech_engine = pytts.init('sapi5') # sapi5 is TTS engine for windows; other TTS are 'nsss' for MacOS & 'espeak' for linux and other os
voices = text_to_speech_engine.getProperty('voices')
# print(voices) # Print availabe voices
# rate = text_to_speech_engine.getProperty('rate')
# print(rate) # Print current speech rate 
# volume = text_to_speech_engine.getProperty('volume')
# print(volume) # Print current speech volume

text_to_speech_engine.setProperty('voices', voices[1].id) # index value can be changed for different types of voices available
text_to_speech_engine.setProperty('rate', 231) 
text_to_speech_engine.setProperty('volume', 1.0)
            
speak('Hello. I am Jarvis. Tony Stark\'s personal virtual assistant. Now Working for Sumit.')        


