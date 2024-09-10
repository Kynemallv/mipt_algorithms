from enum import Enum


def from_adjacency_list_to_adjacency_matrix(al: list[list[int]]) -> list[list[int]]:
    n = len(al)
    am = [[0]*n for _ in range(n)]

    for i in range(n):
        for v in al[i]:
            am[i][v] = 1
    
    return am


def from_adjacency_list_to_edge_list(al: list[int]) -> list[tuple[int, int]]:
    n = len(al)
    el = []

    for i in range(n):
        for v in al[i]:
            el.append((i, v))
    
    return el


def from_adjacency_matrix_to_adjacency_list(am: list[list[int]]) -> list[list[int]]:
    n = len(am)
    al = [[] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if am[i][j] == 1:
                al[i].append(j)
    
    return al


def from_adjacency_matrix_to_edge_list(am: list[list[int]]) -> list[tuple[int, int]]:
    n = len(am)
    el = []

    for i in range(n):
        for j in range(n):
            if am[i][j] == 1:
                el.append((i, j))
    
    return el


def from_edge_list_to_adjacency_list(el: list[tuple[int, int]]) -> list[list[int]]:
    n = 0
    for edge in el:
        n = max(max(edge), n)
    
    al = [[] for _ in range(n)]

    for edge in el:
        al[edge[0]].append(edge[1])
    
    return al


def from_edge_list_to_adjacency_matrix(el: list[tuple[int, int]]) -> list[list[int]]:
    n = 0
    for edge in el:
        n = max(max(edge), n)
    
    am = [[0]*n for _ in range(n)]

    for edge in el:
        am[edge[0]][edge[1]] = 1
    
    return am


class Color(Enum):
    WHITE = 0,
    BLACK = 1,
    GRAY = 2


def task2(graph: list[list[int]]) -> bool:
    c = [Color.WHITE]*len(graph)

    def dfs(v: int):
        if v % 2 == 0:
            return False
        c[v] = Color.GRAY
        for u in graph[v]:
            if c[u] == Color.GRAY or (c[u] == Color.WHITE and dfs[u]):
                return True
            c[v] = Color.BLACK
            return False

    for v in range(len(graph)):
        if c[v] == Color.WHITE and dfs(v):
            return True

    return False


def task3(adjacency_list: list[list[int]], v: int, u: int) -> bool:
    cur_position = [Color.WHITE] * len(adjacency_list)

    def dfs(from_v: int, to_v: int) -> bool:
        cur_position[from_v] = Color.BLACK

        if to_v in adjacency_list[from_v]:
            return True
        
        for adj in adjacency_list[from_v]:
            if (cur_position[adj] == Color.WHITE) and dfs(from_v, to_v):
                return True
        
        return False

    return dfs(v, u) and dfs(u, v)
