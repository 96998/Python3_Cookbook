import heapq
import numpy as np

x = np.random.randint(1, 100000, 500)
print(x)
# x中最大的10个数字
print(heapq.nlargest(10, x))
# x中最下的十个数字
print(heapq.nsmallest(10, x))



