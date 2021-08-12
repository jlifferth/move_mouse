import pyautogui
from datetime import datetime
import time


def infinite_jiggle():
    displacement = -4
    while True:
        if displacement == -4:
            print('move mouse left')
        else:
            print('move mouse right')
        pyautogui.moveRel(displacement, 0)
        displacement = displacement * -1
        counter = 10
        while counter > 0:
            print('move will move again in {} seconds'.format(counter))
            counter -= 1
            time.sleep(1)
        # time.sleep(100)


def set_count_jiggle(cycles):
    i = 0
    while i < cycles:
        print(datetime.now())
        print('move mouse right')
        pyautogui.moveRel(50, 0)
        print('sleep 1 secs')
        time.sleep(1)
        print('move mouse left')
        pyautogui.moveRel(-50, 0)
        print('sleep 1 secs')
        time.sleep(1)
        i += 1
    print('cycles done')


# rounds = 10000
# set_count_jiggle(rounds)
infinite_jiggle()
