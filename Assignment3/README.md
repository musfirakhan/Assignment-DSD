# README for Critical Path Analysis Project

## **Overview**

This project analyzes digital circuits to find their critical path, which is the longest combinational path determining the maximum operating frequency. The program processes circuit descriptions, identifies delays, and visualizes the critical paths using Python.

---

## **Installation Instructions**

1. **Prerequisites**:

   - Python 3.8 or higher
   - `networkx` library: Install using `pip install networkx`
   - `matplotlib` library: Install using `pip install matplotlib`

2. **Setup**:
   - Clone or download the project files.
   - Ensure all circuit description files (`circuit1.txt` to `circuit5.txt`) are in the same directory as the Python script.

---

## **Usage Instructions**

1. **Run the Script**:
   Execute the script using the following command:

   ```bash
   python critical_path_analysis.py
   ```

2. **Input Files**:

   - Place circuit description files in the same directory.
   - Ensure files follow the format:

     ```
     # Circuit name
     # Format: <node_type> <node_id> <input_nodes...>

     INPUT in1
     ADD add1 in1 in2
     ...
     OUTPUT out1 add2
     ```

3. **Output**:
   - For each circuit, the program displays:
     - Critical path
     - Total delay
     - Delay breakdown by component
   - A visual representation of the circuit highlighting the critical path.

---

## **Example Inputs and Outputs**

### Example Input (circuit1.txt):

```
# Circuit name: Basic Circuit
INPUT in1
INPUT in2
ADD add1 in1 in2
MUL mul1 in1 add1
REG reg1 mul1
ADD add2 reg1 in2
OUTPUT out1 add2
```

### Example Output:

```
Analyzing circuit: circuit1.txt
Critical Path: in1 -> add1 -> mul1 -> reg1 -> add2 -> out1
Total Delay: 3.20 time units
Path Components:
- ADD (add1): 1.0 tu
- MUL (mul1): 1.0 tu
- REG (reg1): 0.2 tu
- ADD (add2): 1.0 tu
```

A visual graph with the critical path highlighted in red is also displayed.

---

## **Design Decisions and Assumptions**

1. **Component Delays**:

   - Fixed delays based on component type:
     - Adder (ADD): 1.0 time units
     - Multiplier (MUL): 1.0 time units
     - Register (REG): 0.2 time units
     - Multiplexor (MUX): 1.0 time units
     - Other components: 0.5 time units (default)

2. **Assumptions**:
   - Inputs and outputs are clearly labeled in the circuit files.
   - No cyclic dependencies exist in the circuit graph.
   - Registers (REG) are included only in sequential circuits.

---

## **Unit Tests**

The program was tested on five circuits:

- `circuit1.txt`: Basic circuit with mixed components.
- `circuit2.txt`: A multiplier chain circuit.
- `circuit3.txt`: Sequential circuit with registers.
- `circuit4.txt`: Mixed operations with multiplexors.
- `circuit5.txt`: A complex circuit with multiple inputs and outputs.

All tests confirmed accurate calculation of critical paths and delays.

---

## **Contact**

For issues or feedback, contact [Your Name or Email].
