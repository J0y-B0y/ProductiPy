#+----------------------+
#|   Module Section     |
#+----------------------+
import colorama as color
import speech_recognition as sr, os, pygame, threading

pygame.mixer.init() #Initiates Pygame Mixer - Handles Music & Sound
mixer_lock = threading.Lock() #Creates Threading Lock - Synchronizes Access to Shared Resources to Prevent Data Corruption.

#+-----------------------------------------+
#|       Program Functions Section         |
#+-----------------------------------------+
def prenight1(): #Pre Night 1 Function Plays Local Audio Greeting User before Sleep
    try:
        soundfile = os.path.join("CPS109Project", "GoodNFinally.wav") #Constructs Path to Sound File with CPS109Assignment Directory
        if not os.path.exists(soundfile): #Checks for Sound File
            raise FileNotFoundError(color.Fore.RED + f"File not found: {soundfile}") #Raises Error if file doesn't exist
        with mixer_lock: #Ensures only 1 Thread can access PyGame Mixer at 1 Point in time, Avoids Potential Conflicts
            pygame.mixer.music.load(soundfile) #Loads Specified Sound File in PyGame Mixer
            pygame.mixer.music.play() #Initiates Playback of Loaded Sound File 
            while pygame.mixer.music.get_busy(): #Enters Loop Until Sound Finishes Playing
                pygame.time.Clock().tick(10) #Pauses Loop Execution for Short Duration avoiding Busy-wait Loop
    except Exception as e: #Handles Errors
        print(color.Fore.RED + f"An error occurred: {e}") #Prints Potential Errors
def prenight2(): #Pre Night 2 Function Plays Local Audio Querying for Priority Tasks
    try:
        soundfile = os.path.join("CPS109Project", "PriorityNight.wav") #Constructs Path to Sound File with CPS109Assignment Directory
        if not os.path.exists(soundfile): #Checks for Sound File
            raise FileNotFoundError(color.Fore.RED + f"File not found: {soundfile}") #Raises Error if file doesn't exist
        with mixer_lock: #Ensures only 1 Thread can access PyGame Mixer at 1 Point in time, Avoids Potential Conflicts
            pygame.mixer.music.load(soundfile) #Loads Specified Sound File in PyGame Mixer
            pygame.mixer.music.play() #Initiates Playback of Loaded Sound File
            while pygame.mixer.music.get_busy(): #Enters Loop Until Sound Finishes Playing
                pygame.time.Clock().tick(10) #Pauses Loop Execution for Short Duration avoiding Busy-wait Loop
    except Exception as e: #Handles Errors
        print(color.Fore.RED + f"An error occurred: {e}") #Prints Potential Errors
def smartlisten(): #Speech Recognition Function for Task Utility
    recognizer = sr.Recognizer()
    while True: #Initiating Loop - Listening in...
        with sr.Microphone() as source: #Initiates Microphone Instance
            print(color.Fore.CYAN+"Listening In... ")
            recognizer.adjust_for_ambient_noise(source) #Adjusts Ambient Noise
            audio = recognizer.listen(source, timeout=None) #Captures Audio
        try:
            text = recognizer.recognize_google(audio).lower() #Audio is passed through Google's Speech Recognition service, converted to lowercase and stored in variable text
            if "yes" in text: #Checks for "Yes" in audio
                print(color.Fore.GREEN+"Please go ahead and enter all the priorities for tomorrow;") #Confirms Successful Detection on Terminal Window
                writedown() #Initiates Writing Process to a new TXT File
                break
            elif "no" in text: #Checks for "No" in audio
                print(color.Fore.RED+"No Priorities Set") #Confirms Successful Detection on Terminal Window
                break
        except sr.UnknownValueError: #Handles Speech Recognition Error
            print(color.Fore.RED+"Speech Recognition could not understand audio.") #Confirms Error on Terminal
            return None #Returns function with None
        except sr.RequestError as e: #Handles Google Service Request Error
            print(color.Fore.RED+f"Could not request results from Google Speech Recognition service; {e}") #Confirms Error on Terminal
            return None #Returns function with None
def writedown(): #Write Down Function Inputs Priority Tasks & Writes to New File
    tasks = [] #Initialises New List for User Input Tasks
    for i in range(3): #Loops 3 Times to Request Task Information
        task = input(color.Fore.GREEN+f"Enter task {i+1}: ") #Obtains User Input
        tasks.append(f"[{i+1}]: "+task) #Appends Each Task to the Main List
    with open("CPS109Project/priority.txt", "w") as file: #Attempts to Write to Specified File
        for task in tasks: #Iterating Through List of Tasks
            file.write(task + "\n") #Writing Each Task to New Line in File followed by New Line

#+-----------------------------------------+
#|      Main Program Execution Section     |
#+-----------------------------------------+
prenight2()
smartlisten()
prenight1()
print("Good Night!")
print("-----------")