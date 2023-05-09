from Modules import *

latest_video = ""
latest_short = ""

def getlatestvideo():
    global latest_video
    latest_video = requests.get("")
    print("Latest Video is")

def getlatestshort():
    global latest_short
    latest_short = requests.get("")
    print("Latest Short is")
