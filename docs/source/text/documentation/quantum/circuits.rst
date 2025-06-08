.. include:: /styles.rst

.. _`sec:docs_circuits`:

********
Circuits
********

In Qhronology, quantum circuits are created as instances of the :py:class:`~qhronology.quantum.circuits.QuantumCircuit` class:

.. code:: python

   from qhronology.quantum.circuits import QuantumCircuit

In the circuit diagram picturalism of these structures, time increases from left to right, and so the preparation of *input* states (created as instances of the :py:class:`~qhronology.quantum.states.QuantumState` class and its derivatives) begins in the past (on the left) while the measurement (or postselection) of *output* states occurs in the future (on the right). Operations on these states are represented by quantum gates (created as instances of the various subclasses of the :py:class:`~qhronology.quantum.gates.QuantumGate` base class), and all of these events are connected by quantum wires describing the flow of quantum information (i.e., quantum probabilities) through time.

Main class
==========

.. autoclass:: qhronology.quantum.circuits.QuantumCircuit
   :show-inheritance:

   .. rubric:: :styleheader6:`Examples`

   .. literalinclude:: /text/examples/docstrings/circuit_bitflip.py
      :language: python
      :caption: Bit-flip

   >>> bitflip.diagram(pad=(0, 0), sep=(1, 1), style="unicode")

   ..

      .. raw:: latex

         \vspace{1em}
         \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_circuit_bitflip-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html or latex

         .. image:: /figures/output/text_examples_docstrings_circuit_bitflip-light.png
            :scale: 40 %
            :align: left
            :class: only-light

      .. raw:: latex

         \end{mdframed}
         \vspace{1em}
   
   >>> input_state.print()
   |ψ⟩ = a|0⟩ + b|1⟩

   >>> output_state.print()
   |ψ'⟩ = b|0⟩ + a|1⟩

   .. literalinclude:: /text/examples/docstrings/circuit_arbitrary.py
      :language: python
      :caption: Arbitrary state generation

   >>> generator.diagram(pad=(0, 0), sep=(1, 1), style="unicode")

   ..

      .. raw:: latex
         
         \vspace{1em}
         \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_circuit_arbitrary-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html or latex

         .. image:: /figures/output/text_examples_docstrings_circuit_arbitrary-light.png
            :scale: 40 %
            :align: left
            :class: only-light

      .. raw:: latex
         
         \end{mdframed}
         \vspace{1em}

   >>> arbitrary_state.print()
   |ψ⟩ = cos(θ)|0⟩ + exp(I*φ)*sin(θ)|1⟩

   .. literalinclude:: /text/examples/docstrings/circuit_swapcnots.py
      :language: python
      :caption: CNOTs equivalent to SWAP

   >>> swapcnots.diagram(pad=(0, 0), sep=(1, 1), style="unicode")

   ..

      .. raw:: latex
         
         \vspace{1em}
         \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_circuit_swapcnots-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html or latex

         .. image:: /figures/output/text_examples_docstrings_circuit_swapcnots-light.png
            :scale: 40 %
            :align: left
            :class: only-light

      .. raw:: latex
         
         \end{mdframed}
         \vspace{1em}

   >>> psi.print()
   |ψ⟩ = a|0⟩ + b|1⟩

   >>> upper.print()
   |ψ'⟩⟨ψ'| = c*conjugate(c)|0⟩⟨0| + c*conjugate(d)|0⟩⟨1| + d*conjugate(c)|1⟩⟨0| + d*conjugate(d)|1⟩⟨1|

   >>> phi.print()
   |φ⟩ = c|0⟩ + d|1⟩

   >>> lower.print()
   |φ'⟩⟨φ'| = a*conjugate(a)|0⟩⟨0| + a*conjugate(b)|0⟩⟨1| + b*conjugate(a)|1⟩⟨0| + b*conjugate(b)|1⟩⟨1|

   >>> upper.distance(phi)
   0

   >>> lower.distance(psi)
   0

   >>> upper.fidelity(phi)
   1

   >>> lower.fidelity(psi)
   1

   .. literalinclude:: /text/examples/docstrings/circuit_postselection.py
      :language: python
      :caption: Bell postselection

   >>> postselection.diagram(pad=(0, 0), sep=(4, 1), style="unicode")

   ..

      .. raw:: latex
         
         \vspace{1em}
         \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_circuit_postselection-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html or latex

         .. image:: /figures/output/text_examples_docstrings_circuit_postselection-light.png
            :scale: 40 %
            :align: left
            :class: only-light

      .. raw:: latex
         
         \end{mdframed}
         \vspace{1em}

   >>> input_state.print()
   |ψ⟩ = a|0⟩ + b|1⟩

   >>> output_state.print()
   |ψ'⟩ = a|0⟩ + b|1⟩

   .. literalinclude:: /text/examples/docstrings/circuit_fourier.py
      :language: python
      :caption: Fourier transform decomposition

   >>> fourier.diagram(pad=(0, 0), sep=(0, 1), style="unicode")

   ..

      .. raw:: latex
         
         \vspace{1em}
         \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_circuit_fourier-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html or latex

         .. image:: /figures/output/text_examples_docstrings_circuit_fourier-light.png
            :scale: 40 %
            :align: left
            :class: only-light

      .. raw:: latex
         
         \end{mdframed}
         \vspace{1em}

