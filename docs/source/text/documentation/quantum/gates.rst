.. include:: /styles.rst

.. _`sec:docs_gates`:

*****
Gates
*****

Quantum logic gates provide the building blocks for describing quantum operations that are usually (unitary) interactions between two or more (sub)systems, or (linear) transformations of any number of systems. In Qhronology, they are constructed as instances of the :py:class:`~qhronology.quantum.gates.QuantumGate` base class,

.. code:: python

   from qhronology.quantum.gates import QuantumGate

and its derivatives (subclasses),

.. code:: python

   from qhronology.quantum.gates import Pauli, GellMann, Rotation, Phase, Diagonal, Swap, Summation, Not, Hadamard, Fourier, Measurement

These represent a distinct vertical "slice" in the quantum circuit picturalism, and so include information about the locations of both control and anticontrol nodes, in addition to the presence of any empty wires. They also possess other metadata associated with the gate such as any parameter values, symbolic assumptions, and algebraic conditions.

Facilities to combine gates together are also provided by the package and take two forms: "interleaved" compositions via the :py:class:`~qhronology.quantum.gates.GateInterleave` class, and "stacked" compositions via the :py:class:`~qhronology.quantum.gates.GateStack` class:

.. code:: python

   from qhronology.quantum.gates import GateInterleave, GateStack

Both of these classes concern the creation of more complex spatial ("vertical") gate structures. Temporal ("horizontal") compositions (i.e., gate sequences) as single object instances on the other hand are not supported as this is achievable simply by combining the individual components sequentially in a circuit.

Main class
==========

.. autoclass:: qhronology.quantum.gates.QuantumGate
   :show-inheritance:

   .. rubric:: :styleheader6:`Examples`

   >>> unitary = sp.MatrixSymbol("U", 2, 2).as_mutable()
   >>> U = QuantumGate(spec=unitary, label="U")
   >>> U.output()
   Matrix([
   [U[0, 0], U[0, 1]],
   [U[1, 0], U[1, 1]]])
   >>> U.diagram()

   ..

      .. raw:: latex
         
         \vspace{1em}
         \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_custom_u-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html or latex

         .. image:: /figures/output/text_examples_docstrings_gate_custom_u-light.png
            :scale: 40 %
            :align: left
            :class: only-light

      .. raw:: latex
         
         \end{mdframed}
         \vspace{1em}

   >>> unitary = sp.MatrixSymbol("U", 3, 3).as_mutable()
   >>> U3 = QuantumGate(spec=unitary, label="U", dim=3)
   >>> U3.output()
   Matrix([
   [U[0, 0], U[0, 1], U[0, 2]],
   [U[1, 0], U[1, 1], U[1, 2]],
   [U[2, 0], U[2, 1], U[2, 2]]])
   >>> U3.diagram()

   ..

      .. raw:: latex
         
         \vspace{1em}
         \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_custom_u3-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html or latex

         .. image:: /figures/output/text_examples_docstrings_gate_custom_u3-light.png
            :scale: 40 %
            :align: left
            :class: only-light

      .. raw:: latex
         
         \end{mdframed}
         \vspace{1em}

   >>> unitary = sp.MatrixSymbol("U", 2, 2).as_mutable()
   >>> CU = QuantumGate(spec=unitary, targets=[1], controls=[0], label="U")
   >>> CU.output()
   Matrix([
   [1, 0,       0,       0],
   [0, 1,       0,       0],
   [0, 0, U[0, 0], U[0, 1]],
   [0, 0, U[1, 0], U[1, 1]]])
   >>> CU.diagram()

   ..

      .. raw:: latex
         
         \vspace{1em}
         \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_custom_cu-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html or latex

         .. image:: /figures/output/text_examples_docstrings_gate_custom_cu-light.png
            :scale: 40 %
            :align: left
            :class: only-light

      .. raw:: latex
         
         \end{mdframed}
         \vspace{1em}

.. raw:: latex

   \hrulefillthick

.. _`sec:docs_gates_properties`:

Constructor argument properties
-------------------------------

.. autoproperty:: qhronology.quantum.gates.QuantumGate.spec

.. raw:: latex

   \hrulefillthick

.. autoproperty:: qhronology.quantum.gates.QuantumGate.targets

.. raw:: latex

   \hrulefillthick

.. autoproperty:: qhronology.quantum.gates.QuantumGate.controls

.. raw:: latex

   \hrulefillthick

.. autoproperty:: qhronology.quantum.gates.QuantumGate.anticontrols

.. raw:: latex

   \hrulefillthick

.. autoproperty:: qhronology.quantum.gates.QuantumGate.num_systems

.. raw:: latex

   \hrulefillthick

.. autoproperty:: qhronology.quantum.gates.QuantumGate.dim

.. raw:: latex

   \hrulefillthick

.. autoproperty:: qhronology.quantum.gates.QuantumGate.symbols

.. raw:: latex

   \hrulefillthick

.. autoproperty:: qhronology.quantum.gates.QuantumGate.conditions

.. raw:: latex

   \hrulefillthick

.. autoproperty:: qhronology.quantum.gates.QuantumGate.conjugate

.. raw:: latex

   \hrulefillthick

.. autoproperty:: qhronology.quantum.gates.QuantumGate.exponent

.. raw:: latex

   \hrulefillthick

.. autoproperty:: qhronology.quantum.gates.QuantumGate.coefficient

.. raw:: latex

   \hrulefillthick

.. autoproperty:: qhronology.quantum.gates.QuantumGate.label

.. raw:: latex

   \hrulefillthick

.. autoproperty:: qhronology.quantum.gates.QuantumGate.notation

.. raw:: latex

   \hrulefillthick

.. autoproperty:: qhronology.quantum.gates.QuantumGate.family

.. raw:: latex

   \hrulefillthick

Read-only properties
--------------------

.. autoproperty:: qhronology.quantum.gates.QuantumGate.systems

.. raw:: latex

   \hrulefillthick

.. autoproperty:: qhronology.quantum.gates.QuantumGate.matrix

.. raw:: latex

   \hrulefillthick

.. _`sec:docs_gates_methods`:

Methods
-------

.. automethod:: qhronology.quantum.gates.QuantumGate.output

