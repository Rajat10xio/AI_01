import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voices', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12 :
        speak("Good morning!")

    elif hour>=12 and hour<18 :
        speak("Good afternoon!")

    else:
        speak("Good evening!") 

    speak("Hello, I am jarvis sir. how may I help you")

def takeCommand():
    #It takes microphone input from user and return string output    
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)
      
    try:
        print("Recognizing...") 
        query = recognizer.recognize_google(audio, language='en-in')  
        print("User said :",query)

    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

# def sendEmail(to, content):


if __name__ == "__main__":
    wishMe() 
    while True:
        query = takeCommand().lower()
        
        # logic for excuting tasks based on query
        if 'wikipedia' in query:
            speak("Searching wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia...")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com") 

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")  

        elif 'play music' in query:
            music_dir = 'C:\\Users\\PRAPHULL RAHANGDALE\\Music\\Indian Walk - Nico Staf.mp3'
            # songs = os.listdir(music_dir)
            # print(songs)
            os.startfile(os.path.join(music_dir)) 

        elif 'stop' in query:
            break    

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            path = 'C:\\Program Files\\Microsoft VS Code\\Code.exe'
            os.startfile(path)  

        elif 'send email to praphull' in query:
            try:
                speak("What should I say")    
                content = takeCommand()
                to = "praphullrahangdale.gmail.com"
                sendEmail(to, content)
                speak("Email has been sent...")

            except Exception as e:
                print("e")
                speak("Sorry sir, I am not able to send this email..")      

        
