from graphviz import Digraph
import streamlit as st

def create_mind_map(text):
    graph = Digraph()
    nodes = text.split("\n")[:5]  # استخدم أول 5 أسطر كعقد
    for i, node in enumerate(nodes):
        graph.node(f"{i}", node[:15])
        if i > 0:
            graph.edge(f"{i-1}", f"{i}")
    st.graphviz_chart(graph)
