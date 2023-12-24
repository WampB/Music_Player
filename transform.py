from math import e
from pydub import AudioSegment
import sys,shutil

def trans_m4a_to_other(filepath, hz):
    song = AudioSegment.from_file(filepath)
    song.export(filepath.split(".")[0].split("//")[-1]+ "." + str(hz), format=str(hz))
if __name__=='__main__':
    try:
        print(sys.argv[1:])
        for i in sys.argv[1:]:
            src='m4a\\'+i+'.m4a';target='mp3\\'+i+'.mp3'
            trans_m4a_to_other(src,'mp3')
            print(f'《{i}》 has been transformed from .m4a to .mp3.')
            frm='m4a\\'+i+'.mp3'
            shutil.move(src=frm,dst=target)
            print(f'《{i}》 has been moved from m4a\ to mp3\.')
        input('CMD transform has been completed, input to ensure exit.')
    except:
        name=input('Please input the song\'s name to be transformed.')
        src='m4a\\'+name+'.m4a';target='mp3\\'+name+'.mp3'
        trans_m4a_to_other(src,'mp3')
        print(f'《{name}》 has been transformed from .m4a to .mp3.')
        target='m4a\\'+name+'.mp3'
        shutil.move(src=src,dst=target)
        print(f'《{name}》 has been transformed from .m4a to .mp3.')
        input('INPUT transform has been completed, input to ensure exit.')
    pass
