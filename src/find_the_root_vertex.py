def bfs(graph, start):
    queue = [start]
    visited = {node: False for node in graph}
    visited[start] = True
    reach_count = 1 
    
    while queue:
        vertex = queue.pop(0)
        for neighbour in graph[vertex]:
            if not visited[neighbour]:
                visited[neighbour] = True
                queue.append(neighbour)
                reach_count += 1

    return reach_count


def find_root_vertex(graph):
    n = len(graph)  
    for vertex in graph:
        if bfs(graph, vertex) == n:
            return vertex
    return -1


def read_adj_list_from_file(file_path):
    adj_list = {}
    with open(file_path, 'r') as f:
        for line in f:
            parts = line.strip().split(',')
            vertex = int(parts[0])
            edges = list(map(int, parts[1:]))
            adj_list[vertex] = edges

    return adj_list

def write_root_vertex_to_file(file_path, root_vertex):
    with open(file_path, 'w') as f:
        f.write(str(root_vertex))

file_path = r'C:\Users\Acer\Documents\ПРОГРАМУВАННЯ 1 курс 2 семестр\LABA5\input.txt'        
adj_list = read_adj_list_from_file(file_path)
root_vertex = find_root_vertex(adj_list)
output_file_path = 'output.txt'
write_root_vertex_to_file(output_file_path, root_vertex)
