# QOSF
QOSF task 2. The 3 files are available as both python scripts and Jupyter notebooks. This solution has been carried out with Qiskit (0.20.0) in Python.

# Motivation

The submission is aimed at resolving noise modelled as random gates (X or Z or I) in a simple quantum circuit initialized to |0>. Two solutions have been provided, one assuming only the logical qubit experiences noise and another assuming that any qubit can experience noise in such a way that amongst a logical qubit and its two ancillary qubits, any one of them can experience error(utmost one) and this happens to the other logical qubit too, so two error gates in total. Ofcourse all qubits can experience noise at the same instant, but that assumption has been avoided considering the complexity of the problem.