.. raw:: latex

   \hrulefillthick

.. automethod:: qhronology.quantum.gates.QuantumGate.diagram

   .. rubric:: :styleheader6:`Examples`

   For usage examples, please see those of the :py:class:`~qhronology.quantum.gates.QuantumGate` class and its :ref:`subclasses <sec:docs_gates_subclasses>`.

.. raw:: latex

   \hrulefillthick

.. _`sec:docs_gates_subclasses`:

Subclasses
==========

Please note that the documentation of these subclasses includes only properties and methods that are either new or modified from the base class :py:class:`~qhronology.quantum.gates.QuantumGate`.

.. note::

   In all of these subclasses, the ``spec`` property should not be set.

.. list-table:: List of aliases for the :py:class:`~qhronology.quantum.gates.QuantumGate` subclasses
   :widths: 5 5
   :header-rows: 1

   * - Subclass
     - Alias
   * - :py:class:`~qhronology.quantum.gates.Pauli`
     - ``PAULI``
   * - :py:class:`~qhronology.quantum.gates.GellMann`
     - ``GM``
   * - :py:class:`~qhronology.quantum.gates.Rotation`
     - ``ROT``
   * - :py:class:`~qhronology.quantum.gates.Phase`
     - ``PHS``
   * - :py:class:`~qhronology.quantum.gates.Diagonal`
     - ``DIAG``
   * - :py:class:`~qhronology.quantum.gates.Swap`
     - ``SWAP``
   * - :py:class:`~qhronology.quantum.gates.Summation`
     - ``SUM``
   * - :py:class:`~qhronology.quantum.gates.Not`
     - ``NOT``
   * - :py:class:`~qhronology.quantum.gates.Hadamard`
     - ``HAD``
   * - :py:class:`~qhronology.quantum.gates.Fourier`
     - ``QDFT``
   * - :py:class:`~qhronology.quantum.gates.Measurement`
     - ``METER``

.. autoclass:: qhronology.quantum.gates.Pauli
   :show-inheritance:

   .. rubric:: :styleheader6:`Examples`

   >>> X = Pauli(index=1)
   >>> X.output()
   Matrix([
   [0, 1],
   [1, 0]])
   >>> X.diagram()

   ..

      .. raw:: latex
         
         \vspace{1em}
         \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_pauli_x-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html or latex

         .. image:: /figures/output/text_examples_docstrings_gate_pauli_x-light.png
            :scale: 40 %
            :align: left
            :class: only-light

      .. raw:: latex
         
         \end{mdframed}
         \vspace{1em}

   >>> YI = Pauli(index=2, targets=[0], num_systems=2)
   >>> YI.output()
   Matrix([
   [0, 0, -I,  0],
   [0, 0,  0, -I],
   [I, 0,  0,  0],
   [0, I,  0,  0]])
   >>> YI.diagram()

   ..

      .. raw:: latex
         
         \vspace{1em}
         \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_pauli_yi-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html or latex

         .. image:: /figures/output/text_examples_docstrings_gate_pauli_yi-light.png
            :scale: 40 %
            :align: left
            :class: only-light

      .. raw:: latex
         
         \end{mdframed}
         \vspace{1em}

   >>> IZ = Pauli(index=3, targets=[1])
   >>> IZ.output()
   Matrix([
   [1,  0, 0,  0],
   [0, -1, 0,  0],
   [0,  0, 1,  0],
   [0,  0, 0, -1]])
   >>> IZ.diagram()

   ..

      .. raw:: latex
         
         \vspace{1em}
         \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_pauli_iz-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html or latex

         .. image:: /figures/output/text_examples_docstrings_gate_pauli_iz-light.png
            :scale: 40 %
            :align: left
            :class: only-light

      .. raw:: latex
         
         \end{mdframed}
         \vspace{1em}

   >>> ZZ = Pauli(index=3, targets=[0, 1], label="Z⊗Z")
   >>> ZZ.output()
   Matrix([
   [1,  0,  0, 0],
   [0, -1,  0, 0],
   [0,  0, -1, 0],
   [0,  0,  0, 1]])
   >>> ZZ.diagram()

   ..

      .. raw:: latex
         
         \vspace{1em}
         \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_pauli_zz-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html or latex

         .. image:: /figures/output/text_examples_docstrings_gate_pauli_zz-light.png
            :scale: 40 %
            :align: left
            :class: only-light

      .. raw:: latex
         
         \end{mdframed}
         \vspace{1em}

   >>> CZ = Pauli(index=3, targets=[1], controls=[0])
   >>> CZ.output()
   Matrix([
   [1, 0, 0,  0],
   [0, 1, 0,  0],
   [0, 0, 1,  0],
   [0, 0, 0, -1]])
   >>> CZ.diagram()

   ..

      .. raw:: latex
         
         \vspace{1em}
         \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_pauli_cz-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html or latex

         .. image:: /figures/output/text_examples_docstrings_gate_pauli_cz-light.png
            :scale: 40 %
            :align: left
            :class: only-light

      .. raw:: latex
         
         \end{mdframed}
         \vspace{1em}

   >>> R_xx = Pauli(
   ...     index=1,
   ...     targets=[0, 1],
   ...     exponent="θ/pi",
   ...     coefficient="exp(-I*θ/2)",
   ...     label="R_xx(θ)",
   ... )
   >>> R_xx.output(simplify = True)
   Matrix([
   [   cos(θ/2),           0,           0, -I*sin(θ/2)],
   [          0,    cos(θ/2), -I*sin(θ/2),           0],
   [          0, -I*sin(θ/2),    cos(θ/2),           0],
   [-I*sin(θ/2),           0,           0,    cos(θ/2)]])
   >>> R_xx.diagram()

   ..

      .. raw:: latex
         
         \vspace{1em}
         \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_pauli_rxx-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html or latex

         .. image:: /figures/output/text_examples_docstrings_gate_pauli_rxx-light.png
            :scale: 40 %
            :align: left
            :class: only-light

      .. raw:: latex
         
         \end{mdframed}
         \vspace{1em}

   .. raw:: latex

      \hrulefillthick

   .. autoproperty:: qhronology.quantum.gates.Pauli.index

