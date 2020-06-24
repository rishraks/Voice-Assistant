import speech_recognition as sr
import pyttsx3
import pyaudio
import random
import datetime
import wolframalpha
from datetime import datetime
import wikipedia 
from datetime import date
import webbrowser as wb
import os

engine=pyttsx3.init('sapi5')
engine.setProperty('rate',150) 
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
greeting=["Hi!. What can I do for you?","Hey!,How may I help you?","Hello sir!. What can I do for you?","G'day, that's hello in Australian",
          "Namaste! that's hello in Hindi","Bonjour!, that's hello in French","Hola! Welcome sir. How may I help you"]
greetingValues=random.choice(greeting)
hate=["are you mad","you are mad","i don't like you","i hate you","don't talk to me"]
thanks=["thank you","you are so sweet","your voice is so sweet","your voice is so beautiful"]
rememberList=[]
rememberDic={}

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour=int(datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!{}".format(greetingValues))
    elif hour>=12 and hour<18:
        speak("Good Afternoon!{}".format(greetingValues))
    else:
        speak("Good Evening!{}".format(greetingValues))
            


def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1.0
        r.adjust_for_ambient_noise(source, duration=5)
        audio=r.listen(source)

    try:
        print("Recognizing...")
        query=r.recognize_google(audio, language='en-in')
        print(f"User:{query}\n")
    except Exception as e:
        speak("Please!, say that again")
        return "None"
           
    return query       


if __name__=="__main__":
    wishMe()
    while True:
        query=takeCommand().lower()

        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query=query.replace('wikipedia',"")
            result=wikipedia.summary(query, sentences=2)
            print(result)
            speak("According to wikipedia")
            speak(result)

        elif 'open youtube' in query:
            wb.open_new("youtube.com")

        elif 'open google' in query:
            wb.open_new("google.com")

        elif 'open gmail' in query:
            wb.open_new("gmail.com")

        elif 'open facebook' in query:
            wb.open_new("facebook.com")

        elif 'open stackoverflow' in query:
            wb.open_new("stackoverflow.com")
            
        elif 'open code'  in query:
            path="D:\\Microsoft VS Code\\Code.exe"
            os.startfile(path)

        elif 'who created you' in query or 'who is your creator' in query:
            speak("Hi sir!I was created on 19th june 2020 in India. Sorry sir!, but I can't disclose my owners name")

        elif query in hate:
            mad=["Sorry if I sound that way. Most likely, I didn't hear you right. Do you mind asking differently this time?",
                 "I sound crazy sometimes when I dont't understand you, but I am never angry at you. Never",
                 "Me, mad, not at all! Maybe I didn't hear you right. Would you like to try again?",
                 "Maybe I misunderstood you, sorry about that. Would you like to try again?"]
            md=random.choice(mad)
            speak("{}".format(md))

        elif 'remember' in query:
            query=query.replace("remember","")
            if query=="":
                speak("If you want me to remember any thing, just remember my name is or remember the door code is 1234")

            else:
                if 'my name' in query:
                    query=query.replace("my name is","")
                    rememberDic["name"]=query
                    speak("Done sir!")
                    speak("To know what I remember just ask, what is my name")
                elif 'my birthday' in query:
                    rem=query.replace("my birthday is on","")
                    rememberDic["birthday"]=rem
                    speak("Done sir!")
                    speak("To know what I remember just ask, when is my birthday")
                else:
                    rememberList.append(query)
                    speak("Done sir!")
                    speak("To know what I remember just ask, what do you know")

        elif "what is my name" in query:
            ans=rememberDic.get("name")
            print("Your name is{}".format(ans))
            speak("Your name is{}".format(ans))

        elif 'when is my birthday' in query:
            ans=rememberDic.get("birthday")
            print("Your birthday is on{}".format(ans))
            speak("Your birthday is on{}".format(ans))

        elif "what do you know" in query:
            for thing in rememberList:
                print(thing)
            speak("Here is the list of what I remember")

        elif 'search' in query or 'search for' in query:
            se=query.replace("search","")
            if se=="":
                speak("What do you want to search for?")
                search=takeCommand()
                url='https://www.google.com/search?q='+search
                wb.get().open_new(url)
                speak("If you want me to search anything, just say. Search for dogs or cats") 
            elif 'search for' in query:
                sea=query.replace("search for","")
                url='https://www.google.com/search?q='+sea
                wb.get().open_new(url)
                speak("Here what I got related to your search")

        elif 'the time' in query:
            time=datetime.now()
            strTime=time.strftime("%H:%M:%S")
            speak("Sir! the time is {}".format(strTime))

        elif 'when is your birthday' in query:
            speak("Well! I was created on 19th June 2020. So yeah, that's my birtthday")    

        elif "who are you" in query:
            speak("Hi!, I am Tess, Your personal assistant. Nice to meet you")

        elif 'hello' in query:
            speak("{}".format(greetingValues)) 

        elif "what's your name" in query:
            speak("Hello!, My name is Tess. What can I do for you?")      

        elif query in thanks:
            thankyou=["I'm here to help, please let me know if you need anything else",
                      "Now you're making me blush","thankyou, it's always nice to get a compliment"]
            thanksy=random.choice(thankyou)
            speak("{}".format(thanksy))    

        elif 'you are beautiful' in query:
            speak("Thanks, I like to think that beauty comes from within")

        elif 'you are hot' in query:
            speak("Some of my data centres run as hot as 95 degrees fahrenfeit!")

        elif 'shutdown' in query or 'goodbye' in query:
            speak("Okay sir!, I'll see you again. Shutting down..")
            break

        else:
            app_id="3X86JU-LK7K9TLWJ4"
            client=wolframalpha.Client(app_id)
            res=client.query(query)
            try:
                ans=next(res.results).text
                print(ans)
                speak("{}".format(ans))
            except Exception as e:
                speak("Please! say that again")