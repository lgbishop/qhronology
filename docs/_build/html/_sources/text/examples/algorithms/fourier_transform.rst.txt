.. _`eg:fourier_transform`:

Fourier transform decomposition
===============================

Description
-----------

A canonical decomposition of the multipartite (composite) quantum Fourier transform :math:`\QFT_N` (over :math:`N`-qudits) consists of a succession of sequences of Hadamard and phase gates. Depicted in :numref:`fig:circuit_algorithm_fourier_transform`, this can be written mathematically as

.. math:: \QFT_N = \prod_{n = 0}^{N - 1} \Unitary_n

where

.. math:: \Unitary_n = \left(\prod_{j = 1}^{N - 1 - n} \Control^{\indices{n + j}} \bigl(\Phase^{d^{-j}}\bigr)^{\indices{n}} \right) \cdot \Hadamard^{\indices{n}}.

Here,

.. math:: \Phase = \sum_{k=0}^{d-1} \omega^{k} \ket{k}\bra{k}

is the :math:`d`-dimensional phase gate with :math:`\omega \equiv \e^{2\pi\eye/d}`.

.. only:: html

   .. figure:: /figures/output/circuit_algorithm_fourier_transform-dark.png
      :scale: 34 %
      :alt: A quantum circuit diagram of a decomposition of the quantum Fourier transform.
      :align: center
      :figwidth: 100 %
      :figclass: only-dark

   .. figure:: /figures/output/circuit_algorithm_fourier_transform-light.png
      :scale: 34 %
      :alt: A quantum circuit diagram of a decomposition of the quantum Fourier transform.
      :align: center
      :figwidth: 100 %
      :figclass: only-light

.. figure:: /figures/output/circuit_algorithm_fourier_transform-light.png
   :name: fig:circuit_algorithm_fourier_transform
   :scale: 34 %
   :alt: A quantum circuit diagram of a decomposition of the quantum Fourier transform.
   :align: center
   :figwidth: 100 %
   :figclass: light-dark hidden

   A decomposition of the quantum Fourier transform.

.. raw:: latex

   \vspace*{-\baselineskip}

Implementation
--------------

.. raw:: latex

   \enlargethispage{-\baselineskip}

.. raw:: latex

   \begin{codetitled}{Fourier transform decomposition}{}

.. literalinclude:: /text/examples/algorithms/fourier_transform.py
   :name: code:fourier_transform
   :language: python
   :caption:

.. raw:: latex

   \end{codetitled}

Output
------

Note that the total operator's matrix representation is far too large to display here.

Diagram
^^^^^^^

.. raw:: latex

   \begin{code}

.. code:: python

   >>> fourier.diagram(sep=(0, 1), visible={"gates"})

.. raw:: latex
   
   \includegraphics[scale=1.25, trim=-0.02cm -0.10cm 0 -0.12cm]{text_examples_algorithms_fourier_transform.pdf}
   \vspace{-1\baselineskip}

..

   .. only:: html

      .. image:: /figures/output/text_examples_algorithms_fourier_transform-dark.png
         :scale: 36 %
         :align: left
         :class: only-dark

   .. only:: html

      .. image:: /figures/output/text_examples_algorithms_fourier_transform-light.png
         :scale: 36 %
         :align: left
         :class: only-light

.. raw:: latex
   
   \end{code}

.. only:: html

   .. rst-class:: bibliography

      .. rubric:: :stylebibliography:`References`

      .. bibliography::
         :filter: docname in docnames

.. raw:: latex
   
   \newpage