.. raw:: latex

   \hrulefillthick

.. autoclass:: qhronology.quantum.gates.GellMann
   :show-inheritance:

   .. rubric:: :styleheader6:`Examples`

   >>> L = GellMann(index=8)
   >>> L.output()
   Matrix([
   [sqrt(3)/3,         0,            0],
   [        0, sqrt(3)/3,            0],
   [        0,         0, -2*sqrt(3)/3]])
   >>> L.diagram()

   ..

      .. raw:: latex
         
         \vspace{1em}
         \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_gellmann_l-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html or latex

         .. image:: /figures/output/text_examples_docstrings_gate_gellmann_l-light.png
            :scale: 40 %
            :align: left
            :class: only-light

      .. raw:: latex
         
         \end{mdframed}
         \vspace{1em}

   .. raw:: latex

      \hrulefillthick

   .. autoproperty:: qhronology.quantum.gates.GellMann.index

.. raw:: latex

   \hrulefillthick

.. autoclass:: qhronology.quantum.gates.Rotation
   :show-inheritance:

   .. rubric:: :styleheader6:`Examples`

   >>> R_x = Rotation(axis=1, angle="θ", label="R_x")
   >>> R_x.output()
   Matrix([
   [   cos(θ/2), -I*sin(θ/2)],
   [-I*sin(θ/2),    cos(θ/2)]])
   >>> R_x.diagram()

   ..

      .. raw:: latex
         
         \vspace{1em}
         \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_rotation_x-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html or latex

         .. image:: /figures/output/text_examples_docstrings_gate_rotation_x-light.png
            :scale: 40 %
            :align: left
            :class: only-light

      .. raw:: latex
         
         \end{mdframed}
         \vspace{1em}

   >>> R_y = Rotation(axis=2, angle="φ", label="R_y")
   >>> R_y.output()
   Matrix([
   [cos(φ/2), -sin(φ/2)],
   [sin(φ/2),  cos(φ/2)]])
   >>> R_y.diagram()

   ..

      .. raw:: latex
         
         \vspace{1em}
         \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_rotation_y-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html or latex

         .. image:: /figures/output/text_examples_docstrings_gate_rotation_y-light.png
            :scale: 40 %
            :align: left
            :class: only-light

      .. raw:: latex
         
         \end{mdframed}
         \vspace{1em}

   >>> R_z = Rotation(axis=3, angle="t", label="R_z")
   >>> R_z.output()
   Matrix([
   [exp(-I*t/2),          0],
   [          0, exp(I*t/2)]])
   >>> R_z.diagram()

   ..

      .. raw:: latex
         
         \vspace{1em}
         \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_rotation_z-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html or latex

         .. image:: /figures/output/text_examples_docstrings_gate_rotation_z-light.png
            :scale: 40 %
            :align: left
            :class: only-light

      .. raw:: latex
         
         \end{mdframed}
         \vspace{1em}

   .. raw:: latex

      \hrulefillthick

   .. autoproperty:: qhronology.quantum.gates.Rotation.axis

   .. raw:: latex

      \hrulefillthick

   .. autoproperty:: qhronology.quantum.gates.Rotation.angle

.. raw:: latex

   \hrulefillthick

.. autoclass:: qhronology.quantum.gates.Phase
   :show-inheritance:

   .. rubric:: :styleheader6:`Examples`

   >>> P = Phase()
   >>> P.output()
   Matrix([
   [1,  0],
   [0, -1]])
   >>> P.diagram()

   ..

      .. raw:: latex
         
         \vspace{1em}
         \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_phase_p-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html or latex

         .. image:: /figures/output/text_examples_docstrings_gate_phase_p-light.png
            :scale: 40 %
            :align: left
            :class: only-light

      .. raw:: latex
         
         \end{mdframed}
         \vspace{1em}

   >>> S = Phase(exponent=sp.Rational(1, 2), label="S")
   >>> S.output()
   Matrix([
   [1, 0],
   [0, I]])
   >>> S.diagram()

   ..

      .. raw:: latex
         
         \vspace{1em}
         \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_phase_s-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html or latex

         .. image:: /figures/output/text_examples_docstrings_gate_phase_s-light.png
            :scale: 40 %
            :align: left
            :class: only-light

      .. raw:: latex
         
         \end{mdframed}
         \vspace{1em}

   >>> T = Phase(exponent=sp.Rational(1, 4), label="T")
   >>> T.output()
   Matrix([
   [1,           0],
   [0, exp(I*pi/4)]])
   >>> D.diagram()

   ..

      .. raw:: latex
         
         \vspace{1em}
         \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_phase_t-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html or latex

         .. image:: /figures/output/text_examples_docstrings_gate_phase_t-light.png
            :scale: 40 %
            :align: left
            :class: only-light

      .. raw:: latex
         
         \end{mdframed}
         \vspace{1em}

   >>> P3 = Phase(dim=3)
   >>> P3.output()
   Matrix([
   [1,             0,              0],
   [0, exp(2*I*pi/3),              0],
   [0,             0, exp(-2*I*pi/3)]])
   >>> P3.diagram()

   ..

      .. raw:: latex
         
         \vspace{1em}
         \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_phase_p3-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html or latex

         .. image:: /figures/output/text_examples_docstrings_gate_phase_p3-light.png
            :scale: 40 %
            :align: left
            :class: only-light

      .. raw:: latex
         
         \end{mdframed}
         \vspace{1em}

   >>> W = Phase(phase="w", dim=3, label="W")
   >>> W.output()
   Matrix([
   [1, 0,    0],
   [0, w,    0],
   [0, 0, w**2]])
   >>> W.diagram()

   ..

      .. raw:: latex
         
         \vspace{1em}
         \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_phase_w-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html or latex

         .. image:: /figures/output/text_examples_docstrings_gate_phase_w-light.png
            :scale: 40 %
            :align: left
            :class: only-light

      .. raw:: latex
         
         \end{mdframed}
         \vspace{1em}

   .. raw:: latex

      \hrulefillthick

   .. autoproperty:: qhronology.quantum.gates.Phase.phase

.. raw:: latex

   \hrulefillthick

