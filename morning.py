#+----------------------+
#|   Module Section     |
#+----------------------+
import colorama as color
from datetime import datetime
import subprocess, os, pygame, requests, spotipy, time, threading

pygame.mixer.init() #Initiates Pygame Mixer - Handles Music & Sound
mixer_lock = threading.Lock() #Creates Threading Lock - Synchronizes Access to Shared Resources to Prevent Data Corruption

#+-----------------------------------------+
#|       Program Functions Section         |
#+-----------------------------------------+
def location(): #Location Function Retreives Information about User Location
    try:
        feed = requests.get("https://ipinfo.io") #Sends HTTP GET Request to ipinfo.io endpoint
        data = feed.json() #Parses JSON Response obtained from API
        city = data.get("city", "Unknown") #Retreives Value Associated with key "City" from JSON data, or stores "Unknown" in case of no key available
        country = data.get("country", "Unknown") #Retreives Value Associated with key "Country" from JSON data, or stores "Unknown" in case of no key available
        return f"Location: {city}, {country}" #Constructs & Returns String containing City & Country 
    except Exception as e: print(color.Fore.RED+f"An error occurred: {e}") #Handles Potential Exceptions
def weather(api, city): #Weather Function Retreives Realtime Information about Weather Condtitions around User
    try:
        url = "http://api.openweathermap.org/data/2.5/weather" #Base URL for Open Weather Map API
        #Constructs Dictionary with Parameters for API Requests includes "City", API ID, & Units set to Metric [Can be changed]
        params = {
            'q': city,
            'appid': api,
            'units': 'metric'
        }
        feeding = requests.get(url, params=params) #Send API GET Request to Open Weather Map API
        data = feeding.json() #Parses JSON Response obtained from API
        if 'main' in data and 'weather' in data: #Checks for "main" & "weather" in API Response
            temp = data['main']['temp'] #Extracts Temperature
            weather = data['weather'][0]['description'] #Extracts Weather Description
            return f"{temp}°C, {weather}" #If all information is available, returns string with Temperature & Weather Conditions
        else: return color.Fore.RED+"Weather Information Unable..." #Handles Potential Exceptions  
    except Exception as e: return f"An error occurred: {e}"
def soundon(): #Sound On Function Plays Pre-Specified Song on Spotify
    presong = "Specify Song Here" #Sets Default Song Name to Play on Spotify
    results = spotifyObject.search(presong, 1, 0, "track") #Uses Spotify API, Searches for Specified Song, Parameters specify to Return 1 Result Starting from 1st Result
    songs_dict = results['tracks'] #Extracts "Tracks" dictionary from Search Results
    songitems = songs_dict['items'] #Extracts list of items from "Tracks" Dictionary
    if songitems: #If a song is found;
        selectedrack = songitems[0] #Selects the first song
        songrl = selectedrack['external_urls']['spotify'] #Retreives Spotify URL for selected song
        subprocess.run(["open", "-a", "Spotify", songrl]) #Opens Spotify Application & Plays Song
        print(color.Fore.LIGHTCYAN_EX + 'Music System Online') #Indicator - Music System Online
        time.sleep(10) #Delays Execution by 10 Seconds
    else: print(color.Fore.RED+'Unable to find Song...') #Prints error if no song found
def presoundon(): #Pre Sound On Function Plays Local Audio Indicating the Initiation of Music System
    try:
        soundfile = os.path.join("CPS109Project", "PreSoundOn.wav") #Constructs Path to Sound File with CPS109Assignment Directory
        if not os.path.exists(soundfile): #Checks for Sound File
            raise FileNotFoundError(color.Fore.RED + f"File not found: {soundfile}") #Raises Error if file doesn't exist
        with mixer_lock: #Ensures only 1 Thread can access PyGame Mixer at 1 Point in time, Avoids Potential Conflicts
            pygame.mixer.music.load(soundfile) #Loads Specified Sound File in PyGame Mixer
            pygame.mixer.music.play() #Initiates Playback of Loaded Sound File 
            while pygame.mixer.music.get_busy(): #Enters Loop Until Sound Finishes Playing
                pygame.time.Clock().tick(10) #Pauses Loop Execution for Short Duration avoiding Busy-wait Loop
    except Exception as e: #Handles Errors
        print(color.Fore.RED + f"An error occurred: {e}") #Prints Potential Errors
def set_volume(new_volume): #Set-Volume Function Changes System Volume to Specified Volume
    script = f"set volume output volume {new_volume}" #Constructs AppleScript Designed to Set Output Volume to Specified Volume 
    subprocess.run(["osascript", "-e", script]) #Use Subprocess to Execute AppleScript Command
def news(apikey): #News Function Retreives News Via API
    try:
        url = "https://newsapi.org/v2/top-headlines" #Base URL for News API
        #Constructs Dictionary with Parameters for API Requests includes API Key, Category: "Technology", Page Size "3", & Language "English" [Can be changed]
        params = {
            'apiKey': apikey,
            'category': 'technology',
            'pageSize': 3,
            'language': 'en'
        }
        feedings = requests.get(url, params=params) #Send API GET Request to News API
        data = feedings.json() #Parses JSON Response obtained from API
        if data['status'] == 'ok': #Checks API Response Status for "ok"
            articles = data['articles'] #Extracts List of Articles From Response
            print(color.Fore.GREEN+"Technology News Today:") 
            print("--------------------\n")
            for i, article in enumerate(articles, start=1): #Iterates Over Articles, Prints Titles and URLs
                print(color.Fore.MAGENTA + f"{i}. {article['title']}")
                print(color.Fore.CYAN + f"   URL: {article['url']}")
                print()
        else: print(color.Fore.RED+"News Unavailable at the moment...") #Prints Error for Unavailable News
    except Exception as e: #Handles Error
        print(color.Fore.RED+f"An error occurred: {e}") #Prints Potential Errors
