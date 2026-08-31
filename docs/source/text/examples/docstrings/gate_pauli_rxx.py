from qhronology.quantum.gates import *

R_xx = Pauli(
    index=1,
    targets=[0, 1],
    exponent="θ/pi",
    coefficient="exp(-I*θ/2)",
    label="R_xx(θ)",
)
R_xx.diagram()
print(repr(R_xx.output(simplification=True)))
R_xx.print(simplification=True)
