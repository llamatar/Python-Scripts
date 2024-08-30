# This Counting Problem Changed My Life. Can You Solve It? [Gridwalking]
# youtu.be/3B-D3w292TI
# 2024-01-23

from functools import cache

@cache
def calc_count(x, y):
    if x == 0 and y == 0:
        return 1
    elif x == 0:
        return calc_count(x, y-1)
    elif y == 0:
        return calc_count(x-1, y)
    else:
        return calc_count(x, y-1) + calc_count(x-1, y)

print(calc_count(5, 4))

"""
non-brute-force method of counting:

solution includes 5 R's and 4 D's
RRRRRDDDD
RRRRDRDDD
...
DDDDRRRRR

choose 5 positions for R, then remaining 4 positions must be D
9 choose 5
= 9! / (5!4!)
= 9 * 8 * 7 * 6 / (4 * 3 * 2)
= 3 * 7 * 6
= 126

"""
