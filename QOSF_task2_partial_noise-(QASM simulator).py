#!/usr/bin/env python
# coding: utf-8

# In[12]:


from qiskit import QuantumCircuit,execute,Aer,QuantumRegister
import numpy as np
from math import pi  
import random
from qiskit.visualization import plot_bloch_multivector


# In[13]:


simulator = Aer.get_backend('qasm_simulator')


# In[23]:




    # intialized a quantum circuit with 4 qubits ( 2 input and 2 ancilla) and 2 classical bits
    
    circuit = QuantumCircuit(4,2)
    
    circuit.h(0)
    
    circuit.cx(0, 2)
    
    # Applying noise in the form of a gate ( X or Z or I), chosen at random. The assumption is that noise occurs only on the logical
   # (ie input) qubits. Each qubit can have different gates at the same time.
    error_gates = ['x','z','i']
    error = random.choices(error_gates,weights=(40,30,30),k=2)
  
    print("Error gates:",error)
    if error[0] == 'x':
        circuit.x(0)
    if error[0] == 'z':
        circuit.h(0)
        circuit.z(0)
        circuit.h(0)
    if error[0] == 'i':
        circuit.i(0)
    if error[1] == 'x':
        circuit.x(1)
    if error[1] == 'z':
        circuit.z(1)
    if error[1] == 'i':
        circuit.i(1)
    circuit.cx(1,3)
    circuit.cx(3,1)
    circuit.cx(0,2)
    circuit.cx(2,0)
    circuit.cx(0,1)
    
    


# In[24]:



circuit.measure([0,1], [0,1])
job = execute(circuit, simulator,shots=1000)

# Grab results from the job
result = job.result()
#state = result.get_statevector()
# Returns counts
counts = result.get_counts(circuit)
print("\nQubits of interest are measured(q_0 and q_1)::",counts)

# Draw the circuit
circuit.draw()

#plot_bloch_multivector(state)

