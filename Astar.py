#A star algo implementation

def getHeuristics(n):
  return heuristics.get(n, float('inf'))


def getNeighbors(v):
  return graph.get(v, [])


def astar(start, goal):
  open_set = {start}
  g = {start:0}
  parents = {start:start}

  while open_set:
    n = min(open_set, key=lambda x: g[x]+ getHeuristics(x))

    if n == goal:
      path = []
      while parents[n] != n:
        path.append(n)
        n = parents[n]
      path.append(start)
      path.reverse()

      print("Path found: ")
      print('->'.join(path))
      return path

    open_set.remove(n)
    for m, weight in getNeighbors(n):
      tentative_g = g[n] + weight
      if m not in g or tentative_g<g[m]:
        g[m] = tentative_g
        parents[m] = n
        open_set.add(m)

  print("No path found")
  return None
  



graph = {
    'S': [('A', 1)],         #neighbor with edge weight
    'A': [('B', 3), ('C', 1)],
    'B': [('D', 3)],
    'C': [('D', 1), ('G', 2)],
    'D': [('G', 3)],
    'G': None
}

heuristics = {
    'S': 4,
    'A': 2,
    'B': 6,
    'C': 2,
    'D': 3,
    'G': 0
}

astar('S', 'G')
