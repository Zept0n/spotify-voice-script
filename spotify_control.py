from pywinauto import Application
import pygetwindow as gw
import psutil

class SpotifyControl:
    def __init__(self):
        try:
            # Get a list of all Spotify processes
            spotify_processes = [p for p in psutil.process_iter(['pid', 'name']) if p.info['name'] == 'Spotify.exe']
            # Sort the processes by PID in descending order and get the PID of the first process
            self.main_spotify_pid = sorted(spotify_processes, key=lambda p: p.info['pid'], reverse=True)[0].info['pid']
        except Exception as e:
            print("Error occurred - Spotify process not found:", str(e))
    def spotify_keystroke(self,keystroke):
        try:
            
            # Get current foreground window
            active_window = gw.getActiveWindow()

            # Connect to the main Spotify process
            app = Application().connect(process=self.main_spotify_pid)

            # Get a reference to the Spotify window
            spotify = app.top_window()

            # Minimize the Spotify window
            #spotify.minimize()
            # Simulate key press
            if keystroke=='^{LEFT}':
                spotify.send_keystrokes(keystroke)
                spotify.send_keystrokes(keystroke)
            elif keystroke=='^{UP}' or keystroke=='^{DOWN}':
                spotify.send_keystrokes(keystroke)
                spotify.send_keystrokes(keystroke)
                spotify.send_keystrokes(keystroke)
                spotify.send_keystrokes(keystroke)
            else:
                spotify.send_keystrokes(keystroke)
            # Return to last foreground window
            active_window.activate()

        except Exception as e:
            print("Error occurred:", str(e))

    def play_pause(self):
        self.spotify_keystroke("{SPACE}")
    def next(self):
        self.spotify_keystroke('^{RIGHT}')
    def previous(self):
        self.spotify_keystroke('^{LEFT}')
    def volumeup(self):
        self.spotify_keystroke('^{UP}')
    def volumedown(self):
        self.spotify_keystroke('^{DOWN}')

control=SpotifyControl()
control.play_pause()