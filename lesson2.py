from queue import Queue


def task1_2():
    def topological_sort(graph: list[list[int]]):
        visit = [False] * len(graph)
        order = []

        def dfs(vertex: int):
            queue = Queue()
            queue.put(vertex)

            while not queue.empty():
                v = queue.get()
                queue.put(v)

                visit[v] = True

                for u in graph[v]:
                    if not visit[u]:
                        queue.put(u)
                
                order.append(queue.get())
            
        
        for vertex in range(len(graph)):
            if not visit[vertex]:
                dfs(vertex)
        
        return order[::-1]


    vertices = [
        "Пиджак", 
        "Часы",
        "Брюки",
        "Рубашка",
        "Трусы",
        "Носки",
        "Туфли",
        "Галстук",
        "Ремень"
    ]

    adj_list = [[], [], [6, 8], [8, 7], [2, 6], [6], [], [0], [0]]

    print(*map(lambda x: vertices[x], topological_sort(adj_list)))


def task4():
    def findCircleNum(isConnected):
        graph = []

        for i in isConnected:
            v = []

            for j in range(len(i)):
                if i[j]:
                    v.append(j)

            graph.append(v)

        def topological_sort(graph):
            visit = [False]*len(g)
            amount_elem = 0

            def dfs(v):
                visit[v] = True
                for u in graph[v]:
                    if not visit[u]:
                        dfs(u)

            for i in range(len(graph)):
                if not visit[i]:
                    dfs(i)
                    amount_elem += 1

            return amount_elem

        answ = topological_sort(graph)
        return answ