.. autoclass:: qhronology.quantum.gates.Diagonal
   :show-inheritance:

   .. rubric:: :styleheader6:`Examples`

   >>> D = Diagonal(entries={0: "u", 1: "v"}, exponentiation=False)
   >>> D.output()
   Matrix([
   [u, 0],
   [0, v]])
   >>> D.diagram()

   ..

      .. raw:: latex
         
         \vspace{1em}
         \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_diagonal_d-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html or latex

         .. image:: /figures/output/text_examples_docstrings_gate_diagonal_d-light.png
            :scale: 40 %
            :align: left
            :class: only-light

      .. raw:: latex
         
         \end{mdframed}
         \vspace{1em}

   >>> P = Diagonal(
   ...     entries={1: "p"},
   ...     exponentiation=True,
   ...     symbols={"p": {"real": True}},
   ...     label="P",
   ... )
   >>> P.output()
   Matrix([
   [1,        0],
   [0, exp(I*p)]])
   >>> P.diagram()

   ..

      .. raw:: latex
         
         \vspace{1em}
         \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_diagonal_p-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html or latex

         .. image:: /figures/output/text_examples_docstrings_gate_diagonal_p-light.png
            :scale: 40 %
            :align: left
            :class: only-light

      .. raw:: latex
         
         \end{mdframed}
         \vspace{1em}

   >>> D3 = Diagonal(
   ...     entries={0: "a", 1: "b", 2: "c"},
   ...     exponentiation=False,
   ...     symbols={"a": {"real": True}, "b": {"real": True}, "c": {"real": True}},
   ...     dim=3,
   ... )
   >>> D3.output()
   Matrix([
   [a, 0, 0],
   [0, b, 0],
   [0, 0, c]])
   >>> D3.diagram()

   ..

      .. raw:: latex
         
         \vspace{1em}
         \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_diagonal_p3-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html or latex

         .. image:: /figures/output/text_examples_docstrings_gate_diagonal_p3-light.png
            :scale: 40 %
            :align: left
            :class: only-light

      .. raw:: latex
         
         \end{mdframed}
         \vspace{1em}

   .. raw:: latex

      \hrulefillthick

   .. autoproperty:: qhronology.quantum.gates.Diagonal.entries

   .. raw:: latex

      \hrulefillthick

   .. autoproperty:: qhronology.quantum.gates.Diagonal.exponentiation

.. raw:: latex

   \hrulefillthick

.. .. autoclass:: qhronology.quantum.gates.Permutation
..    :show-inheritance:

..    .. rubric:: :styleheader6:`Examples`

..    >>> P = Permutation(permutation=[1, 0])
..    >>> P.output()
..    
..    >>> P.diagram()

..    ..

..       .. raw:: latex
         
..          \vspace{1em}
..          \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

..       .. only:: html

..          .. image:: /figures/output/text_examples_docstrings_gate_permutation_p-dark.png
..             :scale: 40 %
..             :align: left
..             :class: only-dark

..       .. only:: html or latex

..          .. image:: /figures/output/text_examples_docstrings_gate_permutation_p-light.png
..             :scale: 40 %
..             :align: left
..             :class: only-light

..       .. raw:: latex
         
..          \end{mdframed}
..          \vspace{1em}

..    >>> P3 = Permutation(permutation=[1, 0], dim=3)
..    >>> P3.output()
..    
..    >>> P3.diagram()

..    ..

..       .. raw:: latex
         
..          \vspace{1em}
..          \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

..       .. only:: html

..          .. image:: /figures/output/text_examples_docstrings_gate_permutation_p3-dark.png
..             :scale: 40 %
..             :align: left
..             :class: only-dark

..       .. only:: html or latex

..          .. image:: /figures/output/text_examples_docstrings_gate_permutation_p3-light.png
..             :scale: 40 %
..             :align: left
..             :class: only-light

..       .. raw:: latex
         
..          \end{mdframed}
..          \vspace{1em}

..    >>> PI = Permutation(permutation=[1, 0, 2])
..    >>> PI.output()
..    
..    >>> PI.diagram()

..    ..

..       .. raw:: latex
         
..          \vspace{1em}
..          \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

..       .. only:: html

..          .. image:: /figures/output/text_examples_docstrings_gate_permutation_pi-dark.png
..             :scale: 40 %
..             :align: left
..             :class: only-dark

..       .. only:: html or latex

..          .. image:: /figures/output/text_examples_docstrings_gate_permutation_pi-light.png
..             :scale: 40 %
..             :align: left
..             :class: only-light

..       .. raw:: latex
         
..          \end{mdframed}
..          \vspace{1em}

..    >>> IP = Permutation(permutation=[0, 2, 1])
..    >>> IP.output()
..    
..    >>> IP.diagram()

..    ..

..       .. raw:: latex
         
..          \vspace{1em}
..          \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

..       .. only:: html

..          .. image:: /figures/output/text_examples_docstrings_gate_permutation_ip-dark.png
..             :scale: 40 %
..             :align: left
..             :class: only-dark

..       .. only:: html or latex

..          .. image:: /figures/output/text_examples_docstrings_gate_permutation_ip-light.png
..             :scale: 40 %
..             :align: left
..             :class: only-light

..       .. raw:: latex
         
..          \end{mdframed}
..          \vspace{1em}

..    >>> PP = Permutation(permutation=[1, 0, 3, 2])
..    >>> PP.output()
..    
..    >>> PP.diagram()

..    ..

..       .. raw:: latex
         
..          \vspace{1em}
..          \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

..       .. only:: html

..          .. image:: /figures/output/text_examples_docstrings_gate_permutation_pp-dark.png
..             :scale: 40 %
..             :align: left
..             :class: only-dark

..       .. only:: html or latex

..          .. image:: /figures/output/text_examples_docstrings_gate_permutation_pp-light.png
..             :scale: 40 %
..             :align: left
..             :class: only-light

..       .. raw:: latex
         
..          \end{mdframed}
..          \vspace{1em}

.. .. raw:: latex

..    \hrulefillthick

