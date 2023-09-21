import Arduino.ArduinoService as arduinoService
import SpotifyAdapter.SpotifyAdapter as SpotifyAdapter


previous_gestures = []
spotifyAdapter = SpotifyAdapter.SpotifyAdapter()



def handle_gestures(gesture_list):
    global previous_gestures
    print(gesture_list, previous_gestures)
    if sorted(previous_gestures) == sorted(gesture_list):
        return
    if "a" in gesture_list and "1" in gesture_list:
        spotifyAdapter.skip_to_next()
    if "a" in gesture_list and "2" in gesture_list:
        spotifyAdapter.skip_to_previous()
    
    previous_gestures = gesture_list
    