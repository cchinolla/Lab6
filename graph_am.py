class GraphAM:

    def __init__(self, vertices, weighted=False, directed=False):
        self.am = []

        for i in range(vertices):  # Assumption / Design Decision: 0 represents non-existing edge
            self.am.append([0] * vertices)

        self.directed = directed
        self.weighted = weighted
        self.representation = 'AM'

    def is_valid_vertex(self, u):
        return 0 <= u < len(self.am)

    def insert_vertex(self):
        for lst in self.am:
            lst.append(0)

        new_row = [0] * (len(self.am) + 1)  # Assumption / Design Decision: 0 represents non-existing edge
        self.am.append(new_row)

        return len(self.am) - 1  # Return new vertex id

    def insert_edge(self, src, dest, weight=1):
        if not self.is_valid_vertex(src) or not self.is_valid_vertex(dest):
            return

        self.am[src][dest] = weight

        if not self.directed:
            self.am[dest][src] = weight

    def delete_edge(self, src, dest):
        self.insert_edge(src, dest, 0)

    def num_vertices(self):
        return len(self.am)

    def vertices_reachable_from(self, src):
        reachable_vertices = set()

        for i in range(len(self.am)):
            if self.am[src][i] != 0:
                reachable_vertices.add(i)

        return reachable_vertices


