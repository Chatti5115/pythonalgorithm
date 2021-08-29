
graph = dict()

graph['A'] = ['B', 'C']
graph['B'] = ['A', 'D']
graph['C'] = ['A', 'G', 'H', 'I']
graph['D'] = ['B', 'E', 'F']
graph['E'] = ['D']
graph['F'] = ['D']
graph['G'] = ['C']
graph['H'] = ['C']
graph['I'] = ['C', 'J']
graph['J'] = ['I']


data = [1,2,3]
data.extend([4,5])
print(data)


# def bfs(graph, start_node):
#     visited = list()
#     need_visit = list()
#
#     need_visit.append(start_node)
#
#     while need_visit:
#         node = need_visit.pop(0)
#         if node not in visited:
#             visited.append(node)
#             need_visit.extend(graph[node])
#
#     return visited
#
#
# print(bfs(graph, 'A'))



#시간 복잡도
def bfs(graph, start_node):
    visited = list()
    need_visit = list()
    need_visit.append(start_node)
    count = 0
    while need_visit:
        count += 1
        node = need_visit.pop(0)
        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node])
    print(count)
    return visited

print(bfs(graph, 'A'))

def bfs(graph, start_node):
    visited = list()
    need_visit = list()
    need_visit.append(start_node)
    count = 0
    while need_visit:
        count += 1
        node = need_visit.pop(0)
        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node])
    print(count)
    return visited

def bfs(graph, start_node):
    visitied = list()
    need_visit = list()
    need_visit.append(start_node)
    count = 0
    while need_visit:
        count += 1
        node = need_visit.pop(0)
        if node not in visitied:
            visitied.append(node)
            need_visit.extend(graph[node])
    print(count)
    return visitied