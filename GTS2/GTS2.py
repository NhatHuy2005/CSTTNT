import numpy as np


with open("GTS2c.txt", encoding="utf-8") as f:
    lines = f.readlines()


first_line = lines[0].replace('\ufeff', '')
total_cities, subset_size = map(int, first_line.strip().split())
city_indices = list(map(int, lines[1].strip().split()))
city_indices = [c - 1 for c in city_indices] 


flat_costs = []
for line in lines[2:]:
    numbers = list(map(int, line.strip().split()))
    flat_costs.extend(numbers)

cost_matrix_full = np.array(flat_costs).reshape((total_cities, total_cities))


def greedy_tsp(cost_matrix, start_city):
    n = len(cost_matrix)
    visited = [False] * n
    total_cost = 0

    current = start_city
    visited[current] = True

    for _ in range(n - 1):
        next_city = -1
        min_cost = float('inf')
        for j in range(n):
            if not visited[j] and cost_matrix[current][j] < min_cost:
                min_cost = cost_matrix[current][j]
                next_city = j
        visited[next_city] = True
        total_cost += cost_matrix[current][next_city]
        current = next_city

    total_cost += cost_matrix[current][start_city]
    return total_cost


def find_best_tsp(cost_matrix, cities):
    best_cost = float('inf')
    best_start = None

    for start in cities:
        cost = greedy_tsp(cost_matrix, start)
        if cost < best_cost:
            best_cost = cost
            best_start = start

    return best_start, best_cost


best_start, min_cost = find_best_tsp(cost_matrix_full, city_indices)
print(f"Chi phi thap nhat: {min_cost}")
