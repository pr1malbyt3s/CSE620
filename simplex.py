import time
import random
import scipy as sp
from scipy.optimize import linprog

# This script is used to create linear programming problems and solve them using the SciPy linprog function.
# This script uses a basis minimization problem for all iterations: x1 + x2 + ... + xn-1 + xn.
# It accepts user input for number of variables (n) and number of constraints (m).
# It assumes all bounds for each variable are from zero to infinity.
# It also assumes each constraint is set to where it must equal one, so there are no inequalities.

# Perform input validation to ensure numbers between zero and fifty are provided to construct the variable and constraint arrays.
def input_validate(prompt):
    while True:
        try:
            value = int(input(prompt))
            # If the number of variables or constraints are desired to be more than fifty, change the upper bound in the next line.
            if 0 < value < 51:
                return value
            else:
                print("Supplied number must be between 0 and 50.")
        except ValueError:
            print("Input could not be interpreted. Try again.")

# Get the user's desired number of variables and constraints, passed through input validation.
n_count = input_validate("Enter number of variables (n): ")
m_count = input_validate("Enter number of constraints (m): ")

# Create the variables matrix, c:
c = []
for i in range(n_count): c.append(1)

# Create the equality constraints matrix, A:
A = []
for i in range(m_count):
    # This is performed using submatrices, or lists.
    # First, a list of random integers is created for the constraints equality.
    # This is repeated for however many constraints there are to match the number of variables.
    a = []
    for j in range(n_count):
        # Constraint coefficients are limited to a -10 to 10 range. Adjust the next line to change it.
        a.append(random.randint(-10, 10)) 
    A.append(a)

# Create the equality constraint vector, b:
b = []
for i in range(m_count): b.append(1)

# Capture the start time to measure the run time.
start_time = time.time()

# Solve the problem using linprog.
res = linprog(c, A_eq=A, b_eq=b, method='simplex', options={"disp":True, "presolve":False})

# Capture the end time to measure the run time.
end_time = time.time()

# Print all results.
print(res)
print(" ")
print("Run time elapsed: " + (str)(end_time - start_time))
print(" ")
print("Constraints matrix used: ")
print(A)
