from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator

# Create 1 qubit + 1 classical bit
qc = QuantumCircuit(1, 1)

# Put qubit into superposition
qc.h(0)

# Measure
qc.measure(0, 0)

# Simulator
simulator = AerSimulator()

# Compile and run
compiled = transpile(qc, simulator)
result = simulator.run(compiled, shots=1000).result()

# Display circuit and result
print(qc)
print(result.get_counts())