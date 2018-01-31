from os import chdir
from PyQt5.QtMultimedia import QSound

def musicSelectAndPlay(musicName):
    chdir('../Music')
    musicToPlay = QSound(musicName)
    musicToPlay.play()
    chdir('../Code')

def soundSelectAndPlay(path,soundName):
    folderCount = (path.split("/").length())-1
    chdir(path)
    backToOriginalPath = "../"*folderCount
    soundToPlay = QSound(soundName)
    soundToPlay.play()
    chdir(backToOriginalPath)

def musicSelect(musicName):
    chdir('../Music')
    musicToPlay = QSound(musicName)
    chdir('../Code')
    return(musicToPlay)

def soundSelect(path,soundName):
    folderCount = (path.split("/").length)-1
    chdir(path)
    backToOriginalPath = "../"*folderCount
    soundToPlay = QSound(soundName)
    chdir(backToOriginalPath)
    return(soundToPlay)

def audioSelect(name,path='0',choice='select'):
    pathAnalysis = path.split("/")
    nameAnalysis = name.split(".")
    if nameAnalysis[len(nameAnalysis)-1] != "wav":
        name = name+".wav"
    if path == '0' and choice == 'select':
        return(musicSelect(name))
    if path == '0' and choice == 'play':
        musicSelectAndPlay(name)
    if path != '0' and choice == 'select':
        return(soundSelect(path,name))
    if path != '0' and choice == 'play':
        soundSelectAndPlay(path,name)
