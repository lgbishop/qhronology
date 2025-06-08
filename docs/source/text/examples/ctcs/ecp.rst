.. _`eg:ecp`:

Equivalent-circuit picture for D-CTCs
=====================================

Description
-----------

This algorithm implements the equivalent-circuit picture (ECP, see :ref:`sec:ECP`) of D-CTCs. In its current form, it is not a particularly useful example, having very general input state and unitary matrix symbolic representations that make any subsequent analysis infeasible. Instead, the algorithm is included simply because it is an interesting demonstration of advanced usage of Qhronology. Note that the larger the number of algebraic symbols (and associated conditions) that are contained within the states and gates, the higher the complexity of the internal calculations, resulting in correspondingly longer computation times.

.. only:: html

   .. figure:: /figures/output/circuit_ctc_dctc_ecp-dark.png
      :scale: 36 %
      :alt: A quantum circuit diagram of the equivalent-circuit picture of a D-CTC.
      :align: center
      :figwidth: 100 %
      :figclass: only-dark

   .. figure:: /figures/output/circuit_ctc_dctc_ecp-light.png
      :scale: 36 %
      :alt: A quantum circuit diagram of the equivalent-circuit picture of a D-CTC.
      :align: center
      :figwidth: 100 %
      :figclass: only-light

.. figure:: /figures/output/circuit_ctc_dctc_ecp-light.png
   :scale: 36 %
   :alt: A quantum circuit diagram of the equivalent-circuit picture of a D-CTC.
   :align: center
   :figwidth: 100 %
   :figclass: light-dark hidden

   The equivalent-circuit picture of a D-CTC.

Implementation
--------------

The desired number of iterations can be changed by setting ``iterations`` to an appropriate positive integer.

.. literalinclude:: /text/examples/ctcs/ecp.py
   :name: code:ecp
   :language: python
   :caption:

Output
------

Diagram
^^^^^^^

.. code:: python

   >>> iteration.diagram()

..

   .. raw:: latex
      
      \vspace{1em}
      \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

   .. only:: html

      .. image:: /figures/output/text_examples_ctcs_ecp-dark.png
         :scale: 40 %
         :align: left
         :class: only-dark

   .. only:: html or latex

      .. image:: /figures/output/text_examples_ctcs_ecp-light.png
         :scale: 40 %
         :align: left
         :class: only-light

   .. raw:: latex
      
      \end{mdframed}
      \vspace{1em}

States
^^^^^^

.. code:: python

   >>> seed_state.print()
   τ_0 = 1/2|0⟩⟨0| + 1/2|1⟩⟨1|

.. raw:: latex
   
   \newpage