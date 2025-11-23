import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

def load(p):
    sr, x = wavfile.read(p)
    x = x.astype(float)
    if np.max(np.abs(x)) > 1: x /= np.max(np.abs(x))
    return sr, x

def autocorr(x):
    return np.correlate(x, x, mode="full")

def crosscorr(x, y):
    return np.correlate(x, y, mode="full")

sr1, clean = load("clean_audio.wav")
sr2, noisy = load("noisy_audio.wav")
sr3, periodic = load("periodic_audio.wav")

ac_clean = autocorr(clean)
ac_noisy = autocorr(noisy)
ac_periodic = autocorr(periodic)

cc_clean_noisy = crosscorr(clean, noisy)
cc_clean_periodic = crosscorr(clean, periodic)

plt.figure(figsize=(12,10))

plt.subplot(3,2,1); plt.plot(ac_clean); plt.title("Autocorrelation - Clean")
plt.subplot(3,2,3); plt.plot(ac_noisy); plt.title("Autocorrelation - Noisy")
plt.subplot(3,2,5); plt.plot(ac_periodic); plt.title("Autocorrelation - Periodic")

plt.subplot(3,2,2); plt.plot(cc_clean_noisy); plt.title("Cross-Corr: Clean vs Noisy")
plt.subplot(3,2,4); plt.plot(cc_clean_periodic); plt.title("Cross-Corr: Clean vs Periodic")

plt.tight_layout()
plt.show()