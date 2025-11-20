import numpy as np
import matplotlib.pyplot as plt

# Parameters
fs = 1000   # Sampling frequency
t = np.linspace(0, 1, fs, endpoint=False)

# Signals
sine_5Hz = np.sin(2 * np.pi * 5 * t)
sine_10Hz = np.sin(2 * np.pi * 10 * t)
combined_signal = sine_5Hz + sine_10Hz

# Plot
plt.figure(figsize=(10, 5))
plt.plot(t, sine_5Hz, label='5 Hz Sine')
plt.plot(t, sine_10Hz, label='10 Hz Sine')
plt.plot(t, combined_signal, label='Combined', linewidth=2)
plt.title('Addition of 5 Hz and 10 Hz Sine Waves')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.legend()
plt.show()
