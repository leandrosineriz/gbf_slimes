import pyautogui as py
import time

k = 1 #step
loop = 0 #loop
running_start = time.time() #start of script
time_inic = time.time() #counter
reload = "f5" #reload button
reload_count = 0 #reload counter
x, y = -1, -1 #position variables
while True:
    if k == 1:
        #Granblue slimes bookmark
        try:
            x, y = py.locateCenterOnScreen("resources/granblue_bookmark.PNG" , confidence=0.9)
        except:
            x, y = -1, -1
    if k == 2:
        #summon
        try:
            x, y = py.locateCenterOnScreen("resources/summon.PNG" , confidence=0.9)
        except:
            x, y = -1, -1
    if k == 3:
        #Ok button
        try:
            x, y = py.locateCenterOnScreen("resources/button_ok.PNG" , confidence=0.9)
        except:
            x, y = -1, -1
    if k == 4:
        #Search Gran icon
        try:
            x, y = py.locateCenterOnScreen("resources/personaje_gran.PNG" , confidence=0.9)
        except:
            #Search Potion use button
            try:
                #item_loc = py.locateOnScreen("resources/potion.PNG" , confidence=0.9)
                x, y = py.locateCenterOnScreen("resources/potion.PNG" , confidence=0.9)
                py.click(x, y+150)
                time_inic = time.time()
                continue
            except:
                x, y = -1, -1
            #Search ok button for refill
            try:
                x, y = py.locateCenterOnScreen("resources/button_ok_refill.PNG" , confidence=0.9)
                py.click(x, y)
                time_inic = time.time()
                continue
            except:
                x, y = -1, -1
    if k == 5:
        #Gran habilidad
        try:
            x, y = py.locateCenterOnScreen("resources/habilidad_gran.PNG" , confidence=0.9)
        except:
            x, y = -1, -1
    if k == 6:
        #Granblue slimes bookmark
        try:
            x, y = py.locateCenterOnScreen("resources/granblue_bookmark.PNG" , confidence=0.9)
        except:
            x, y = -1, -1
    if k == 7:
        #Saraza
        try:
            x, y = py.locateCenterOnScreen("resources/personaje_saraza.PNG" , confidence=0.9)
        except:
            x, y = -1, -1
    if k == 8:
        #Saraza habilidad
        try:
            x, y = py.locateCenterOnScreen("resources/habilidad_saraza.PNG" , confidence=0.9)
        except:
            x, y = -1, -1
    if k == 9:
        #Reload
        time.sleep(1)
        py.press(reload)
        k += 1
        continue
    if k == 10:
        # Restart
        #Ok button
        try:
            x, y = py.locateCenterOnScreen("resources/button_ok2.PNG" , confidence=0.9)
        except:
            x, y = -1, -1
    
    #Control print
    running_time = time.time() - running_start
    print("Loop:", loop, "- Stage:", k, "- Time:", "{:.2f}".format(running_time/60))
    loop += 1
    
    #validates image found and does the click on position x, y
    if  x != -1 and y != -1:
        #Reload timer and reload count
        time_inic = time.time()
        reload_count = 0
        #Reload loop
        if k == 10:
            k = 1
            continue
        #delay before gran
        if k == 4:
            time.sleep(1)
        #delay before narmaya 
        elif k == 7:
            time.sleep(2)
        #Click
        py.click(x, y)
        #Press f5 to avoid stuck on f6
        if k == 6:
            py.press(reload)
        k += 1
        
    #validates timer and reload the page based on step do other things
    if time.time() - time_inic > 10:
        #Before entering battle restart from step 1
        if k == 2:
            k = 4
        elif k < 5:
            k = 1
        #Rollback to gran's turn
        elif k < 6:
            k = 4
        #Rollback to saraza's turn
        elif k < 9:
            k = 7
        
        #If reload more than 3 times without cliking start from step 1
        if reload_count > 3:
            k = 1
        
        #Reloads
        #Search bookmark and clicks
        try:
            x, y = py.locateCenterOnScreen("resources/granblue_bookmark.PNG" , confidence=0.9)
            py.click(x, y)
            time.sleep(1)
        except:
            x, y = -1, -1
        py.press(reload)
        time.sleep(2)
        time_inic = time.time() #reload timer
        reload_count += 1 #Add to reload counter