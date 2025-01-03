# Assignment-DSD

Circuit Analysis Tool
Installation Instructions
Clone the Repository
To get started, clone the repository to your local machine:

bash
Copy code
git clone https://github.com/musfirakhan/Assignment-DSD.git
Install Dependencies
This project requires Python and the following libraries:

networkx for graph operations
matplotlib for visualizing the circuit graph
You can install these dependencies using pip:

bash
Copy code
pip install networkx matplotlib
Ensure Python is Installed
Make sure you have Python 3.6 or higher installed. You can check this by running:

bash
Copy code
python --version
Prepare Circuit Description Files
This tool requires a .txt file that describes the circuits. You can create these files manually or use sample files provided in the repository.

Usage Instructions
Prepare Your Circuit Description File
The circuit description file should define the components and their relationships in the following format:

plaintext
Copy code
INPUT <input_name>
ADD <add_node> <input_node_1> <input_node_2>
MUL <mul_node> <input_node_1> <input_node_2>
REG <reg_node> <input_node>
OUTPUT <output_node> <input_node>
Run the Tool
To analyze a circuit, simply run the script. Provide the path to the circuit description file in the circuit_files list. Example:

bash
Copy code
python circuit_analysis.py
View the Results
After running the script, the tool will output the critical path in the circuit along with the total propagation delay. The circuit graph will be displayed in a pop-up window, with the critical path highlighted.

Example Inputs and Outputs
Example Circuit Input:
Consider a circuit description file named circuit2.txt:

plaintext
Copy code
# Circuit name: Intermediate Circuit
# Format: <node_type> <node_id> <input_nodes...>

INPUT in1
INPUT in2
ADD add1 in1 in2
MUL mul1 add1 in2
REG reg1 mul1
OUTPUT out1 reg1
Example Output:
After running the analysis tool, the output might look like this:

plaintext
Copy code
Processing file: circuit2.txt
Critical Path: in1 -> add1 -> mul1 -> reg1
Total Propagation Delay: 3.20 units
Path Details:
  - ADD (add1): 1.0 units
  - MUL (mul1): 1.0 units
  - REG (reg1): 0.2 units
The circuit graph will be rendered with the critical path (in red) highlighted.

Design Decisions and Assumptions
Design Decisions:
Directed Graph Representation:
The circuit is represented as a directed graph where nodes represent components (such as ADD, MUL, REG), and edges represent the flow of data between components.

Node Delays:
Each component type has a fixed delay associated with it. These delays are predefined (e.g., ADD has a delay of 1.0 units, REG has a delay of 0.2 units) and are used to calculate the total propagation delay along each path.

Critical Path Calculation:
The tool identifies the longest path (the critical path) in the circuit based on the delay values. This is important because the critical path determines the overall performance of the circuit.

Graph Visualization:
The circuit is visualized using matplotlib, with node colors representing different component types. The critical path is highlighted in crimson for easy identification.

