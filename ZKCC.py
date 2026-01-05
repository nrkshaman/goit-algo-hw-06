import time
import networkx as nx
import matplotlib.pyplot as plt

from collections import deque

def bfs_iterative(graph, start):
    # Ініціалізація порожньої множини для зберігання відвіданих вершин
    visited = set()
    # Ініціалізація черги з початковою вершиною
    queue = deque([start])

    while queue:  # Поки черга не порожня, продовжуємо обхід
        # Вилучаємо першу вершину з черги
        vertex = queue.popleft()
        # Перевіряємо, чи була вершина відвідана раніше
        if vertex not in visited:
            # Якщо не була відвідана, друкуємо її
            print(vertex, end=" ")
            # Додаємо вершину до множини відвіданих вершин
            visited.add(vertex)
            # Додаємо всіх невідвіданих сусідів вершини до кінця черги
            # Операція різниці множин вилучає вже відвідані вершини зі списку сусідів
            queue.extend(set(graph[vertex]) - visited)
    # Повертаємо множину відвіданих вершин після завершення обходу
    return visited  

def dfs_iterative(graph, start_vertex):
    visited = set()
    # Використовуємо стек для зберігання вершин
    stack = [start_vertex]  
    while stack:
        # Вилучаємо вершину зі стеку
        vertex = stack.pop()  
        if vertex not in visited:
            print(vertex, end=' ')
            # Відвідуємо вершину
            visited.add(vertex)
            # Додаємо сусідні вершини до стеку
            stack.extend(reversed(list(graph[vertex])))  

def dijkstra(graph:nx.Graph, start):
    # Ініціалізація відстаней та множини невідвіданих вершин
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    unvisited = list(graph.nodes())

    while unvisited:
        # Знаходження вершини з найменшою відстанню серед невідвіданих
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])

        # Якщо поточна відстань є нескінченністю, то ми завершили роботу
        if distances[current_vertex] == float('infinity'):
            break

        for neighbor, properties in graph[current_vertex].items():
            distance = distances[current_vertex] + properties["distance"]
            # Якщо нова відстань коротша, то оновлюємо найкоротший шлях
            if distance < distances[neighbor]:
                distances[neighbor] = distance
        # Видаляємо поточну вершину з множини невідвіданих
        unvisited.remove(current_vertex)

    return distances

G = nx.Graph()
G.add_edge("Acciaiuoli", "Medici", distance=15)
G.add_edge("Castellani", "Peruzzi", distance=9)
G.add_edge("Castellani", "Strozzi", distance=2)
G.add_edge("Castellani", "Barbadori", distance=6)
G.add_edge("Medici", "Barbadori", distance=3)
G.add_edge("Medici", "Ridolfi", distance=8)
G.add_edge("Medici", "Tornabuoni", distance=13)
G.add_edge("Medici", "Albizzi", distance=6)
G.add_edge("Medici", "Salviati", distance=1)
G.add_edge("Salviati", "Pazzi", distance=5)
G.add_edge("Peruzzi", "Strozzi", distance=9)
G.add_edge("Peruzzi", "Bischeri", distance=11)
G.add_edge("Strozzi", "Ridolfi", distance=23)
G.add_edge("Strozzi", "Bischeri", distance=8)
G.add_edge("Ridolfi", "Tornabuoni", distance=7)
G.add_edge("Tornabuoni", "Guadagni", distance=3)
G.add_edge("Albizzi", "Ginori", distance=4)
G.add_edge("Albizzi", "Guadagni", distance=11)
G.add_edge("Bischeri", "Guadagni", distance=7)
G.add_edge("Guadagni", "Lamberteschi", distance=1)

# print(G.nodes())
# print(G.edges())

print(f"number_of_nodes: {G.number_of_nodes()}")
print(f"number_of_edges: {G.number_of_edges()}")
print(f"is_connected: {nx.is_connected(G)}")

print(f"degree_centrality: {nx.degree_centrality(G)}")
print(f"closeness_centrality: {nx.closeness_centrality(G)}")
print(f"betweenness_centrality:{nx.betweenness_centrality(G)}")

print(f"shortest_path Acciaiuoli to Ridolfi:{nx.shortest_path(G, source="Acciaiuoli", target="Ridolfi")}")
print(f"average_shortest_path_length: {nx.average_shortest_path_length(G)}")

# Запуск алгоритму BFS
print("bfs_iterative route:")
bfs_iterative(G, 'Lamberteschi')
print()
# Виклик функції DFS
print("dfs_iterative route:")
dfs_iterative(G, 'Lamberteschi')
print()
print(dijkstra(G, 'Guadagni'))

nx.draw(G, with_labels=True)
plt.show()

