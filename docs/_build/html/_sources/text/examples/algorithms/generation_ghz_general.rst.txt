.. _`eg:generation_ghz_general`:

Generation of the generalized GHZ state
=======================================

Description
-----------

The circuit in :numref:`fig:circuit_algorithm_generation_ghz_general` illustrates an algorithm for the generation of an entangled :math:`\Number`-qudit state,

.. math::

   \begin{aligned}
       \ket{\mathrm{GHZ}} &= \frac{1}{\sqrt{\Dimension}} \sum_{k=0}^{\Dimension - 1} \bigotimes_{n=1}^{\Number} \ket{k} \\
       &= \frac{1}{\sqrt{\Dimension}} \sum_{k=0}^{\Dimension - 1} \ket{k}^{\otimes \Number} \\
       &= \frac{1}{\sqrt{\Dimension}} \sum_{k=0}^{\Dimension - 1} \ket{k} \otimes \ldots \otimes \ket{k},
   \end{aligned}

from primitive :math:`\ket{0}` states. This is a generalized version of the GHZ state (see :numref:`eg:generation_ghz` :ref:`eg:generation_ghz`).

.. only:: html

   .. figure:: /figures/output/circuit_algorithm_generation_ghz_general-dark.png
      :scale: 34 %
      :alt: A quantum circuit diagram depicting the generation of a generalized GHZ state.
      :align: center
      :figwidth: 100 %
      :figclass: only-dark

   .. figure:: /figures/output/circuit_algorithm_generation_ghz_general-light.png
      :scale: 34 %
      :alt: A quantum circuit diagram depicting the generation of a generalized GHZ state.
      :align: center
      :figwidth: 100 %
      :figclass: only-light

.. figure:: /figures/output/circuit_algorithm_generation_ghz_general-light.png
   :name: fig:circuit_algorithm_generation_ghz_general
   :scale: 34 %
   :alt: A quantum circuit diagram depicting the generation of a generalized GHZ state.
   :align: center
   :figwidth: 100 %
   :figclass: light-dark hidden

   Generation of the generalized GHZ state.

.. raw:: latex

   \vspace*{-\baselineskip}

The complete unitary transformation described by this circuit is the product

.. math::
   
   \begin{aligned}
       \Unitary &= \Control^{\Number - 2} \SUM^{\Number - 1} \cdot \ldots \cdot \Control^1 \SUM^2 \cdot \Control^0 \SUM^1 \cdot \Hadamard^0 \\
       &= \Biggl(\prod_{n = \Number - 1}^{1} \Control^{n - 1} \SUM^{n} \Biggr) \Hadamard^0.
   \end{aligned}

Implementation
--------------

.. raw:: latex

   \enlargethispage{-2\baselineskip}

.. raw:: latex

   \begin{codetitled}{Generation of the generalized GHZ state}{}

.. literalinclude:: /text/examples/algorithms/generation_ghz_general.py
   :name: code:generation_ghz_general
   :language: python
   :caption:

.. raw:: latex

   \end{codetitled}

Output
------

.. raw:: latex

   \enlargethispage{2\baselineskip}

Diagram
^^^^^^^

.. raw:: latex

   \begin{code}

.. code:: python

   >>> generator.diagram()

.. raw:: latex
   
   \includegraphics[scale=1.25, trim=-0.02cm -0.10cm 0 -0.12cm]{text_examples_algorithms_generation_ghz_general.pdf}
   \vspace{-1\baselineskip}

..

   .. only:: html

      .. image:: /figures/output/text_examples_algorithms_generation_ghz_general-dark.png
         :scale: 40 %
         :align: left
         :class: only-dark

   .. only:: html

      .. image:: /figures/output/text_examples_algorithms_generation_ghz_general-light.png
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
   |GHZ⟩ = 1/2|0,0,0,0⟩ + 1/2|1,1,1,1⟩ + 1/2|2,2,2,2⟩ + 1/2|3,3,3,3⟩

.. raw:: latex

   \end{code}

.. raw:: latex
   
   \newpage
