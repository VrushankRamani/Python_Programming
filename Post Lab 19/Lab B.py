import numpy as np
from scipy.signal import dlti

zeros_roots = [0.7, 0.9]
poles_roots = [0.6, 0.4]
num = 0.5 * np.poly(zeros_roots) 
den = np.poly(poles_roots)         

# Create discrete-time LTI system
system = dlti(num, den)

# Extract zeros and poles
zeros = system.zeros
poles = system.poles

print("Zeros:", zeros)
print("Poles:", poles)

stable = np.all(np.abs(poles) < 1)
print("Stability:", "Stable" if stable else "Unstable")