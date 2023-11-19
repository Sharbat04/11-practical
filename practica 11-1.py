import numpy as np
import matplotlib.pyplot as plt

np.random.seed(54)
sales_time = np.random.rand(100) * 12  
performance = 2 * sales_time + np.random.randn(100) * 2  

model = np.polyfit(sales_time, performance, 1)
slope, intercept = model

predicted_performance = slope * sales_time + intercept

plt.scatter(sales_time, performance, label='Naqty satylym')
plt.plot(sales_time, predicted_performance, color='green', label='Linear regression')
plt.xlabel('Zhumys uaqyty (sagat)')
plt.ylabel('Satylym')
plt.legend()
plt.show()

print(f"Linear model：Satylym = {slope:.2f} * Zhumys uaqyty + {intercept:.2f}")

