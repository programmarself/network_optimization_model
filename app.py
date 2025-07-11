import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from optimizer import optimize_routing

st.set_page_config(page_title="Network Optimization Model", layout="wide")
st.title("🌐 Network Optimization Model")

st.markdown("Simulated computer network traffic with optimization techniques for data center management.")

# Simulate network nodes and traffic
nodes = ["A", "B", "C", "D", "E"]
edges = [
    ("A", "B", 10), ("A", "C", 15), ("B", "C", 5),
    ("B", "D", 20), ("C", "E", 30), ("D", "E", 10)
]
traffic = {("A", "E"): 25, ("A", "D"): 10, ("B", "E"): 15}

st.subheader("📊 Network Traffic & Configuration")
st.write("Nodes:", nodes)
st.write("Edges (with cost):", edges)
st.write("Traffic Demands:", traffic)

# Optimize routing
result_df, total_cost = optimize_routing(nodes, edges, traffic)
st.subheader("✅ Optimization Result")
st.write(result_df)
st.success(f"Total Optimized Cost: {total_cost}")

# Plot network
st.subheader("📡 Network Graph")
fig, ax = plt.subplots()
pos = {"A": (0, 1), "B": (1, 2), "C": (2, 1), "D": (1, 0), "E": (3, 1)}
for (u, v, w) in edges:
    x = [pos[u][0], pos[v][0]]
    y = [pos[u][1], pos[v][1]]
    ax.plot(x, y, "k-", lw=1)
    ax.text((x[0]+x[1])/2, (y[0]+y[1])/2 + 0.05, f"{w}", color="blue")

for node in pos:
    ax.plot(pos[node][0], pos[node][1], "ro")
    ax.text(pos[node][0], pos[node][1] + 0.1, node, ha="center")

ax.axis("off")
st.pyplot(fig)
