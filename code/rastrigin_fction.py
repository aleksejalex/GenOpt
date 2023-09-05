"""
Rastrigin's function: evaluation and plot3d

created by AG, 20230821
"""

import numpy as np
import matplotlib.pyplot as plt


def rastrigin(x: float, y: float):
    """
    evaluates Rastrigin's function in 2D
    :param x:
    :param y:
    :return: z value of Rastrigin function
    """
    z = 20 + x ** 2 - 10 * np.cos(2 * np.pi * x) + y ** 2 - 10 * np.cos(2 * np.pi * y)
    return z


def rastrigin_taking_2d_list(coordinates: list):
    """
    same function as rastrigin, just another input format.
    :param coordinates: list, len(coordinates) must be equal to 2. coordinates = [x, y]
    :return: z value of Rastrigin function
    """
    if len(coordinates) != 2:
        raise ValueError("Function 'rastrigin_taking_2d_list' takes as argument a list of length 2.")
    return rastrigin(coordinates[0], coordinates[1])


def rastrigin_plot_in_3d():
    x = np.linspace(-5, 5, 1000)
    y = np.linspace(-5, 5, 1000)
    X, Y = np.meshgrid(x, y)

    # Calculate the Z values using a function (e.g., Rastrigin's function)
    Z = rastrigin(X, Y)

    # Create a 3D plot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Plot the surface
    surface = ax.plot_surface(X, Y, Z, cmap='viridis')

    # Add labels and title
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title("Rastrigin's function (two arguments)")

    # Add colorbar
    fig.colorbar(surface, ax=ax, shrink=0.5, aspect=10)

    # Show the plot
    plt.show()


if __name__ == '__main__':
    rastrigin_plot_in_3d()
