use std::collections::HashMap;

fn recursive_graph_traversal(graph: &HashMap<usize, Vec<usize>>, vertex: usize) {
  if let Some(neighbors) = graph.get(&vertex) {
    for neighbor in neighbors {
      recursive_graph_traversal(graph, neighbor)
    }
  }
}

fn iterative_graph_traversal(graph: &HashMap<usize, Vec<usize>>, vertex: usize) {
  let mut stack = vec![vertex];
  while let Some(vertex) = stack.pop() {
    if let Some(neighbors) = graph.get(&vertex) {
      for neighbor in neighbors {
        if !stack.contains(&neighbor) {
          stack.push(neighbor)
        }
      }
    }
  }
}

fn main() {
  let mut graph = HashMap::new();
  graph.insert(0, vec![1, 2]);
  graph.insert(1, vec![2]);
  graph.insert(2, vec![0, 3]);
  graph.insert(3, vec![3]);

  println!("Recursive graph traversal:");
  recursive_graph_traversal(&graph, 0);

  println!("\nIterative graph traversal:");
  iterative_graph_traversal(&graph, 0);
}

// This code defines two functions: recursive_graph_traversal() and iterative_graph_traversal(). The recursive_graph_traversal() function traverses the graph recursively, starting from the given vertex. The iterative_graph_traversal() function traverses the graph iteratively, starting from the given vertex.

//The main function creates a graph and then calls the two traversal functions. The output of the program is:
