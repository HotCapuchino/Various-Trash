with open("as20000102.txt") as f:
    amount = 0
    graph = ""
    string = ""
    top_ten_values = [0] * 10
    top_ten_indexes = [0] * 10
    while True:
        string = f.readline()[:-1]
        if len(string.split()) < 3:
            break
        if "Nodes:" in string:
            amount = int(string.split()[2])
            graph = [0] * amount
            # print(graph)
    graph[int(string.split()[0])] += 1
    graph[int(string.split()[1])] += 1
    while True:
        string = f.readline()[:-1]
        if string == " " or string == "":
            break
        graph[int(string.split()[0])] += 1
        graph[int(string.split()[1])] += 1
    for i in range(len(graph)):
        if graph[i] > top_ten_values[0]:
            for j in range(len(top_ten_values)):
                if graph[i] < top_ten_values[j]:
                    for k in range(j):
                        top_ten_values[k] = top_ten_values[k + 1]
                        top_ten_indexes[k] = top_ten_indexes[k + 1]
                    top_ten_values[j - 1] = graph[i]
                    top_ten_indexes[j - 1] = i
                    break
                elif j == len(top_ten_values) - 1:
                    for k in range(j):
                        top_ten_values[k] = top_ten_values[k + 1]
                        top_ten_indexes[k] = top_ten_indexes[k + 1]
                    top_ten_values[j] = graph[i]
                    top_ten_indexes[j] = i
                    break
print("Top Ten Nodes:")
for i in range(len(top_ten_values) - 1, -1, -1):
    print("Node Number: " + str(top_ten_indexes[i]) + " -> " + "Amount of edges: " + str(top_ten_values[i]))