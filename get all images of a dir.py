import time
import os
import pyautogui as py


image_list = []

# Get list of all files in current directory
directory = os.listdir("resources")

# Find files that end with .png or .jpg and add to image_list
for file in directory:
    if file.endswith('.PNG') or file.endswith('.jpg'):
        image_list.append(file)

while True:    
    # Loop through list to find all the images
    for image in image_list:
        screenShots = [py.locateCenterOnScreen("resources/" + image, confidence=0.9)] 
        for i in screenShots:
            print(image, " - ", i)
            if i is not None:
                print("entre if")
                py.click(i.x, i.y)
                # pyautogui.hotkey("ctrl", "w")
                
        #x += 1
        #time.sleep(1)
        


    