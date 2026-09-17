from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator

qc = QuantumCircuit(1, 1)

# Apply X gate
qc.x(0)

# Measure
qc.measure(0, 0)

simulator = AerSimulator()
compiled = transpile(qc, simulator)

result = simulator.run(compiled, shots=1000).result()

print(qc)
print(result.get_counts())