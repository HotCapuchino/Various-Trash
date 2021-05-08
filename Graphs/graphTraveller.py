import sys


def firstTask():
    n = int(input('Введите количество вершин: '))
    if n < 3:
        print('Слишком мало вершин!')
        sys.exit(-1)
    matrix = []
    print('Введите матрицу смежности НЕВЗВЕШЕННОГО графа:', end='\n')
    for i in range(n):
        try:
            user_str = list(map(int, input().split(' ')))
            for i in range(len(user_str)):
                if user_str[i] < 0:
                    raise Exception('Расстояние не может быть отрицательным')
                elif user_str[i] > 1:
                    user_str[i] = 1
            if len(user_str) > n:
                matrix.append(user_str[:n])
            elif len(user_str) < n:
                matrix.append(user_str + ([0] * (n - len(user_str))))
            else:
                matrix.append(user_str)
        except TypeError:
            print('Cтрока содержит недопустимые симвлолы!')
            sys.exit(-1)
    target_vertex = int(input('Введите вершину, с которой начнется обход графа:'))
    if target_vertex > n or target_vertex == 0:
        print('Вершины с таким номером нет в графе!')
        sys.exit(-1)
    calculate_distances(target_vertex - 1, matrix)


def calculate_distances(start_vertex, matrix):
    minimal_pathes = [None] * len(matrix[0])
    minimal_pathes[start_vertex] = 0
    queue = [start_vertex]
    current_queue_index = 0
    while current_queue_index < len(queue):
        current_vertex = queue[current_queue_index]
        current_queue_index += 1
        for j in range(len(matrix[current_vertex])):
            if minimal_pathes[j] is None and matrix[current_vertex][j] != 0:
                minimal_pathes[j] = minimal_pathes[current_vertex] + 1
                queue.append(j)
    for j in range(len(minimal_pathes)):
        if minimal_pathes[j] is None:
            print(f'There\'s no way to get to {j + 1} vertex!')
        else:
            print(f'{j + 1}: {minimal_pathes[j]}')