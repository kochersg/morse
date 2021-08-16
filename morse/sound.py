import struct
import numpy as np
#from scipy import signal as sg
import wave

class CMySound():
    """
    Generate beep-sounds as wave files, save, load and play them

    Attributes
    ----------
    export_file_short_beep:str
        URL-string to export wave file for short beep. Default: './static/sound/beeps.wav'
    export_file_long_beep:str
        URL-string to export wave file for long beep. Default: './static/sound/beepl.wav'
    freq_hertz:float
        Audible frequency for beep in Hertz. Default: 440Hz
    sampling_rate_hertz:float
        Rate for sampling of the audible signal in Hertz. Default: 44100Hz
    duration_short_seconds:float
        Duration of the short beep in seconds. Default: 0.1s
    duration_long_seconds:float
        Duration of the long beep in seconds. Default: 0.3s
        
    Methods
    -------
    generate_beep:
        Generates a sine-wave as numpy-array and saves it to specified wav-file
    """
    def __init__(self, 
                export_file_short_beep:str='./static/sound/beeps.wav',
                export_file_long_beep:str='./static/sound/beepl.wav'
            ):
        """
        Generate beep-sounds as wave files, save, load and play them

        Parameters
        ----------
        export_file_short_beep:str, optional
            URL-string to export wave file for short beep. Default: './static/sound/beeps.wav'
        export_file_long_beep:str, optional
            URL-string to export wave file for long beep. Default: './static/sound/beepl.wav'
        """
        self.export_file_short_beep=export_file_short_beep
        self.export_file_long_beep=export_file_long_beep
        self.freq_hertz=440.0
        self.sampling_rate_hertz=44100.0
        self.duration_short_seconds=.1
        self.duration_long_seconds=.3

    def generate_beep(self,duration_seconds:float=1, export_file:str='./static/sound/beeps.wav'):
        """
        Generate a sin-wave with given duration, frequency and sampling as numpy-array. 
        Save it as wav-file using the wave module.

        Parameters
        ----------
        duration_seconds:float, optional
            Duration of the beep-sound in seconds. Default: 1.0
        export_file: str, optional
            URL-string to export wave file for the generated beep
        """
        # number of bytes per sample
        n_bytes=2
        # number of audio channels
        n_channels=1
        # Calculate the number of samples that the wave file will contain. It needs to be an integer number.
        n_samples = int(self.sampling_rate_hertz*duration_seconds)
        # generate a numpy array from 0...n_samples-1 (n_samples values)
        x=np.arange(n_samples)
        # max amplitude is given by n_bytes. We have 8bit per byte (16bit for 2byte)
        max_amplitude=2**(8*n_bytes-1)-1
        # calculate the sine-function of the audio wave
        y=max_amplitude*np.sin(2.0*np.pi*self.freq_hertz*x/self.sampling_rate_hertz)
        # convert y into 16bit integer array
        y=np.int16(y)
        # Create an bytearray with all the values aligned in correct by order
        for channel in range(n_channels):
            if channel==0:
                frames = struct.pack('={}h'.format(len(y)),*y)
            else:
                frames = struct.pack('={}h'.format(len(y)),*y)
        # Write wave file
        with wave.open(export_file,'w') as fh:
            # setparams uses the following parameter:
            # n_channels: Number of sound channels. I use the value 1 (Mono).
            # sampling_width: number of bytes used to store one value. I use the value 2 (16bit)
            # sampling_rate
            # n_samples: number of samples (duration * sampling_rate_hertz)
            # the parameters 'None' and 'not compressed' need to be set
            # see also https://docs.python.org/3/library/wave.html
            fh.setparams((n_channels,n_bytes,self.sampling_rate_hertz,n_samples,'NONE','not compressed'))
            fh.writeframesraw(frames)

if __name__=='__main__':
    ms=CMySound()
    ms.generate_beep(duration_seconds=ms.duration_short_seconds, export_file=ms.export_file_short_beep)
    ms.generate_beep(duration_seconds=ms.duration_long_seconds, export_file=ms.export_file_long_beep)
