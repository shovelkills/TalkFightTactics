
import pyautogui as pygui, pyaudio, speech_recognition as sr, time, pandas as pd
recognizer = sr.Recognizer()
microphone = sr.Microphone()
response = {
    "success": True,
    "error": None,
    "transcription": None
}
muted = {
    "success": True,
    "error": None,
    "transcription": None
}
def testmicrophone(storage):
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Say something")
        audio = recognizer.listen(source)
    try:
        storage["transcription"] = recognizer.recognize_google(audio)
    except sr.RequestError:
        storage["success"] = False
        storage["error"] = "API unavailable"
    except sr.UnknownValueError:
        storage["error"] = "Unable to recognize speech"


while response["transcription"] != "end":
    testmicrophone(response)
    if not response["success"]:
        print("Not Sucessful")
    elif response["transcription"] == "stop":
        while True:
            testmicrophone(muted)
            print("Waiting for you to say start")
            if muted["transcription"] == "start":
                muted["transcription"] = None
                break
    else:
        print(response["transcription"])

print("Ending")

