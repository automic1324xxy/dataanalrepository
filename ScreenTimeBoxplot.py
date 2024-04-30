import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

data = np.array([5, 6, 6, 3, 9, 6, 9, 8, 5, 8, 7, 8, 5, 8, 8, 7, 3, 3, 7, 7, 2, 5, 4, 8, 7, 4, 4, 4, 5, 2, 6, 10, 3, 12, 7, 5, 7, 2, 5, 4])

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
plt.xlabel('Hours of Screen Time')
plt.title('Boxplot of the Average Screen Time')
plt.show()