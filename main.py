import time
from pynput.mouse import Controller
from pynput.keyboard import Listener, KeyCode

mouse = Controller()
TOGGLE_KEY = KeyCode.from_vk(118) # F7
is_moving = False

def on_press(key):
    global is_moving
    if key == TOGGLE_KEY:
        is_moving = True

def on_release(key):
    global is_moving
    if key == TOGGLE_KEY:
        is_moving = False

listener = Listener(on_press=on_press, on_release=on_release)
listener.start()

print("Максимальная скорость активирована. Зажмите F7.")

try:
    while True:
        if is_moving:
            # Увеличили шаг до 20 пикселей и убрали sleep
            mouse.move(20, 0)
        else:
            # Спим только когда кнопка НЕ нажата, чтобы не грузить CPU
            time.sleep(0.01)
except KeyboardInterrupt:
    pass
