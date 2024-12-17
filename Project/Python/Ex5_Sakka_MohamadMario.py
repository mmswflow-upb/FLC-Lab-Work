import re
import matplotlib.pyplot as plt
import networkx as nx

def dfa_simulation(input_string):
    # Define the DFA transitions
    transitions = {
        'q0': {'0': 'q1', '1': 'q2'},
        'q1': {'0': 'q1', '1': 'q3'},
        'q2': {'0': 'q4', '1': 'q2'},
        'q3': {'0': 'q5', '1': 'q3'},
        'q4': {'0': 'q5', '1': 'q6'},
        'q5': {'0': 'q5', '1': 'q6'},
        'q6': {'0': 'q6', '1': 'q6'},
    }

    # Define the accepting states
    accepting_states = {'q6'}

    # Start at the initial state
    current_state = 'q0'

    # Process the input string
    for char in input_string:
        if char in transitions[current_state]:
            current_state = transitions[current_state][char]
        else:
            return False  # Invalid input leads to rejection

    return current_state in accepting_states

def draw_dfa():
    # Create a directed graph
    dfa = nx.DiGraph()

    # Define the DFA nodes and edges
    states = ['q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6']
    edges = [
        ('q0', 'q1', '0'), ('q0', 'q2', '1'),
        ('q1', 'q1', '0'), ('q1', 'q3', '1'),
        ('q2', 'q4', '0'), ('q2', 'q2', '1'),
        ('q3', 'q5', '0'), ('q3', 'q3', '1'),
        ('q4', 'q5', '0'), ('q4', 'q6', '1'),
        ('q5', 'q5', '0'), ('q5', 'q6', '1'),
        ('q6', 'q6', '0'), ('q6', 'q6', '1'),
    ]

    # Add nodes and edges to the graph
    for state in states:
        dfa.add_node(state, shape='circle')
    for edge in edges:
        dfa.add_edge(edge[0], edge[1], label=edge[2])

    # Draw the DFA
    pos = nx.spring_layout(dfa)
    nx.draw(dfa, pos, with_labels=True, node_size=3000, node_color='lightblue')
    edge_labels = nx.get_edge_attributes(dfa, 'label')
    nx.draw_networkx_edge_labels(dfa, pos, edge_labels=edge_labels)
    plt.title("DFA Diagram")
    plt.show()

# Example usage
if __name__ == "__main__":
    input_string = "1001011"
    if dfa_simulation(input_string):
        print(f"The string '{input_string}' is accepted by the DFA.")
    else:
        print(f"The string '{input_string}' is rejected by the DFA.")

    draw_dfa()
