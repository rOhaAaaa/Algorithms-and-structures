import sys

def dfs(node, graph, visited, tribe):
    stack = [node]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            tribe.append(vertex)
            for neighbour in graph[vertex]:
                if neighbour not in visited:
                    stack.append(neighbour)

def solve(file_path):
    with open(file_path, 'r') as file:
        data = file.read().split('\n')
    n = int(data[0].strip())
    pairs = [tuple(map(int, line.split())) for line in data[1:n+1] if line.strip()]
    
    graph = {}
    for a, b in pairs:
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []
        graph[a].append(b)
        graph[b].append(a)

    visited = set()
    tribes = []
    for person in graph:
        if person not in visited:
            tribe = []
            dfs(person, graph, visited, tribe)
            tribes.append(tribe)

    count_boys = []
    count_girls = []
    for tribe in tribes:
        boys = sum(1 for x in tribe if x % 2 != 0)
        girls = sum(1 for x in tribe if x % 2 == 0)
        count_boys.append(boys)
        count_girls.append(girls)

    total_pairs = 0
    for i in range(len(tribes)):
        for j in range(i + 1, len(tribes)):
            total_pairs += count_boys[i] * count_girls[j] + count_boys[j] * count_girls[i]

    print(total_pairs)

if __name__ == "__main__":
    file_path = r'tests\resources\input1.txt'
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
    solve(file_path)


