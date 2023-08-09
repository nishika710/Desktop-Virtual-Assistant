import pyttsx3    #convert text to speech
import datetime   #to display current data and time
import speech_recognition as sr #pip install SpeechRecognition == speech from mic to text format
import pyautogui  #to send whatsapp msgs
import webbrowser as wb  #opens whatsapp browser
from time import sleep   #takes time to speak while browser is loading
import wikipedia   #search on wikipedia
import pywhatkit
import requests
from newsapi.newsapi_client import NewsApiClient
import clipboard
import os
import pyjokes #to generate jokes
import time as tt
import string
import random

engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices') #getting details of current voice
#print(voices[0].id)
engine.setProperty('voice', voices[0].id)
 

def speak(audio):
    engine.say(audio)  
    engine.runAndWait() 

def date():
       year=int(datetime.datetime.now().year)
       month=int(datetime.datetime.now().month) 
       date=int(datetime.datetime.now().day)
       speak("the current date is:")
       print("the current date is:")
       speak(date)
       speak(month)
       speak(year)
       print(date)
       print(month)
       print(year)
def time():
    Time=datetime.datetime.now().strftime("%I:%M:%S")
    speak("The current time is: ")
    print("The current time is: ")
    speak(Time)
    print(Time)
    
def greeting():
     hour = int(datetime.datetime.now().hour)
     if hour>=0 and hour<12:
         speak("Good Morning !")
         print("Good Morning !")
     elif hour>=12 and hour<18:
        speak("Good Afternoon !")
        print("Good Afternoon !")
     else:
       speak("Good Evening !")
       print("Good Evening !")

def wishMe():
     #time()
     #date()
     #greeting()
     speak("Please tell me, how may I help you?")           
def takeCommandCMD():   #run commands by taking text input from the user
    query=input("Please tell me, how may I help you?")
    return query
def takeCommandMic():
    r = sr.Recognizer()  # It takes microphone input from the user and returns string output
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=1)
    
    query = ""  # Default value for query
    
    try:
        print("Recognizing...")  # recognizes audio
        query = r.recognize_google(audio, show_all=False, language="en-IN")
        print(query)  # User query will be printed.
    except Exception as e:
        print("Exception: " + str(e))
    
    return query

def sendwhatsmsg(phone_no,message):
    Message = message
    wb.open('https://web.whatsapp.com/send?phone='+phone_no+'&text='+Message)
    sleep(5)
    pyautogui.press("enter")
def searchgoogle():
    speak("what should i search for ?")
    print("what should i search for ?")
    search=takeCommandMic()
    wb.open('https://www.google.com/search?q='+search)


def news():
    newsapi = NewsApiClient(api_key='cc8781f24d594e9cb00217fd7489a814')
    speak("what topic u need news about?")
    topic=takeCommandMic()
    all_articles = newsapi.get_everything(q=topic,
                                      language='en',
                                      sort_by='relevancy',
                                      page_size=5)
                                  
    
    newsdatas=all_articles['articles']
    for x,y in enumerate(newsdatas):
        print(f'{x} {y["description"]}')
        speak((f'{x} {y["description"]}'))
           
def text2speech(): #reads the selected text
    text=clipboard.paste()
    print(text)    
    speak(text)

def screenshot(): #takes snapshot and store it screenshot folder
   name_img = tt.time()
   name_img=f'C:\\Users\\hp\\Desktop\\project\\screenshot\\{name_img}.png'
   img=pyautogui.screenshot(name_img)
   img.show()
def passwordgen():
    s1=string.ascii_uppercase
    s2=string.ascii_lowercase
    s3=string.digits
    s4=string.punctuation
    passlen=8
    s=[]
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    random.shuffle(s)
    newpass=(" ".join(s[0:passlen]))
    print(newpass)
    speak(newpass)

   
if __name__=="__main__" :
     speak("Welcome , I am Jarvis ")
     time()
     date()
     wishMe()
     while True:
         query=takeCommandCMD().lower()
         #query=takeCommandMic().lower()
         
         if 'time' in query:
             time()
         elif 'date' in query:
             date()
         elif 'message' in query:
             user_name= {
                 'Nishika':'+91 99685 15359'
             }
             try:
                 speak("To whom you want to send the whats app message?")
                 name=takeCommandMic()
                 phone_no=user_name[name]
                 speak("what is the message?")
                 message=takeCommandMic()
                 sendwhatsmsg(phone_no,message)
                 speak("message has been sent successfully")
             except Exception as e:
                 print(e)
                 speak("unable to send the message")
         elif 'wikipedia' in query:
             speak("searching on wikipedia...")
             query=query.replace("wikipedia","")
             result=wikipedia.summary(query,sentences=2)
             print(result)
             speak(result)
         #opens my document
         elif 'open document' in query:
             os.system('explorer C://{}'.format(query.replace('open','')))
         #open VS Code
         elif 'code' in query:
             os.startfile('C:\\Users\\Lenovo\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code\\Visual Studio Code.lnk')
         elif 'search' in query:
             searchgoogle()
         elif 'youtube' in query:
             speak("what should I search for on youtube ?")
             topic= takeCommandMic()
             pywhatkit.playonyt(topic) #whatever the first result it will play that video
         elif'weather' in query:
             
             url=f'https://api.openweathermap.org/data/2.5/weather?q=delhi&units=imperial&appid=bf537d35a9f70a9ef930d942ce29067c'
             res=requests.get(url)
             data=res.json()
             weather=data['weather'] [0] ['main']
             temp=data['main']['temp']
             desp=data['weather'] [0] ['description']
             temp=round((temp-32)*5/9)
             print(weather)
             print(temp)
             print(desp)
             speak(f'climate in delhi is like')
             speak('Temperature is:{} degree celcius'.format(temp))
             speak('weather is: {}'.format(desp))
         elif 'news'in query: 
             news() 
        #read the selected data
         elif 'read' in query:
             text2speech()
         elif 'joke' in query:
             speak(pyjokes.get_joke())
             
         elif 'screenshot' in query:
             screenshot()
         elif 'remember that' in query:
             print("what should I remember?")
             speak("what should I remember?")
             data = takeCommandMic()
             print("You said me to remember that"+data)
             speak("You said me to remember that"+data)
             remember=open('data.txt','w')
             remember.write(data)
             remember.close()
         elif 'do you know anything' in query:
             remember=open('data.txt','r')
             speak("you told me to remember that"+remember.read())
         elif 'password' in query: 
             passwordgen()
         elif 'stop' in query:
             quit()
             

             
          
