import pyfirmata

ard=pyfirmata.Arduino("COM5")
pin_states = {1:0,2:0,3:0,4:0,5:0}


def toggle_digital_out(pin):
    ard.digital[pin].write(pin_states[pin]^1)
    pin_states[pin]^=1
