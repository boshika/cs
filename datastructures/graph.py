class Graph:
  def __init__(self, nodes):
    self.nodes = nodes
    self.list = {}

    for n in self.nodes:
      self.list[n] = []

  def p(self):
    for node in self.nodes:
      print(node, self.list[node])

  def add_edges(self, u, v):
    self.list[u].append(v)
    self.list[v].append(u)


adj = Graph(['A', 'B', 'C', 'D', 'E'])
adj.add_edges('A', 'B')
adj.add_edges('B', 'C')
adj.add_edges('A', 'D')
adj.add_edges('D', 'E')
adj.p()

