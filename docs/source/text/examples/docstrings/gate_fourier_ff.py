from qhronology.quantum.gates import *

FF = Fourier(targets=[0, 1])
FF.diagram()
print(repr(FF.output()))
FF.print()
