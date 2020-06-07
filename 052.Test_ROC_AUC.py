import numpy as np
from sklearn import metrics

# 1
y = np.array([1, 1, 2, 2])
pred = np.array([0.1, 0.4, 0.35, 0.8])
fpr, tpr, _ = metrics.roc_curve(y, pred, pos_label=2)
print(1, fpr, tpr)
print(1, metrics.auc(fpr, tpr))
"""
1 [0.  0.5 0.5 1. ] [0.5 0.5 1.  1. ]
1 0.75
"""

# 2
y = np.array([1, 2, 1, 2])
pred = np.array([0.1, 0.8, 0.4, 0.35])
fpr, tpr, _ = metrics.roc_curve(y, pred, pos_label=2)
print(2, fpr, tpr)
print(2, metrics.auc(fpr, tpr))
"""
2 [0.  0.5 0.5 1. ] [0.5 0.5 1.  1. ]
2 0.75
"""

# 3, ERROR
try:
    y = np.array([1, 1, 2, 2])
    pred = np.array([0.1, 0.4, 0.35, 0.8])
    print(3, metrics.auc(y, pred))
except Exception as e:
    print(3, e.args)
"""
3 0.375
"""

# 4, ERROR
try:
    y = np.array([1, 2, 1, 2])
    pred = np.array([0.1, 0.8, 0.4, 0.35])
    print(4, metrics.auc(y, pred))
except Exception as e:
    print(4, e.args)
"""
4 ('Reordering is not turned on, and the x array is not increasing: [1 2 1 2]',)
"""
