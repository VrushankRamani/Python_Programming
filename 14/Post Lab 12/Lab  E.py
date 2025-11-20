
import numpy as np
import matplotlib.pyplot as plt
fs = 1000
t = np.linspace(0, 1, fs, endpoint=False)

sine_5Hz = np.sin(2 * np.pi * 5 * t)
reversed_sine = sine_5Hz[::-1]  # Reverse signal

plt.figure(figsize=(10, 5))
plt.plot(t, sine_5Hz, label='Original 5 Hz Sine')
plt.plot(t, reversed_sine, label='Reversed Sine', linestyle='--')
plt.title('Time Reversal of 5 Hz Sine Wave')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.legend()
plt.show()