.. autoclass:: qhronology.quantum.gates.Swap
   :show-inheritance:

   .. rubric:: :styleheader6:`Examples`

   >>> S = Swap(targets=[0, 1])
   >>> S.output()
   Matrix([
   [1, 0, 0, 0],
   [0, 0, 1, 0],
   [0, 1, 0, 0],
   [0, 0, 0, 1]])
   >>> S.diagram()

   ..

      .. raw:: latex
         
         \vspace{1em}
         \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_swap_s-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html or latex

         .. image:: /figures/output/text_examples_docstrings_gate_swap_s-light.png
            :scale: 40 %
            :align: left
            :class: only-light

      .. raw:: latex
         
         \end{mdframed}
         \vspace{1em}

   >>> S3 = Swap(targets=[0, 1], dim=3)
   >>> S3.output()
   Matrix([
   [1, 0, 0, 0, 0, 0, 0, 0, 0],
   [0, 0, 0, 1, 0, 0, 0, 0, 0],
   [0, 0, 0, 0, 0, 0, 1, 0, 0],
   [0, 1, 0, 0, 0, 0, 0, 0, 0],
   [0, 0, 0, 0, 1, 0, 0, 0, 0],
   [0, 0, 0, 0, 0, 0, 0, 1, 0],
   [0, 0, 1, 0, 0, 0, 0, 0, 0],
   [0, 0, 0, 0, 0, 1, 0, 0, 0],
   [0, 0, 0, 0, 0, 0, 0, 0, 1]])
   >>> S3.diagram()

   ..

      .. raw:: latex
         
         \vspace{1em}
         \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_swap_s3-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html or latex

         .. image:: /figures/output/text_examples_docstrings_gate_swap_s3-light.png
            :scale: 40 %
            :align: left
            :class: only-light

      .. raw:: latex
         
         \end{mdframed}
         \vspace{1em}

   >>> SIS = Swap(targets=[0, 2])
   >>> SIS.output()
   Matrix([
   [1, 0, 0, 0, 0, 0, 0, 0],
   [0, 0, 0, 0, 1, 0, 0, 0],
   [0, 0, 1, 0, 0, 0, 0, 0],
   [0, 0, 0, 0, 0, 0, 1, 0],
   [0, 1, 0, 0, 0, 0, 0, 0],
   [0, 0, 0, 0, 0, 1, 0, 0],
   [0, 0, 0, 1, 0, 0, 0, 0],
   [0, 0, 0, 0, 0, 0, 0, 1]])
   >>> SIS.diagram()

   ..

      .. raw:: latex
         
         \vspace{1em}
         \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_swap_sis-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html or latex

         .. image:: /figures/output/text_examples_docstrings_gate_swap_sis-light.png
            :scale: 40 %
            :align: left
            :class: only-light

      .. raw:: latex
         
         \end{mdframed}
         \vspace{1em}

   >>> SCS = Swap(targets=[0, 2], controls=[1])
   >>> SCS.output()
   Matrix([
   [1, 0, 0, 0, 0, 0, 0, 0],
   [0, 1, 0, 0, 0, 0, 0, 0],
   [0, 0, 1, 0, 0, 0, 0, 0],
   [0, 0, 0, 0, 0, 0, 1, 0],
   [0, 0, 0, 0, 1, 0, 0, 0],
   [0, 0, 0, 0, 0, 1, 0, 0],
   [0, 0, 0, 1, 0, 0, 0, 0],
   [0, 0, 0, 0, 0, 0, 0, 1]])
   >>> SCS.diagram()

   ..

      .. raw:: latex
         
         \vspace{1em}
         \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_swap_scs-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html or latex

         .. image:: /figures/output/text_examples_docstrings_gate_swap_scs-light.png
            :scale: 40 %
            :align: left
            :class: only-light

      .. raw:: latex
         
         \end{mdframed}
         \vspace{1em}

   >>> RSWAP = Swap(targets=[0, 1], exponent=sp.Rational(1, 2), label="√SWAP", family="GATE")
   >>> RSWAP.output()
   Matrix([
   [1,         0,         0, 0],
   [0, 1/2 + I/2, 1/2 - I/2, 0],
   [0, 1/2 - I/2, 1/2 + I/2, 0],
   [0,         0,         0, 1]])
   >>> RSWAP.diagram()

   ..

      .. raw:: latex
         
         \vspace{1em}
         \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_swap_rswap-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html or latex

         .. image:: /figures/output/text_examples_docstrings_gate_swap_rswap-light.png
            :scale: 40 %
            :align: left
            :class: only-light

      .. raw:: latex
         
         \end{mdframed}
         \vspace{1em}

   >>> PSWAP = Swap(
   ...     targets=[0, 1],
   ...     exponent="p",
   ...     symbols={"p": {"real": True}},
   ...     label="SWAP^p",
   ...     family="GATE",
   ... )
   >>> PSWAP.output()
   Matrix([
   [1,                   0,                   0, 0],
   [0, exp(I*pi*p)/2 + 1/2, 1/2 - exp(I*pi*p)/2, 0],
   [0, 1/2 - exp(I*pi*p)/2, exp(I*pi*p)/2 + 1/2, 0],
   [0,                   0,                   0, 1]])
   >>> PSWAP.diagram()

   ..

      .. raw:: latex
         
         \vspace{1em}
         \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_swap_pswap-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html or latex

         .. image:: /figures/output/text_examples_docstrings_gate_swap_pswap-light.png
            :scale: 40 %
            :align: left
            :class: only-light

      .. raw:: latex
         
         \end{mdframed}
         \vspace{1em}

   >>> CSWAP = Swap(targets=[1, 2], controls=[0])
   >>> CSWAP.output()
   Matrix([
   [1, 0, 0, 0, 0, 0, 0, 0],
   [0, 1, 0, 0, 0, 0, 0, 0],
   [0, 0, 1, 0, 0, 0, 0, 0],
   [0, 0, 0, 1, 0, 0, 0, 0],
   [0, 0, 0, 0, 1, 0, 0, 0],
   [0, 0, 0, 0, 0, 0, 1, 0],
   [0, 0, 0, 0, 0, 1, 0, 0],
   [0, 0, 0, 0, 0, 0, 0, 1]])
   >>> CSWAP.diagram()

   ..

      .. raw:: latex
         
         \vspace{1em}
         \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_swap_cswap-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html or latex

         .. image:: /figures/output/text_examples_docstrings_gate_swap_cswap-light.png
            :scale: 40 %
            :align: left
            :class: only-light

      .. raw:: latex
         
         \end{mdframed}
         \vspace{1em}

