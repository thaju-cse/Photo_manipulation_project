import networkx as nx
import matplotlib.pyplot as plt

def visualize_nfa(transitions, start_state, accept_states):
    G = nx.DiGraph()

    for state, transitions in transitions.items():
        for symbol, next_states in transitions.items():
            for next_state in next_states:
                G.add_edge(state, next_state, label=symbol)

    pos = nx.spring_layout(G)  # Layout for better visualization
    labels = {state: state for state in G.nodes()}

    # Highlight start and accept states
    node_colors = ['cyan' if node == start_state else 'yellow' if node in accept_states else 'white' for node in G.nodes()]

    nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=700)
    nx.draw_networkx_edges(G, pos)
    nx.draw_networkx_labels(G, pos, labels=labels)
    nx.draw_networkx_edge_labels(G, pos, edge_labels={(i, j): G[i][j]['label'] for i, j in G.edges()})

    plt.show()

# Example transitions for the NFA
nfa_transitions = {
    'q0': {'0': {'q1', 'q2'}, '1': {'q0', 'q3'}},
    'q1': {'0': {'q4'}, '1': {'q5'}},
    'q2': {'0': {'q3'}, '1': {'q6'}},
    'q3': {'0': {'q7'}, '1': {'q8'}},
    'q4': {'0': {'q9'}, '1': {'q0'}},
    'q5': {'0': {'q1'}, '1': {'q2'}},
    'q6': {'0': {'q3'}, '1': {'q4'}},
    'q7': {'0': {'q5'}, '1': {'q6'}},
    'q8': {'0': {'q7'}, '1': {'q8'}},
    'q9': {'0': {'q9'}, '1': {'q0'}},
}

# Example start and accept states
nfa_start_state = 'q0'
nfa_accept_states = {'q4', 'q5', 'q6'}

visualize_nfa(nfa_transitions, nfa_start_state, nfa_accept_states)
