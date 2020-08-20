#Uses omxplayer to shuffle through a directory of MP3s
#By default will not play a track more than once in every 10 tracks
#Change the integer on line 24 to alter allowed number of repetitions
#Default music dir is "~/piShuffle/music"

import os
import random
import repeats


def getTrack():
   return os.listdir('')[random.randint(0, len(os.listdir(''))) - 1]

def play(track):
   os.system('omxplayer -b -o hdmi "' + track + '"')

def checkRepeats(track, repeatList):
   for repeat in repeatList:
      if repeat.find(track[5:-6]) > 0:
         #print(track + ' ' + repeat)
         return False
   return True


if __name__ == '__main__':
   os.chdir('/home/pi/piShuffle/music')
   repeatList = repeats.repeatList(10)
   nextTrack = getTrack()
   play(nextTrack)
   repeatList.add(nextTrack)


   while True:
      nextTrack = getTrack()
      if not checkRepeats(nextTrack, repeatList.data) or not nextTrack.endswith('mp3'):
         continue
      play(nextTrack)
      repeatList.add(nextTrack)
      #print(repeatList.data)


