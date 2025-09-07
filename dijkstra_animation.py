import networkx as nx
import matplotlib.pyplot as plt
import heapq

# ======== Graph Setup (contoh 20 kota, 24 jalan) ========
G = nx.Graph()
edges = [
("Oradea", "Zerind", 71),
("Zerind", "Arad", 75),
("Arad", "Sibiu", 140),
("Arad", "Timisoara", 118),
("Sibiu", "Oradea", 151),
("Sibiu", "Fagaras", 99),
("Sibiu", "Rimnicu Vilcea", 80),
("Timisoara", "Lugoj", 111),
("Lugoj", "Mehadia", 70),
("Mehadia", "Dobreta", 75),
("Dobreta", "Craiova", 120),
("Craiova", "Rimnicu Vilcea", 146),
("Craiova", "Pitesti", 138),
("Rimnicu Vilcea", "Pitesti", 97),
("Fagaras", "Bucharest", 211),
("Pitesti", "Bucharest", 101),
("Bucharest", "Giurgiu", 90),
("Bucharest", "Urziceni", 85),
("Urziceni", "Hirsova", 98),
("Hirsova", "Eforie", 86),
("Urziceni", "Vaslui", 142),
("Vaslui", "Iasi", 92),
("Iasi", "Neamt", 87)
]
for u, v, w in edges:
    G.add_edge(u, v, weight=w)

# ======== Dijkstra Algorithm dengan Animasi ========
def dijkstra_animated(G, start:str, goal:str):
    # Inisialisasi
    if start not in G.nodes() or goal not in G.nodes():
        return float('inf'), []
    
    heap = [(0, start)]
    dist = {node: float('inf') for node in G.nodes()}
    prev = {node: None for node in G.nodes()}
    dist[start] = 0
    
    # Untuk animasi
    step = 0
    pos = nx.spring_layout(G, seed=42)
    
    # Set untuk melacak node yang sudah dikunjungi
    visited = set()
    
    plt.figure(figsize=(8, 6))
    
    while heap:

        # Pop node dengan jarak terkecil
        _, u = heapq.heappop(heap)
        
        # Skip jika sudah dikunjungi dengan jarak yang lebih baik
        if u in visited:
            continue
            
        visited.add(u)
        
        # ======== Visualization ========
        plt.clf()
        
        # Gambar semua node dan edges
        nx.draw_networkx_nodes(G, pos, node_color="lightblue", node_size=400)
        nx.draw_networkx_edges(G, pos, alpha=0.3)
        nx.draw_networkx_labels(G, pos, font_size=10)
        
        # Tampilkan weight pada edges
        edge_labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)
        
        # Highlight node yang sedang diproses (orange)
        nx.draw_networkx_nodes(G, pos, nodelist=[u], node_color="orange", node_size=400)
        
        # Highlight node yang sudah dikunjungi (hijau)
        if len(visited) > 1:
            nx.draw_networkx_nodes(G, pos, nodelist=list(visited - {u}), node_color="green", node_size=400)
        
        # Tampilkan jalur dari start ke node saat ini
        if u != start:
            path = []
            current = u
            while current is not None:
                path.append(current)
                current = prev[current]
            path.reverse()
            
            # Gambar edges pada path
            path_edges = [(path[i], path[i+1]) for i in range(len(path)-1)]
            nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color="red", width=2)
        
        plt.title(f"Step {step}: Memproses node {u} (Jarak: {dist[u]})", fontsize=8)
        plt.axis('off')  # Hilangkan axis
        plt.tight_layout()  # Optimalkan layout
        plt.pause(0.5)  # delay for animation
        step += 1
        
        # Jika mencapai goal, hentikan
        if u == goal:
            # Rekonstruksi path akhir
            path = []
            current = goal
            while current is not None:
                path.append(current)
                current = prev[current]
            path.reverse()
            
            # Tampilkan path akhir
            plt.clf()
            nx.draw_networkx_nodes(G, pos, node_color="lightblue", node_size=400)
            nx.draw_networkx_edges(G, pos, alpha=0.3)
            nx.draw_networkx_labels(G, pos, font_size=10)
            nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)
            
            # Highlight path terakhir
            path_edges = [(path[i], path[i+1]) for i in range(len(path)-1)]
            nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color="red", width=2)
            nx.draw_networkx_nodes(G, pos, nodelist=path, node_color="green", node_size=400)
            
            plt.title(f"Path ditemukan! Jarak: {dist[goal]}\nPath: {' -> '.join(path)}", fontsize=8)
            plt.axis('off')
            plt.tight_layout()
            plt.pause(1.0)
            
            return dist[goal], path
        
        # ======== Algoritma Dijkstra ========
        # Proses neighbors
        for v in G.neighbors(u):
            if v in visited:
                continue
                
            weight = G[u][v]['weight']
            new_dist = dist[u] + weight
            if new_dist < dist[v]:
                dist[v] = new_dist
                prev[v] = u
                heapq.heappush(heap, (new_dist, v))
    
    return float('inf'), []  # Tidak ditemukan path

# ======== User Input ========
start_city = input("Kota asal: ")
goal_city = input("Kota tujuan: ")

# ======== Run Dijkstra dengan Animasi ========
distance, path = dijkstra_animated(G, start_city, goal_city)

if distance < float('inf'):
    print(f"Jalur terpendek: {' -> '.join(path)}")
    print(f"Total jarak: {distance}")
else:
    print("Tidak ditemukan path dari", start_city, "ke", goal_city)

plt.show()

