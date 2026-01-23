<p align="center">
  <picture>
    <img width="720" alt="Qhronology logo" src="https://raw.githubusercontent.com/lgbishop/qhronology/latest/docs/source/art/output/logo-main-50fps-3sec-animated-60compressed.webp">
  </picture>
</p>

# Qhronology

*Qhronology* is a Python package for computing the states of the chronology-respecting (CR) and chronology-violating (CV) quantum systems according to the foremost quantum prescriptions of closed timelike curves (CTCs). By providing a unique approach to describing general quantum objects (such as states and gates), Qhronology can also function as a complete quantum circuit simulator, and additionally contains an engine for the visualization of quantum circuit diagrams. Its main features include:

- calculation of the states of the CR and CV quantum systems according to quantum-mechanical prescriptions of closed timelike curves
  - Deutsch's model (D-CTCs)
  - postselected teleportation (P-CTCs)
- simulation of general quantum information processing and computation
  - numerical and symbolic calculations involving any number of variables and parameters
  - (classical) replication of quantum experiments
- visualization of quantum circuit diagrams
  - text-based semigraphical diagrams constructed using glyphs from monospace fonts

The primary purpose of Qhronology is to facilitate the study of quantum models of antichronological time travel and quantum algorithms of quantum computing in both educational and research capacities. As part of this, the project aims to make the expression of quantum states, gates, circuits, and models of CTCs near-limitlessly possible within a framework that is syntactically simple, informationally dense, mathematically powerful, extremely flexible, and easily extensible. Qhronology therefore provides a sufficiently complete and self-contained set of tools with the intention that using external packages and libraries to perform transformations on its quantum constructs should not be necessary (at least in most cases). Its underlying mathematical system accomplishes this using the standard $d$-dimensional matrix mechanics of discrete-variable quantum theory in a general $\mathbb{C}^d$-representation.

