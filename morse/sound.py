import struct
import numpy as np
#from scipy import signal as sg
import wave

class CMySound():
    def __init__(self, 
                export_file_short_beep:str='./static/sound/beeps.wav',
                export_file_long_beep:str='./static/sound/beepl.wav'
            ):
        self.export_file_short_beep=export_file_short_beep
        self.export_file_long_beep=export_file_long_beep
        self.freq_hertz=440
        self.sampling_rate_hertz=44100
        self.duration_short_seconds=.1
        self.duration_long_seconds=.3

    def generate_beep(self,duration_seconds:float=1, export_file:str='./static/sound/beeps.wav'):
        n_samples = int(self.sampling_rate_hertz*duration_seconds)
        x=np.arange(n_samples)
        y=32767.0*np.sin(2.0*np.pi*self.freq_hertz*x/self.sampling_rate_hertz)
        y=np.int16(y)
        frames = struct.pack('={}h'.format(len(y)),*y)
        frames+= struct.pack('={}h'.format(len(y)),*y)
        with wave.open(export_file,'w') as fh:
            fh.setparams((2,2,self.sampling_rate_hertz,n_samples,'NONE','not compressed'))
            fh.writeframesraw(frames)

if __name__=='__main__':
    ms=CMySound()
    ms.generate_beep(duration_seconds=ms.duration_short_seconds, export_file=ms.export_file_short_beep)
    ms.generate_beep(duration_seconds=ms.duration_long_seconds, export_file=ms.export_file_long_beep)
