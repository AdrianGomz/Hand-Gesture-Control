# import Arduino.ArduinoService as ArduinoService
import SpotifyAdapter.SpotifyAdapter as SpotifyAdapter
import requests

previous_gestures = []
spotifyAdapter = SpotifyAdapter.SpotifyAdapter()
esp8266_port = "192.168.204"


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
        try:
            requests.get(esp8266_port+"/light?num=1")
        except:
            pass
        # ArduinoService.toggle_digital_out(2)
    if "L" in gesture_list and "2" in gesture_list:
        # ArduinoService.toggle_digital_out(3)
        try:
            requests.get(esp8266_port+"/light?num=2")
        except:
            pass
    if "L" in gesture_list and "3" in gesture_list:
        # ArduinoService.toggle_digital_out(4)
        try:
            requests.get(esp8266_port+"/light?num=3")
        except:
            pass

    # Arduiono vent
    if "A" in gesture_list and "1" in gesture_list:
        # ArduinoService.toggle_digital_out(5)
        try:
            requests.get(esp8266_port+"/fan?num=1")
        except:
            pass
    if "A" in gesture_list and "2" in gesture_list:
        # ArduinoService.toggle_digital_out(6)
        try:
            requests.get(esp8266_port+"/fan?num=2")
        except:
            pass
    
    # Spotify
    if "C" in gesture_list and "1" in gesture_list:
        spotifyAdapter.skip_to_next()
    if "C" in gesture_list and "2" in gesture_list:
        spotifyAdapter.skip_to_previous()
    if "C" in gesture_list and "3" in gesture_list:
        spotifyAdapter.toggle_pause_play()
    
    
    if len(previous_gestures) > 3:
        previous_gestures.pop(0)
    