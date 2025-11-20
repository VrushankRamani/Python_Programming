import numpy as np
import matplotlib.pyplot as plt
fs = 1000
t = np.linspace(0, 1, fs, endpoint=False)

sine_5Hz = np.sin(2 * np.pi * 5 * t)
shifted_sine = np.sin(2 * np.pi * 5 * (t - 0.1))  # Shift by 0.1 sec

plt.figure(figsize=(10, 5))
plt.plot(t, sine_5Hz, label='Original 5 Hz Sine')
plt.plot(t, shifted_sine, label='Shifted by 0.1 sec', linestyle='--')
plt.title('Time Shifted Signal')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.legend()
plt.show()