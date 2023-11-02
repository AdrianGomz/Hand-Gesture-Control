import Arduino.ArduinoService as ArduinoService
import SpotifyAdapter.SpotifyAdapter as SpotifyAdapter


previous_gestures = []
spotifyAdapter = SpotifyAdapter.SpotifyAdapter()



def handle_gestures(gesture_list):
    global previous_gestures
    # print(gesture_list, previous_gestures)
    if sorted(previous_gestures) == sorted(gesture_list):
        return
    # Arduino leds
    if "L" in gesture_list and "1" in gesture_list:
        ArduinoService.toggle_digital_out(2)
    if "L" in gesture_list and "2" in gesture_list:
        ArduinoService.toggle_digital_out(3)
    if "L" in gesture_list and "3" in gesture_list:
        ArduinoService.toggle_digital_out(4)
   
    # Arduiono vent
    if "B" in gesture_list and "1" in gesture_list:
        ArduinoService.toggle_digital_out(5)
    if "B" in gesture_list and "2" in gesture_list:
        ArduinoService.toggle_digital_out(6)
    
    # Spotify
    if "C" in gesture_list and "1" in gesture_list:
        spotifyAdapter.skip_to_next()
    if "C" in gesture_list and "2" in gesture_list:
        spotifyAdapter.skip_to_previous()
    if "C" in gesture_list and "3" in gesture_list:
        spotifyAdapter.toggle_pause_play()
    
    previous_gestures = gesture_list
    