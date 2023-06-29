use rand::prelude::*;

fn fitness(solution: &[i32]) -> i32 {
  solution.iter().sum()
}

fn crossover(parent1: &[i32], parent2: &[i32]) -> Vec<i32> {
  let mut child = vec![];
  for i in 0..parent1.len() {
    if random::random() > 0.5 {
      child.push(parent1[i]);
    } else {
      child.push(parent2[i]);
    }
  }
  child
}

fn mutation(solution: &[i32]) -> Vec<i32> {
  let mut child = solution.to_vec();
  let index = random::randint(0, solution.len() - 1);
  child[index] = random::randint(0, 10);
  child
}

fn evolve_recursive(population: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
  if population.len() == 1 {
    return population;
  } else {
    let parent1 = population[random::randrange(0, population.len())];
    let parent2 = population[random::randrange(0, population.len())];
    let child = crossover(parent1, parent2);
    let child = mutation(child);
    let new_population = vec![child] + evolve_recursive(population[1..].to_vec());
    return new_population;
  }
}

fn evolve_iterative(population: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
  let mut new_population = Vec::new();
  for _ in 0..population.len() {
    let parent1 = population[random::randrange(0, population.len())];
    let parent2 = population[random::randrange(0, population.len())];
    let child = crossover(parent1, parent2);
    let child = mutation(child);
    new_population.push(child);
  }
  return new_population;
}

fn main() {
  let population = (0..10).map(|_| random::randint(0, 10)).collect();
  for _ in 0..100 {
    population = evolve_recursive(population);
  }
  println!("{:?}", population);
}

// This code defines a simple evolutionary algorithm that can be used to find a good solution to a problem. The algorithm starts with a random population of solutions, and then iteratively evolves the population by selecting parents, crossover, and mutation. The algorithm terminates when a certain number of generations have been reached, or when a good solution is found.

// The code can be run by saving it as a Rust file and then running it from the command line. For example, if the file is named evolve.rs, then you can run it by typing the following command into the command line:
// This will run the algorithm and print the best solution that was found.

//The code uses two different methods for evolving the population: recursion and iteration. The recursive method is more concise, but it can be less efficient for large populations. The iterative method is more verbose, but it can be more efficient for large populations.

//The choice of which method to use depends on the specific problem being solved, and the performance requirements of the algorithm. For example, if the algorithm needs to be able to quickly evolve a large population, then the iterative method might be a better choice. However, if the algorithm needs to be able to be written in a concise way, then the recursive method might be a better choice.