.. raw:: latex

   \hrulefillthick

.. _`sec:docs_circuits_properties`:

Constructor argument properties
-------------------------------

.. autoproperty:: qhronology.quantum.circuits.QuantumCircuit.inputs

.. raw:: latex

   \hrulefillthick

.. autoproperty:: qhronology.quantum.circuits.QuantumCircuit.gates

.. raw:: latex

   \hrulefillthick

.. autoproperty:: qhronology.quantum.circuits.QuantumCircuit.traces

.. raw:: latex

   \hrulefillthick

.. autoproperty:: qhronology.quantum.circuits.QuantumCircuit.postselections

.. raw:: latex

   \hrulefillthick

.. autoproperty:: qhronology.quantum.circuits.QuantumCircuit.symbols

.. raw:: latex

   \hrulefillthick

.. autoproperty:: qhronology.quantum.circuits.QuantumCircuit.conditions

.. raw:: latex

   \hrulefillthick

Read-only properties
--------------------

.. autoproperty:: qhronology.quantum.circuits.QuantumCircuit.dim

.. raw:: latex

   \hrulefillthick

.. autoproperty:: qhronology.quantum.circuits.QuantumCircuit.systems

.. raw:: latex

   \hrulefillthick

.. autoproperty:: qhronology.quantum.circuits.QuantumCircuit.systems_traces

.. raw:: latex

   \hrulefillthick

.. autoproperty:: qhronology.quantum.circuits.QuantumCircuit.systems_postselections

.. raw:: latex

   \hrulefillthick

.. autoproperty:: qhronology.quantum.circuits.QuantumCircuit.systems_removed

.. raw:: latex

   \hrulefillthick

.. autoproperty:: qhronology.quantum.circuits.QuantumCircuit.num_systems

.. raw:: latex

   \hrulefillthick

.. autoproperty:: qhronology.quantum.circuits.QuantumCircuit.num_systems_inputs

.. raw:: latex

   \hrulefillthick

.. autoproperty:: qhronology.quantum.circuits.QuantumCircuit.num_systems_gates

.. raw:: latex

   \hrulefillthick

.. autoproperty:: qhronology.quantum.circuits.QuantumCircuit.num_systems_gross

.. raw:: latex

   \hrulefillthick

.. autoproperty:: qhronology.quantum.circuits.QuantumCircuit.num_systems_net

.. raw:: latex

   \hrulefillthick

.. autoproperty:: qhronology.quantum.circuits.QuantumCircuit.num_systems_removed

.. raw:: latex

   \hrulefillthick

.. autoproperty:: qhronology.quantum.circuits.QuantumCircuit.input_is_vector

.. raw:: latex

   \hrulefillthick

.. autoproperty:: qhronology.quantum.circuits.QuantumCircuit.gate_is_linear

.. raw:: latex

   \hrulefillthick

.. autoproperty:: qhronology.quantum.circuits.QuantumCircuit.post_is_vector

.. raw:: latex

   \hrulefillthick

.. autoproperty:: qhronology.quantum.circuits.QuantumCircuit.output_is_vector

.. raw:: latex

   \hrulefillthick

.. autoproperty:: qhronology.quantum.circuits.QuantumCircuit.matrix

.. raw:: latex

   \hrulefillthick

.. _`sec:docs_circuits_methods`:

Methods
-------

.. automethod:: qhronology.quantum.circuits.QuantumCircuit.input

.. raw:: latex

   \hrulefillthick

.. automethod:: qhronology.quantum.circuits.QuantumCircuit.gate

.. raw:: latex

   \hrulefillthick

.. automethod:: qhronology.quantum.circuits.QuantumCircuit.output

.. raw:: latex

   \hrulefillthick

.. automethod:: qhronology.quantum.circuits.QuantumCircuit.state

.. raw:: latex

   \hrulefillthick

.. automethod:: qhronology.quantum.circuits.QuantumCircuit.measure

.. raw:: latex

   \hrulefillthick

