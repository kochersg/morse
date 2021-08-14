import struct
import numpy as np
#from scipy import signal as sg
import wave

class CMySound():
    def __init__(self, export_file:str='./static/sound/beep.wav'):
        self.export_file=export_file
        self.freq_hertz=440
        self.sampling_rate_hertz=44100
        self.duration_seconds=5

    def generate_beep(self):
        n_samples = self.sampling_rate_hertz*self.duration_seconds
        x=np.arange(n_samples)
        y=32767.0*np.sin(2.0*np.pi*self.freq_hertz*x/self.sampling_rate_hertz)
        w=wave.open(self.export_file,'w')
        w.setparams((2,2,self.sampling_rate_hertz,n_samples,'NONE','not compressed'))

        frames = ''.join(''.join(struct.pack('h', int(sample)) for sample in y))
        w.writeframesraw(frames)

        w.close()

if __name__=='__main__':
    ms=CMySound(export_file='./static/sound/beep.wav')
    ms.generate_beep()
