.. _`eg:deutsch_jozsa`:

Deutsch-Jozsa algorithm
=======================

Description
-----------

The *Deutsch-Jozsa algorithm* :cite:p:`deutsch_rapid_1992` is a deterministic quantum algorithm for solving the associated *Deutsch-Jozsa problem*---a black box (i.e., query) problem which is specifically designed to be easy to solve on a quantum computer and difficult to solve (deterministically) on a classical computer.

In the Deutsch-Jozsa problem, we are given a function,

.. math:: f : \{0,1\}^n \rightarrow \{0,1\},

with the promise that :math:`f` is either *constant* (:math:`f = 0` or :math:`f = 1` for the entire input domain) or *balanced* (:math:`f = 0` for exactly half of the input domain and :math:`f = 1` for the other half). The task is to determine, through querying the function (via its manifestation as a black box computer), whether :math:`f` is constant or balanced.

Classically, the Deutsch-Jozsa problem can be solved deterministically with at most :math:`2^{n-1} + 1` evaluations (queries) of :math:`f`, where :math:`n` is the number of bits. This is to say that, for a deterministic algorithm, just over half of the entire input domain must be evaluated in order to be able to arrive at a solution with no possibility of error. Alternatively, in the statistically unlikely (especially for large :math:`n`) best case, if :math:`f` is balanced, just two evaluations are required.

Alternatively, the quantum-mechanical Deutsch-Jozsa algorithm solves the query problem, without error, in a single evaluation of :math:`f`. As such, although solving the Deutsch-Jozsa problem is of little practical use, it is an example of a problem where there exists a quantum algorithm that is exponentially faster than any possible deterministic classical algorithm.

Note that the Deutsch-Jozsa algorithm generalizes earlier work by David Deutsch, specifically that of *Deutsch's algorithm* :cite:p:`deutsch_quantum_1985`, which is historically one of the first quantum algorithms to demonstrate a quantum advantage (i.e., a reduction in query complexity compared to the classical case). In this simplier variant, which concerns the special case of :math:`n=1`, the query problem is solved non-deterministically, with a probability of success of :math:`1/2`.

It is also important to note that, while deterministic, the first incarnation of the Deutsch-Jozsa algorithm (as it was originally presented in 1992) required exactly two queries of :math:`f`. Later improvements by Cleve et al. :cite:p:`cleve_quantum_1998` resulted in an algorithm that is both deterministic and requires only a single query of :math:`f`, and it is this form that is known today canonically as the "Deutsch-Jozsa algorithm".

Algorithm
---------

In the Deutsch-Jozsa algorithm (depicted in :numref:`fig:circuit_algorithm_deutsch_jozsa`), querying of the function :math:`f` is implemented as an oracle :math:`\Oracle_f`, which has the action

.. math:: \Oracle_f \ket{x} \otimes \ket{y} = \ket{x} \otimes \ket{y \oplus f(x)}.
   :label: eq:deutsch_jozsa_oracle_action

.. only:: html

   .. figure:: /figures/output/circuit_algorithm_deutsch_jozsa-dark.png
      :scale: 34 %
      :alt: A quantum circuit diagram of the Deutsch-Jozsa algorithm.
      :align: center
      :figwidth: 100 %
      :figclass: only-dark

   .. figure:: /figures/output/circuit_algorithm_deutsch_jozsa-light.png
      :scale: 34 %
      :alt: A quantum circuit diagram of the Deutsch-Jozsa algorithm.
      :align: center
      :figwidth: 100 %
      :figclass: only-light

.. figure:: /figures/output/circuit_algorithm_deutsch_jozsa-light.png
   :name: fig:circuit_algorithm_deutsch_jozsa
   :scale: 34 %
   :alt: A quantum circuit diagram of the Deutsch-Jozsa algorithm.
   :align: center
   :figwidth: 100 %
   :figclass: light-dark hidden

   The Deutsch-Jozsa algorithm.

.. raw:: latex

   \vspace*{-\baselineskip}

The input to the algorithm consists of two registers: the :math:`n`-qubit *address* register and the single-qubit *target* register, which are initalized to the states :math:`\ket{0}^{\otimes n}` and :math:`\ket{0}`, respectively. This gives a total input state of

.. math:: \ket{\Psi_0} = \ket{0}^{\otimes n} \otimes \ket{0}.

The first step of the algorithm is to transform the target qubit to a :math:`\ket{1}` state, which is achieved with a Pauli-:math:`X` gate on its register, i.e.,

.. math::

   \begin{aligned}
       \ket{\Psi_1} &= \PauliX^{\indices{n}} \ket{\Psi_0} \\
       &= (\Identity^{\otimes n} \otimes \PauliX) \ket{\Psi_0} \\
       &= \ket{0}^{\otimes n} \otimes \ket{1}.
   \end{aligned}

Next, all systems are transformed by a Hadamard gate, yielding the superposition

.. math::

   \begin{aligned}
       \ket{\Psi_2} &= \Hadamard^{\otimes (n+1)} \ket{\Psi_1} \\
       &= \ket{+}^{\otimes n} \otimes \ket{-} \\
       &= \frac{1}{\sqrt{2^{n+1}}} \sum_{x = 0}^{2^n - 1} \ket{x} \otimes \bigl(\ket{0} - \ket{1}\bigr),
   \end{aligned}

where each :math:`x` represents a number from :math:`0` to :math:`2^n - 1` encoded as an :math:`n`-qubit string. Applying the oracle then gives

