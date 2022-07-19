from numpy import random
import matplotlib.pyplot as plt
temp = random.pareto(a=5, size=(6, 9))
r = random.zipf(a=2, size=(2, 3))
my_arr = np.array([1, 2, 5, ])
res_arr = []
for element in my_arr:
  if element &gt; 1:
    res_arr.append(0)
  else:
    res_arr.append(1)
newarr = my_arr[res_arr]
print(res_arr)