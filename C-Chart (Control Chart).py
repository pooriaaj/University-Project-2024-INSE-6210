import numpy as np

samples = np.array([5, 2, 1, 3, 2, 24, 5, 3, 6])

C_bar = samples.mean()

UCL = C_bar + 3 * np.sqrt(C_bar)
LCL = max(0, C_bar - 3 * np.sqrt(C_bar))

plt.plot(samples, marker='o', linestyle='-')
plt.axhline(C_bar, color='green', linestyle='--', label='Centerline (C-bar)')
plt.axhline(UCL, color='red', linestyle='--', label='UCL')
plt.axhline(LCL, color='blue', linestyle='--', label='LCL')
plt.legend()
plt.show()