.. math::

   \begin{aligned}
       \ket{\Psi_3} &= \Oracle_f \ket{\Psi_2} \\
       &= \frac{1}{\sqrt{2^{n+1}}} \sum_{x = 0}^{2^n - 1} \ket{x} \otimes \bigl(\ket{0 \oplus f(x)} - \ket{1 \oplus f(x)}\bigr) \\
       &= \frac{1}{\sqrt{2^{n+1}}} \sum_{x = 0}^{2^n - 1} (-1)^{f(x)} \ket{x} \otimes \bigl(\ket{0} - \ket{1}\bigr)
   \end{aligned}

where :math:`\oplus` denotes addition (modulo :math:`2`). Finally, transforming the address register with Hadamard gates results in the final output state

.. math::

   \begin{aligned}
       \ket{\Psi_4} &= (\Hadamard^{\otimes n} \otimes \Identity) \ket{\Psi_3} \\
       &= \frac{1}{2^{n}} \sum_{y = 0}^{2^n - 1} \sum_{x = 0}^{2^n - 1} (-1)^{f(x)} (-1)^{x \cdot y} \ket{y} \otimes \ket{-},
   \end{aligned}

where the used the general form of the Hadamard operator's action

.. math:: \Hadamard^{\otimes n} \ket{k} = \frac{1}{\sqrt{2^{n}}} \sum_{j = 0}^{2^n - 1} (-1)^{j \cdot k} \ket{j}

with the bitwise product

.. math:: j \cdot k \equiv \bigoplus_{i = 0}^{n - 1} j_i k_i.

Performing a measurement on the address register in the computational basis yields the probability of obtaining an output state of :math:`\ket{z}` to be

.. math:: p_z = \abs{\frac{1}{2^n} \sum_{x = 0}^{2^n - 1} (-1)^{f(x)} (-1)^{x \cdot z}}^2.

The probability of measuring an outcome of :math:`z = 0`, corresponding to :math:`\ket{0}^{\otimes n}`, is therefore

.. math::

   \begin{aligned}
   p_0 &= \abs{\frac{1}{2^n} \sum_{x = 0}^{2^n - 1} (-1)^{f(x)}}^2 \\
       &= \begin{cases}
           0, & \text{if } f \text{ is balanced}; \\
           1, & \text{if } f \text{ is constant}.
       \end{cases}
   \end{aligned}

The bifurcation in this result---the forking of the output into two distinct, discrete values---is due to inteference in the summation: constructive interference when :math:`f` is constant and destructive interference when :math:`f` is balanced. This means that, when we measure the output state to be :math:`\ket{0}^{\otimes n}`, the function :math:`f` must be constant, while obtaining any other output state signifies that :math:`f` must be balanced.

Implementation
--------------

It is useful to note that, given the action of the Deutsch-Jozsa oracle as per :eq:`eq:deutsch_jozsa_oracle_action`, a defintion of the oracle as an operator is simply

.. math:: \Oracle_f = \sum_{x,y = 0}^{2^n - 1} \Bigl[\bigl(1 - f(x)\bigr) \ket{x}\bra{x} \otimes \ket{y}\bra{y} + f(x) \ket{x}\bra{x} \otimes \ket{y \oplus 1}\bra{y}\Bigr].

This may alternatively be written equivalently as

.. math:: \Oracle_f = \bigoplus_{x = 0}^{2^n - 1} \left[\bigl(1 - f(x)\bigr) \Identity + f(x) \PauliX \right],

which is the definition we use in the implementation here.

.. raw:: latex

   \newpage

.. raw:: latex

   \begin{codetitled}{Deutsch-Jozsa algorithm}{}

.. literalinclude:: /text/examples/algorithms/deutsch_jozsa.py
   :name: code:deutsch_jozsa
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

   >>> deutsch_jozsa.diagram(pad=(1, 0), sep=(1, 2), force_separation=True)

.. raw:: latex
   
   \includegraphics[scale=1.25, trim=-0.02cm -0.10cm 0 -0.12cm]{text_examples_algorithms_deutsch_jozsa.pdf}
   \vspace{-1\baselineskip}

..

   .. only:: html

      .. image:: /figures/output/text_examples_algorithms_deutsch_jozsa-dark.png
         :scale: 36 %
         :align: left
         :class: only-dark

   .. only:: html

      .. image:: /figures/output/text_examples_algorithms_deutsch_jozsa-light.png
         :scale: 36 %
         :align: left
         :class: only-light

.. raw:: latex
   
   \end{code}

Results
^^^^^^^

If :python:`constant` is :python:`True`:

.. raw:: latex

   \begin{code}

.. code:: python

   >>> print(f"The function: {result_function}")
   The function: constant

.. raw:: latex

   \end{code}

.. raw:: latex

   \begin{code}

.. code:: python

   >>> print(f"The Deutsch-Jozsa result: {result_algorithm}")
   The Deutsch-Jozsa result: constant

.. raw:: latex

   \end{code}

If :python:`constant` is :python:`False`:

.. raw:: latex

   \begin{code}

.. code:: python

   >>> print(f"The function: {result_function}")
   The function: balanced

.. raw:: latex

   \end{code}

.. raw:: latex

   \begin{code}

.. code:: python

   >>> print(f"The Deutsch-Jozsa result: {result_algorithm}")
   The Deutsch-Jozsa result: balanced

.. raw:: latex

   \end{code}

.. only:: html

   .. rst-class:: bibliography

      .. rubric:: :stylebibliography:`References`

      .. bibliography::
         :filter: docname in docnames

.. raw:: latex
   
   \newpage
