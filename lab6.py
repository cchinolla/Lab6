from GraphAL import GraphAL
from dsf import DisjointSetForest
from collections import deque


def topological_sort(graph):

    if graph.adj_list is None:  # Base case
        return None

    all_in_degrees = indegree_vertex(graph)
    sort_result = list()
    queue = deque([])

    for i in range(len(all_in_degrees)):
        if all_in_degrees[i] == 0:
            queue.append(i)

    while len(queue) != 0:
        u = queue.popleft()
        sort_result.append(u)

        for adj_vertex in graph.get_adj_vertices(u):
            all_in_degrees[adj_vertex] -= 1

            if all_in_degrees[adj_vertex] == 0:
                queue.append(adj_vertex)

    if len(sort_result) != len(graph.adj_list):  #check if exists a cycle
        return None

    return sort_result


def kruskal(graph):
    if graph.adj_list is None:
        return None
    edges = list()

    for i in range(len(graph.adj_list)):
        tmp = graph.adj_list[i]
        while tmp is not None:
            edges.append([i, tmp.item, tmp.weight])
            tmp = tmp.next

    def sort_key(elem):
        return elem[2]

    edges = sorted(edges, key=sort_key)
    tree = list()
    dsf = DisjointSetForest(len(graph.adj_list))

    for edge in edges:
        if dsf.find(edge[0]) != dsf.find(edge[1]):
            dsf.union(edge[0], edge[1])
            tree.append(edge)

    return tree


def indegree_vertex(graph):
    if graph.adj_list is None:
        return None
    final = [0] * len(graph.adj_list)
    for i in range(len(graph.adj_list)):
        tmp = graph.adj_list[i]
        while tmp != None:
            final[tmp.item] += 1
            tmp = tmp.next
    return final


def main():
    print("_________________________________")
    print("Topological Sort")
    print()

    graph_topological = GraphAL(initial_num_vertices=6, is_directed=True)
    graph_topological.add_edge(0, 1)
    graph_topological.add_edge(0, 2)
    graph_topological.add_edge(0, 4)
    graph_topological.add_edge(1, 5)
    graph_topological.add_edge(2, 3)
    graph_topological.add_edge(3, 4)
    print("The topological order of the vertices")
    print(topological_sort(graph_topological))

    graph_topological = GraphAL(initial_num_vertices=4, is_directed=True)
    graph_topological.add_edge(0, 1)
    graph_topological.add_edge(0, 2)
    graph_topological.add_edge(1, 3)
    graph_topological.add_edge(3, 2)
    print("The topological order of the vertices")
    print(topological_sort(graph_topological))

    print("_________________________________")
    print("Kruskals Algorithm")

    graph_kruskal = GraphAL(initial_num_vertices = 4, is_directed = False)
    graph_kruskal.add_edge(0, 1, 7.0)
    graph_kruskal.add_edge(1, 2, 3.0)
    graph_kruskal.add_edge(0, 2, 4.0)
    graph_kruskal.add_edge(1, 3, 7.0)
    graph_kruskal.add_edge(2, 3, 1.0)
    graph_kruskal.add_edge(1, 2, 2.0)

    for value in kruskal(graph_kruskal):
        print(value)

    print("testing kruskal's algorithm with another graph")

    graph_kruskal = GraphAL(initial_num_vertices = 5, is_directed = False)
    graph_kruskal.add_edge(0, 1, 7.0)
    graph_kruskal.add_edge(2, 3, 6.0)
    graph_kruskal.add_edge(1, 3, 5.0)
    graph_kruskal.add_edge(1, 2, 4.0)
    graph_kruskal.add_edge(0, 2, 3.0)
    graph_kruskal.add_edge(1, 4, 2.0)
    graph_kruskal.add_edge(3, 4, 1.0)
    for value in kruskal(graph_kruskal):
        print(value)
    print()



main()