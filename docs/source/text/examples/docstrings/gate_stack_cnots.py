from qhronology.quantum.gates import *

gates = [Not(targets=[(i + 1) % 2], controls=[i % 2]) for i in range(0, 4)]
CNOTs = GateStack(*gates)
CNOTs.diagram()
print(repr(CNOTs.output()))
CNOTs.print()
