import smtplib
import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import wikipedia
import webbrowser
import os
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty("voice", voices[1].id)

def speak(audio):
  engine.say(audio)
  engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour<=12:
        speak("good morning!")
    elif hour >=12 and hour<=18:
        speak("good afetrnoon!")
    else:
        speak("good evening!")
    speak("i am jarvis sir please tell me how may i help you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recogniting...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        # print(e)

        print('Say that again please....')
        return "None"
    return query


def sendEmail(do,content):
  server = smtplib.SMTP('smtp.gmail.com',587)
  server.ehlo()
  server.starttls()
  server.login("yourmail","password")
  server,sendEmail("yourmail",to,content)
  server.close()


if __name__=="__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if "wikipedia" in query:
            speak('searching wikipedia....')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        
        elif 'open google' in query:
           webbrowser.open("google.com")

        elif 'open youtube' in query:
           webbrowser.open("youtube.com")
 
        elif 'open stack' in query:
           webbrowser.open("youtube.com")

        
        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\navne\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code\\Code.exe"
            os.startfile(codePath)

        elif "email to navneet" in query:
            try:
                speak("what should i say")
                content = takeCommand()
                to = "your email"
                sendEmail(to,content) 
                speak("email has been sent")
            except Exception as e:
                print(e)
                speak("soory unable to send email")


        elif 'play music' in query:
         music_dir = "fordre adderss"
         songs = os.listdir(music_dir)
        print(songs)
        os.startfile(os.path.join(music_dir, songs[0]))




       

        
