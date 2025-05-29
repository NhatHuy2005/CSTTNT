import heapq

def read_graph(filename):
    try:
        with open(filename, 'r', encoding='utf-8-sig') as f:
            lines = f.read().strip().split('\n')
    except FileNotFoundError:
        print(f"Lỗi: Không thể mở tệp: {filename}")
        return None

    if len(lines) < 3:
        print("Lỗi: Tệp không chứa đủ dữ liệu.")
        return None

    try:
        n, m = map(int, lines[0].split())
        s, t = map(int, lines[1].split())
    except:
        print("Lỗi: Định dạng số đỉnh/cạnh hoặc đỉnh bắt đầu/kết thúc không hợp lệ.")
        return None

    if s < 1 or s > n or t < 1 or t > n:
        print("Lỗi: Đỉnh bắt đầu hoặc đỉnh kết thúc nằm ngoài phạm vi!")
        return None

    graph = [[] for _ in range(n + 1)]
    for i in range(m):
        try:
            u, v, w = map(int, lines[2 + i].split())
        except:
            print(f"Lỗi: Định dạng cạnh không hợp lệ tại dòng {i + 3}")
            return None
        if u < 1 or u > n or v < 1 or v > n:
            print(f"Lỗi: Đỉnh không hợp lệ tại cạnh dòng {i + 3}")
            return None
        graph[u].append((v, w))
        graph[v].append((u, w))

    try:
        heuristic = list(map(int, lines[2 + m].split()))
        if len(heuristic) != n:
            print("Lỗi: Số lượng giá trị heuristic không đúng.")
            return None
    except:
        print("Lỗi: Định dạng giá trị heuristic không hợp lệ.")
        return None

    return n, s, t, graph, heuristic


def a_star_with_path(start, goal, n, graph, heuristic):
    g_score = [float('inf')] * (n + 1)
    came_from = [-1] * (n + 1)

    g_score[start] = 0
    open_set = [(heuristic[start - 1], 0, start)]

    while open_set:
        f, g, current = heapq.heappop(open_set)

        if current == goal:
            path = []
            while current != -1:
                path.append(current)
                current = came_from[current]
            path.reverse()
            return g_score[goal], path

        for neighbor, weight in graph[current]:
            tentative_g = g_score[current] + weight
            if tentative_g < g_score[neighbor]:
                g_score[neighbor] = tentative_g
                came_from[neighbor] = current
                f_score = tentative_g + heuristic[neighbor - 1]
                heapq.heappush(open_set, (f_score, tentative_g, neighbor))

    return -1, []


filename = "C:\\vs_code\\CSTTNT\\A star\\graph4.txt"
result = read_graph(filename)

if result:
    n, s, t, graph, heuristic = result
    cost, path = a_star_with_path(s, t, n, graph, heuristic)
    if cost == -1:
        print("Không tìm thấy đường đi")
    else:
        print("Tổng chi phí đường đi ngắn nhất:", cost)
        print("Đường đi:", ' -> '.join(map(str, path)))
