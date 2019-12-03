
class Edge:

    def __init__(self, item, next, weight):
        self.item = item
        self.weight = weight
        self.next = next


class GraphAL:

    def __init__(self, initial_num_vertices, is_directed):
        self.adj_list = [None] * initial_num_vertices
        self.is_directed = is_directed

    def is_valid_vertex(self, u):
        return 0 <= u < len(self.adj_list)

    def add_vertex(self):
        self.adj_list.append(None)
        return len(self.adj_list) - 1

    def add_edge(self, src, dest, weight = 1.0):
        if not self.is_valid_vertex(src) or not self.is_valid_vertex(dest):
            return

        self.adj_list[src] = Edge(dest, self.adj_list[src], weight)

        if not self.is_directed:
            self.adj_list[dest] = Edge(src, self.adj_list[dest], weight)

    def remove_edge(self, src, dest):
        self.__remove_directed_edge(src, dest)

        if not self.is_directed:
            self.__remove_directed_edge(dest, src)

    def __remove_directed_edge(self, src, dest):
        if not self.is_valid_vertex(src) or not self.is_valid_vertex(dest):
            return

        if self.adj_list[src] is None:
            return

        if self.adj_list[src].item == dest:
            self.adj_list[src] = self.adj_list[src].next
        else:
            prev = self.adj_list[src]
            curr = self.adj_list[src].next

            while curr is not None:
                if curr.item == dest:
                    prev.next = curr.next
                    return

                prev = prev.next
                curr = curr.next

    def get_num_vertices(self):
        return len(self.adj_list)

    def get_vertices_reachable_from(self, src):
        reachable_vertices = set()

        tmp = self.adj_list[src]

        while tmp is not None:
            reachable_vertices.add(tmp.item)
            tmp = tmp.next

        return reachable_vertices


    def get_vertices_that_point_to(self, dest):
        vertices = set()

        for i in range(len(self.adj_list)):
            tmp = self.adj_list[i]

            while tmp is not None:
                if tmp.item == dest:
                    vertices.add(i)
                    break

                tmp = tmp.next

        return vertices

    def get_highest_cost_edge(self):
        most = 0
        for node in self.adj_list:
            temp = node
            while temp != None:
                most = max(most, temp.weight)
                temp = temp.next
        return most

    def get_num_edges (self):
        counter = 0
        for node in self.adj_list:
            temp = node
            while temp != None:
                counter += 1
                temp = temp.next
        return counter

    def get_edge_weight(self, src, dest): # Calculates the weight of the edge from src to dest
        if not self.is_valid_vertex(src) or not self.is_valid_vertex(dest):
            return 0
        temp = self.adj_list[src]
        while temp.item != dest:
            temp =temp.next
        return temp.weight

    def reverse_edges(self):
        if not self.is_directed:
            return
        temp_list = [None] * len(self.adj_list)
        for i in range(len(self.adj_list)):
            temp = self.adj_list[i]
            while temp != None:
                temp_list[temp.item] = \
                    Edge(i, temp_list[temp.item], temp.weight)
                temp = temp.next
        self.adj_list = temp_list

    def num_self_edges(self):
        counter = 0
        for i in range(len(self.adj_list)):
            temp = self.adj_list[i]
            while temp != None:
                if temp.item == i:
                    counter += 1
                temp = temp.next
        return counter

    def get_adj_vertices(self, vertex):
        if vertex >= len(self.adj_list):
            return None
        adj = list()
        temp = self.adj_list[vertex]
        while temp != None:
            adj.append(temp.item)
            temp = temp.next
        return adj