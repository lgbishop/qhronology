.. include:: /styles.rst

.. _`sec:docs_prescriptions`:

*************
Prescriptions
*************

In Qhronology, quantum circuit models of closed timelike curves (CTCs) are created as instances of the :py:class:`~qhronology.quantum.prescriptions.QuantumCTC` class:

.. raw:: latex

   \begin{code}

.. code:: python

   from qhronology.quantum.prescriptions import QuantumCTC

.. raw:: latex

   \end{code}

This provides almost identical functionality as the :py:class:`~qhronology.quantum.circuits.QuantumCircuit` class (from which it is derived), differing only in the addition of the :py:attr:`~qhronology.quantum.prescriptions.QuantumCTC.systems_respecting` and :py:attr:`~qhronology.quantum.prescriptions.QuantumCTC.systems_violating` properties.

Built upon the :py:class:`~qhronology.quantum.prescriptions.QuantumCTC` class are the various theoretical models (prescriptions) of quantum time travel. Qhronology currently implements two such prescriptions: *Deutsch's model* (D-CTCs) and *postselected teleportation* (P-CTCs):

.. raw:: latex

   \begin{code}

.. code:: python

   from qhronology.quantum.prescriptions import DCTC, PCTC

.. raw:: latex

   \end{code}

Due to their close relationship, instances of the :py:class:`~qhronology.quantum.prescriptions.QuantumCTC` class can be created directly from instances of the :py:class:`~qhronology.quantum.circuits.QuantumCircuit` class. This is achieved by way of the :python:`circuit` argument in the :py:class:`~qhronology.quantum.prescriptions.QuantumCTC` constructor, whereby all attributes of the given :py:class:`~qhronology.quantum.circuits.QuantumCircuit` instance are copied (deeply) to the :py:class:`~qhronology.quantum.prescriptions.QuantumCTC` instance during initialization. Importantly, this enables the various subclasses, such as :py:class:`~qhronology.quantum.prescriptions.DCTC` and :py:class:`~qhronology.quantum.prescriptions.PCTC`, to be instantiated entirely using a single :py:class:`~qhronology.quantum.prescriptions.QuantumCTC` instance, thereby reducing duplication (of arguments) in cases where one wishes to study multiple prescriptions of the same CTC circuit.

Main class
==========

Please note that the documentation of this class includes only properties and methods that are either new or modified from its base class :py:class:`~qhronology.quantum.circuits.QuantumCircuit`.

.. autoclass:: qhronology.quantum.prescriptions.QuantumCTC
   :show-inheritance:

   .. raw:: latex

      \begin{adjustwidth}{0.00cm}{0cm}

   .. rubric:: :styleheader6:`Examples`

   .. raw:: latex

      \begin{codetitled}{SWAP interaction with a CTC}{}

   .. literalinclude:: /text/examples/docstrings/prescription_swap.py
      :language: python
      :caption: SWAP interaction with a CTC

   .. raw:: latex

      \tcblowerspaced

   .. code:: python

      >>> SWAP.diagram()

   .. raw:: latex
      
      \includegraphics[scale=1.25, trim=-0.02cm 0.12cm 0 0.02cm]{text_examples_docstrings_prescription_swap.pdf}
      \vspace{-1\baselineskip}

   ..

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_prescription_swap-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_prescription_swap-light.png
            :scale: 40 %
            :align: left
            :class: only-light

   .. code:: python

      >>> SWAP_DCTC_respecting.print()
      ρ_D = ρ[0, 0]|0⟩⟨0| + ρ[0, 1]|0⟩⟨1| + ρ[1, 0]|1⟩⟨0| + ρ[1, 1]|1⟩⟨1|
      >>> SWAP_DCTC_violating.print()
      τ_D = ρ[0, 0]|0⟩⟨0| + ρ[0, 1]|0⟩⟨1| + ρ[1, 0]|1⟩⟨0| + ρ[1, 1]|1⟩⟨1|
      >>> SWAP_PCTC_respecting.print()
      ρ_P = ρ[0, 0]|0⟩⟨0| + ρ[0, 1]|0⟩⟨1| + ρ[1, 0]|1⟩⟨0| + ρ[1, 1]|1⟩⟨1|
      >>> SWAP_PCTC_violating.print()
      τ_P = ρ[0, 0]|0⟩⟨0| + ρ[0, 1]|0⟩⟨1| + ρ[1, 0]|1⟩⟨0| + ρ[1, 1]|1⟩⟨1|

   .. raw:: latex

      \end{codetitled}

   .. raw:: latex

      \enlargethispage{\baselineskip}

   .. raw:: latex

      \begin{codetitled}{CNOT interaction with a CTC}{}

   .. literalinclude:: /text/examples/docstrings/prescription_cnot.py
      :language: python
      :caption: CNOT interaction with a CTC

   .. raw:: latex

      \tcblowerspaced

   .. code:: python

      >>> CNOT.diagram()

   .. raw:: latex
      
      \includegraphics[scale=1.25, trim=-0.02cm 0.12cm 0 0.02cm]{text_examples_docstrings_prescription_cnot.pdf}
      \vspace{-1\baselineskip}

   ..

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_prescription_cnot-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_prescription_cnot-light.png
            :scale: 40 %
            :align: left
            :class: only-light

   .. code:: python

      >>> CNOT_DCTC_respecting.print()
      ρ_D = ρ[0, 0]|0⟩⟨0| + 2*g*ρ[0, 1]|0⟩⟨1| + 2*g*ρ[1, 0]|1⟩⟨0| + ρ[1, 1]|1⟩⟨1|
      >>> CNOT_DCTC_violating.print()
      τ_D = 1/2|0⟩⟨0| + g|0⟩⟨1| + g|1⟩⟨0| + 1/2|1⟩⟨1|
      >>> CNOT_PCTC_respecting.print()
      ρ_P = |0⟩⟨0|
      >>> CNOT_PCTC_violating.print()
      τ_P = 1/2|0⟩⟨0| + 1/2|1⟩⟨1|

   .. raw:: latex

      \end{codetitled}

   .. raw:: latex

      \end{adjustwidth}

