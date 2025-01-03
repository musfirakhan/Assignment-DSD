import networkx as nx
import matplotlib.pyplot as plt

def load_circuit_description(filepath):
    """Load the circuit description file and create a directed graph."""
    circuit_graph = nx.DiGraph()
    component_timings = {
        "ADD": 1.0,
        "MUL": 1.0,
        "REG": 0.2,
        "MUX": 1.0,
    }

    with open(filepath, 'r') as file:
        for entry in file:
            entry = entry.strip()
            if not entry or entry.startswith('#'):
                continue

            details = entry.split()
            component_type, component_id = details[0], details[1]
            input_components = details[2:]

            circuit_graph.add_node(
                component_id, 
                category=component_type, 
                delay=component_timings.get(component_type, 0.5)
            )

            for input_id in input_components:
                circuit_graph.add_edge(input_id, component_id)

    return circuit_graph

def compute_path_delay(path, circuit_graph):
    """Compute the total delay along a specific path."""
    return sum(circuit_graph.nodes[component]['delay'] for component in path)

def determine_longest_path(circuit_graph):
    """Identify the critical path with the maximum delay in the circuit."""
    longest_path = []
    highest_delay = 0

    end_components = [node for node in circuit_graph.nodes if circuit_graph.out_degree(node) == 0]

    for start_node in nx.topological_sort(circuit_graph):
        for end_node in end_components:
            possible_paths = list(nx.all_simple_paths(circuit_graph, source=start_node, target=end_node))

            for path in possible_paths:
                path_delay = compute_path_delay(path, circuit_graph)
                if path_delay > highest_delay:
                    highest_delay = path_delay
                    longest_path = path

    return longest_path, highest_delay

def render_circuit(circuit_graph, highlighted_path):
    """Render the circuit graph and emphasize the critical path."""
    layout = nx.spring_layout(circuit_graph)

    node_colors = []
    for node in circuit_graph.nodes:
        category = circuit_graph.nodes[node]['category']
        if category == 'ADD':
            node_colors.append('lightgreen')
        elif category == 'MUL':
            node_colors.append('lightcoral')
        elif category == 'REG':
            node_colors.append('lightblue')
        elif category == 'MUX':
            node_colors.append('lightskyblue')
        else:
            node_colors.append('skyblue')

    nx.draw(
        circuit_graph, layout, with_labels=True, 
        node_color=node_colors, node_size=2200, font_size=10
    )

    edge_path = [(highlighted_path[i], highlighted_path[i + 1]) for i in range(len(highlighted_path) - 1)]
    nx.draw_networkx_edges(circuit_graph, layout, edgelist=edge_path, edge_color='crimson', width=2)

    plt.show()


def evaluate_circuits(filepaths):
    """Evaluate multiple circuit files and display their critical paths."""
    for filepath in filepaths:
        print(f"\nProcessing file: {filepath}")
        circuit_graph = load_circuit_description(filepath)
        longest_path, max_delay = determine_longest_path(circuit_graph)

        print(f"Critical Path: {' -> '.join(longest_path)}")
        print(f"Total Propagation Delay: {max_delay:.2f} units")
        print("Path Details:")
        for component in longest_path:
            component_info = circuit_graph.nodes[component]
            print(f"  - {component_info['category']} ({component}): {component_info['delay']} units")

        render_circuit(circuit_graph, longest_path)

def start_analysis():
    circuit_files = [
        "example_1.txt",
        "example_2.txt", 
        "example_3.txt", 
        "example_4.txt", 
        "example_5.txt"
    ]
    evaluate_circuits(circuit_files)

if __name__ == "__main__":
    start_analysis()