def bac2vscode(windowss): #Back To VSCode Function Shifts Screen Back to VSCode
    try:
        #Constructs AppleScript Code Designed to Interact with System Events & VSCode Application
        applescript_code = f''' 
            tell application "System Events"
                tell process "Code"
                    set frontmost to true
                    if exists (first window whose (title contains "{windowss}" or value of attribute "AXTitle"          contains "{windowss}")) then
                        tell (first window whose (title contains "{windowss}" or value of attribute "AXTitle"           contains "{windowss}"))
                            perform action "AXRaise"
                        end tell
                    end if
                end tell
            end tell
        '''
        subprocess.run(["osascript", "-e", applescript_code], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) #Uses Subprocess to Execute Constructed AppleScript Code using osascript tool
    except subprocess.CalledProcessError as e: #Handles Non-Zero Exit Code Error
        print(color.Fore.RED+f"Error occurred while switching to VSCode: {e}") #Prints Potential Specific Errors
    except Exception as e: #Handles Errors
        print(color.Fore.RED+f"An unexpected error occurred: {e}") #Prints Potential Errors
def presoundon2(): #Pre Sound On 2 Function Plays Local Audio Greeting User
    try:
        soundfile = os.path.join("CPS109Project", "GoodMGreet.wav") #Constructs Path to Sound File with CPS109Assignment Directory
        if not os.path.exists(soundfile): #Checks for Sound File
            raise FileNotFoundError(color.Fore.RED + f"File not found: {soundfile}") #Raises Error if file doesn't exist
        with mixer_lock: #Ensures only 1 Thread can access PyGame Mixer at 1 Point in time, Avoids Potential Conflicts
            pygame.mixer.music.load(soundfile) #Loads Specified Sound File in PyGame Mixer
            pygame.mixer.music.play() #Initiates Playback of Loaded Sound File 
            while pygame.mixer.music.get_busy(): #Enters Loop Until Sound Finishes Playing
                pygame.time.Clock().tick(10) #Pauses Loop Execution for Short Duration avoiding Busy-wait Loop
    except Exception as e: #Handles Errors
        print(color.Fore.RED + f"An error occurred: {e}") #Prints Potential Errors
def fileread(path2file): #File Read Function Reads Text File & Prints its Content
    try:
        with open(path2file, "r") as file: #Attempts to Open Specified by path2file
            content = file.read() #Reads and Stores content of txt File
            print(color.Fore.MAGENTA+"Top Priority Tasks for Today:")
            print("--------------------")
            print(color.Fore.CYAN+content)
            print("--------------------")
            try:
                import os
                os.remove(path2file) #Attempts to Remove File After Successfully Reading & Printing it
            except Exception as e: #Handles Errors
                print(color.Fore.RED+f"Error deleting file: {e}") #Prints Potential Errors
    except FileNotFoundError: #Handles File Unavailable Error
        print(color.Fore.RED+f"No Priorities Set for Today...") #Prints Potential File Errors
        return #Exits Function after Handling Exception
    except Exception as e: #Handles Errors
        print(color.Fore.RED+f"Error deleting file: {e}") #Prints Potential Errors

#+-----------------------------------------+
#|     API Keys & Path Defining Section    |
#+-----------------------------------------+

username = "Specify Spotify Username" #Spotify Username
clientID = 'Enter ClientID from Spotify Developer Dashboard' #Spotify Developer Client ID
clientSecret = 'Enter Client Secret from Spotify Developer Dashboard' #Spotify Developer Client Secret
redirect_uri = 'http://google.com/callback/' #Redirect URL for Authorisation
api = "Enter openweathermap.org API Key" #OpenWeatherMap API Key
newsapi = 'Enter newsapi.org API Key' #News API Key
path2file = "CPS109Project/priority.txt" #Priority Tasks TXT File Address

#+-----------------------------------------+
#|      Main Program Execution Section     |
#+-----------------------------------------+
try:
    oauthobj = spotipy.SpotifyOAuth(clientID, clientSecret, redirect_uri, scope='user-library-read') #Sets Up Spotify Authorisation
    tokenfo = oauthobj.get_access_token(as_dict=False) #Retreives Access Token from Spotify OAuth object
    token = tokenfo 
    spotifyObject = spotipy.Spotify(auth=token) #Creates Spotify Object using Retreived Token
    usern = spotifyObject.current_user() #Gets User Information about Current Spotify User

    #Setting Up Variables
    city = "Specify City Location" #Change Location According to User Preferrences
    currenttime = datetime.now()
    locationfo = location()
    weatherfo = weather(api, city)
    currentimeco = currenttime.strftime("%H:%M:%S")

    window = "Specify VSCode Window Title [Window Title to Switch to]"
    presoundon2()
    print(color.Back.BLACK + color.Fore.GREEN + "Current Time: " + currentimeco + (" " * 64) + locationfo)
    print(color.Back.BLACK + color.Fore.GREEN + weatherfo)
    print("--------------------\n")


    prevol = 50 #Set Volume
    set_volume(prevol)
    music_thread = threading.Thread(target=presoundon)
    time.sleep(5)
    music_thread.start()
    music_thread.join()
    soundon()
    print("--------------------\n")

    fileread(path2file)
    bac2vscode(window)
    print("--------------------\n")
    news(newsapi)
except spotipy.SpotifyException as e: #Handles Error
    print(f"Spotify Exception: {e}") #Prints Potential Errors