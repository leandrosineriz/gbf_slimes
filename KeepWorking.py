import time
import pyautogui

k = 1
#x = 0
while True:
    if k == 1:
        #first summon
        if pyautogui.pixelMatchesColor(309, 462, (55, 44, 39)):
            pyautogui.click(309, 462)
            k += 1
    elif k == 2:
        #button ok - summon
        if pyautogui.pixelMatchesColor(383, 791, (82, 125, 138)):
            pyautogui.click(383, 791)
            k += 1
    elif k == 3:
        #gran or refill
        if pyautogui.pixelMatchesColor(108, 610, (150, 103, 76)):
            time.sleep(1)
            pyautogui.click(108, 610)
            k += 1
        elif pyautogui.pixelMatchesColor(159, 755, (63, 110, 127)):
            pyautogui.click(159, 755)
        elif pyautogui.pixelMatchesColor(284, 713, (66, 114, 132)):
            pyautogui.click(284, 713)
    elif k == 4:
        #gran hability
        if pyautogui.pixelMatchesColor(199, 693, (255, 255, 166)):
            pyautogui.click(199, 693)
            k += 1
            time.sleep(1)
    elif k == 5:
        #granblue bookmark
        if pyautogui.pixelMatchesColor(26, 78, (220, 113, 95)):
            pyautogui.click(26, 78)
            k += 1
    elif k == 6:
        #saraza
        if pyautogui.pixelMatchesColor(374, 628, (190, 185, 176)):
            time.sleep(2)
            pyautogui.click(374, 628)
            k += 1
    elif k == 7:
        #saraza hability
        if pyautogui.pixelMatchesColor(392, 712, (230, 49, 255)):
            pyautogui.click(392, 712)
            k += 1
            time.sleep(1)
    elif k == 8:
        #reload
        pyautogui.press('f5')
        k += 1
    elif k == 9:
        #granblue bookmark
        if pyautogui.pixelMatchesColor(237, 606, (46, 79, 94)):
            if pyautogui.pixelMatchesColor(26, 78, (220, 113, 95)):
                pyautogui.click(26, 78)
                k = 1   
    """    
    print(pyautogui.position())
    print(pyautogui.screenshot().getpixel(pyautogui.position()))
    time.sleep(1)
    """
    print("step: " + str(k))
"""  
screenShots = [pyautogui.locateCenterOnScreen("resources/granblue_bookmark.PNG")] 
    for i in screenShots:
        #print("entre loop")
        if i is not None:
            print("entre if")
            pyautogui.click(i.x, i.y)
            # pyautogui.hotkey("ctrl", "w")
            if k != 9:
                k += 1
            else:
                k = 1
    print("Loop: " + str(x))
    print("Step: " + str(k))
    x += 1
    time.sleep(1)
""" 
