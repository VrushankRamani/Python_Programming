import numpy as np
import matplotlib.pyplot as plt

fs = 500
t = np.linspace(0, 2, 2 * fs, endpoint=False)

sine_5Hz = np.sin(2 * np.pi * 5 * t)
cosine_10Hz = np.cos(2 * np.pi * 10 * t)
product_signal = sine_5Hz * cosine_10Hz

plt.figure(figsize=(10, 5))
plt.plot(t, product_signal, label='Product Signal')
plt.title('Multiplication of 5 Hz Sine and 10 Hz Cosine')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.legend()
plt.show()