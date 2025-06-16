.. _`eg:generation_arbitrary`:

Generation of a generalized GHZ state
=====================================

Description
-----------

The circuit in :numref:`fig:circuit_algorithm_generation_arbitrary` illustrates an algorithm for the generation of an entangled :math:`\Number`-qudit state,

.. math::

   \begin{aligned}
       \ket{\mathrm{GHZ}} &= \frac{1}{\sqrt{\Dimension}} \sum_{k=0}^{\Dimension - 1} \bigotimes_{n=1}^{\Number} \ket{k} \\
       &= \frac{1}{\sqrt{\Dimension}} \sum_{k=0}^{\Dimension - 1} \ket{k}^{\otimes \Number} \\
       &= \frac{1}{\sqrt{\Dimension}} \sum_{k=0}^{\Dimension - 1} \ket{k} \otimes \ldots \otimes \ket{k},
   \end{aligned}

from primitive :math:`\ket{0}` states. This is also known as the *generalized* GHZ state (see :ref:`eg:generation_ghz`).

.. only:: html

   .. figure:: /figures/output/circuit_algorithm_generation_arbitrary-dark.png
      :scale: 36 %
      :alt: A quantum circuit diagram depicting the generation of a generalized GHZ state.
      :align: center
      :figwidth: 100 %
      :figclass: only-dark

   .. figure:: /figures/output/circuit_algorithm_generation_arbitrary-light.png
      :scale: 36 %
      :alt: A quantum circuit diagram depicting the generation of a generalized GHZ state.
      :align: center
      :figwidth: 100 %
      :figclass: only-light

.. figure:: /figures/output/circuit_algorithm_generation_arbitrary-light.png
   :name: fig:circuit_algorithm_generation_arbitrary
   :scale: 36 %
   :alt: A quantum circuit diagram depicting the generation of a generalized GHZ state.
   :align: center
   :figwidth: 100 %
   :figclass: light-dark hidden

   Generation of a generalized GHZ state.

The complete unitary transformation described by this circuit is the product

.. math::
   
   \begin{aligned}
       \Unitary &= \Control^{\Number - 1} \SUM^{\Number} \cdot \ldots \cdot \Control^1 \SUM^2 \cdot \Control^0 \SUM^1 \cdot \Hadamard^0 \\
       &= \Biggl(\prod_{n = 1}^{\Number} \Control^{\Number - n} \SUM^{\Number + 1 - n} \Biggr) \Hadamard^0.
   \end{aligned}

Implementation
--------------

.. literalinclude:: /text/examples/algorithms/generation_arbitrary.py
   :name: code:generation_arbitrary
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

      .. image:: /figures/output/text_examples_algorithms_generation_arbitrary-dark.png
         :scale: 40 %
         :align: left
         :class: only-dark

   .. only:: html or latex

      .. image:: /figures/output/text_examples_algorithms_generation_arbitrary-light.png
         :scale: 40 %
         :align: left
         :class: only-light

   .. raw:: latex
      
      \end{mdframed}
      \vspace{1em}

State
^^^^^

.. code:: python

   >>> entangled_state.print()
   |GHZ⟩ = 1/2|0,0,0,0⟩ + 1/2|1,1,1,1⟩ + 1/2|2,2,2,2⟩ + 1/2|3,3,3,3⟩

.. raw:: latex
   
   \newpage