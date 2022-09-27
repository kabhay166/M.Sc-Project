from matplotlib import rc
rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
## for Palatino and other serif fonts use:
#rc('font',**{'family':'serif','serif':['Palatino']})
rc('text', usetex=True)
import numpy as np
from qiskit.quantum_info import Statevector
import matplotlib.pyplot as plt
from qiskit import QuantumCircuit, QuantumRegister, Aer
from qiskit.circuit.library import QFT
from  qft_functions import *
kappa = 1; tf = 1
L = 2*np.pi; N = 1024; h = L/N
j = np.arange(0,N); x = j*h
qubits = int(np.log2(N))
y = []
for i in x:
    y.append( np.exp(-2*(i-np.pi)**2) )
norm = np.linalg.norm(y);y = y/norm
q = QuantumRegister(qubits);qc = QuantumCircuit(q)
qc.initialize(y,q);qft(qc,qubits)
fk = np.asarray(Statevector.from_instruction(qc))*norm
kx = np.linspace(0, N, N )
time_values = [0,0.1,0.2,0.3,0.4,1]
for t in time_values:
    fk_t = fk*np.exp(-kappa*kx**2*t)
    fk_t = [i.real for i in fk_t ]
    norm = np.linalg.norm(fk_t);fk_t = fk_t/norm
    q = QuantumRegister(qubits);qc = QuantumCircuit(q)
    qc.initialize(fk_t,q);inverse_qft(qc,qubits)
    f_t = np.asarray(Statevector.from_instruction(qc))*norm
    plt.plot(x,f_t,label=f"t = {t}")
plt.plot([],[],label="u(x,0) = "+ r"$\displaystyle e^{-2(x- \pi)^{2}}$")
plt.legend()
plt.title("Solution of Diffusion Equation for different times")
plt.xlabel("x")
plt.ylabel("u(x)")
plt.tight_layout()
plt.savefig("diffusion.jpg",dpi=800)
plt.show()
    


    



    





