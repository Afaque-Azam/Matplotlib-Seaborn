import matplotlib.pyplot as plt
import numpy as np

for i in range(5):
    plt.plot(np.random.rand(100), linewidth = 1)

plt.title("Too Much Data Can be Confusing")
plt.grid(True)
plt.tight_layout()
plt.legend()
plt.show()