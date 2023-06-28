# The greedy method can be built in both iteration and recursion. In iteration, the algorithm would repeatedly choose the next best option until it reaches a stopping condition. In recursion, the algorithm would call itself recursively to find the next best option, until it reaches a base case.
def knapsack(items, capacity):
  """
  Finds the subset of items that has the maximum total value and fits in the knapsack.

  Args:
    items: A list of items, where each item has a value and a weight.
    capacity: The capacity of the knapsack.

  Returns:
    A list of items that have the maximum total value and fits in the knapsack.
  """

  # Initialize a solution set.
  solution = []

  # Iterate over the items.
  for item in items:
    # If the item fits in the knapsack, add it to the solution set.
    if item.weight <= capacity:
      solution.append(item)
      capacity -= item.weight

  return solution

def knapsack(items, capacity, solution):
  """
  Finds the subset of items that has the maximum total value and fits in the knapsack.

  Args:
    items: A list of items, where each item has a value and a weight.
    capacity: The capacity of the knapsack.
    solution: A list of items that have already been added to the solution.

  Returns:
    A list of items that have the maximum total value and fits in the knapsack.
  """

  # Base case: If the capacity is 0, return an empty solution.
  if capacity == 0:
    return solution

  # Recursive case: Find the best item that fits in the knapsack and add it to the solution.
  best_item = None
  for item in items:
    if item.weight <= capacity and (best_item is None or item.value > best_item.value):
      best_item = item

  # Recursively call the function with the remaining items and the updated solution.
  return knapsack(items[items.index(best_item) + 1:], capacity - best_item.weight, solution + [best_item])
