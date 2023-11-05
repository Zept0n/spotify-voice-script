# Spotify Voice Control

In order to control Spotify with voice commands using the Spotify API you will need Spotify Premium, this project allows you basic control of Spotify with voice commands by sending key combinations to the Spotify Desktop application without Spotify Premium.
It uses the `speech_recognition` and `pyaudio` libraries to recognize voice commands and the `pywinauto` and `pygetwindow` libraries to control Spotify.

## Installation

This project uses pipenv for dependency management. If you don't have pipenv installed, you can install it with pip:

```bash
pip install pipenv
```

Then, you can install the project dependencies with:

```bash
pipenv install
```

This will create a virtual environment and install the dependencies specified in the Pipfile.

Now you're ready to run the project within the pipenv shell:

```bash
pipenv run pythonw run_hidden.py
```

## Usage

To use this project, run the `Spotify Control.bat` file. This will start the voice recognition script in the background. You can then use the following voice commands to control Spotify:

- "play", "pause", "resume", "stop song", "start song", "stop", "start", to play or pause the current song.
- "previous", "last" to go to the previous song.
- "next" to go to the next song.
- "volume up", "volumeup", "up" to increase the volume.
- "volume down", "volumedown", "down" to decrease the volume.

## License
This project is licensed under the terms of the MIT license.
