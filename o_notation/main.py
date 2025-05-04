import numpy as np
import matplotlib.pyplot as plt
from math import factorial

x = np.linspace(0.0, 15, 100)

# Funktionen
f1 = x ** 2
f2 = (x ** 2) * np.log(x)

# Plot
plt.figure(figsize=(10, 6))
plt.plot(x, f1, label=r'O-Notation: $f_1(x) = x²$', color='red')
plt.plot(x, f2, label=r'$f_2(x) = x^2 \cdot \log(x)$', color='blue')


# y-Achse logarithmisch
plt.yscale('log')
plt.xlabel('x')
plt.ylabel('y mit $\log_{10}$')
plt.title('Big O-Notation')
plt.grid(True, which="both", ls="--", linewidth=0.5)
plt.legend()
plt.tight_layout()
plt.show()