.. raw:: latex

   \hrulefillthick

.. autoclass:: qhronology.quantum.gates.Summation
   :show-inheritance:

   .. rubric:: :styleheader6:`Examples`

   >>> SUM = Summation(shift=1)
   >>> SUM.output()
   Matrix([
   [0, 1],
   [1, 0]])
   >>> SUM.diagram()

   ..

      .. raw:: latex
         
         \vspace{1em}
         \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_summation_sum-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html or latex

         .. image:: /figures/output/text_examples_docstrings_gate_summation_sum-light.png
            :scale: 40 %
            :align: left
            :class: only-light

      .. raw:: latex
         
         \end{mdframed}
         \vspace{1em}

   >>> SUM3 = Summation(shift=1, dim=3)
   >>> SUM3.output()
   Matrix([
   [0, 0, 1],
   [1, 0, 0],
   [0, 1, 0]])
   >>> SUM3.diagram()

   ..

      .. raw:: latex
         
         \vspace{1em}
         \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_summation_sum3-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html or latex

         .. image:: /figures/output/text_examples_docstrings_gate_summation_sum3-light.png
            :scale: 40 %
            :align: left
            :class: only-light

      .. raw:: latex
         
         \end{mdframed}
         \vspace{1em}

   .. raw:: latex

      \hrulefillthick

   .. autoproperty:: qhronology.quantum.gates.Summation.shift

.. raw:: latex

   \hrulefillthick

.. autoclass:: qhronology.quantum.gates.Not
   :show-inheritance:

   .. rubric:: :styleheader6:`Examples`

   >>> N = Not(targets=[0])
   >>> N.output()
   Matrix([
   [0, 1],
   [1, 0]])
   >>> N.diagram()

   ..

      .. raw:: latex
         
         \vspace{1em}
         \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_not_n-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html or latex

         .. image:: /figures/output/text_examples_docstrings_gate_not_n-light.png
            :scale: 40 %
            :align: left
            :class: only-light

      .. raw:: latex
         
         \end{mdframed}
         \vspace{1em}

   >>> NN = Not(targets=[0, 1])
   >>> NN.output()
   Matrix([
   [0, 0, 0, 1],
   [0, 0, 1, 0],
   [0, 1, 0, 0],
   [1, 0, 0, 0]])
   >>> NN.diagram()

   ..

      .. raw:: latex
         
         \vspace{1em}
         \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_not_nn-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html or latex

         .. image:: /figures/output/text_examples_docstrings_gate_not_nn-light.png
            :scale: 40 %
            :align: left
            :class: only-light

      .. raw:: latex
         
         \end{mdframed}
         \vspace{1em}

   >>> CNOT = Not(targets=[1], controls=[0])
   >>> CNOT.output()
   Matrix([
   [1, 0, 0, 0],
   [0, 1, 0, 0],
   [0, 0, 0, 1],
   [0, 0, 1, 0]])
   >>> CNOT.diagram()

   ..

      .. raw:: latex
         
         \vspace{1em}
         \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_not_cnot-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html or latex

         .. image:: /figures/output/text_examples_docstrings_gate_not_cnot-light.png
            :scale: 40 %
            :align: left
            :class: only-light

      .. raw:: latex
         
         \end{mdframed}
         \vspace{1em}

   >>> ANOT = Not(targets=[1], anticontrols=[0])
   >>> ANOT.output()
   Matrix([
   [0, 1, 0, 0],
   [1, 0, 0, 0],
   [0, 0, 1, 0],
   [0, 0, 0, 1]])
   >>> ANOT.diagram()

   ..

      .. raw:: latex
         
         \vspace{1em}
         \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_not_anot-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html or latex

         .. image:: /figures/output/text_examples_docstrings_gate_not_anot-light.png
            :scale: 40 %
            :align: left
            :class: only-light

      .. raw:: latex
         
         \end{mdframed}
         \vspace{1em}

   >>> CCNOT = Not(targets=[2], controls=[0, 1])
   >>> CCNOT.output()
   Matrix([
   [1, 0, 0, 0, 0, 0, 0, 0],
   [0, 1, 0, 0, 0, 0, 0, 0],
   [0, 0, 1, 0, 0, 0, 0, 0],
   [0, 0, 0, 1, 0, 0, 0, 0],
   [0, 0, 0, 0, 1, 0, 0, 0],
   [0, 0, 0, 0, 0, 1, 0, 0],
   [0, 0, 0, 0, 0, 0, 0, 1],
   [0, 0, 0, 0, 0, 0, 1, 0]])
   >>> CCNOT.diagram()

   ..

      .. raw:: latex
         
         \vspace{1em}
         \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_not_ccnot-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html or latex

         .. image:: /figures/output/text_examples_docstrings_gate_not_ccnot-light.png
            :scale: 40 %
            :align: left
            :class: only-light

      .. raw:: latex
         
         \end{mdframed}
         \vspace{1em}

   >>> RNOT = Not(targets=[0], exponent=sp.Rational(1, 2))
   >>> RNOT.output()
   Matrix([
   [1/2 + I/2, 1/2 - I/2],
   [1/2 - I/2, 1/2 + I/2]])
   >>> RNOT.diagram()

   ..

      .. raw:: latex
         
         \vspace{1em}
         \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_not_rnot-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html or latex

         .. image:: /figures/output/text_examples_docstrings_gate_not_rnot-light.png
            :scale: 40 %
            :align: left
            :class: only-light

      .. raw:: latex
         
         \end{mdframed}
         \vspace{1em}

.. raw:: latex

   \hrulefillthick

