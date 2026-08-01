.. _`eg:generation_w_general`:

Generation of the generalized W state
=====================================

Description
-----------

The circuit in :numref:`fig:circuit_algorithm_generation_w_general` illustrates an algorithm for the generation of a generalized :math:`\Number`-qubit W state (see :numref:`eg:generation_w` :ref:`eg:generation_w`),

.. math::

   \begin{aligned}
       \ket{\mathrm{W}} &= \frac{1}{\sqrt{\Number}} \sum_{k=0}^{\Number - 1} \left(\bigotimes_{n=0}^{\Number - 1 - k} \ket{0}\right) \otimes \ket{1} \otimes \left(\bigotimes_{n=\Number - 1 - k}^{0} \ket{0}\right) \\
       &= \frac{1}{\sqrt{\Number}} \sum_{k=0}^{\Number - 1} \ket{0}^{\otimes k} \otimes \ket{1} \otimes \ket{0}^{\otimes (\Number - 1 - k)} \\
       &= \frac{1}{\sqrt{\Number}} \bigl[\ket{1} \otimes \ket{0} \otimes \ldots \otimes \ket{0} \\
       &\qquad \quad\;\; + \ket{0} \otimes \ket{1} \otimes \ldots \otimes \ket{0} \\ 
       &\qquad \quad\;\; + \ldots \\
       &\qquad \quad\;\; + \ket{0} \otimes \ket{0} \otimes \ldots \otimes \ket{1}\bigr],
   \end{aligned}

from primitive :math:`\ket{0}` states.

.. only:: html

   .. figure:: /figures/output/circuit_algorithm_generation_w_general-dark.png
      :scale: 34 %
      :alt: A quantum circuit diagram depicting the generation of a generalized W state.
      :align: center
      :figwidth: 100 %
      :figclass: only-dark

   .. figure:: /figures/output/circuit_algorithm_generation_w_general-light.png
      :scale: 34 %
      :alt: A quantum circuit diagram depicting the generation of a generalized W state.
      :align: center
      :figwidth: 100 %
      :figclass: only-light

.. figure:: /figures/output/circuit_algorithm_generation_w_general-light.png
   :name: fig:circuit_algorithm_generation_w_general
   :scale: 34 %
   :alt: A quantum circuit diagram depicting the generation of a generalized W state.
   :align: center
   :figwidth: 100 %
   :figclass: light-dark hidden

   Generation of the generalized W state.

.. raw:: latex

   \vspace*{-\baselineskip}

The complete unitary transformation described by this circuit is the product

.. math::
   
   \begin{aligned}
       \Unitary &= \NOT^{\indices{0}} \cdot \Control^{\indices{0}} \NOT^{\indices{1}} \cdot \Control^{\indices{1}} \NOT^{\indices{2}} \cdot \ldots \cdot \Control^{\indices{\Number - 2}} \NOT^{\indices{\Number - 1}} \\
       &\quad \cdot \; \Control^{\indices{\Number - 3}} \Rotation_{y}^{\indices{\Number - 2}}(\theta_{\Number - 2}) \cdot \ldots \cdot \Control^{\indices{1}} \Rotation_{y}^{\indices{2}}(\theta_{2}) \cdot \Control^{\indices{0}} \Rotation_{y}^{\indices{1}}(\theta_{1}) \cdot \Rotation_{y}^{\indices{0}}(\theta_{0}) \\
       &= \NOT^{\indices{0}} \cdot \Biggl(\prod_{n = 1}^{\Number - 1} \Control^{\indices{n - 1}} \NOT^{\indices{n}} \Biggr) \cdot \Biggl(\prod_{n = \Number - 2}^{1} \Control^{\indices{n - 1}} \Rotation_{y}^{\indices{n}}(\theta_{n})  \Biggr) \cdot \Rotation_{y}^{\indices{0}}(\theta_{0}),
   \end{aligned}

where the :math:`y`-rotation angles are given by :math:`\theta_n = 2 \arccos\left(\tfrac{1}{\sqrt{\Number - n}}\right)`.

.. raw:: latex

   \vspace*{-0.15\baselineskip}

Implementation
--------------

.. raw:: latex

   \begin{codetitled}{Generation of the generalized W state}{}

.. literalinclude:: /text/examples/algorithms/generation_w_general.py
   :name: code:generation_w_general
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
   
   \includegraphics[scale=1.25, trim=-0.02cm -0.10cm 0 -0.12cm]{text_examples_algorithms_generation_w_general.pdf}
   \vspace{-1\baselineskip}

..

   .. only:: html

      .. image:: /figures/output/text_examples_algorithms_generation_w_general-dark.png
         :scale: 36 %
         :align: left
         :class: only-dark

   .. only:: html

      .. image:: /figures/output/text_examples_algorithms_generation_w_general-light.png
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
   |W⟩ = 1/2|0,0,0,1⟩ + 1/2|0,0,1,0⟩ + 1/2|0,1,0,0⟩ + 1/2|1,0,0,0⟩

.. raw:: latex

   \end{code}

.. raw:: latex
   
   \newpage
