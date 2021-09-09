#
from bisect import bisect_left, bisect_right

a = [1,2,4,4,8]
print(bisect_left(a,2))
print(bisect_right(a,2))
