def genetic_algorithm(population, fitness_function):
  """
  Finds the best solution in a population of chromosomes using a genetic algorithm.

  Args:
    population: A list of chromosomes.
    fitness_function: A function that takes a chromosome as input and returns its fitness.

  Returns:
    The chromosome with the highest fitness.
  """

  if len(population) == 1:
    return population[0]

  parents = select_parents(population, fitness_function)
  children = crossover(parents)
  children = mutate(children)

  return genetic_algorithm(children, fitness_function)

def select_parents(population, fitness_function):
  """
  Selects a pair of parents from a population of chromosomes.

  Args:
    population: A list of chromosomes.
    fitness_function: A function that takes a chromosome as input and returns its fitness.

  Returns:
    A pair of chromosomes.
  """

  parents = []
  for _ in range(2):
    best_chromosome = None
    best_fitness = -float("inf")
    for chromosome in population:
      fitness = fitness_function(chromosome)
      if fitness > best_fitness:
        best_chromosome = chromosome
        best_fitness = fitness
    parents.append(best_chromosome)

  return parents

def crossover(parents):
  """
  Produces a new child from two parents.

  Args:
    parents: A list of two chromosomes.

  Returns:
    A new chromosome.
  """

  child = []
  for index in range(len(parents[0])):
    if random.random() > 0.5:
      child.append(parents[0][index])
    else:
      child.append(parents[1][index])

  return child

def mutate(children):
  """
  Mutates a child chromosome.

  Args:
    children: A list of chromosomes.

  Returns:
    A new list of chromosomes.
  """

  for child in children:
    if random.random() < 0.01:
      index = random.randrange(len(child))
      child[index] = random.randrange(0, 1)

  return children
