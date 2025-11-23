import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import dlti, freqz

def analyze_z_transfer_function(num, den):
    # Create a Discrete-Time LTI system
    system = dlti(num, den)

    # Get the poles and zeros
    zeros = system.zeros
    poles = system.poles
    print("Zeros:", zeros)
    print("Poles:", poles)

    # Stability Analysis (poles inside unit circle)
    stable = all(np.abs(pole) < 1 for pole in poles)
    print("Stability:", "Stable" if stable else "Unstable")

    # Causality Analysis (basic check: denominator order >= numerator order)
    causal = len(den) >= len(num)
    print("Causality:", "Causal" if causal else "Non-Causal")

    # Time Invariance Analysis
    time_invariant = True
    print("Time Invariance:", "Time Invariant" if time_invariant else "Time Variant")

    # Frequency response (instead of bode for discrete-time)
    w, h = freqz(num, den, worN=512)
    mag = 20 * np.log10(abs(h))
    phase = np.angle(h, deg=True)

    # Plot magnitude and phase
    plt.figure(figsize=(12, 8))
    plt.subplot(2, 1, 1)
    plt.plot(w, mag)
    plt.title('Magnitude Response')
    plt.xlabel('Frequency [rad/sample]')
    plt.ylabel('Magnitude [dB]')
    plt.grid()

    plt.subplot(2, 1, 2)
    plt.plot(w, phase)
    plt.title('Phase Response')
    plt.xlabel('Frequency [rad/sample]')
    plt.ylabel('Phase [degrees]')
    plt.grid()

    plt.tight_layout()
    plt.show()