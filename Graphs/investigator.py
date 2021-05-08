def secondTask():
    data = None
    with open('./res/square_graph_dataset.txt', 'r') as f:
        data = f.read().split('\n')
    graphs_array = [None] * int(data[0])
    data = data[2:len(data) - 1]
    for i in range(len(data)):
        if len(data[i]) == 0:
            data[i] = 'separator'
    data = (',').join(data).split('separator')
    for i in range(len(data)):
        data[i] = list(filter(lambda elem: len(elem) > 0, data[i].split(',')))
        vertex_amount = int(data[i][0].split()[0])
        matrix = [[0] * vertex_amount] * vertex_amount
        for j in range(1, len(data[i]), 1):
            v1, v2 = int(data[i][j].split()[0]) - 1, int(data[i][j].split()[1]) - 1
            matrix[v1][v2] = 1
            matrix[v2][v1] = 1
        graphs_array[i] = matrix
    with open('./out/results.txt', 'w') as f:
        for i in range(len(graphs_array)):
            f.write(f'{i + 1} Graph has cycles with the length of four: {findCycle(graphs_array[i], 4)}\n')


def findCycle(matrix, cycle_length):
    marked = [False] * len(matrix[0])
    count = 0
    for i in range(len(matrix[0]) - (cycle_length - 1)):
        count = DFS(matrix, marked, cycle_length - 1, i, i, count, len(matrix[0]))
        marked[i] = True
    if count > 0:
        return True
    else:
        return False


def DFS(graph, marked, n, vertex, start, count, vertexes_amount):
    marked[vertex] = True
    if n == 0:
        marked[vertex] = False
        if graph[vertex][start] == 1:
            count = + 1
        return count
    for i in range(vertexes_amount):
        if not marked[i] and graph[vertex][i] == 1:
            count = DFS(graph, marked, n - 1, i, start, count, vertexes_amount)
    marked[vertex] = False
    return count
