# import heapq
#
# queue = []
# graph_data = [[2, 'A'], [5,'B'], [3,'C']]
#
# # for edge in graph_data:
# #     heapq.heappush(queue, edge)
# #
# # for index in range(len(queue)):
# #     print(heapq.heappop(queue))
# #
# # print(queue)
#
#
# for index in range(len(graph_data)):
#     print(heapq.heappop(graph_data))
#
# print(graph_data)
#
#
#
#


# from collections import defaultdict
#
# list_dict = defaultdict(list)
# print(list_dict['key1'])


myedges = [
    (7, 'A', 'B'), (5, 'A', 'D'),
    (8, 'B', 'C'), (9, 'B', 'D'), (7, 'B', 'E'),
    (5, 'C', 'E'),
    (7, 'D', 'E'), (6, 'D', 'F'),
    (8, 'E', 'F'), (9, 'E', 'G'),
    (11, 'F', 'G')
]


# from collections import defaultdict
# from heapq import *
#
# def prim(start_node, edges):
#     mst = list()
#     adjacent_edges = defaultdict(list)
#     for weight, n1, n2, in edges:
#         adjacent_edges[n1].append((weight, n1, n2))
#         adjacent_edges[n2].append((weight, n1, n2))
#
#     connected_node = set(start_node)
#     candidate_edge_list = adjacent_edges[start_node]
#     heapify(candidate_edge_list)
#
#     while candidate_edge_list:
#         weight, n1, n2 = heappop(candidate_edge_list)
#         if n2 not in connected_node:
#             connected_node.add(n2)
#             mst.append((weight, n1, n2))
#
#             for edges in adjacent_edges[n2]:
#                 if edges[2] not in connected_node:
#                     heappush(candidate_edge_list, edges)
#
#     return mst
#
# print(prim('A',myedges))



from heapdict import heapdict

def prim(graph, start):
    mst, keys, pi, total_weight = list(), heapdict(), dict(), 0
    for node in graph.keys():
        keys[node] = float('inf')
        pi[node] = None
    keys[start], pi[start] =0, start

    while keys:
        current_nodes, current_key = keys.popitem()
        mst.append([pi[current_nodes], current_nodes, current_key])
        total_weight += current_key
        for adjacent, weight in mygraph[current_nodes].items():
            if adjacent in keys and weight < keys[adjacent]:
                keys[adjacent] = weight
                pi[adjacent] = current_nodes
    return mst, total_weight

mygraph = {
    'A': {'B': 7, 'D': 5},
    'B': {'A': 7, 'D': 9, 'C': 8, 'E': 7},
    'C': {'B': 8, 'E': 5},
    'D': {'A': 5, 'B': 9, 'E': 7, 'F': 6},
    'E': {'B': 7, 'C': 5, 'D': 7, 'F': 8, 'G': 9},
    'F': {'D': 6, 'E': 8, 'G': 11},
    'G': {'E': 9, 'F': 11}
}
mst, total_weight = prim(mygraph, 'A')
print ('MST:', mst)
print ('Total Weight:', total_weight)