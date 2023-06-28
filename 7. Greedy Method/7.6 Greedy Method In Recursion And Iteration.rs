fn knapsack(items: Vec<Item>, capacity: u32) -> Vec<Item> {
  // Sort the items by their value per unit weight.
  items.sort_by(|a, b| a.value / a.weight.cmp(&b.value / b.weight));

  // Initialize a solution set.
  let mut solution = Vec::new();

  // Iterate over the items.
  for item in items {
    // If the item fits in the knapsack, add it to the solution set.
    if item.weight <= capacity {
      solution.push(item);
      capacity -= item.weight;
    }
  }

  // Return the solution set.
  solution
}

// This code first sorts the items by their value per unit weight. This ensures that the algorithm will always choose the items that have the maximum total value, even if they do not necessarily fit in the knapsack.

//The code then iterates over the items. For each item, the code checks if the item fits in the knapsack. If the item fits, the code adds it to the solution set and decrements the capacity by the item's weight.

//The code continues iterating over the items until the capacity is 0 or there are no more items to consider. The code then returns the solution set.

//This code is not guaranteed to find the optimal solution to the knapsack problem, but it is often able to find a good solution quickly.
