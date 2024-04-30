import matplotlib.pyplot as plt
import numpy as np

hours = [5, 6, 6, 3, 9, 6, 9, 8, 5, 8, 7, 8, 5, 8, 8, 7, 3, 3, 7, 7, 2, 5, 4, 8, 7, 4, 4, 4, 5, 2, 6, 10, 3, 12, 7, 5, 7, 2, 5, 4]
happiness = [6, 4, 7, 4, 8, 2, 5, 7, 8, 4, 4, 7, 6, 5, 3, 8, 6, 8, 3, 7, 9, 8, 2, 7, 6, 8, 7, 7, 6, 5, 9, 7, 8, 3, 9, 4, 7, 8, 5, 6]

correlation_coefficient = np.corrcoef(hours, happiness)[0, 1]
print("Correlation Coefficient:", correlation_coefficient)

plt.figure(figsize=(8, 6))
plt.scatter(hours, happiness)
plt.xlabel('Hours of Phone Usage')
plt.ylabel('Happiness Level')
plt.title('Scatter Plot of Hours of Phone Usage vs. Happiness Level')
plt.show()