.. autoclass:: qhronology.quantum.gates.Hadamard
   :show-inheritance:

   .. rubric:: :styleheader6:`Examples`

   >>> H = Hadamard()
   >>> H.output()
   Matrix([
   [sqrt(2)/2,  sqrt(2)/2],
   [sqrt(2)/2, -sqrt(2)/2]])
   >>> H.diagram()

   ..

      .. raw:: latex
         
         \vspace{1em}
         \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_hadamard_h-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html or latex

         .. image:: /figures/output/text_examples_docstrings_gate_hadamard_h-light.png
            :scale: 40 %
            :align: left
            :class: only-light

      .. raw:: latex
         
         \end{mdframed}
         \vspace{1em}

   >>> HH = Hadamard(targets=[0, 1], label="H⊗H")
   >>> HH.output()
   Matrix([
   [1/2,  1/2,  1/2,  1/2],
   [1/2, -1/2,  1/2, -1/2],
   [1/2,  1/2, -1/2, -1/2],
   [1/2, -1/2, -1/2,  1/2]])
   >>> HH.diagram()

   ..

      .. raw:: latex
         
         \vspace{1em}
         \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_hadamard_hh-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html or latex

         .. image:: /figures/output/text_examples_docstrings_gate_hadamard_hh-light.png
            :scale: 40 %
            :align: left
            :class: only-light

      .. raw:: latex
         
         \end{mdframed}
         \vspace{1em}

   >>> H3 = Hadamard(dim=3)
   >>> H3.output()
   Matrix([
   [sqrt(3)/3,                sqrt(3)/3,                sqrt(3)/3],
   [sqrt(3)/3, sqrt(3)*exp(-2*I*pi/3)/3,  sqrt(3)*exp(2*I*pi/3)/3],
   [sqrt(3)/3,  sqrt(3)*exp(2*I*pi/3)/3, sqrt(3)*exp(-2*I*pi/3)/3]])
   >>> H3.diagram()

   ..

      .. raw:: latex
         
         \vspace{1em}
         \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_hadamard_h3-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html or latex

         .. image:: /figures/output/text_examples_docstrings_gate_hadamard_h3-light.png
            :scale: 40 %
            :align: left
            :class: only-light

      .. raw:: latex
         
         \end{mdframed}
         \vspace{1em}

.. raw:: latex

   \hrulefillthick

.. autoclass:: qhronology.quantum.gates.Fourier
   :show-inheritance:

   .. rubric:: :styleheader6:`Examples`

   >>> F = Fourier()
   >>> F.output()
   Matrix([
   [sqrt(2)/2,  sqrt(2)/2],
   [sqrt(2)/2, -sqrt(2)/2]])
   >>> F.diagram()

   ..

      .. raw:: latex
         
         \vspace{1em}
         \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_fourier_f-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html or latex

         .. image:: /figures/output/text_examples_docstrings_gate_fourier_f-light.png
            :scale: 40 %
            :align: left
            :class: only-light

      .. raw:: latex
         
         \end{mdframed}
         \vspace{1em}

   >>> F3 = Fourier(dim=3)
   >>> F3.output()
   Matrix([
   [sqrt(3)/3,                sqrt(3)/3,                sqrt(3)/3],
   [sqrt(3)/3, sqrt(3)*exp(-2*I*pi/3)/3,  sqrt(3)*exp(2*I*pi/3)/3],
   [sqrt(3)/3,  sqrt(3)*exp(2*I*pi/3)/3, sqrt(3)*exp(-2*I*pi/3)/3]])
   >>> F3.diagram()

   ..

      .. raw:: latex
         
         \vspace{1em}
         \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_fourier_f3-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html or latex

         .. image:: /figures/output/text_examples_docstrings_gate_fourier_f3-light.png
            :scale: 40 %
            :align: left
            :class: only-light

      .. raw:: latex
         
         \end{mdframed}
         \vspace{1em}

   >>> FF = Fourier(targets=[0, 1])
   >>> FF.output()
   Matrix([
   [1/2,  1/2,  1/2,  1/2],
   [1/2, -1/2,  1/2, -1/2],
   [1/2,  I/2, -1/2, -I/2],
   [1/2, -I/2, -1/2,  I/2]])
   >>> FF.diagram()

   ..

      .. raw:: latex
         
         \vspace{1em}
         \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_fourier_ff-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html or latex

         .. image:: /figures/output/text_examples_docstrings_gate_fourier_ff-light.png
            :scale: 40 %
            :align: left
            :class: only-light

      .. raw:: latex
         
         \end{mdframed}
         \vspace{1em}

   .. raw:: latex

      \hrulefillthick

   .. autoproperty:: qhronology.quantum.gates.Fourier.composite

   .. raw:: latex

      \hrulefillthick

   .. autoproperty:: qhronology.quantum.gates.Fourier.reverse

.. raw:: latex

   \hrulefillthick

.. autoclass:: qhronology.quantum.gates.Measurement
   :show-inheritance:

   .. rubric:: :styleheader6:`Examples`

   >>> from qhronology.mechanics.matrices import ket
   >>> basis_vectors = [ket(i) for i in [0, 1]]
   >>> M_basis = Measurement(operators=basis_vectors, observable=False)
   >>> M_basis.diagram()

   ..

      .. raw:: latex
         
         \vspace{1em}
         \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_measurement_basis-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html or latex

         .. image:: /figures/output/text_examples_docstrings_gate_measurement_basis-light.png
            :scale: 40 %
            :align: left
            :class: only-light

      .. raw:: latex
         
         \end{mdframed}
         \vspace{1em}

   >>> pauli_matrices = [Pauli(index=i) for i in [1, 2, 3]]
   >>> M_pauli = Measurement(operators=pauli_matrices, observable=True, targets=[0], num_systems=2)
   >>> M_pauli.diagram()

   ..

      .. raw:: latex
         
         \vspace{1em}
         \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_measurement_pauli-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html or latex

         .. image:: /figures/output/text_examples_docstrings_gate_measurement_pauli-light.png
            :scale: 40 %
            :align: left
            :class: only-light

      .. raw:: latex
         
         \end{mdframed}
         \vspace{1em}

   >>> from qhronology.mechanics.matrices import ket
   >>> plus = (ket(0) + ket(1)) / sp.sqrt(2)
   >>> minus = (ket(0) - ket(1)) / sp.sqrt(2)
   >>> M_pm = Measurement(operators=[plus, minus], observable=False, targets=[1], num_systems=2)
   >>> M_pm.diagram()

   ..

      .. raw:: latex
         
         \vspace{1em}
         \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_measurement_pm-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html or latex

         .. image:: /figures/output/text_examples_docstrings_gate_measurement_pm-light.png
            :scale: 40 %
            :align: left
            :class: only-light

      .. raw:: latex
         
         \end{mdframed}
         \vspace{1em}

   .. raw:: latex

      \hrulefillthick

   .. autoproperty:: qhronology.quantum.gates.Measurement.operators

   .. raw:: latex

      \hrulefillthick

   .. autoproperty:: qhronology.quantum.gates.Measurement.observable

   .. raw:: latex

      \hrulefillthick

