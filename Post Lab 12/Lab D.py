import numpy as np
import matplotlib.pyplot as plt
fs = 1000
t = np.linspace(0, 1, fs, endpoint=False)

sine_10Hz = np.sin(2 * np.pi * 10 * t)
scaled_sine = 3 * sine_10Hz

plt.figure(figsize=(10, 5))
plt.plot(t, sine_10Hz, label='Original 10 Hz Sine')
plt.plot(t, scaled_sine, label='Scaled (x3)', linestyle='--')
plt.title('Amplitude Scaling of 10 Hz Sine')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.legend()
plt.show()