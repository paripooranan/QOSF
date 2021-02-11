#!/usr/bin/env python
# coding: utf-8

# In[7]:


from qiskit import QuantumCircuit,execute,Aer,QuantumRegister
import numpy as np
from math import pi  
import random
from qiskit.visualization import plot_bloch_multivector


# In[2]:


simulator = Aer.get_backend('statevector_simulator')


# In[32]:




    # intialized a quantum circuit with 2 input qubits and 2 ancilla qubits
    qr = QuantumRegister(2,'q')
    anc = QuantumRegister(2,'ancilla')
    circuit = QuantumCircuit(qr,anc)
    
    circuit.h(qr[0])
    
    circuit.cx(qr[0], anc[0])
    
   # Applying noise in the form of a gate ( X or Z or I), chosen at random. The assumption is that noise occurs only on the logical
   # (ie input) qubits. Each qubit can have different gates at the same time.
    error_gates = ['x','z','i']
    error = random.choices(error_gates,weights=(40,30,30),k=2)
   
    print("Error gates:",error)
    if error[0] == 'x':
        circuit.x(qr[0])
    if error[0] == 'z':
        circuit.h(qr[0])
        circuit.z(qr[0])
        circuit.h(qr[0])
    if error[0] == 'i':
        circuit.i(qr[0])
    if error[1] == 'x':
        circuit.x(qr[1])
    if error[1] == 'z':
        circuit.z(qr[1])
    if error[1] == 'i':
        circuit.i(qr[1])
        
        
    circuit.cx(qr[1],anc[1])
    circuit.cx(anc[1],qr[1])
    circuit.cx(qr[0], anc[0])
    circuit.cx(anc[0], qr[0])
    circuit.cx(qr[0], qr[1])
    
    


# In[33]:




job = execute(circuit, simulator)

# Grab results from the job
result = job.result()
state = result.get_statevector()
# Returns counts
counts = result.get_counts(circuit)
print("\nQubits of interest are the 1st and 2nd qubits from right to left(q_0 and q_1):",counts)

# Draw the circuit
circuit.draw()

#plot_bloch_multivector(state)

