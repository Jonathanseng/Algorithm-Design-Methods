fn local_search(initial_solution: Vec<i32>, neighborhood_function: &Fn(Vec<i32>) -> Vec<Vec<i32>>, objective_function: &Fn(Vec<i32>) -> i32) -> Vec<i32> {
  let mut current_solution = initial_solution;
  let mut best_solution = current_solution;

  loop {
    let neighboring_solutions = neighborhood_function(&current_solution);
    let mut best_neighboring_solution = None;
    let mut best_neighboring_solution_value = i32::MIN;

    for neighboring_solution in neighboring_solutions {
      let neighboring_solution_value = objective_function(&neighboring_solution);
      if neighboring_solution_value > best_neighboring_solution_value {
        best_neighboring_solution = neighboring_solution;
        best_neighboring_solution_value = neighboring_solution_value;
      }
    }

    if best_neighboring_solution.is_none() {
      break;
    }

    if objective_function(&best_neighboring_solution) > objective_function(&current_solution) {
      current_solution = best_neighboring_solution;
    }
  }

  return best_solution;
}

fn local_search_recursive(initial_solution: Vec<i32>, neighborhood_function: &Fn(Vec<i32>) -> Vec<Vec<i32>>, objective_function: &Fn(Vec<i32>) -> i32) -> Vec<i32> {
  if !neighborhood_function(&initial_solution).is_empty() {
    let best_neighboring_solution = neighborhood_function(&initial_solution).iter().min_by_key(|neighboring_solution| objective_function(neighboring_solution)).unwrap();
    return local_search_recursive(best_neighboring_solution, neighborhood_function, objective_function);
  } else {
    return initial_solution;
  }
}

# This code is similar to the Python code that I provided earlier. The main difference is that the Rust code uses functions instead of methods.

#The local_search function implements the local search algorithm iteratively. The local_search_recursive function implements the local search algorithm recursively.

#The neighborhood_function takes a solution as input and returns a set of neighboring solutions. The objective_function takes a solution as input and returns its objective value.

#The local_search and local_search_recursive functions both return the best solution found by the local search algorithm. The local_search function iterates through the neighborhood of the current solution, while the local_search_recursive function recursively searches the neighborhood of the current solution.