.. automethod:: qhronology.quantum.circuits.QuantumCircuit.diagram

   .. rubric:: :styleheader6:`Examples`

   .. literalinclude:: /text/examples/docstrings/diagram_circuit.py
      :language: python

   >>> circuit.diagram(pad=(0, 0), sep=(1, 1), style="unicode")

   ..

      .. raw:: latex
         
         \vspace{1em}
         \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_diagram_circuit_unicode-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html or latex

         .. image:: /figures/output/text_examples_docstrings_diagram_circuit_unicode-light.png
            :scale: 40 %
            :align: left
            :class: only-light

      .. raw:: latex
         
         \end{mdframed}
         \vspace{1em}

   >>> circuit.diagram(pad=(0, 0), sep=(1, 1), style="ascii")

   ..

      .. raw:: latex
         
         \vspace{1em}
         \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_diagram_circuit_ascii-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html or latex

         .. image:: /figures/output/text_examples_docstrings_diagram_circuit_ascii-light.png
            :scale: 40 %
            :align: left
            :class: only-light

      .. raw:: latex
         
         \end{mdframed}
         \vspace{1em}

   >>> circuit.diagram(pad=(0, 0), sep=(1, 1), style="unicode_alt")

   ..

      .. raw:: latex
         
         \vspace{1em}
         \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_diagram_circuit_shaded-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html or latex

         .. image:: /figures/output/text_examples_docstrings_diagram_circuit_shaded-light.png
            :scale: 40 %
            :align: left
            :class: only-light

      .. raw:: latex
         
         \end{mdframed}
         \vspace{1em}

   >>> circuit.diagram(pad=(0, 0), sep=(1, 1), force_separation=True, style="unicode")

   ..

      .. raw:: latex
         
         \vspace{1em}
         \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_diagram_circuit_forceseparation-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html or latex

         .. image:: /figures/output/text_examples_docstrings_diagram_circuit_forceseparation-light.png
            :scale: 40 %
            :align: left
            :class: only-light

      .. raw:: latex
         
         \end{mdframed}
         \vspace{1em}

   >>> circuit.diagram(pad=(0, 0), sep=(1, 1), uniform_spacing=True, style="unicode")

   ..

      .. raw:: latex
         
         \vspace{1em}
         \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_diagram_circuit_uniformspacing-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html or latex

         .. image:: /figures/output/text_examples_docstrings_diagram_circuit_uniformspacing-light.png
            :scale: 40 %
            :align: left
            :class: only-light

      .. raw:: latex
         
         \end{mdframed}
         \vspace{1em}

   >>> circuit.diagram(pad=(0, 1), sep=(1, 1), force_separation=True, style="unicode")

   ..

      .. raw:: latex
         
         \vspace{1em}
         \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_diagram_circuit_padding_vertical_increase-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html or latex

         .. image:: /figures/output/text_examples_docstrings_diagram_circuit_padding_vertical_increase-light.png
            :scale: 40 %
            :align: left
            :class: only-light

      .. raw:: latex
         
         \end{mdframed}
         \vspace{1em}

   >>> circuit.diagram(pad=(1, 0), sep=(1, 1), force_separation=True, style="unicode")

   ..

      .. raw:: latex
         
         \vspace{1em}
         \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_diagram_circuit_padding_horizontal_increase-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html or latex

         .. image:: /figures/output/text_examples_docstrings_diagram_circuit_padding_horizontal_increase-light.png
            :scale: 40 %
            :align: left
            :class: only-light

      .. raw:: latex
         
         \end{mdframed}
         \vspace{1em}

   >>> circuit.diagram(pad=(0, 0), sep=(1, 2), force_separation=True, style="unicode")

   ..

      .. raw:: latex
         
         \vspace{1em}
         \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_diagram_circuit_separation_vertical_increase-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html or latex

         .. image:: /figures/output/text_examples_docstrings_diagram_circuit_separation_vertical_increase-light.png
            :scale: 40 %
            :align: left
            :class: only-light

      .. raw:: latex
         
         \end{mdframed}
         \vspace{1em}

   >>> circuit.diagram(pad=(0, 0), sep=(2, 1), force_separation=True, style="unicode")

   ..

      .. raw:: latex
         
         \vspace{1em}
         \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_diagram_circuit_separation_horizontal_increase-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html or latex

         .. image:: /figures/output/text_examples_docstrings_diagram_circuit_separation_horizontal_increase-light.png
            :scale: 40 %
            :align: left
            :class: only-light

      .. raw:: latex
         
         \end{mdframed}
         \vspace{1em}

   >>> circuit.diagram(pad=(0, 0), sep=(0, 1), force_separation=True, style="unicode")

   ..

      .. raw:: latex
         
         \vspace{1em}
         \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_diagram_circuit_separation_horizontal_decrease-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html or latex

         .. image:: /figures/output/text_examples_docstrings_diagram_circuit_separation_horizontal_decrease-light.png
            :scale: 40 %
            :align: left
            :class: only-light

      .. raw:: latex
         
         \end{mdframed}
         \vspace{1em}