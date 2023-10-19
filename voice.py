import speech_recognition as sr
import pyaudio
import sys
from spotify_control import SpotifyControl
import keyboard


global exiting
exiting=False

def exit_script():
    global exiting
    exiting=True
    print("Exiting the script.")
    sys.exit()

try:
    # start listening for voice commands
    play_commands = ['play','pause','resume','stop song','start song','stop','false']
    previous_commands =['previous','last']
    next_commands=['next']
    volumeup_commands=['volume up','volumeup','up']
    volumedown_commands=['volume down','volumedown','down']
    control=SpotifyControl()
    r = sr.Recognizer()
    m= sr.Microphone()
    print("Listening...")
    with m as source:
            r.adjust_for_ambient_noise(source,duration=2) # ambient noise adjust
            keyboard.add_hotkey('ctrl+x', exit_script)
            while exiting == False:  # loop to continuously listen for commands
                try:
                    audio = r.listen(source, phrase_time_limit=3)
                except sr.WaitTimeoutError as e:
                    print(f"Timeout error: {e}")
                    continue  # Continue the loop when a timeout error occurs

                if audio:
                    try:
                        command = r.recognize_google(audio).lower()
                        print(f"You said: {command}")

                        if any(word in command for word in play_commands):
                            control.play_pause()
                        elif any(word in command for word in previous_commands):
                            control.previous()
                        elif any(word in command for word in next_commands):
                            control.next()
                        elif any(word in command for word in volumeup_commands):
                            control.volumeup()
                        elif any(word in command for word in volumedown_commands):
                            control.volumedown()

                    except sr.UnknownValueError:
                        #print("Google Speech Recognition could not understand audio")
                        continue
                    except sr.RequestError as e:
                        print(f"Could not request results from Google Speech Recognition service; {e}")
                        continue
                    except pyaudio.paBadStreamPtr:
                        # Ignore this exception if the program is exiting
                        raise
except Exception as e:
    sys.exit()