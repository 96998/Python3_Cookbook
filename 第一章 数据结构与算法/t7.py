import math

nums = [1.23e+18, 1, -1.23e+18]
# 观察到1消失了
print(sum(nums))
print(math.fsum(nums))
