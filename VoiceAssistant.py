import datetime
import random
import webbrowser
import time
import os
import playsound
from gtts import gTTS
import speech_recognition as sr

recon = sr.Recognizer()
class voice_assistant:
    def __init__(self, user_name='',name='Jarvis'):
        self.name = name
        self.user_name = user_name

    def sofia_speak(self, audio_string):
        tts = gTTS(text=audio_string, lang='en')
        audio_file = 'audio-' + str(random.randint(1, 1000000))
        tts.save(audio_file)
        playsound.playsound(audio_file)
        os.remove(audio_file)


    def record_voice(self, text=False):
        if text:
            self.sofia_speak(text)
        with sr.Microphone() as source:
            source = recon.listen(source)
            try:
                audio = recon.recognize_google(source)
            except sr.UnknownValueError:
                audio = ''
                self.sofia_speak('Sorry I didn´t get that')
            return audio

    def respond(self, audio):
        if audio == "hola" or audio == 'hi' or audio == 'hello':
            self.sofia_speak('Nice to meet you')
        elif 'date' in audio:
            self.sofia_speak(datetime.date.today())
        elif 'what is your name' == audio:
            user= voice_assistant()
            self.sofia_speak(user.name)
        elif 'search' in audio:
            search = self.record_voice('What do you want to search?')
            url = 'https://www.google.com/search?q=' + search
            webbrowser.get().open(url)
            self.sofia_speak('Here is what I found!')
        elif 'location' in audio:
            search = self.record_voice('What location do you want to look for?')
            url = 'https://google.nl/maps/place/' + search + '/&amp;'
            webbrowser.get().open(url)
            self.sofia_speak('Here is what I found!')
        elif 'my name' in audio:
            if self.user_name == '':
                self.user_name = self.record_voice('What is your name?')
            self.sofia_speak('Your name is' + self.user_name)
        elif 'exit' in audio:
            self.sofia_speak('Ok, see you later')
            exit()
        else:
            self.sofia_speak('Try again')


time.sleep(1)
assistant = voice_assistant()
assistant.sofia_speak("Hi, what can I help you with?")
while 1:
    assistant.respond(assistant.record_voice())
    assistant.sofia_speak('Ready for next comand')
