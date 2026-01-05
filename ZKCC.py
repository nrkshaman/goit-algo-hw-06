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


G = nx.Graph()
G.add_edge("Acciaiuoli", "Medici")
G.add_edge("Castellani", "Peruzzi")
G.add_edge("Castellani", "Strozzi")
G.add_edge("Castellani", "Barbadori")
G.add_edge("Medici", "Barbadori")
G.add_edge("Medici", "Ridolfi")
G.add_edge("Medici", "Tornabuoni")
G.add_edge("Medici", "Albizzi")
G.add_edge("Medici", "Salviati")
G.add_edge("Salviati", "Pazzi")
G.add_edge("Peruzzi", "Strozzi")
G.add_edge("Peruzzi", "Bischeri")
G.add_edge("Strozzi", "Ridolfi")
G.add_edge("Strozzi", "Bischeri")
G.add_edge("Ridolfi", "Tornabuoni")
G.add_edge("Tornabuoni", "Guadagni")
G.add_edge("Albizzi", "Ginori")
G.add_edge("Albizzi", "Guadagni")
G.add_edge("Bischeri", "Guadagni")
G.add_edge("Guadagni", "Lamberteschi")


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

nx.draw(G, with_labels=True)
plt.show()

