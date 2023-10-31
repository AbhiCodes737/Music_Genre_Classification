from pydub import AudioSegment
t1 = 60000 #Works in milliseconds
t2 = 90000
waveFile = AudioSegment.from_file("audio-pop.wav")
waveFile = waveFile[t1:t2]
waveFile.export('audio_sample_30s_pop.wav', format="wav")