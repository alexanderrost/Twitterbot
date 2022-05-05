import sys
from twython import Twython
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import time
from datetime import datetime

# Let's not talk about the True loop. This had to be made very quickly for the joke to land
while True:

    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")
    print("Current Time =", current_time)
    
    # Req was the speedrun website with api token so removed for security reasons.
    req = Request('',
                  headers={'User-Agent': 'Mozilla/5.0'})
    # Url also empty due to security reasons.
    url = ""
    html = urlopen(req).read()
    soup = BeautifulSoup(html, features="html.parser")

    # kill all script and style elements
    for script in soup(["script", "style"]):
        script.extract()  # rip it out

    # get text
    text = soup.get_text()

    # break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in text.splitlines())
    # break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # drop blank lines
    text = '\n'.join(chunk for chunk in chunks if chunk)
    x = text.split(",")
    arraytest = []
    for i in x:
        arraytest.append(i)
    print(arraytest[5])
    # Excuse the poor variable names, x is the time pulled from the website
    # x[11] is the location of the seconds (2:14) and required him to hit a number below 5 to get the new world record
    # Thus only needing to make sure elemnt 11 is a 4 for this to fullfil it's porpouse.
    x = arraytest[5]
    print(x[11])
    test = '4'

    if x[11] == test:
        tweetStr = "Holy moly he did it!! What now?"
        # Your twitter consumer and access information goes here
        # note: these are garbage strings and won't work
        apiKey = '123'
        apiSecret = '123'
        accessToken = '123'
        accessTokenSecret = '123'

        api = Twython(apiKey, apiSecret, accessToken, accessTokenSecret)

        api.update_status(status=tweetStr)
        print("tweeted")
    else:
        # Currenttime was added to prevent twitter for complaining about tweeting the same thing over and over
        tweetStr = "Did Sevve hit a run? No! nice try g.. Current Time: " + current_time
        # your twitter consumer and access information goes here
        # note: these are garbage strings and won't work
        apiKey = '123'
        apiSecret = '123'
        accessToken = '123'
        accessTokenSecret = '123'

        api = Twython(apiKey, apiSecret, accessToken, accessTokenSecret)

        api.update_status(status=tweetStr)
        print("tweeted")
    
    # 7200 seconds delay to ensure twitter would not flag the bot for spam. Anything over 30 minutes would've been fine but overkill.
    time.sleep(7200)

# I applogize for the eyesoar this code is, cheers!



