import numpy as np
rainfall = np.array([12, 25, 8, 30, 15, 40, 22, 18, 35, 10])
print("Rainfall measurements:", rainfall)
print("First 5 days:", rainfall[:5])
print("Last 3 days:", rainfall[-3:])
print("Total rainfall:", np.sum(rainfall), "mm")
print("Average rainfall:", np.mean(rainfall), "mm")
print("Maximum rainfall:", np.max(rainfall), "mm")
print("Minimum rainfall:", np.min(rainfall), "mm")

modified_rainfall = rainfall + 5


print("Modified rainfall array:", modified_rainfall)
