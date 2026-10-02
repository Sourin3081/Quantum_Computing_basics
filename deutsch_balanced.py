from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator

qc = QuantumCircuit(2, 1)
qc.x(1)
qc.h(0)
qc.h(1)
qc.cx(0, 1)
qc.h(0)
qc.measure(0, 0)
simulator = AerSimulator()
compiled = transpile(qc, simulator)
result = simulator.run(compiled, shots=1000).result()
print(qc)
counts = result.get_counts()
print(counts)
if '0' in counts:
    print("Function is CONSTANT")
else:
    print("Function is BALANCED")