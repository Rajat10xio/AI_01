import pyttsx3
import datetime
import pyaudio
import speech_recognition as sr
import wikipedia

engine = pyttsx3.init('sapi5')
voices = engine.getProperty("voices") 
#print(voices[0].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour =  int(datetime.datetime.now().hour)
    if 1 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour <  18:
        speak("Good Afternoon!")
    else: 
        speak("Good Evening!")
    speak("i am rojaa.  please tell me how can i help you")   

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            query = r.recognize_bing(audio,language="en-in")
            print(f"user said :",{query})
            return query
        except Exception as e:
            return "some  error occured"  


if __name__=="__main__" :
    wishme() 
    while True :
        query = takecommand()
        speak(query)
#i love you 
