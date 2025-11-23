
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.signal import convolve

# Load audio and impulse response
fs1, audio = wavfile.read('audio.wav')
fs2, ir = wavfile.read('impulse_response.wav')

# Use only one channel if stereo
if audio.ndim > 1:
    audio = audio[:, 0]
if ir.ndim > 1:
    ir = ir[:, 0]

# Linear convolution
linear = convolve(audio, ir)

# Circular convolution using FFT
N = len(audio) + len(ir) - 1
audio_pad = np.pad(audio, (0, N - len(audio)))
ir_pad = np.pad(ir, (0, N - len(ir)))
circular = np.fft.ifft(np.fft.fft(audio_pad) * np.fft.fft(ir_pad)).real

# Plot results
plt.figure(figsize=(10, 5))
plt.subplot(2, 1, 1)
plt.title("Linear Convolution")
plt.plot(linear)

plt.subplot(2, 1, 2)
plt.title("Circular Convolution")
plt.plot(circular)

plt.tight_layout()
plt.show()