Combining gates
===============

.. autoclass:: qhronology.quantum.gates.GateInterleave
   :show-inheritance:

   .. rubric:: :styleheader6:`Examples`

   >>> HI = Hadamard(targets=[0], num_systems=2)
   >>> IH = Hadamard(targets=[1], num_systems=2)
   >>> HH = GateInterleave(HI, IH, merge=True)
   >>> HH.output()
   Matrix([
   [1/2,  1/2,  1/2,  1/2],
   [1/2, -1/2,  1/2, -1/2],
   [1/2,  1/2, -1/2, -1/2],
   [1/2, -1/2, -1/2,  1/2]])
   >>> HH.diagram(sep=(1, 2))

   ..

      .. raw:: latex
         
         \vspace{1em}
         \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_composition_hh-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html or latex

         .. image:: /figures/output/text_examples_docstrings_gate_composition_hh-light.png
            :scale: 40 %
            :align: left
            :class: only-light

      .. raw:: latex
         
         \end{mdframed}
         \vspace{1em}

   >>> XII = Pauli(index=1, targets=[0], num_systems=3)
   >>> IYI = Pauli(index=2, targets=[1], num_systems=3)
   >>> IIZ = Pauli(index=3, targets=[2], num_systems=3)
   >>> XYZ = GateInterleave(XII, IYI, IIZ)
   >>> XYZ.output()
   Matrix([
   [0,  0,  0, 0, 0,  0, -I, 0],
   [0,  0,  0, 0, 0,  0,  0, I],
   [0,  0,  0, 0, I,  0,  0, 0],
   [0,  0,  0, 0, 0, -I,  0, 0],
   [0,  0, -I, 0, 0,  0,  0, 0],
   [0,  0,  0, I, 0,  0,  0, 0],
   [I,  0,  0, 0, 0,  0,  0, 0],
   [0, -I,  0, 0, 0,  0,  0, 0]])
   >>> XYZ.diagram(sep=(1, 2))

   ..

      .. raw:: latex
         
         \vspace{1em}
         \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_composition_xyz-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html or latex

         .. image:: /figures/output/text_examples_docstrings_gate_composition_xyz-light.png
            :scale: 40 %
            :align: left
            :class: only-light

      .. raw:: latex
         
         \end{mdframed}
         \vspace{1em}

   >>> CNII = Not(targets=[1], controls=[0], num_systems=4)
   >>> IINC = Not(targets=[2], controls=[3], num_systems=4)
   >>> CNNC = GateInterleave(CNII, IINC)
   >>> CNNC.diagram()

   ..

      .. raw:: latex
         
         \vspace{1em}
         \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_composition_cncn-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html or latex

         .. image:: /figures/output/text_examples_docstrings_gate_composition_cncn-light.png
            :scale: 40 %
            :align: left
            :class: only-light

      .. raw:: latex
         
         \end{mdframed}
         \vspace{1em}

   .. raw:: latex

      \hrulefillthick

   .. autoproperty:: qhronology.quantum.gates.GateInterleave.gates

   .. raw:: latex

      \hrulefillthick

   .. autoproperty:: qhronology.quantum.gates.GateInterleave.merge

   .. raw:: latex

      \hrulefillthick

.. autoclass:: qhronology.quantum.gates.GateStack
   :show-inheritance:

   .. rubric:: :styleheader6:`Examples`

   >>> X = Pauli(index=1)
   >>> Y = Pauli(index=2)
   >>> Z = Pauli(index=3)
   >>> XYZ = GateStack(X, Y, Z)
   >>> XYZ.output()
   Matrix([
   [0,  0,  0, 0, 0,  0, -I, 0],
   [0,  0,  0, 0, 0,  0,  0, I],
   [0,  0,  0, 0, I,  0,  0, 0],
   [0,  0,  0, 0, 0, -I,  0, 0],
   [0,  0, -I, 0, 0,  0,  0, 0],
   [0,  0,  0, I, 0,  0,  0, 0],
   [I,  0,  0, 0, 0,  0,  0, 0],
   [0, -I,  0, 0, 0,  0,  0, 0]])
   >>> XYZ.diagram(sep=(1, 2))

   ..

      .. raw:: latex
         
         \vspace{1em}
         \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_stack_xyz-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html or latex

         .. image:: /figures/output/text_examples_docstrings_gate_stack_xyz-light.png
            :scale: 40 %
            :align: left
            :class: only-light

      .. raw:: latex
         
         \end{mdframed}
         \vspace{1em}

   >>> gates = [Not(targets=[(i + 1) % 2], controls=[i % 2]) for i in range(0, 4)]
   >>> CNOTs = GateStack(*gates)
   >>> CNOTS.diagram()

   ..

      .. raw:: latex
         
         \vspace{1em}
         \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_stack_cnots-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html or latex

         .. image:: /figures/output/text_examples_docstrings_gate_stack_cnots-light.png
            :scale: 40 %
            :align: left
            :class: only-light

      .. raw:: latex
         
         \end{mdframed}
         \vspace{1em}

   >>> gates = [GellMann(index=i) for i in range(1, 9)]
   >>> L = GateStack(*gates)
   >>> L.diagram(sep=(1, 1))

   ..

      .. raw:: latex
         
         \vspace{1em}
         \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_stack_gellmann-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html or latex

         .. image:: /figures/output/text_examples_docstrings_gate_stack_gellmann-light.png
            :scale: 40 %
            :align: left
            :class: only-light

      .. raw:: latex
         
         \end{mdframed}
         \vspace{1em}