from typing import List


def transpose_graph(graph: List[List[int]]) -> List[List[int]]:
    n = len(graph)
    new_adj = [[] for _ in range(n)]
    for i in range(n):
        for j in graph[i]:
            new_adj[j].append(i)
    return new_adj


def topo_sort(graph: List[List[int]]) -> List[int]:
    n = len(graph)
    visited = [False] * n
    order = []

    def dfs(vert: int):
        visited[vert] = True
        for adj in graph[vert]:
            if not visited[adj]:
                dfs(adj)
        order.append(vert)

    for vert in range(n):
        if not visited[vert]:
            dfs(vert)

    return order[::-1]


def strong_components(graph: List[List[int]]) -> List[int]:
    t = transpose_graph(graph)
    topo_sorted = topo_sort(graph)
    n = len(graph)

    component_index = [-1] * n
    current_comp = 0

    def dfs(vert: int):
        component_index[vert] = current_comp
        for adj in t[vert]:
            if component_index[adj] == -1:
                dfs(adj)

    for vert in topo_sorted:
        if component_index[vert] == -1:
            dfs(vert)
            current_comp += 1

    return component_index


def component_graph(graph, comp_ind):
    comp_n = max(comp_ind)
    comp_adj = [[] for _ in range(comp_n)]

    for vert in range(len(graph)):
        cur_comp = comp_ind[vert]
        for adj in graph[vert]:
            adj_comp = comp_ind[adj]
            if adj_comp != cur_comp and adj_comp not in comp_adj[cur_comp]:
                comp_adj[cur_comp].append(adj_comp)

    return comp_adj


def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
    adj_l = [[] for i in range(n)]
    for conn in connections:
        adj_l[conn[0]].append(conn[1])
        adj_l[conn[1]].append(conn[0])

    times = [-1] * n
    critical = []

    def dfs(vert, time, previous):
        times[vert] = time + 1
        min_time = time + 1
        for adj in adj_l[vert]:
            if adj == previous:
                continue
            if times[adj] == -1:
                dfs(adj, time + 1, vert)
            min_time = min(min_time, times[adj])
            if times[adj] > time + 1:
                critical.append([vert, adj])
        times[vert] = min_time

    dfs(0, 0, -1)

    return critical


def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
    times = [-1]*n
    times[headID] = 0

    queue = [i for i in range(n)]
    mx = 0

    while len(queue):
        employee = queue[-1]
        mngr = manager[employee]

        if times[employee] != -1:
            queue.pop()
            continue

        if times[mngr] != -1:
            times[employee] = times[mngr] + informTime[mngr]
            mx = max(mx, times[employee])
        else:
            queue.append(mngr)

    return mx


def min_added_edges(graph):
    comp_graph = component_graph(graph)

    def mae_cg(comp_graph):
        s = 0
        t = 0
        q = 0
        n = len(comp_graph)
        
        es = []
        ee = []

        for i in range(n):
            for adj in comp_graph[i]:
                es.append(i)
                ee.append(adj)

        for i in range(n):
            if i in es:
                s += 1
            elif i in ee:
                t += 1
            else:
                q += 1

        return max(q+s, q+t)
    
    return mae_cg(comp_graph)


def largestPathValue(self, colors: str, edges: list[list[int]]) -> int:
    n = len(colors)
    unique_colors = set(colors)

    a = [[] for i in range(n)]
    for i in edges:
        a[i[0]].append(i[1])

    def topo_sort(graph: list[list[int]]) -> list[int]:
        n = len(graph)
        visited = [0] * n
        order = []

        def dfs(vert: int):
            visited[vert] = 1
            for adj in graph[vert]:
                if visited[adj] == 0:
                    dfs(adj)
                if visited[adj] == 1:
                    return -1
            
            visited[vert] = 2
            order.append(vert)

        b = []
        prev = 0
        for vert in range(n):
            if not visited[vert]:
                if dfs(vert) == -1:
                    return -1
                
                cur = sum(visited) // 2
                b.append(cur - prev)
                prev = cur

        order = order[::-1]
        c = []
        s = 0
        for i in b:
            d = []
            for j in range(i):
                d.append(order[j + s])
            c.append(d)
            s += i
        return c
    
    topo = topo_sort(a)
    if topo == -1:
        return -1
    
    mx = -1
    cache = []

    def dfs(vert, char):
        if cache[vert] != -1:
            return cache[vert]
        count = 0
        for adj in a[vert]:
            count = max(count, dfs(adj, char))
        if char == colors[vert]:
            count += 1
        cache[vert] = count
        return count
    for component in topo:
        head = component[0]
        for char in set(colors):
            cache = [-1] * n
            mx = max(mx, dfs(head, char))

    return mx