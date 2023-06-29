import random

def greedy_algorithm(items, capacity):
  """
  Solves the knapsack problem using a greedy algorithm.

  Args:
    items: A list of items, where each item is a tuple of (value, weight).
    capacity: The capacity of the knapsack.

  Returns:
    A list of items that are included in the knapsack.
  """

  included_items = []
  current_weight = 0

  for item in items:
    if current_weight + item[1] <= capacity:
      included_items.append(item)
      current_weight += item[1]

  return included_items


def heuristic_algorithm(items, capacity):
  """
  Solves the knapsack problem using a heuristic algorithm.

  Args:
    items: A list of items, where each item is a tuple of (value, weight).
    capacity: The capacity of the knapsack.

  Returns:
    A list of items that are included in the knapsack.
  """

  included_items = []
  current_weight = 0

  for item in items:
    if current_weight + item[1] <= capacity:
      included_items.append(item)
      current_weight += item[1]
    else:
      break

  return included_items


def main():
  items = [(10, 5), (20, 10), (30, 15)]
  capacity = 20

  included_items = greedy_algorithm(items, capacity)
  print("The greedy algorithm solution is:")
  for item in included_items:
    print(item)

  included_items = heuristic_algorithm(items, capacity)
  print("The heuristic algorithm solution is:")
  for item in included_items:
    print(item)


if __name__ == "__main__":
  main()

# This code first defines two functions called greedy_algorithm() and heuristic_algorithm(). Both functions take two arguments: items and capacity. items is a list of items, where each item is a tuple of (value, weight). capacity is the capacity of the knapsack.

#The greedy_algorithm() function then works by iterating through the list of items. For each item, it checks if the current weight of the knapsack plus the weight of the item is less than or equal to the capacity of the knapsack. If it is, then the item is included in the knapsack and the current weight of the knapsack is increased by the weight of the item.

#The heuristic_algorithm() function works similarly to the greedy_algorithm() function, but it stops iterating through the list of items once the knapsack is full.

#The main() function then calls the greedy_algorithm() function and the heuristic_algorithm() function with the list of items and the capacity of the knapsack. The main() function then prints the solutions that are found by each algorithm.

##To run this code, you can save it as a Python file and then run it from the command line. For example, if you save the code as heuristic_algorithm.py, you can run it by typing the following command into the command line:
