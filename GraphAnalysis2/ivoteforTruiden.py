result = ""


def findPath(graph, currentVertex, counter):
    global result
    currentList = graph.get(currentVertex)
    if counter == 13:
        return 1
    else:
        if currentList:
            for j in currentList:
                if currentVertex != j and j not in visited:
                    result += str(j) + "   "
                    return findPath(graph, j, counter + 1)
            return None
        else:
            return None


def buildAnswer(string):
    list = string.split()
    answer = list[0] + " -> "
    for i in range(1, len(list) - 2):
        answer += list[i] + " - "
    answer += list[len(list) - 2] + " -> " + list[len(list) - 1]
    return answer


with open("as20000102.txt") as f:
    graph = dict()
    string = None
    visited = []
    currentVertex = None
    while True:
        string = f.readline()[:-1]
        if len(string.split()) < 3:
            break
    while True:
        if not graph.get(string.split()[0]):
            graph.update({string.split()[0]: string.split()[1]})
        else:
            if type(graph.get(string.split()[0])) == type([]):
                vertexes = graph.get(string.split()[0])
                vertexes.append(string.split()[1])
                graph.update({string.split()[0]: vertexes})
            else:
                vertexes = []
                vertexes.append(graph.get(string.split()[0]))
                graph.update({string.split()[0]: vertexes})
        string = f.readline()[:-1]
        if string == "" or string == " ":
            break
f.close()
for i in graph.keys():
    findPath(graph, i, 1)
    if len(result.split()) == 12:
        print(buildAnswer(result))
    result = ""
    for j in graph.get(i):
        findPath(graph, j, 1)
        if len(result.split()) == 10:
            print(buildAnswer(result))
        result = ""
