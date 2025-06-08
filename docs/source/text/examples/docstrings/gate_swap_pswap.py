from qhronology.quantum.gates import *

PSWAP = Swap(
    targets=[0, 1],
    exponent="p",
    symbols={"p": {"real": True}},
    label="SWAP^p",
    family="GATE",
)
PSWAP.diagram()
print(repr(PSWAP.output()))
PSWAP.print()
