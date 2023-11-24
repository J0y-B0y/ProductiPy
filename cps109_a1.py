#+-----------------------------+
#|      Program Statement      |
#+-----------------------------+

#In the dynamic world of programming, professionals grapple with the challenge of efficiently sourcing diverse, critical information. The absence of a centralized platform results in fragmented workflows, impeding seamless access to updates and industry insights. To address this, a solution is proposed: integrating various APIs into a unified terminal interface.

#This consolidated platform streamlines information retrieval, providing a comprehensive overview in a single window. Furthermore, a night program enables users to note and prioritize tasks, enhancing morning planning.

#By offering a comprehensive solution, this system aims to empower programmers with an efficient, organized workflow, fostering productivity and informed decision-making throughout their workday. The challenge is to develop a unified platform that seamlessly integrates multiple APIs, catering to the nuanced needs of programming professionals.

#+----------------------+
#|   Module Section     |
#+----------------------+
import speech_recognition as sr
import subprocess, time, os, colorama, math, random
import colorama as color
from tqdm import tqdm, trange

sound_playing = False #Variable sound_playing set default to False

#+-----------------------------------------+
#|       Program Functions Section         |
#+-----------------------------------------+
def newwinmor(script_dir): #Opens Up Fresh VSCode Window & Initiates Morning Program
    global sound_playing #Global Variable sound_playing is used to control flow of function
    try:
        while sound_playing: time.sleep(20)  #Waits for sound to finish
        code_path = os.path.join(script_dir, "CPS109Project/morning.py")
        subprocess.run(["clear"]) #Clears the Console
        subprocess.run(["python", code_path]) #Runs Morning File
    except Exception as e: print(f"An error occurred while opening VSCode sub-terminal: {e}") #Handles Exception
def newwinnight(script_dir): #Opens Up Fresh VSCode Window & Initiates Night Program
    global sound_playing #Global Variable sound_playing is used to control flow of function
    try:
        while sound_playing: time.sleep(20) #Waits for sound to finish
        code_path = os.path.join(script_dir, "CPS109Project/night.py") 
        subprocess.run(["clear"]) #Clears the Console
        subprocess.run(["python", code_path]) #Runs Morning File
    except Exception as e: print(f"An error occurred while opening VSCode sub-terminal: {e}") #Handles Exception
def smartlisten(): #Speech Recognition Function for Mode Selection
    recognizer = sr.Recognizer()
    waking = False #Variable is initiated to detect specific phrases & Prevents repititive recognition
    while True: #Initiating Loop - Listening in...
        with sr.Microphone() as source: #Initiates Microphone Instance
            print(colorama.Fore.MAGENTA+"Listening In... ")
            recognizer.adjust_for_ambient_noise(source) #Adjusts Ambient Noise
            audio = recognizer.listen(source, timeout=None) #Captures Audio
        try:
            text = recognizer.recognize_google(audio).lower() #Audio is passed through Google's Speech Recognition service, converted to lowercase and stored in variable text
            if "good morning" in text and not waking: #Checks for "Good Morning" in audio
                print(colorama.Fore.YELLOW+"Good Morning detected!") #Confirms Successful Detection on Terminal Window
                with trange(22, miniters=5) as ran: #Initialises tqdm range 
                    for i in ran:
                        ran.set_description(color.Fore.YELLOW+f"Systems Running {i+1}") #Update Description of Progress Bar - Indicates Current State
                        processing = random.randint(1, 100) / 100 #Simulates Processing - Generates Random Value
                        time.sleep(processing) #Simulate Processing Time - Sleeps for Calculated Time
                waking = True #Sets waking to True
                return "morning" #Returns function with "morning"
            elif "good night" in text and not waking: #Checks for "Good Night" in audio
                print(colorama.Fore.CYAN+"Good Night detected!") #Confirms Successful Detection on Terminal Window
                with trange(22, miniters=5) as ran: #Initialises tqdm range 
                    for i in ran:
                        ran.set_description(color.Fore.CYAN+f"Systems Running {i+1}") #Update Description of Progress Bar - Indicates Current State
                        processing = random.randint(1, 100) / 100 #Simulates Processing - Generates Random Value
                        time.sleep(processing) #Simulate Processing Time - Sleeps for Calculated Time
                waking = True #Sets waking to True
                return "night" #Returns function with "morning"
        except sr.UnknownValueError: #Handles Speech Recognition Error
            print(colorama.Fore.RED+"Speech Recognition could not understand audio.") #Confirms Error on Terminal
            return None #Returns function with None
        except sr.RequestError as e: #Handles Google Service Request Error
            print(f"Could not request results from Google Speech Recognition service; {e}") #Confirms Error on Terminal
            return None #Returns function with None
        waking = False #Waking remains false if no interpretable phrase is passed through

#+-----------------------------------------+
#|      Main Program Execution Section     |
#+-----------------------------------------+
if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath("Enter absolute path of directory: CPS109Project")) #Obtains absolute path of the directory containing the script
    morning_script_path = os.path.join(script_dir, "CPS109Project/morning.py") #Concatenate Main Script Path to Morning Program File
    night_script_path = os.path.join(script_dir, "CPS109Project/night.py") #Concatenate Main Script Path to Night Program File
    scenario = smartlisten() #Smarlisten Function is called and it's return value is stored in scenario i.e Morning/Night
    if scenario == "morning": newwinmor(script_dir) #If scenario is Morning, Morning Program is executed over Fresh VSCode Window 
    elif scenario == "night": newwinnight(script_dir) #If scenario is Morning, Morning Program is executed over Fresh VSCode Window 
    else: print("No action taken...") #Prints if scenario is none of the above