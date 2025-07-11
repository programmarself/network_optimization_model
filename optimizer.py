import pandas as pd
import networkx as nx

def optimize_routing(nodes, edges, traffic):
    G = nx.DiGraph()
    for u, v, cost in edges:
        G.add_edge(u, v, weight=cost)

    routes = []
    total_cost = 0

    for (src, dst), demand in traffic.items():
        try:
            path = nx.shortest_path(G, src, dst, weight="weight")
            cost = sum(G[u][v]['weight'] for u, v in zip(path[:-1], path[1:]))
            routes.append({
                "From": src,
                "To": dst,
                "Path": " → ".join(path),
                "Traffic": demand,
                "Cost": cost * demand
            })
            total_cost += cost * demand
        except nx.NetworkXNoPath:
            routes.append({
                "From": src,
                "To": dst,
                "Path": "No path",
                "Traffic": demand,
                "Cost": "∞"
            })

    return pd.DataFrame(routes), total_cost