Qhronology is written entirely in the [Python](https://www.python.org/) programming language. Being high-level, dynamically type-checked, and interpreted (at least within the context of its CPython reference implementation), Python is well-suited for building an accessible framework that emphasizes interactivity and scriptability. Additionally, like any popular language, it has both an extensive standard library and a plethora of powerful packages available to it. Qhronology is built around features from two such packages: the canonical [SymPy](https://sympy.org) ([repository](https://github.com/sympy/sympy)) and [NumPy](https://numpy.org) ([repository](https://github.com/numpy/numpy)) projects. In particular, the package greatly leverages the symbolic and linear algebra capabilities of the former, and so aims to have a deep compatibility with SymPy and its matrix objects. It is therefore hoped that users who possess experience with these projects find Qhronology's interface both familiar and intuitive.

> [!NOTE]
> Qhronology, in its current form, is considered to be highly experimental. Its output may not always be correct, and some features may not work as intended. Additionally, please note that all components of the package, including its functions, methods, classes, modules, and subpackages, may be subject to change in future versions.

## Features

### Quantum computing simulations

Designed to provide a powerful set of features with a simple and intuitive syntax, Qhronology facilitates the simulation of quantum computation, information processing, and algebraic calculations.

<p align="center">
  <picture>
    <source width="500" media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/lgbishop/qhronology/latest/docs/source/figures/output/circuit_algorithm_teleportation-dark.png">
    <source width="500" media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/lgbishop/qhronology/latest/docs/source/figures/output/circuit_algorithm_teleportation-light.png">
    <img width="500" alt="Quantum teleportation" src="https://raw.githubusercontent.com/lgbishop/qhronology/latest/docs/source/figures/output/circuit_algorithm_teleportation-light.png">
  </picture>
</p>

### Quantum resolutions to antichronological time-travel paradoxes

The fundamental indeterminism of quantum mechanics can be leveraged to provide resolutions to quantum formulations of classic time-travel paradoxes (such as the infamous *grandfather paradox*). A select few prescriptions by which this may be achieved, including Deutsch's model (D-CTCs) and the postselected teleportation prescription (P-CTCs), are implemented both as bare functions and class methods.

<p align="center">
  <picture>
    <source width="300" media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/lgbishop/qhronology/latest/docs/source/figures/output/circuit_ctc-dark.png">
    <source width="300" media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/lgbishop/qhronology/latest/docs/source/figures/output/circuit_ctc-light.png">
    <img width="300" alt="Quantum closed timelike curve" src="https://raw.githubusercontent.com/lgbishop/qhronology/latest/docs/source/figures/output/circuit_ctc-light.png">
  </picture>
</p>

### Quantum circuit visualization

Quantum circuit diagrams provide a powerful picturalism through which any quantum process can be visualized as a network of quantum logic gates connected by wires. Qhronology provides this functionality for any quantum process constructed using its built-in classes.

<p align="center">
  <picture>
    <source width="350" media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/lgbishop/qhronology/latest/docs/source/figures/output/text_examples_algorithms_generation_w-dark.png">
    <source width="350" media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/lgbishop/qhronology/latest/docs/source/figures/output/text_examples_algorithms_generation_w-light.png">
    <img width="350" alt="W state generation" src="https://raw.githubusercontent.com/lgbishop/qhronology/latest/docs/source/figures/output/text_examples_algorithms_generation_w-light.png">
  </picture>
</p>

### Numerous examples

Bundled with the project is a small collection of complete examples that showcase its capabilities and syntax. These are divided into two categories: *Quantum algorithms and protocols* and *Quantum closed timelike curves*. The former contains implementations of canonical algorithms in quantum computing, while the latter consists of more exotic circuits that use quantum mechanics to resolve paradoxical scenarios of antichronological time travel.

<p align="center">
  <picture>
    <source width="300" media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/lgbishop/qhronology/latest/docs/source/figures/output/circuit_ctc_grandfather-dark.png">
    <source width="300" media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/lgbishop/qhronology/latest/docs/source/figures/output/circuit_ctc_grandfather-light.png">
    <img width="300" alt="Quantum grandfather paradox" src="https://raw.githubusercontent.com/lgbishop/qhronology/latest/docs/source/figures/output/circuit_ctc_grandfather-light.png">
  </picture>
</p>

### Extensive documentation

All of the functions, classes, and methods in each of the various submodules have been rigorously detailed in their respective sections within the documentation. This includes multiple examples of usage for each, aiding the user's understanding of every available feature.

<p align="center">
  <picture>
    <source width="250" media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/lgbishop/qhronology/latest/docs/source/figures/output/diagram_bloch_sphere-dark.png">
    <source width="250" media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/lgbishop/qhronology/latest/docs/source/figures/output/diagram_bloch_sphere-light.png">
    <img width="250" alt="Bloch sphere" src="https://raw.githubusercontent.com/lgbishop/qhronology/latest/docs/source/figures/output/diagram_bloch_sphere-light.png">
  </picture>
</p>

### Foundational theory

All of the underlying mathematics upon which Qhronology is built is presented as a series of pedagogical reference articles within the documentation. This includes sections on the mathematical foundations of quantum mechanics (Hilbert spaces, linear operators, composite systems, etc.), quantum theory on both discrete and continuous Hilbert spaces, a brief overview of the quantum circuitry picturalism, and physical theories of time travel (both classical and quantum).

The aim of this theory is to serve as a comprehensive and complete reference for basic quantum mechanics and physical theories of time travel, thereby enabling the keen user to embark upon further research into these fascinating areas of study.

<p align="center">
  <picture>
    <source width="400" media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/lgbishop/qhronology/latest/docs/source/figures/output/diagram_spacetime_minkowski-dark.png">
    <source width="400" media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/lgbishop/qhronology/latest/docs/source/figures/output/diagram_spacetime_minkowski-light.png">
    <img width="400" alt="Minkowski spacetime" src="https://raw.githubusercontent.com/lgbishop/qhronology/latest/docs/source/figures/output/diagram_spacetime_minkowski-light.png">
  </picture>
</p>

## Package installation and structure

Local installation of Qhronology from [PyPI](https://pypi.org/project/qhronology/) can be accomplished using `pip` ([website](https://pip.pypa.io/), [repository](https://github.com/pypa/pip)) via your operating system's command line, e.g.,

```sh
$ pip install qhronology
```
You may also be able to use an alternative package manager of your choice.

After installation, the package can be imported in Python in the usual way. One suggestion is as follows:

```python
import qhronology as qy
```
The package has the following directory structure:

```
qhronology
├──quantum
│  ├──circuits.py
│  ├──gates.py
│  ├──prescriptions.py
│  └──states.py
├──mechanics
│  ├──matrices.py
│  ├──operations.py
│  └──quantities.py
└──utilities (intended for internal use only)
  ├──classification.py
  ├──diagrams.py
  ├──helpers.py
  ├──objects.py
  └──symbolics.py
```

### Requirements

Within the package and documentation, SymPy and NumPy are imported in their conventional manners:

```python
import sympy as sp
import numpy as np
```

Qhronology is compatible with the following package versions (from [requirements.txt](https://github.com/lgbishop/qhronology/blob/latest/requirements.txt)):

```py
sympy>=1.12
numpy>=1.26
```

These are the earliest versions with which the current release has been tested, but older versions may also be compatible. It also requires

```py
python>=3.11
```

## Examples

### Generation of a Bell state

Generation of the $\ket{\Phi^+}$ Bell state from primitive $\ket{0}$ states:

```python
from qhronology.quantum.states import VectorState
from qhronology.quantum.gates import Hadamard, Not
from qhronology.quantum.circuits import QuantumCircuit

# Input
zero_state = VectorState(spec=[(1, [0])], label="0")

# Gates
HI = Hadamard(targets=[0], num_systems=2)
CN = Not(targets=[1], controls=[0], num_systems=2)

# Circuit
generator = QuantumCircuit(inputs=[zero_state, zero_state], gates=[HI, CN])
generator.diagram()

# Output
phi_plus = generator.state(label="Φ+")

# Results
phi_plus.print()
```

```python
>>> generator.diagram()
```

> <p align="left">
>   <picture>
>     <source width="175" media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/lgbishop/qhronology/latest/docs/source/figures/output/text_examples_algorithms_generation_bell-dark.png">
>     <source width="175" media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/lgbishop/qhronology/latest/docs/source/figures/output/text_examples_algorithms_generation_bell-light.png">
>     <img width="175" alt="Bell state generation" src="https://raw.githubusercontent.com/lgbishop/qhronology/latest/docs/source/figures/output/text_examples_algorithms_generation_bell-light.png">
>   </picture>
> </p>

```python
>>> phi_plus.print()
|Φ+⟩ = sqrt(2)/2|0,0⟩ + sqrt(2)/2|1,1⟩
```

### Quantum teleportation

Quantum teleportation of an arbitrary qubit $\ket{\psi} = a\ket{0} + b\ket{1}$:

```python
from qhronology.quantum.states import VectorState
from qhronology.quantum.gates import Hadamard, Not, Measurement, Pauli
from qhronology.quantum.circuits import QuantumCircuit
from qhronology.mechanics.matrices import ket

# Input
teleporting_state = VectorState(
    spec=[["a", "b"]],
    symbols={"a": {"complex": True}, "b": {"complex": True}},
    conditions=[("a*conjugate(a) + b*conjugate(b)", 1)],
    label="ψ",
)
zero_state = VectorState(spec=[(1, [0, 0])], label="0,0")

# Gates
IHI = Hadamard(targets=[1], num_systems=3)
ICN = Not(targets=[2], controls=[1], num_systems=3)
CNI = Not(targets=[1], controls=[0], num_systems=3)
HII = Hadamard(targets=[0], num_systems=3)
IMI = Measurement(
    operators=[ket(0), ket(1)],
    observable=False,
    targets=[1],
    num_systems=3,
)
MII = Measurement(
    operators=[ket(0), ket(1)],
    observable=False,
    targets=[0],
    num_systems=3,
)
ICX = Pauli(index=1, targets=[2], controls=[1], num_systems=3)
CIZ = Pauli(index=3, targets=[2], controls=[0], num_systems=3)

# Circuit
teleporter = QuantumCircuit(
    inputs=[teleporting_state, zero_state],
    gates=[IHI, ICN, CNI, HII, IMI, MII, ICX, CIZ],
    traces=[0, 1],
)
teleporter.diagram(force_separation=True)

# Output
teleported_state = teleporter.state(norm=1, label="ρ")

# Results
teleporting_state.print()
teleported_state.print()

print(teleporting_state.distance(teleported_state))
print(teleporting_state.fidelity(teleported_state))
```

```python
>>> teleporter.diagram(force_separation=True)
```

> <p align="left">
>   <picture>
>     <source width="470" media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/lgbishop/qhronology/latest/docs/source/figures/output/text_examples_algorithms_teleportation-dark.png">
>     <source width="470" media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/lgbishop/qhronology/latest/docs/source/figures/output/text_examples_algorithms_teleportation-light.png">
>     <img width="470" alt="Quantum teleportation" src="https://raw.githubusercontent.com/lgbishop/qhronology/latest/docs/source/figures/output/text_examples_algorithms_teleportation-light.png">
>   </picture>
> </p>

```python
>>> teleporting_state.print()
|ψ⟩ = a|0⟩ + b|1⟩
```

```python
>>> teleported_state.print()
ρ = a*conjugate(a)|0⟩⟨0| + a*conjugate(b)|0⟩⟨1| + b*conjugate(a)|1⟩⟨0| + b*conjugate(b)|1⟩⟨1|
```

```python
>>> teleporting_state.distance(teleported_state)
0
```

```python
>>> teleporting_state.fidelity(teleported_state)
1
```

### Unproven-theorem paradox

Computing resolutions to the unproven-theorem paradox according to various prescriptions of quantum time travel (D-CTCs and P-CTCs):

```python
from qhronology.quantum.states import VectorState
from qhronology.quantum.gates import Not, Swap
from qhronology.quantum.prescriptions import QuantumCTC, DCTC, PCTC

# Input
mathematician_state = VectorState(spec=[(1, [0])], label="0")
book_state = VectorState(spec=[(1, [0])], label="0")

# Gates
NIC = Not(targets=[0], controls=[2], num_systems=3)
CNI = Not(targets=[1], controls=[0], num_systems=3)
IS = Swap(targets=[1, 2], num_systems=3)

# CTC
unproven = QuantumCTC(
    inputs=[mathematician_state, book_state],
    gates=[NIC, CNI, IS],
    systems_respecting=[0, 1],
)
unproven.diagram()

# Output
# D-CTCs
unproven_DCTC = DCTC(circuit=unproven)
unproven_DCTC_respecting = unproven_DCTC.state_respecting(norm=1, label="ρ_D")
unproven_DCTC_violating = unproven_DCTC.state_violating(norm=1, label="τ_D")

# P-CTCs
unproven_PCTC = PCTC(circuit=unproven)
unproven_PCTC_respecting = unproven_PCTC.state_respecting(norm=1, label="ψ_P")
unproven_PCTC_violating = unproven_PCTC.state_violating(norm=1, label="τ_P")

# Results
unproven_DCTC_respecting.print()
unproven_DCTC_violating.print()
unproven_PCTC_respecting.print()
unproven_PCTC_violating.print()
```

```python
>>> unproven.diagram()
```

> <p align="left">
>   <picture>
>     <source width="175" media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/lgbishop/qhronology/latest/docs/source/figures/output/text_examples_ctcs_unproven-dark.png">
>     <source width="175" media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/lgbishop/qhronology/latest/docs/source/figures/output/text_examples_ctcs_unproven-light.png">
>     <img width="175" alt="Unproven-theorem paradox" src="https://raw.githubusercontent.com/lgbishop/qhronology/latest/docs/source/figures/output/text_examples_ctcs_unproven-light.png">
>   </picture>
> </p>

```python
>>> unproven_DCTC_respecting.print()
ρ_D = g|0,0⟩⟨0,0| + (1 - g)|1,1⟩⟨1,1|
```

```python
>>> unproven_DCTC_violating.print()
τ_D = g|0⟩⟨0| + (1 - g)|1⟩⟨1|
```

```python
>>> unproven_PCTC_respecting.print()
|ψ_P⟩ = sqrt(2)/2|0,0⟩ + sqrt(2)/2|1,1⟩
```

```python
>>> unproven_PCTC_violating.print()
τ_P = 1/2|0⟩⟨0| + 1/2|1⟩⟨1|
```

## Documentation

The latest version of the documentation for the package is available at:

- The official website: https://qhronology.com
- The official PDF document: [Qhronology.pdf](https://github.com/lgbishop/qhronology/blob/latest/docs/_build/latex/Qhronology.pdf)

Both of these are built using [Sphinx](https://www.sphinx-doc.org) ([repository](https://github.com/sphinx-doc/sphinx)), with their shared source files residing within the `docs` directory at the root of the project's repository. This includes all project text and artwork. Please see [shell-sphinx.nix](https://github.com/lgbishop/qhronology/blob/latest/docs/shell-sphinx.nix) within that directory for a list of dependencies required to build both documentation targets. Note that a full LaTeX system installation from 2024 or later is required to build the project's PDF documentation, figures, and artwork (including the logo). Also note that the documentation's rendered circuit diagrams (generated from the package itself) were created using a custom LaTeX template [render-text.tex](https://github.com/lgbishop/qhronology/blob/latest/docs/source/figures/render-text.tex) and associated shell script [render-text.sh](https://github.com/lgbishop/qhronology/blob/latest/docs/source/figures/render-text.sh).

## License

Please see [LICENSE](https://github.com/lgbishop/qhronology/blob/latest/LICENSE) for details about Qhronology's license.

## Contributing

Contributions to Qhronology (both the package and its documentation), including any features, fixes, and suggestions, are welcome provided they are compatible with the project's concept and vision, while also conforming to its style. Please see [CONTRIBUTING](https://github.com/lgbishop/qhronology/blob/latest/CONTRIBUTING) for more details about contributing to the project. Feel free to contact lachlanbishop@protonmail.com to discuss any significant additions or changes you wish to propose.

## Citation

- The package:
```bibtex
@software{bishop_qhronology-software_2025,
  title = {Qhronology: {{A Python}} Package for Studying Quantum Models of Closed Timelike Curves and Simulating General Quantum Information Processing \& Computation},
  author = {Bishop, Lachlan G.},
  year = {2025},
  url = {https://github.com/lgbishop/qhronology},
  addendum = {Source code: \url{https://github.com/lgbishop/qhronology}}
}
```

- The project documentation:
```bibtex
@misc{bishop_qhronology-documentation_2025,
  title = {Qhronology: {{Documentation}}, {{Examples}}, and {{Theory}}},
  author = {Bishop, Lachlan G.},
  year = {2025},
  url = {https://github.com/lgbishop/qhronology/blob/latest/docs/_build/latex/Qhronology.pdf},
  addendum = {Available online: \url{https://github.com/lgbishop/qhronology}}
}
```

## Possible future work

- Package:
  - Write proper (more formal) unit tests.
  - Permit more intuitive usage (i.e., summation and multiplication) of quantum objects via operator overloading.
  - Tighter integration with SymPy's `pprint()` functionality for enhanced state and gate printing.
  - Implement T-CTCs (the *transition-probabilities* quantum model of time travel).
  - Create the ability for circuit visualizations to target *Quantikz* LaTeX output.
    - Automatically rasterize using available (local) LaTeX installation.
  - Add the ability to label a circuit's output systems.
  - Implement the permutation (PERM) gate.
  - Add the ability for circuits to be optimized (to reduced gate depth).
  - Add the ability for circuits and/or gates to be decomposed (using a specified gate set).
- Documentation:
  - More examples.
  - Website:
    - Fix citation numbering.
- Theory:
  - Expand section on the Cauchy problem near CTCs.
  - Add a section on the general theory of relativity and the associated geometric theories of CTCs.