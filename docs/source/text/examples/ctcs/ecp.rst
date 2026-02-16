.. _`eg:ecp`:

Equivalent-circuit picture of D-CTCs
====================================

Description
-----------

This algorithm implements the equivalent-circuit picture (ECP, see :numref:`sec:ECP` :ref:`sec:ECP`) of D-CTCs. In its current form, it is not a particularly useful example, having very general input state and unitary matrix symbolic representations that make any subsequent analysis infeasible. Instead, the algorithm is included simply because it is an interesting demonstration of advanced usage of Qhronology. Note that the larger the number of algebraic symbols (and associated conditions) that are contained within the states and gates, the higher the complexity of the internal calculations, resulting in correspondingly longer computation times.

.. only:: html

   .. figure:: /figures/output/circuit_ctc_dctc_ecp-dark.png
      :scale: 34 %
      :alt: A quantum circuit diagram of the equivalent-circuit picture of a D-CTC.
      :align: center
      :figwidth: 100 %
      :figclass: only-dark

   .. figure:: /figures/output/circuit_ctc_dctc_ecp-light.png
      :scale: 34 %
      :alt: A quantum circuit diagram of the equivalent-circuit picture of a D-CTC.
      :align: center
      :figwidth: 100 %
      :figclass: only-light

.. figure:: /figures/output/circuit_ctc_dctc_ecp-light.png
   :scale: 34 %
   :alt: A quantum circuit diagram of the equivalent-circuit picture of a D-CTC.
   :align: center
   :figwidth: 100 %
   :figclass: light-dark hidden

   The equivalent-circuit picture of a D-CTC.

   .. raw:: latex

      \vspace*{-0.85\baselineskip}

Implementation
--------------

.. raw:: latex

   \enlargethispage{-\baselineskip}

The desired number of iterations can be changed by setting :python:`iterations` to an appropriate positive integer.

.. raw:: latex

   \begin{codetitled}{Equivalent-circuit picture of D-CTCs}{}

.. literalinclude:: /text/examples/ctcs/ecp.py
   :name: code:ecp
   :language: python
   :caption:

.. raw:: latex

   \end{codetitled}

.. raw:: latex

   \enlargethispage{\baselineskip}

.. raw:: latex

   \vspace*{-0.1\baselineskip}

Output
------

.. raw:: latex

   \vspace*{-0.1\baselineskip}

Diagram
^^^^^^^

.. raw:: latex

   \vspace*{-0.1\baselineskip}

.. raw:: latex

   \begin{code}

.. code:: python

   >>> iteration.diagram()

.. raw:: latex
   
   \includegraphics[scale=1.25, trim=-0.02cm -0.10cm 0 -0.12cm]{text_examples_ctcs_ecp.pdf}
   \vspace{-1\baselineskip}

..

   .. only:: html

      .. image:: /figures/output/text_examples_ctcs_ecp-dark.png
         :scale: 40 %
         :align: left
         :class: only-dark

   .. only:: html

      .. image:: /figures/output/text_examples_ctcs_ecp-light.png
         :scale: 40 %
         :align: left
         :class: only-light

.. raw:: latex
   
   \end{code}

.. raw:: latex

   \vspace*{-0.1\baselineskip}

States
^^^^^^

.. raw:: latex

   \vspace*{-0.1\baselineskip}

.. raw:: latex

   \begin{code}

.. code:: python

   >>> seed_state.print()
   τ_0 = 1/2|0⟩⟨0| + 1/2|1⟩⟨1|

.. raw:: latex

   \end{code}

Of course, this example uses general (symbolic) forms for the input state :math:`\StateCR` and interaction :math:`\Unitary`. Instead, you can set explicit forms for both of these, and thereby investigate the ECP in the context of specific time-travel scenarios.

.. raw:: latex
   
   \newpage