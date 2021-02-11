#!/usr/bin/env python
# coding: utf-8

# In[13]:


from qiskit import QuantumCircuit,execute,Aer,QuantumRegister
import numpy as np
from math import pi  
import random
from qiskit.visualization import plot_bloch_multivector


# In[14]:


simulator = Aer.get_backend('statevector_simulator')


# In[39]:


# intialized a quantum circuit where the 1st (q_0) and 4th (q_3) qubits are the input qubits and the rest are ancilla qubits
   
circuit = QuantumCircuit(6)
circuit.h(0)
circuit.cx(0,1)
circuit.cx(0,2)
circuit.cx(3,4)
circuit.cx(3,5)
   
   
# Applying noise in the form of a gate ( X or Z or I), chosen at random. The assumption is that the noise occurs 
# at utmost one qubit in a collection ( a collection here is 1 input qubit and its 2 ancillary qubits). So one gate chosen
# at random for either of q_0,q_1 or q_2 and another for either of q_3,q_4 or q_5. Each gate can be different at a given time.

error_gates = ['x','z','i']
error = random.choices(error_gates,weights=(40,30,30),k=2)
error_bits_1 = [0,1,2]
error_bit_1 = random.choices(error_bits_1,weights=(40,30,30),k=1)
error_bits_2 = [3,4,5]
error_bit_2 = random.choices(error_bits_2,weights=(40,30,30),k=1)
# error = ['z', 'x']
print(error_bit_1)
if error[0] == 'x':
   circuit.x(error_bit_1[0])
if error[0] == 'z':
   if error_bit_1[0] == 0:
       circuit.h(error_bit_1[0])
       circuit.z(error_bit_1[0])
       circuit.h(error_bit_1[0])
   else:
       circuit.z(error_bit_1[0])
if error[0] == 'i':
   circuit.i(error_bit_1[0])
if error[1] == 'x':
   circuit.x(error_bit_2[0])
if error[1] == 'z':
   circuit.z(error_bit_2[0])
if error[1] == 'i':
   circuit.i(error_bit_2[0])
   
   

circuit.cx(0,1)
circuit.cx(0,2)
circuit.ccx(2,1,0)
circuit.cx(3,4)
circuit.cx(3,5)
circuit.ccx(5,4,3)
circuit.cx(0,3)


# In[42]:


job = execute(circuit, simulator)

# Grab results from the job
result = job.result()
state = result.get_statevector()
# Returns counts
counts = result.get_counts(circuit)
print("\n Qubits of interest are the first and fourth qubits from right to left (q_0 and q_3):",counts)

# Draw the circuit
circuit.draw()

#plot_bloch_multivector(state)

