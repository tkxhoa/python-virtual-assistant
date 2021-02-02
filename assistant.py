import speech_recognition
import pyttsx3
from datetime import date, datetime

#init
robot_ear = speech_recognition.Recognizer()
robot_mouth = pyttsx3.init()
robot_brain = ""

#listening
while True:
    with speech_recognition.Microphone() as mic:
        print("Robot: I am listening")
        audio = robot_ear.listen(mic)

    try:
        you = robot_ear.recognize_google(audio)
    except:
        you = "You didn't say anything"   

    print("You: " + you)
    print("...")
    #AI
    if you == "":
        robot_brain = "I can't hear you, try again"
    elif "hello" in you:    
        robot_brain = "Hello Kevin Tran"
    elif "today" in you:    
        today = date.today()
        robot_brain = today.strftime("%B %d, %Y")
    elif "time" in you:   
        now = datetime.now() 
        robot_brain = now.strftime("%H hours %M minutes %S seconds")      
    elif "bye" in you: 
        robot_brain = "Goodbye, see you again" 
        print("Robot: " + robot_brain)
        robot_mouth.say(robot_brain)
        robot_mouth.runAndWait()
        break
    else:
        robot_brain = "I'm fine, thank you and you?"    
   
    #speaking
    print("Robot: " + robot_brain)
    robot_mouth.say(robot_brain)
    robot_mouth.runAndWait()