# CPS 109 Assignment - ProductiPy
**Author:** Divjot Singh

## Assignment Problem Statement:

In the dynamic world of programming, professionals grapple with the challenge of efficiently sourcing diverse, critical information. The absence of a centralized platform results in fragmented workflows, impeding seamless access to updates and industry insights. To address this, a solution is proposed: integrating various APIs into a unified terminal interface.

This consolidated platform streamlines information retrieval, providing a comprehensive overview in a single window. Furthermore, a night program enables users to note and prioritize tasks, enhancing morning planning.

By offering a comprehensive solution, this system aims to empower programmers with an efficient, organized workflow, fostering productivity and informed decision-making throughout their workday. The challenge is to develop a unified platform that seamlessly integrates multiple APIs, catering to the nuanced needs of programming professionals.

## Pre-Requisites:

- Apple MacOS Operating System
- Spotify Application
- Microsoft Visual Studio Code Application

## Base Structure:

The entire assignment is mainly comprised of 3 Python Files [1 Parent Files, 2 Child Files], 4 Locally stored audio files [.wav format], a README file, and a `requirements.txt` file [helps initiate virtual environment].

- **Parent File (`cps109_a1.py`):**
  This is the main file responsible for initiating the entire program. This file further branches into night and morning programs based on user response. This file has 2 main functionalities: Speech Recognition & New Window Initiation.

- **Child File (`morning.py`):**
  This is the program file for the morning. It has multiple interactions with various APIs to retrieve location, weather, time, sound, etc., information and further processes it into one unified terminal window. This file also has functions defined to play certain voices with correspondence to the processes to enhance user experience and make systems comprehensive to the user. Additionally, this program reads into a pre-specified file to extract priority tasks for the user, making their day more comprehensive. Various API Keys and Private Keys are to be first loaded into the file's dedicated variables for the file to work properly without errors.

- **Child File (`night.py`):**
  This is the program file for the night. Included in this file are 3 essential functions: speech recognition, file writing & creation, and playing sounds just like `morning.py`. The main work of this program is to provide a good transition to rest for the user while also ensuring a good start to the next day by asking the user for priority tasks that set the target for tomorrow.

- **Locally Stored Audio Files:**
  These files were created via genny.lovo.ai website to bring in an audio element to the program, making it more efficient than rudimentary reading interpretation. These audio files make the program work seamlessly and enhance user experience.

- **Configuration File (`requirements.txt`):**
  This is a .txt file that helps users install pre-requisite modules with their compatible versions to avoid potential module errors and provide a seamless experience within a virtual environment.

## Unsettled Variables:
These are the list of variables in all three python files that require configuration prior to running the program. They are:

**File: `morning.py`**
**Function - soundon()**
1. `presong`

**Spotify Developer Private Information Containers:**
1. `username`
2. `ClientID`
3. `clientSecret`

**Open Weather Map Information Container:**
1. `api`

**News API Information Container:**
1. `newsapi`

**Main Execution Section:**
1. `city`
2. `window`
3. `prevol` (default is set to 50% volume)

## Dependencies:
Please check `requirements.txt` file. This program is to be run in a virtual environment with `requirements.txt` dependencies installed.
