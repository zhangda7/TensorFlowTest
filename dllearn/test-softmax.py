# _*_ coding:utf-8
"""Softmax."""

#scores是自己程序输出的结果
#scores = [3.0, 1.0, 0.2]


import numpy as np
import math
scores = np.array([3.0, 1.0, 0.2])
def softmax(x):
    """Compute softmax values for each sets of scores in x."""
    pass  # TODO: Compute and return softmax(x)
    # 步骤：1.求出y的数组；2.对y的数组用logstic计算每个y的概率

    return np.exp(x) / np.sum(np.exp(x), axis = 0)

print(softmax(scores * 10))

# Plot softmax curves
import matplotlib.pyplot as plt
x = np.arange(-2.0, 6.0, 0.1)

# scores.shape is (3, 80)
scores = np.vstack([x, np.ones_like(x), 0.2 * np.ones_like(x)])

plt.plot(x, softmax(scores).T, linewidth=2)
plt.show()
