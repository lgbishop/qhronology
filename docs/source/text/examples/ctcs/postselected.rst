.. _`eg:postselected`:

Manual P-CTC
============

Description
-----------

This example merely serves as a proof of the P-CTC prescription (for qubits). This is achieved by explicitly performing the Bell state preselection and postselection, and subsequently comparing the output to the prescription's CR map.

.. only:: html

   .. figure:: /figures/output/circuit_ctc_pctc_postselected-dark.png
      :scale: 36 %
      :alt: A quantum circuit diagram of the P-CTC algorithm with explicit preselection and postselection.
      :align: center
      :figwidth: 100 %
      :figclass: only-dark

   .. figure:: /figures/output/circuit_ctc_pctc_postselected-light.png
      :scale: 36 %
      :alt: A quantum circuit diagram of the P-CTC algorithm with explicit preselection and postselection.
      :align: center
      :figwidth: 100 %
      :figclass: only-light

.. figure:: /figures/output/circuit_ctc_pctc_postselected-light.png
   :name: fig:circuit_ctc_pctc_postselected
   :scale: 36 %
   :alt: A quantum circuit diagram of the P-CTC algorithm with explicit preselection and postselection.
   :align: center
   :figwidth: 100 %
   :figclass: light-dark hidden

   The P-CTCs prescription with explicit preselection and postselection.


Implementation
--------------

.. literalinclude:: /text/examples/ctcs/postselected.py
   :name: code:postselected
   :language: python
   :caption:

Output
------

Diagram
^^^^^^^

.. code:: python

   >>> postselected_teleportation.diagram(pad=(1, 0), sep=(1, 1), force_separation=True)

..

   .. raw:: latex
      
      \vspace{1em}
      \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

   .. only:: html

      .. image:: /figures/output/text_examples_ctcs_postselected-dark.png
         :scale: 40 %
         :align: left
         :class: only-dark

   .. only:: html or latex

      .. image:: /figures/output/text_examples_ctcs_postselected-light.png
         :scale: 40 %
         :align: left
         :class: only-light

   .. raw:: latex
      
      \end{mdframed}
      \vspace{1em}

States
^^^^^^

.. code:: python

   >>> input_state.print()
   |ψ⟩ = a|0⟩ + b|1⟩

.. code:: python

   >>> output_state.print()
   |ψ'⟩ = (a*U[0, 0] + a*U[1, 1] + b*U[0, 2] + b*U[1, 3])/2|0⟩ + (a*U[2, 0] + a*U[3, 1] + b*U[2, 2] + b*U[3, 3])/2|1⟩

.. code:: python

   >>> pctc_output.print()
   |ψ_P⟩ = (a*U[0, 0] + a*U[1, 1] + b*U[0, 2] + b*U[1, 3])/2|0⟩ + (a*U[2, 0] + a*U[3, 1] + b*U[2, 2] + b*U[3, 3])/2|1⟩

Results
^^^^^^^

.. code:: python

   >>> output_state.distance(pctc_output)
   0

.. raw:: latex
   
   \newpage