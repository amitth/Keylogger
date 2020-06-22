from pynput.keyboard import Key, Listener

def On_Press(key):
    print(key)

def On_Release(key):
    if key == Key.esc:
        return False

with Listener(on_press=On_Press, on_release=On_Release) as listener:
    listener.join()
