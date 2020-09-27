import scipy as sp
from scipy.optimize import linprog

# First iteration (n=4, m=2)
c = [1, 1, 1, 1]
A = [[1, 2, -1, -1], [-1, -5, 2, 3]]
b = [1, 1]
x0_bounds = (0, None)
x1_bounds = (0, None)
x2_bounds = (0, None)
x3_bounds = (0, None)

res = linprog(c, A_ub=A, b_ub=b, bounds=(x0_bounds, x1_bounds, x2_bounds, x3_bounds), method='simplex', options={"disp":True})

# Second iteration (n=10, m=6)

# Third iteration (n=50, m=10)

print(res)
