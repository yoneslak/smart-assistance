import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import wikipedia
import os

# Initialize the text-to-speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# Define a function to speak text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Define a function to take user input
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 0.7
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print("You said:", query)
            return query
        except Exception as e:
            print(e)
            print("Say that again, please.")
            return None

# Define a function to tell the current day
def tell_day():
    day = datetime.datetime.today().weekday() + 1
    day_dict = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday', 7: 'Sunday'}
    if day in day_dict:
        day_of_the_week = day_dict[day]
        print(day_of_the_week)
        speak("Today is " + day_of_the_week)

# Define a function to tell the current time
def tell_time():
    time = str(datetime.datetime.now())
    print(time)
    hour = time[11:13]
    minute = time[14:16]
    speak("The time is " + hour + " hours and " + minute + " minutes")

# Define a function to greet the user
def greet():
    speak("Hello! I'm your yunus intelligence. How can I help you today?")

# Define a function to handle user queries
def handle_query():
    greet()
    while True:
        query = take_command()
        if query is None:
            continue

        query = query.lower()  # Move the lower() call here

        if "open geeksforgeeks" in query:
            speak("Opening GeeksforGeeks...")
            webbrowser.open("www.geeksforgeeks.com")
        elif "open google" in query:
            speak("Open Google...")
            webbrowser.open("www.google.com")
        elif "what day is it" in query:
            tell_day()
        elif "what time is it" in query:
            tell_time()
        elif "bye" in query:
            speak("Goodbye! Check out GeeksforGeeks for more exciting things.")
            break
        elif "from wikipedia" in query:
            speak("Checking Wikipedia...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=4)
            speak("According to Wikipedia, " + result)
        elif "what's your name" in query:
            speak("I'm Jarvis, your desktop assistant.")

if __name__ == "__main__":
    handle_query()
#کد یک دستیار هوشمند