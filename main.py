import eyed3
import sys
import os

i = input()

def editor(song):
    try:
        path = r"%s" %i + "\\" + r"%s" %song
        audiofile = eyed3.load(r"%s" %path)
        audiofile.tag.artist = song.split(' -')[0]
        audiofile.tag.title = song.split(' -')[1].split("-")[0]
        audiofile.tag.save()
        print(path)
    except Exception:
        try:
            path = r"%s" %i + "\\" + r"%s" %song
            audiofile = eyed3.load(r"%s" %path)
            audiofile.tag.title = song.split(' -')[0].rsplit('.')[0].split('-')[0]
            audiofile.tag.save()
            print(path)
        except Exception:
            print("Error on " + path)
            pass



for filename in os.listdir(i):
    editor(str(filename))
