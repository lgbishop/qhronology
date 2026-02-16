.. include:: /styles.rst

.. _`sec:docs_circuits`:

********
Circuits
********

In Qhronology, quantum circuits are created as instances of the :py:class:`~qhronology.quantum.circuits.QuantumCircuit` class:

.. raw:: latex

   \begin{code}

.. code:: python

   from qhronology.quantum.circuits import QuantumCircuit

.. raw:: latex

   \end{code}

In the circuit diagram picturalism, time increases from left to right. Accordingly, the preparation of *input* states (given as instances of the :py:class:`~qhronology.quantum.states.QuantumState`) begins in the past (on the left), while post-processing (such as postselections and partial traces) occurs in the future (on the right). Intermediary operations on these states are represented by quantum gates, given as instances of the :py:class:`~qhronology.quantum.gates.QuantumGate` class and its derivatives. All of these events are connected by quantum wires describing the flow of quantum information (i.e., quantum probabilities) through time.

Main class
==========

.. autoclass:: qhronology.quantum.circuits.QuantumCircuit
   :show-inheritance:

   .. raw:: latex

      \begin{adjustwidth}{0.00cm}{0cm}

   .. rubric:: :styleheader6:`Examples`

   .. raw:: latex

      \enlargethispage{\baselineskip}

   .. raw:: latex

      \begin{codetitled}{Quantum bit-flip}{}

   .. literalinclude:: /text/examples/docstrings/circuit_bitflip.py
      :language: python
      :caption: Quantum bit-flip

   .. raw:: latex

      \tcblowerspaced

   .. code:: python

      >>> bitflip.diagram(pad=(0, 0), sep=(1, 1), style="unicode")

   .. raw:: latex
      
      \includegraphics[scale=1.25, trim=-0.02cm 0.10cm 0 0.00cm]{text_examples_docstrings_circuit_bitflip.pdf}
      \vspace{-1\baselineskip}

   ..

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_circuit_bitflip-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_circuit_bitflip-light.png
            :scale: 40 %
            :align: left
            :class: only-light

   .. code:: python

      >>> input_state.print()
      |ψ⟩ = a|0⟩ + b|1⟩
      >>> output_state.print()
      |ψ′⟩ = b|0⟩ + a|1⟩

   .. raw:: latex

      \end{codetitled}

   .. raw:: latex

      \begin{codetitled}{Arbitrary state generation}{}

   .. literalinclude:: /text/examples/docstrings/circuit_arbitrary.py
      :language: python
      :caption: Arbitrary state generation

   .. raw:: latex

      \tcblowerspaced

   .. code:: python

      >>> generator.diagram(pad=(0, 0), sep=(1, 1), style="unicode")

   .. raw:: latex
      
      \includegraphics[scale=1.25, trim=-0.02cm 0.10cm 0 0.00cm]{text_examples_docstrings_circuit_arbitrary.pdf}
      \vspace{-1\baselineskip}

   ..

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_circuit_arbitrary-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_circuit_arbitrary-light.png
            :scale: 40 %
            :align: left
            :class: only-light

   .. code:: python

      >>> arbitrary_state.print()
      |ψ⟩ = cos(θ)|0⟩ + exp(I*φ)*sin(θ)|1⟩

   .. raw:: latex

      \end{codetitled}

   .. raw:: latex

      \begin{codetitled}{CNOTs equivalent to SWAP}{}

   .. literalinclude:: /text/examples/docstrings/circuit_swapcnots.py
      :language: python
      :caption: CNOTs equivalent to SWAP

   .. raw:: latex

      \tcblowerspaced

   .. code:: python

      >>> swapcnots.diagram(pad=(0, 0), sep=(1, 1), style="unicode")

   .. raw:: latex
      
      \includegraphics[scale=1.25, trim=-0.02cm 0.10cm 0 0.00cm]{text_examples_docstrings_circuit_swapcnots.pdf}
      \vspace{-1\baselineskip}

   ..

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_circuit_swapcnots-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_circuit_swapcnots-light.png
            :scale: 40 %
            :align: left
            :class: only-light

   .. code:: python

      >>> print(repr(swapcnots.gate()))
      Matrix([
      [1, 0, 0, 0],
      [0, 0, 1, 0],
      [0, 1, 0, 0],
      [0, 0, 0, 1]])
      >>> input_upper.print()
      |ψ⟩ = a|0⟩ + b|1⟩
      >>> input_lower.print()
      |φ⟩ = c|0⟩ + d|1⟩
      >>> swapcnots.input().print()
      |ψ⊗φ⟩ = a*c|0,0⟩ + a*d|0,1⟩ + b*c|1,0⟩ + b*d|1,1⟩
      >>> output_upper.print()
      |ψ′⟩⟨ψ′| = c*conjugate(c)|0⟩⟨0| + c*conjugate(d)|0⟩⟨1| + d*conjugate(c)|1⟩⟨0| + d*conjugate(d)|1⟩⟨1|
      >>> output_lower.print()
      |φ′⟩⟨φ′| = a*conjugate(a)|0⟩⟨0| + a*conjugate(b)|0⟩⟨1| + b*conjugate(a)|1⟩⟨0| + b*conjugate(b)|1⟩⟨1|
      >>> output_total.print()
      |(ψ⊗φ)′⟩ = a*c|0,0⟩ + b*c|0,1⟩ + a*d|1,0⟩ + b*d|1,1⟩
      >>> output_upper.distance(input_lower)
      0
      >>> output_lower.distance(input_upper)
      0
      >>> output_upper.fidelity(input_lower)
      1
      >>> output_lower.fidelity(input_upper)
      1

   .. raw:: latex

      \end{codetitled}

   .. raw:: latex

      \begin{codetitled}{Bell postselection}{}

   .. literalinclude:: /text/examples/docstrings/circuit_postselection.py
      :language: python
      :caption: Bell postselection

   .. raw:: latex

      \tcblowerspaced

   .. code:: python

      >>> postselection.diagram(pad=(0, 0), sep=(4, 1), style="unicode")

   .. raw:: latex
      
      \includegraphics[scale=1.25, trim=-0.02cm 0.10cm 0 0.00cm]{text_examples_docstrings_circuit_postselection.pdf}
      \vspace{-1\baselineskip}

   ..

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_circuit_postselection-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_circuit_postselection-light.png
            :scale: 40 %
            :align: left
            :class: only-light

   .. code:: python

      >>> input_state.print()
      |ψ⟩ = a|0⟩ + b|1⟩
      >>> output_state.print()
      |ψ′⟩ = a|0⟩ + b|1⟩

   .. raw:: latex

      \end{codetitled}

   .. raw:: latex

      \begin{codetitled}{Unitarity of general symbolic gates}{}

   .. literalinclude:: /text/examples/docstrings/circuit_unitarity.py
      :language: python
      :caption: Unitarity of general symbolic gates

   .. raw:: latex

      \tcblowerspaced

   .. code:: python

      >>> unitarity.diagram(pad=(0, 0), sep=(1, 1), style="unicode")

   .. raw:: latex

      \includegraphics[scale=1.25, trim=-0.02cm 0.10cm 0 0.00cm]{text_examples_docstrings_circuit_unitarity.pdf}
      \vspace{-1\baselineskip}

   ..

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_circuit_unitarity-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_circuit_unitarity-light.png
            :scale: 40 %
            :align: left
            :class: only-light

   .. code:: python

      >>> print(repr(U))
      Matrix([
      [U[0, 0], U[0, 1]],
      [U[1, 0], U[1, 1]]])
      >>> print(repr(Ud))
      Matrix([
      [conjugate(U[0, 0]), conjugate(U[1, 0])],
      [conjugate(U[0, 1]), conjugate(U[1, 1])]])
      >>> print(repr(unitarity.gate()))
      Matrix([
      [1, 0],
      [0, 1]])

   .. raw:: latex

      \end{codetitled}

   .. raw:: latex

      \begin{codetitled}{Fourier transform decomposition}{}

   .. literalinclude:: /text/examples/docstrings/circuit_fourier.py
      :language: python
      :caption: Fourier transform decomposition

   .. raw:: latex

      \tcblowerspaced

   .. code:: python

      >>> fourier.diagram(pad=(0, 0), sep=(0, 1), style="unicode")

   .. raw:: latex
      
      \includegraphics[scale=1.25, trim=-0.02cm -0.12cm 0 0.00cm]{text_examples_docstrings_circuit_fourier.pdf}
      \vspace{-1\baselineskip}

   ..

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_circuit_fourier-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_circuit_fourier-light.png
            :scale: 40 %
            :align: left
            :class: only-light

   .. raw:: latex

      \end{codetitled}

   .. raw:: latex

      \end{adjustwidth}

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

