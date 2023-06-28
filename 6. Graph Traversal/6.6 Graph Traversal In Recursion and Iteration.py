from collections import defaultdict

def recursive_graph_traversal(graph, vertex):
  """Traverses the graph recursively, starting from the given vertex."""
  if vertex in graph:
    print(vertex)
    for neighbor in graph[vertex]:
      recursive_graph_traversal(graph, neighbor)

def iterative_graph_traversal(graph, vertex):
  """Traverses the graph iteratively, starting from the given vertex."""
  visited = set()
  stack = [vertex]
  while stack:
    vertex = stack.pop()
    if vertex not in visited:
      visited.add(vertex)
      print(vertex)
      for neighbor in graph[vertex]:
        if neighbor not in visited:
          stack.append(neighbor)

def main():
  graph = defaultdict(list)
  graph[0].append(1)
  graph[0].append(2)
  graph[1].append(2)
  graph[2].append(0)
  graph[2].append(3)
  graph[3].append(3)

  print("Recursive graph traversal:")
  recursive_graph_traversal(graph, 0)

  print("\nIterative graph traversal:")
  iterative_graph_traversal(graph, 0)

if __name__ == "__main__":
  main()

# This code defines two functions: recursive_graph_traversal() and iterative_graph_traversal(). The recursive_graph_traversal() function traverses the graph recursively, starting from the given vertex. The iterative_graph_traversal() function traverses the graph iteratively, starting from the given vertex.

#The main function creates a graph and then calls the two traversal functions. The output of the program is:


