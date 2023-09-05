import numpy as np
from scipy.optimize import minimize
from scipy.optimize import differential_evolution
from rastrigin_fction import rastrigin_taking_2d_list

# Define the 3D function you want to minimize
def objective_function(x):
    # For example, let's use a simple 3D quadratic function
    return x[0] ** 2 + x[1] ** 2 + x[2] ** 2

# Initial guess (starting point for the optimization)
initial_guess = [-5, 5]  # You can set this to any initial point you like

# Use the minimize function to find the minimum
#result = minimize(rastrigin_taking_2d_list, initial_guess, method='BFGS')  # You can choose other optimization methods as well
result = differential_evolution(rastrigin_taking_2d_list, [[-5,5],[-5,5]])

# Extract the minimum and the location
minimum = result.fun
minimum_location = result.x

print("Minimum:", minimum)
print("Location of minimum:", minimum_location)

x = minimum_location[0]
y = minimum_location[1]
print(f'Rastrigin({x},{y}) = {rastrigin_taking_2d_list([x,y])} and should be {minimum}')
print(f'Rastrigin({0},{0}) = {rastrigin_taking_2d_list([0,0])} and should be {np.nan}')


























