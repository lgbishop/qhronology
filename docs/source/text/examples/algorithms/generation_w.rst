.. _`eg:generation_w`:

Generation of a W state
=======================

Description
-----------

The circuit in :numref:`fig:circuit_algorithm_generation_w` illustrates an algorithm for the generation of a W state :eq:`eq:W_state` from primitive :math:`\ket{0}` states.

.. only:: html

   .. figure:: /figures/output/circuit_algorithm_generation_w-dark.png
      :scale: 36 %
      :alt: A quantum circuit diagram depicting the generation of a W state.
      :align: center
      :figwidth: 100 %
      :figclass: only-dark

   .. figure:: /figures/output/circuit_algorithm_generation_w-light.png
      :scale: 36 %
      :alt: A quantum circuit diagram depicting the generation of a W state.
      :align: center
      :figwidth: 100 %
      :figclass: only-light

.. figure:: /figures/output/circuit_algorithm_generation_w-light.png
   :name: fig:circuit_algorithm_generation_w
   :scale: 36 %
   :alt: A quantum circuit diagram depicting the generation of a W state.
   :align: center
   :figwidth: 100 %
   :figclass: light-dark hidden

   Generation of a W state.

The complete unitary transformation described by this circuit is the product

.. math:: \Unitary = \NOT^0 \cdot \Control^0 \NOT^1 \cdot \Control^1 \NOT^2 \cdot \Control^0 \Hadamard^1 \cdot \Rotation_{y}^0(\theta)

where the :math:`y`-rotation angle is :math:`\theta = 2 \arccos\left(\tfrac{1}{\sqrt{3}}\right)`.

Implementation
--------------

.. literalinclude:: /text/examples/algorithms/generation_w.py
   :name: code:generation_w
   :language: python
   :caption:

Output
------

Diagram
^^^^^^^

.. code:: python

   >>> generator.diagram()

..

   .. raw:: latex
      
      \vspace{1em}
      \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

   .. only:: html

      .. image:: /figures/output/text_examples_algorithms_generation_w-dark.png
         :scale: 40 %
         :align: left
         :class: only-dark

   .. only:: html or latex

      .. image:: /figures/output/text_examples_algorithms_generation_w-light.png
         :scale: 40 %
         :align: left
         :class: only-light

   .. raw:: latex
      
      \end{mdframed}
      \vspace{1em}

State
^^^^^

.. code:: python

   >>> w_state.print()
   |W⟩ = sqrt(3)/3|0,0,1⟩ + sqrt(3)/3|0,1,0⟩ + sqrt(3)/3|1,0,0⟩

.. raw:: latex
   
   \newpage