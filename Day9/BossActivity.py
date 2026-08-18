#Student Performance Analyser

import numpy as np

# You're given marks for 10 students across 5 subjects:
#
# Mathematics
# Python
# DBMS
# Data Structures
# AI/ML

marks = np.array([
    [85, 78, 92, 88, 95],
    [72, 65, 70, 75, 80],
    [90, 88, 95, 92, 96],
    [55, 60, 58, 62, 65],
    [68, 74, 70, 72, 75],
    [95, 92, 98, 96, 94],
    [45, 50, 48, 52, 55],
    [82, 85, 80, 88, 90],
    [76, 70, 78, 75, 72],
    [88, 91, 85, 89, 93]
])

print(marks)
print(marks.shape)
print(marks.ndim)
print(marks.size)
print(marks.dtype)

print(np.sum(marks))
print(np.average(marks))

print(np.mean(marks,axis=0))
print(np.max(marks,axis=0))
print(np.min(marks,axis=0))
print(np.std(marks,axis=0))

print(np.sum(marks,axis=1))
print(np.average(marks,axis=1))
print(np.max(marks,axis=1))
print(np.min(marks,axis=1))

print(marks[marks>90])
print(marks[marks<50])
# print(marks[70,90])
#dont know

