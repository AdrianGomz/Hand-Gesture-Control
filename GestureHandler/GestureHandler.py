# import Arduino.ArduinoService as ArduinoService
import SpotifyAdapter.SpotifyAdapter as SpotifyAdapter
import requests

previous_gestures = []
spotifyAdapter = SpotifyAdapter.SpotifyAdapter()
esp8266_port = "http://192.168.81.204"


def handle_gestures(gesture_list):
    if len(gesture_list) == 0:
        gesture_set = frozenset(["empty"])
    else:
        gesture_set = frozenset(gesture_list)
    global previous_gestures
    print(gesture_list, previous_gestures)
    
    previous_gestures.append(gesture_set)
    out = None
    if len(previous_gestures)<3:
        return
    if len(previous_gestures) > 3:
            out = previous_gestures.pop(0)

    if len(set(previous_gestures))>1:
        return
    
    if frozenset(gesture_list)==out:
        return
    # Arduino leds
    if "L" in gesture_list and "1" in gesture_list:
        requests.get(esp8266_port+"/light?num=1")
        # ArduinoService.toggle_digital_out(2)
    if "L" in gesture_list and "2" in gesture_list:
        # ArduinoService.toggle_digital_out(3)
        requests.get(esp8266_port+"/light?num=2")
    if "L" in gesture_list and "3" in gesture_list:
        # ArduinoService.toggle_digital_out(4)
        requests.get(esp8266_port+"/light?num=3")
   
    # Arduiono vent
    if "A" in gesture_list and "1" in gesture_list:
        # ArduinoService.toggle_digital_out(5)
        requests.get(esp8266_port+"/fan?num=1")
    if "A" in gesture_list and "2" in gesture_list:
        # ArduinoService.toggle_digital_out(6)
        requests.get(esp8266_port+"/fan?num=2")
    
    # Spotify
    if "C" in gesture_list and "1" in gesture_list:
        spotifyAdapter.skip_to_next()
    if "C" in gesture_list and "2" in gesture_list:
        spotifyAdapter.skip_to_previous()
    if "C" in gesture_list and "3" in gesture_list:
        spotifyAdapter.toggle_pause_play()
    
    
    if len(previous_gestures) > 3:
        previous_gestures.pop(0)
    