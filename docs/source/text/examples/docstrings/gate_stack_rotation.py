from qhronology.quantum.gates import *

labels = ("x", "y", "z")
gates = [Rotation(axis=i, angle="θ", label=f"R_{labels[i - 1]}") for i in range(1, 4)]
Rotations = GateStack(*gates)
Rotations.diagram(sep=(1, 1))
print(repr(Rotations.output()))
Rotations.print()
