There are two common methods for building graph traversal: recursion and iteration.

#**Recursion:** In recursion, the algorithm calls itself to traverse the graph. The algorithm starts at a vertex and recursively traverses all of its neighbors. If a neighbor has not been visited, then the algorithm calls itself again to traverse that neighbor. This process continues until all vertices in the graph have been visited.

#**Iteration:** In iteration, the algorithm uses a stack to traverse the graph. The algorithm starts by pushing the initial vertex onto the stack. Then, it repeatedly pops the top vertex off the stack and visits it. If the vertex has any unvisited neighbors, then the algorithm pushes those neighbors onto the stack. This process continues until the stack is empty, which means that all vertices in the graph have been visited.

#Here is an example of how to implement a recursive graph traversal algorithm:

```python
def recursive_graph_traversal(graph, vertex):
  """Traverses the graph recursively, starting from the given vertex."""
  if vertex in graph:
    for neighbor in graph[vertex]:
      recursive_graph_traversal(graph, neighbor)

def iterative_graph_traversal(graph, vertex):
  """Traverses the graph iteratively, starting from the given vertex."""
  stack = [vertex]
  while stack:
    vertex = stack.pop()
    for neighbor in graph[vertex]:
      if neighbor not in stack:
        stack.append(neighbor)
```

#The recursive algorithm is more concise, but it can be less efficient for large graphs. The iterative algorithm is more verbose, but it can be more efficient for large graphs.

#The choice of which method to use depends on the specific problem being solved, and the performance requirements of the algorithm. For example, if the algorithm needs to be able to traverse a large graph quickly, then the iterative method might be a better choice. However, if the algorithm needs to be able to be written in a concise way, then the recursive method might be a better choice.
