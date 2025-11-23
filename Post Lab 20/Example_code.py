import soundfile as sf


# Load audio file
audio, sample_rate = sf.read(r'C:\Users\Slock\OneDrive\Desktop\song.wav') # Write audio file
sf.write('new_audio_file.wav', audio, sample_rate) 
import matplotlib.pyplot as plt
import numpy as np  
import soundfile as sf # Load audio file
#audio, sample_rate = sf.read('audio_file.wav') # Create time axis
time = np.arange(0, len(audio)) / sample_rate # Plot audio signal
plt.plot(time, audio) 
plt.xlabel('Time (s)') 
plt.ylabel('Amplitude') 
plt.show()