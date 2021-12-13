import time

import speech_recognition as sr

import main

listener = sr.Recognizer()

MY_NAME="friday"
# print(voices[1].id)
# engine.setProperty('voice', voices[0].id)
# engine.setProperty("rate", 150)
def take_command():
    try:
        # print(str(audio_file))
        msg = ""

        with sr.Microphone() as source:
            print("Listening.....")
            voice = listener.listen(source, 10, 10)
            msg = listener.recognize_google(voice)
            msg = msg.lower()
            # if (MY_NAME) in msg:
            #     # playsound(audio_file)
            #     main.talk("Yes Sir")
            #     msg = msg.replace(MY_NAME, '')



    except:

        pass

    return msg


while True:

    wake_up = take_command()
    first_wake = 1
    if (MY_NAME) in wake_up:
        print("waking up")
        main.run_friday(first_wake)
        first_wake = 0

    # os.startfile("C:\\Users\\pludh\\PycharmProjects\\alexa_2\\main.py")
