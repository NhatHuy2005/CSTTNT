def read_graph(filename):
    with open(filename, 'r', encoding='utf-8-sig') as f: 
        n = int(f.readline().strip())
        adj_matrix = [list(map(int, f.readline().split())) for _ in range(n)]
    return n, adj_matrix

def degree(node, adj_matrix):
    return sum(adj_matrix[node])

def welch_powell_coloring(n, adj_matrix):
    colors = [-1] * n  
    nodes = sorted(range(n), key=lambda x: -degree(x, adj_matrix)) 

    current_color = 0
    for u in nodes:
        if colors[u] == -1:
            colors[u] = current_color
            for v in nodes:
                if colors[v] == -1 and adj_matrix[u][v] == 0:
                    if all(adj_matrix[v][k] == 0 or colors[k] != current_color for k in range(n)):
                        colors[v] = current_color
            current_color += 1
    return colors

n, adj_matrix = read_graph("color4.txt")
result = welch_powell_coloring(n, adj_matrix)

print(f"Tổng số màu sử dụng: {max(result) + 1}")