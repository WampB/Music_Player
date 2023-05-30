from pydub import AudioSegment

def trans_m4a_to_other(filepath, hz):
    song = AudioSegment.from_file(filepath)
    song.export(filepath.split(".")[0].split("//")[-1]+ "." + str(hz), format=str(hz))

path=""
trans_m4a_to_other(path, "mp3")
