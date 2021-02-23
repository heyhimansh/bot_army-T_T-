import pyautogui, time    #pip install pyautogui

time.sleep(5)    # Set the timer to run the code
for word in open("script.txt", "r"):  #Location of script,lyrics or whatever loaded 'r' to read
    pyautogui.typewrite(word) #This will write words in the line
    pyautogui.press("enter") #This will change the line
    
    
