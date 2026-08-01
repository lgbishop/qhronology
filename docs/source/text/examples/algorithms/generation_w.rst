.. _`eg:generation_w`:

Generation of the W state
=========================

Description
-----------

The circuit in :numref:`fig:circuit_algorithm_generation_w` illustrates an algorithm for the generation of a W state :eq:`eq:W_state` from primitive :math:`\ket{0}` states.

.. only:: html

   .. figure:: /figures/output/circuit_algorithm_generation_w-dark.png
      :scale: 34 %
      :alt: A quantum circuit diagram depicting the generation of a W state.
      :align: center
      :figwidth: 100 %
      :figclass: only-dark

   .. figure:: /figures/output/circuit_algorithm_generation_w-light.png
      :scale: 34 %
      :alt: A quantum circuit diagram depicting the generation of a W state.
      :align: center
      :figwidth: 100 %
      :figclass: only-light

.. figure:: /figures/output/circuit_algorithm_generation_w-light.png
   :name: fig:circuit_algorithm_generation_w
   :scale: 34 %
   :alt: A quantum circuit diagram depicting the generation of a W state.
   :align: center
   :figwidth: 100 %
   :figclass: light-dark hidden

   Generation of the W state.

.. raw:: latex

   \vspace*{-\baselineskip}

The complete unitary transformation described by this circuit is the product

.. math:: \Unitary = \NOT^{\indices{0}} \cdot \Control^{\indices{0}} \NOT^{\indices{1}} \cdot \Control^{\indices{1}} \NOT^{\indices{2}} \cdot \Control^{\indices{0}} \Hadamard^{\indices{1}} \cdot \Rotation_{y}^{\indices{0}}(\theta),

where the :math:`y`-rotation angle is :math:`\theta = 2 \arccos\left(\tfrac{1}{\sqrt{3}}\right)`.

Implementation
--------------

.. raw:: latex

   \enlargethispage{-3\baselineskip}

.. raw:: latex

   \begin{codetitled}{Generation of the W state}{}

.. literalinclude:: /text/examples/algorithms/generation_w.py
   :name: code:generation_w
   :language: python
   :caption:

.. raw:: latex

   \end{codetitled}

Output
------

Diagram
^^^^^^^

.. raw:: latex

   \begin{code}

.. code:: python

   >>> generator.diagram()

.. raw:: latex
   
   \includegraphics[scale=1.25, trim=-0.02cm -0.10cm 0 -0.12cm]{text_examples_algorithms_generation_w.pdf}
   \vspace{-1\baselineskip}

..

   .. only:: html

      .. image:: /figures/output/text_examples_algorithms_generation_w-dark.png
         :scale: 36 %
         :align: left
         :class: only-dark

   .. only:: html

      .. image:: /figures/output/text_examples_algorithms_generation_w-light.png
         :scale: 36 %
         :align: left
         :class: only-light

.. raw:: latex
   
   \end{code}

State
^^^^^

.. raw:: latex

   \begin{code}

.. code:: python

   >>> w_state.print()
   |W⟩ = sqrt(3)/3|0,0,1⟩ + sqrt(3)/3|0,1,0⟩ + sqrt(3)/3|1,0,0⟩

.. raw:: latex

   \end{code}

.. raw:: latex
   
   \newpage