.. _`eg:generation_ghz`:

Generation of the GHZ state
===========================

Description
-----------

The circuit in :numref:`fig:circuit_algorithm_generation_ghz` illustrates an algorithm for the generation of a GHZ state :eq:`eq:GHZ_state` from primitive :math:`\ket{0}` states.

.. only:: html

   .. figure:: /figures/output/circuit_algorithm_generation_ghz-dark.png
      :scale: 34 %
      :alt: A quantum circuit diagram depicting the generation of a GHZ state.
      :align: center
      :figwidth: 100 %
      :figclass: only-dark

   .. figure:: /figures/output/circuit_algorithm_generation_ghz-light.png
      :scale: 34 %
      :alt: A quantum circuit diagram depicting the generation of a GHZ state.
      :align: center
      :figwidth: 100 %
      :figclass: only-light

.. figure:: /figures/output/circuit_algorithm_generation_ghz-light.png
   :name: fig:circuit_algorithm_generation_ghz
   :scale: 34 %
   :alt: A quantum circuit diagram depicting the generation of a GHZ state.
   :align: center
   :figwidth: 100 %
   :figclass: light-dark hidden

   Generation of the GHZ state.

.. raw:: latex

   \vspace*{-\baselineskip}

The complete unitary transformation described by this circuit is the product

.. math:: \Unitary = \Control^1 \NOT^2 \cdot \Control^0 \NOT^1 \cdot \Hadamard^0.

Implementation
--------------

.. raw:: latex

   \begin{codetitled}{Generation of the GHZ state}{}

.. literalinclude:: /text/examples/algorithms/generation_ghz.py
   :name: code:generation_ghz
   :language: python
   :caption:

.. raw:: latex

   \end{codetitled}

.. raw:: latex

   \newpage

Output
------

Diagram
^^^^^^^

.. raw:: latex

   \begin{code}

.. code:: python

   >>> generator.diagram()

.. raw:: latex
   
   \includegraphics[scale=1.25, trim=-0.02cm -0.10cm 0 -0.12cm]{text_examples_algorithms_generation_ghz.pdf}
   \vspace{-1\baselineskip}

..

   .. only:: html

      .. image:: /figures/output/text_examples_algorithms_generation_ghz-dark.png
         :scale: 40 %
         :align: left
         :class: only-dark

   .. only:: html

      .. image:: /figures/output/text_examples_algorithms_generation_ghz-light.png
         :scale: 40 %
         :align: left
         :class: only-light

.. raw:: latex
   
   \end{code}

State
^^^^^

.. raw:: latex

   \begin{code}

.. code:: python

   >>> ghz_state.print()
   |GHZ⟩ = sqrt(2)/2|0,0,0⟩ + sqrt(2)/2|1,1,1⟩

.. raw:: latex

   \end{code}

.. raw:: latex
   
   \newpage