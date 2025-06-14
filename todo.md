Put comparison overloading to all data structures
Add enumeration and other features in HashTable

  def get_edges(self, undirected=False):
        edges = []
        seen = set()

        for u in self.adj_list:
            for v, w in self.adj_list[u]:
                if undirected and (v, u, w) in seen:
                    continue
                edges.append((u, v, w))
                seen.add((u, v, w))

        return edges

