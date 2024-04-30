import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

data = np.array([6, 4, 7, 4, 8, 2, 5, 7, 8, 4, 4, 7, 6, 5, 3, 8, 6, 8, 3, 7, 9, 8, 2, 7, 6, 8, 7, 7, 6, 5, 9, 7, 8, 3, 9, 4, 7, 8, 5, 6])

# Calculate mean, median, and mode
mean = np.mean(data)
median = np.median(data)
mode = stats.mode(data)

print("Mean:", mean)
print("Median:", median)
print("Mode:", mode)

# Create a boxplot
plt.figure(figsize=(8, 6))
plt.boxplot(data, vert=False)
plt.xlabel('Scale of Happiness')
plt.title('Boxplot of the Happiness')
plt.show()