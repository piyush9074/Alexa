import pyautogui
import wikipedia
def call():
    pyautogui.hotkey('fn', 'F7')
    pyautogui.hotkey('ctrl', 'a')


#call()

def wikisearch(command):
    response=wikipedia.summary(command,1)
    print(response)


wikisearch("Batman")