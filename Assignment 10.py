import numpy as np


arr = np.arange(1, 11)
print("Original Array:", arr)


print("First 5 elements:", arr[:5])
print("Last 3 elements:", arr[-3:])
print("Elements from index 2 to 7:", arr[2:8])


print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))


arr_modified = arr * 2   
print("Array after broadcasting (×2):", arr_modified)






Original Array: [ 1  2  3  4  5  6  7  8  9 10]
First 5 elements: [1 2 3 4 5]
Last 3 elements: [ 8  9 10]
Elements from index 2 to 7: [3 4 5 6 7 8]
Sum: 55
Mean: 5.5
Maximum: 10
Minimum: 1
Array after broadcasting (×2): [ 2  4  6  8 10 12 14 16 18 20]
