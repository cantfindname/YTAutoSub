import os
import youtube_dl
import vtt2text as conv


def getAutoVTT():

    url = None
    url = input('input youtube url address:')
    ydl_opts = {
        'writeautomaticsub' : True, 
        'skip_download' : True
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.extract_info(url)

def getTXT():
    for file in os.listdir(os.curdir):
        if file.endswith('.txt'):
            return file
    return None

def getVTT():
    for file in os.listdir(os.curdir):
        if file.endswith('.vtt'):
            return file
    return None

def cleanVTT():
    fileName = getVTT()
    if fileName == None:
        print('No subtitle generated, the video does not have automatic subtitle')
    else:
        conv.main(fileName)

def deleteAllFiles():
    for file in os.listdir(os.curdir):
        if file.endswith('.vtt') or file.endswith('.txt'):
            os.remove(file)

def printTxt():
    try:
        with open(getTXT()) as file:
            lines = file.read()
            print (lines)
    except:
        print('the txt file does not exist')

def main():
    getAutoVTT()
    cleanVTT()
    printTxt()
    deleteAllFiles()

if __name__ == "__main__":
    main()