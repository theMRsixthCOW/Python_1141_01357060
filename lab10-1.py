import sympy as sp
import numpy as np
from numpy import exp
import scipy
from scipy import linalg # Linear algebra
from scipy import optimize # Optimization
from scipy import integrate # Integration
from scipy import interpolate # Interpolation
from scipy import signal # Signal processing
from scipy import stats # Statistics
from scipy import sparse
import matplotlib.pyplot as plt
from  matplotlib.pyplot import show 
from  matplotlib.pyplot import  fill_between 
import scipy 
from scipy.integrate import quad


def f(x):
    return np.exp(-x**2)

x_vals = np.linspace(-1, 3, 500) #（初位置，末位置，圆滑度or 多少切点）


y_vals = f(x_vals)

plt.figure(figsize=(10, 6))
plt.plot(x_vals, y_vals, label=r'$f(x)', color='blue', linewidth=2)

x_fill = np.linspace(0, 2, 200)
y_fill = f(x_fill)
plt.fill_between(x_fill, y_fill, color='gray', alpha=0.5, label=r' 0 to 2')
# f(x) jifen
integral_value, error = quad(f, 0, 2)
print(f"定积分值为: {integral_value:.6f}")


plt.text(1.0, 0.8, f'I = {integral_value:.6f}', fontsize=12, bbox=dict(facecolor='red', alpha=0.8))
print(f"")
plt.title(r'f(x)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True, alpha=0.3)

plt.show()