from pywinauto import application
import psutil

def play_pause_spotify():
    try:
        # Get a list of all Spotify processes
        spotify_processes = [p for p in psutil.process_iter(['pid', 'name']) if p.info['name'] == 'Spotify.exe']
        # Sort the processes by PID in descending order and get the PID of the first process
        main_spotify_pid = sorted(spotify_processes, key=lambda p: p.info['pid'], reverse=True)[0].info['pid']
        # Connect to the main Spotify process
        app = application.Application().connect(process=main_spotify_pid)

        # Get a reference to the Spotify window
        spotify = app.top_window()

        # Simulate the space key press
        spotify.type_keys('{SPACE}')
    except Exception as e:
        print("Error occurred:", str(e))

play_pause_spotify()