.. raw:: latex

   \hrulefillthick

.. _`sec:docs_prescriptions_properties`:

Constructor argument properties
-------------------------------

.. autoproperty:: qhronology.quantum.prescriptions.QuantumCTC.systems_respecting

.. raw:: latex

   \hrulefillthick

.. autoproperty:: qhronology.quantum.prescriptions.QuantumCTC.systems_violating

.. raw:: latex

   \hrulefillthick

Read-only properties
--------------------

.. autoproperty:: qhronology.quantum.prescriptions.QuantumCTC.matrix

.. raw:: latex

   \hrulefillthick

.. _`sec:docs_prescriptions_methods`:

Methods
-------

.. automethod:: qhronology.quantum.prescriptions.QuantumCTC.input

.. raw:: latex

   \hrulefillthick

.. .. automethod:: qhronology.quantum.prescriptions.QuantumCTC.output_violating

.. .. raw:: latex

..    \hrulefillthick

.. .. automethod:: qhronology.quantum.prescriptions.QuantumCTC.output_respecting

.. .. raw:: latex

..    \hrulefillthick

.. .. automethod:: qhronology.quantum.prescriptions.QuantumCTC.state_violating

.. .. raw:: latex

..    \hrulefillthick

.. .. automethod:: qhronology.quantum.prescriptions.QuantumCTC.state_respecting

.. .. raw:: latex

..    \hrulefillthick

.. automethod:: qhronology.quantum.prescriptions.QuantumCTC.diagram

   .. raw:: latex

      \begin{adjustwidth}{0.00cm}{0cm}

   .. rubric:: :styleheader6:`Examples`
         
   Please see the examples of the :py:class:`~qhronology.quantum.prescriptions.QuantumCTC` class itself. For advanced usage examples, see the corresponding :py:meth:`~qhronology.quantum.circuits.QuantumCircuit.diagram` method of the :py:class:`~qhronology.quantum.circuits.QuantumCircuit` class.

   .. raw:: latex

      \end{adjustwidth}

.. raw:: latex

   \hrulefillthick

Subclasses
==========

Please note that the documentation of these subclasses includes only properties and methods that are either new or modified from the base class :py:class:`~qhronology.quantum.prescriptions.QuantumCTC`.

.. only:: html

   D-CTCs
   ------

.. toctree::
   :maxdepth: 2

   prescriptions/D-CTCs

.. only:: html

   P-CTCs
   ------

.. toctree::
   :maxdepth: 2

   prescriptions/P-CTCs

.. T-CTCs
.. ------

.. .. toctree::
..    :maxdepth: 2

..    prescriptions/T-CTCs
