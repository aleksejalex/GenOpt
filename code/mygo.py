"""


"""

import random
import numpy as np
from rastrigin_fction import rastrigin_taking_2d_list

my_population_set = {1, 2, 3, -45.3}
my_population = list(my_population_set)


def generate_random_vector(length: int, min_value, max_value, population_type: str):
    """
    generates a vector of rnd elements (each element uniformly distributed)
    :param length:
    :param min_value:
    :param max_value:
    :param population_type:
    :return:
    """
    if population_type == 'bool':
        return [random.randint(0, 1) for _ in range(length)]
    if population_type == 'int':
        return [random.randint(min_value, max_value) for _ in range(length)]
    if population_type == 'float':
        return [random.uniform(min_value, max_value) for _ in range(length)]
    else:
        raise ValueError("Population type has to be in set { 'bool', 'int', 'float' }. ")


def sort_by_criteria(population, criteria, descending: bool = True, additional_vars=None):
    if additional_vars is None:
        additional_vars = []
    sorted_population = sorted(population, key=criteria, reverse=descending)
    # This 'reverse=True' means the list will be sorted in descending order according to specified criteria (aka key)
    return sorted_population


def generate_population(num_of_elements: int, length_of_element: int, population_type: str = 'bool', min_value=0,
                        max_value=1):
    """
    generates (ORDERED) population is sense of GO
    :param max_value:
    :param min_value:
    :param population_type:
    :param num_of_elements: how many things are in population
    :param length_of_element: length of each element of the population
    :return: population (list)
    """
    population = list()
    for _ in range(num_of_elements):
        population.append(generate_random_vector(length_of_element, min_value, max_value, population_type))
    population = sort_by_criteria(population, rastrigin_taking_2d_list, descending=False)  # descending=False,
    # because we are searching for minimum of Rastrigin function, not maximum. Later this can be added as external
    # argument (minimise/maximalise)
    return population


def choose_parent(population: list):
    """
    returns randomly chosen parent from the population
    :param population: (list of elements)
    :return:
    """
    parent = random.choice(population)
    return parent


def crossover(father, mother, prob_crossover: float):
    """
    with probability prob_crossover child will have MALE gene
    with probability (1-prob_crossover) child will have FEMALE gene
    :param father:
    :param mother:
    :param prob_crossover: probability (between 0 and 1)
    :return: child
    """
    if prob_crossover > 1 or prob_crossover < 0:
        raise ValueError("Probability must be <= 1 and >= 0")
    if len(father) != len(mother):
        raise RuntimeError("'mother' and 'father' have to be the same size.")
    child = list()
    for j in range(len(father)):
        curr_num = random.uniform(min(father[j], mother[j]), max(father[j], mother[j]))
        child.append(curr_num)
    return child


def mutate(child, p_mut: float, mutation_step: float = 1):
    """
    makes mutation of inputed child.
    :param child:
    :param p_mut: zero means no mutation, just keep the same. 1 means surely change every element by the 'mutation_step'
    :param mutation_step: if gene is doing to mutate, this is the small change that will occur
    :return:
    """
    if p_mut > 1 or p_mut < 0:
        raise ValueError("Probability must be <= 1 and >= 0")
    for j in range(len(child)):
        p = random.uniform(0, 1)
        if p > p_mut:
            child[j] = child[j]
        else:
            child[j] = np.abs(child[j] - mutation_step)
    return child


def generate_hyperpopulation(population, criteria_for_sorting, num_of_iter=10, prob_crossover=0.5, p_mut=0.5, mutation_step = 0.4):
    """
    uses several functions defined above (file 'mygo.py'), generates hyperpopulation (that needs to be cut)
    contains: choice of parents, crossover, mutation
    :param criteria_for_sorting: function handler (in python - funciton by itself).
           should take 2 float arguments to be able to assign for each 'x' and 'y' a value 'z'
    :param population:
    :param num_of_iter: how many children we should make by mutations
    :param prob_crossover: probability of crossover happening (=P[child will have MALE gene])
    :param p_mut: probability of mutation happenng
    :return: the hyperpopulation (type=list)
    """
    if num_of_iter < len(population):
        num_of_iter = len(population) + 1
    hyperpopulation = list()
    for _ in range(num_of_iter):
        father = choose_parent(population)
        mother = choose_parent(population)
        child = crossover(father, mother, prob_crossover)
        mutated_child = mutate(child, p_mut, mutation_step=mutation_step)
        hyperpopulation.append(mutated_child)
    hyperpopulation = sort_by_criteria(hyperpopulation, criteria_for_sorting)
    return hyperpopulation


def trim_hyperpopulation(hyperpopulation: list, num_of_elements: int):
    """
    Trims given hyperpopulation to given size, so it has only 'num_of_elements' elements.
    :param hyperpopulation:
    :param num_of_elements:
    :return:
    """
    if len(hyperpopulation) <= num_of_elements:
        trimmed_population = hyperpopulation
    else:
        trimmed_population = hyperpopulation[:num_of_elements]  # trims the list
    return trimmed_population


def print_z_values(population):
    """
    this function for given population returns a list of evaluated values (in the same order as inputted list)
    :param population:
    :return:
    """
    return [rastrigin_taking_2d_list(coords) for coords in population]



if __name__ == '__main__':
    """
     main 'function' for brief testing of GO, won't run in case of importing this file as a package
    """
    N = 3
    popul = generate_population(num_of_elements=N, length_of_element=2, population_type='float', min_value=-5,
                                max_value=5)
    print(popul)
    # print(f'parent = {choose_parent(popul)}')
    # father = choose_parent(popul)
    # mother = choose_parent(popul)
    # print(f'father = {father}')
    # print(f'mother = {mother}')
    # child = crossover(father, mother, 0.5)
    # print(f' child = {child}')
    # mutated_child = mutate(child, 0.5, mutation_step=0.1)
    # print(f'mchild = {mutated_child}')
    hypopul = generate_hyperpopulation(popul, rastrigin_taking_2d_list, num_of_iter=10)
    print(f'hypopul = {hypopul}')

    # just for debugging:
    print(print_z_values(hypopul))
    trimedpopul = trim_hyperpopulation(hypopul, num_of_elements=N)
    print(f'trimedhypopul = {trimedpopul}')
    print(print_z_values(trimedpopul))
