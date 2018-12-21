import moviepy.editor as mp

def convertToMp3(name, directory):
    
    oldName = directory + "/" + name
    newName = oldName + ".mp3"
    clip = mp.VideoFileClip(oldName).subclip(0,20)
    clip.audio.write_audiofile(newName)
