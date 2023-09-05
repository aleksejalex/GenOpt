"""
one run of simulation (with or without picutres)
"""

# necessary imports
import mygo as mg
import matplotlib.pyplot as plt
import numpy as np
import rastrigin_fction as rf

# setting macros
N = 7  # how many elements are in a population (in each time)
n_iter = 500  # number of iterations of GO
continuous_plotting = bool(0)

# generating starting population
popul = mg.generate_population(num_of_elements=N, length_of_element=2, population_type='float', min_value=-5,
                               max_value=5)

# evaluationg Rastrigin's function on the whole surface
x = np.linspace(-5, 5, 1000)
y = np.linspace(-5, 5, 1000)
X, Y = np.meshgrid(x, y)
Z = rf.rastrigin(X, Y)

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the function ("bent surface")
surface = ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.2)  # alpha parameter sets the transparency of the graph
plt.show(block=False)

# Starting the GO in for cycle, with plotting in real time
print(f'>>>  started with >>>> ')
print(popul)
print(mg.print_z_values(popul))

for j in range(n_iter):
    hypopul = mg.generate_hyperpopulation(popul, criteria_for_sorting=rf.rastrigin_taking_2d_list, num_of_iter=10, prob_crossover=0.5, p_mut=0.8, mutation_step=0.01)
    trimedpopul = mg.trim_hyperpopulation(hypopul, num_of_elements=N)
    popul = trimedpopul
    # Plot the points
    plt.title("interation " + str(j) + " / " + str(n_iter))
    if continuous_plotting == True:
        if j < (n_iter - 1): # plot smaller red points when GO runs ...
            for pt in popul:     # pt - element of population (point), in this case x and y coordinate of a point
                ax.scatter(pt[0], pt[1], rf.rastrigin(pt[0], pt[1]), c='black', marker='o', s=6)
        else:  # and plot the last one as big black stars
            for pt in popul:
                ax.scatter(pt[0], pt[1], rf.rastrigin(pt[0], pt[1]), c='red', marker='*', s=150)
        plt.pause(0.07)

print(f'>>>>  ended with >>>> ')
print(popul)
print(mg.print_z_values(popul))
print("found minimum : ")
print(rf.rastrigin_taking_2d_list(popul[0]))
ax.scatter(popul[0][0], popul[0][1], rf.rastrigin(popul[0][0], popul[0][1]), c='red', marker='*', s=150) # plotting final (found extreme)
fig.colorbar(surface, ax=ax, shrink=0.5, aspect=10)
plt.show()





