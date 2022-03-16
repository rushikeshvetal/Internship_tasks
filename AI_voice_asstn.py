import os
import playsound, pyttsx3, wikipedia, webbrowser
import time, subprocess, datetime
import speech_recognition as sr
from gtts import gTTS

shut='shut'
remember = ['write','remember','note', 'create']
chrome = 'C:/Program Files (x86)/Google %s'
yutube_query = 'https://www.youtube.com/results?search_query='
vs_code = 'C:\\Users\\Anish\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'

def note(text):
    date = datetime.datetime.now()
    filename = str(date).replace(':','-') + '-note.txt'
    with open(filename, 'w') as f:
        f.write(text)
    sublime_path = 'C:\Program Files\Sublime Text 3\sublime_text.exe'
    subprocess.Popen(['notepad.exe', filename])

def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.say(text)
    #engine.save_to_file('C:\Users\Anish\Desktop\pygame\small projects', 'test.mp3')
    engine.runAndWait()

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.energy_threshold = 250
        audio = r.listen(source)
        said = ''
        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print('Not Working')
    return said

def record(speaker):
    pass

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 4:speak('Good Evening sir, you are working nighthours again!')
    elif hour >= 4 and hour < 12:speak('Good Morning sir, have a good work today!')
    elif hour >= 12 and hour < 16:speak('Good Afternoon sir, half the day is almost over!')
    else:
        speak("Good Evening sir, i hope you will complete your today's schedule!")
    speak("How can i help you sir!")




speak('Im Working!')
while True:
    try:
        data = get_audio()
        #writing text
        for i in remember:
            if i in data:
                print('listening.....')
                speak('listening you')
                data = get_audio()
                note(data)
                speak('It is done!')
                data=''
                break
        #closing bot
        if 'shut' in data or 'close' in data:
            speak('see you soon sir!')
            break
        #wake up greetings
        elif 'wake' in data or 'start' in data or 'hello' in data or 'hi' in data or 'hey' in data:
            wishMe()
        #clear
        elif 'clear' in data:
             data = ''
             speak('Commands cleared')
        #wikipedia
        elif 'Wikipedia' in data:
            print('Searching')
            speak('Searching wikipedia..')
            data = data.replace("wikipedia", "")
            results = wikipedia.summary(data, sentences=2)
            speak('wikipedia says')
            speak(results)
        #youtube
        elif 'YouTube' in data:
            speak('Opening youtube!')
            webbrowser.get(chrome).open("https://youtube.com")
        #Google
        elif 'Google' in data:
            speak('Opening google!')
            webbrowser.get(chrome).open("https://google.com")
        #searching
        elif 'search' in data:
            print('Searching...')
            speak('Searching on youtube..')
            data = data.replace("search", "")
            print(data)
            webbrowser.get(chrome).open(yutube_query+data)
        #holding
        elif 'hold' in data:
            print('holding..')
            speak('On hold!')
            #time.sleep(180)
            while True:
                try:
                    data = get_audio()
                    if 'start' in data or 'restart' in data:break
                except:print('Not getting!')
        #time
        elif 'time' in data:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
        #code editor
        elif 'open' in data and 'code' in data:
            speak('Running vs code')
            os.startfile(vs_code)
        time.sleep(2)
        speak('waiting!')
    except:speak('can you speak again sir!')


