import sympy as sp

def z_transform_unit_step():
    # Define symbols
    n, z = sp.symbols('n z')
    
    # Unit step sequence: u[n] = 1 for n >= 0
    x_n = 1
    
    # Compute Z-transform
    X_z = sp.summation(x_n * z**(-n), (n, 0, sp.oo))
    
    print("Z-transform of unit step function:")
    print(X_z)
    
    # Region of convergence
    roc = "|z| > 1"
    print("Region of Convergence (ROC):", roc)
    
    # Stability check
    stable = "Stable" if "unit circle" in roc else "Unstable"
    print("System Stability:", stable)

# Run function
z_transform_unit_step()