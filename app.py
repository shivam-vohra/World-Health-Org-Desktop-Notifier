import time
import datetime
from getTopTweet import getTweet
from plyer import notification


ICON_PATH = "./43-twitter-512.png"

foundTweet = getTweet()

if (foundTweet != None):
    while (True):
        notification.notify(
            title = "World Health Organization Update: {}".format(datetime.date.today()),
            message = foundTweet,
            app_icon = "Bokehlicia-Pacifica-Twitter.ico",
            timeout = 50
        )

        time.sleep(60*60*4)