.. raw:: latex

   \enlargethispage{2\baselineskip}

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

.. raw:: latex

   \enlargethispage{\baselineskip}

.. automethod:: qhronology.quantum.circuits.QuantumCircuit.output

.. raw:: latex

   \hrulefillthick

.. raw:: latex

   \enlargethispage{-\baselineskip}

.. automethod:: qhronology.quantum.circuits.QuantumCircuit.state

.. raw:: latex

   \hrulefillthick

.. raw:: latex

   \enlargethispage{\baselineskip}

.. automethod:: qhronology.quantum.circuits.QuantumCircuit.measure

.. raw:: latex

   \hrulefillthick

.. raw:: latex

   \enlargethispage{-\baselineskip}

.. automethod:: qhronology.quantum.circuits.QuantumCircuit.diagram

   .. raw:: latex

      \enlargethispage{\baselineskip}

   .. raw:: latex

      \begin{adjustwidth}{0.00cm}{0cm}

   .. rubric:: :styleheader6:`Examples`

   .. raw:: latex

      \begin{code}

   .. literalinclude:: /text/examples/docstrings/diagram_circuit.py
      :language: python

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> circuit.diagram(pad=(0, 0), sep=(1, 1), style="unicode")

   .. raw:: latex
      
      \includegraphics[scale=1.25, trim=-0.02cm -0.12cm 0 0.00cm]{text_examples_docstrings_diagram_circuit_unicode.pdf}
      \vspace{-1\baselineskip}

   ..

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_diagram_circuit_unicode-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_diagram_circuit_unicode-light.png
            :scale: 40 %
            :align: left
            :class: only-light

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> circuit.diagram(pad=(0, 0), sep=(1, 1), style="unicode_alt")

   .. raw:: latex
      
      \includegraphics[scale=1.25, trim=-0.02cm -0.12cm 0 0.00cm]{text_examples_docstrings_diagram_circuit_shaded.pdf}
      \vspace{-1\baselineskip}

   ..

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_diagram_circuit_shaded-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_diagram_circuit_shaded-light.png
            :scale: 40 %
            :align: left
            :class: only-light

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> circuit.diagram(pad=(0, 0), sep=(1, 1), style="ascii")

   .. raw:: latex
      
      \includegraphics[scale=1.25, trim=-0.02cm -0.12cm 0 0.00cm]{text_examples_docstrings_diagram_circuit_ascii.pdf}
      \vspace{-1\baselineskip}

   ..

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_diagram_circuit_ascii-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_diagram_circuit_ascii-light.png
            :scale: 40 %
            :align: left
            :class: only-light

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> circuit.diagram(pad=(0, 0), sep=(1, 1), force_separation=True)

   .. raw:: latex
      
      \includegraphics[scale=1.25, trim=-0.02cm -0.12cm 0 0.00cm]{text_examples_docstrings_diagram_circuit_forceseparation.pdf}
      \vspace{-1\baselineskip}

   ..

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_diagram_circuit_forceseparation-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_diagram_circuit_forceseparation-light.png
            :scale: 40 %
            :align: left
            :class: only-light

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \newpage

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> circuit.diagram(pad=(0, 0), sep=(1, 1), uniform_spacing=True)

   .. raw:: latex
      
      \includegraphics[scale=1.25, trim=-0.02cm -0.12cm 0 0.00cm]{text_examples_docstrings_diagram_circuit_uniformspacing.pdf}
      \vspace{-1\baselineskip}

   ..

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_diagram_circuit_uniformspacing-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_diagram_circuit_uniformspacing-light.png
            :scale: 40 %
            :align: left
            :class: only-light

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> circuit.diagram(pad=(0, 0), sep=(2, 1), force_separation=True)

   .. raw:: latex
      
      \includegraphics[scale=1.25, trim=-0.02cm -0.12cm 0 0.00cm]{text_examples_docstrings_diagram_circuit_separation_horizontal_increase.pdf}
      \vspace{-1\baselineskip}

   ..

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_diagram_circuit_separation_horizontal_increase-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_diagram_circuit_separation_horizontal_increase-light.png
            :scale: 40 %
            :align: left
            :class: only-light

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> circuit.diagram(pad=(0, 0), sep=(0, 1), force_separation=True)

   .. raw:: latex
      
      \includegraphics[scale=1.25, trim=-0.02cm -0.12cm 0 0.00cm]{text_examples_docstrings_diagram_circuit_separation_horizontal_decrease.pdf}
      \vspace{-1\baselineskip}

   ..

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_diagram_circuit_separation_horizontal_decrease-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_diagram_circuit_separation_horizontal_decrease-light.png
            :scale: 40 %
            :align: left
            :class: only-light

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \enlargethispage{-\baselineskip}

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> circuit.diagram(pad=(0, 0), sep=(1, 2), force_separation=True)

   .. raw:: latex
      
      \includegraphics[scale=1.25, trim=-0.02cm -0.12cm 0 0.00cm]{text_examples_docstrings_diagram_circuit_separation_vertical_increase.pdf}
      \vspace{-1\baselineskip}

   ..

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_diagram_circuit_separation_vertical_increase-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_diagram_circuit_separation_vertical_increase-light.png
            :scale: 40 %
            :align: left
            :class: only-light

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> circuit.diagram(pad=(1, 0), sep=(1, 1), force_separation=True)

   .. raw:: latex
      
      \includegraphics[scale=1.25, trim=-0.02cm -0.12cm 0 0.00cm]{text_examples_docstrings_diagram_circuit_padding_horizontal_increase.pdf}
      \vspace{-1\baselineskip}

   ..

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_diagram_circuit_padding_horizontal_increase-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_diagram_circuit_padding_horizontal_increase-light.png
            :scale: 40 %
            :align: left
            :class: only-light

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> circuit.diagram(pad=(0, 1), sep=(1, 1), force_separation=True)

   .. raw:: latex
      
      \includegraphics[scale=1.25, trim=-0.02cm -0.12cm 0 0.00cm]{text_examples_docstrings_diagram_circuit_padding_vertical_increase.pdf}
      \vspace{-1\baselineskip}

   ..

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_diagram_circuit_padding_vertical_increase-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_diagram_circuit_padding_vertical_increase-light.png
            :scale: 40 %
            :align: left
            :class: only-light

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \end{adjustwidth}