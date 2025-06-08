from qhronology.quantum.gates import *

IP = Permutation(permutation=[0, 2, 1])
IP.diagram()
print(repr(IP.output()))
IP.print()
