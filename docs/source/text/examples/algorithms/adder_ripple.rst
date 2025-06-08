.. _`eg:adder_ripple`:

Ripple-carry adder
==================

Description
-----------

In this example, we use the single quantum adder circuit described in :ref:`Example: Full adder <eg:adder_full>` to construct a quantum *ripple-carry* adder. Given two (non-negative) integers :math:`x` and :math:`y` (encoded using qubits) as input, a ripple-carry adder computes the (encoded) arithmetic sum :math:`s` of these integers, that is, :math:`s = x + y`. In this form, the two integers are known as *summands*, and are also specifically called *augend* (:math:`x`) and *addend* (:math:`y`) according to the order in which they appear in the addition operation.

In the case of a single adder, the magnitudes of the summands and their sum are confined to being within the dimensionality (e.g., binary) of their single-unit (e.g., bit) encoding. Integers larger than this limit therefore require multiple units of information to be encoded. For example, a non-negative integer :math:`z` can be encoded with a number :math:`\Number` of :math:`\Dimension`-dimensional unit values provided :math:`z \leq \Dimension^\Number - 1`. Under this encoding, the integer can be represented using an ordered array (or set or string) of such values,

.. math:: z \equiv (z_{\Number - 1}, z_{\Number - 2}, \ldots, z_1, z_0) = (z_n)_{n = 0}^{\Number - 1}
   :label: eq:encoding

which collectively reconstruct the (decimal) value of the integer with the unique decoding expansion

.. math::
   :label: eq:decoding
   
   \begin{aligned}
       z &= \sum_{n = 0}^{\Number - 1} z_n \Dimension^n \\
       &= z_0\Dimension^0 + z_1\Dimension^1 + \ldots + z_{\Number - 2}\Dimension^{\Number - 2} + z_{\Number - 1}\Dimension^{\Number - 1}.
   \end{aligned}

This is a type of *unsigned* integer encoding: all units of information are used to store the magnitude of the number, and there is no unit (e.g., a *sign bit*) reserved for storing the sign of the integer. It is perhaps the simplest integer encoding scheme possible, and so can be readily implemented in the context of quantum computing by utilizing the ability of quantum states to store information (both classical and quantum). This is typically realized using :math:`2`-dimensional (binary) qubits (due to their simplicity), and so a collection of :math:`\Number` such states allows for the encoding of (non-negative) integers up to :math:`2^\Number - 1` via the scheme described in :eq:`eq:encoding` and :eq:`eq:decoding`. The addition of any two such encoded integers, for example,

.. math::

   \begin{aligned}
       \ket{x} &\equiv \bigotimes_{n = \Number - 1}^{0}\ket{x_n} = \ket{x_{\Number - 1},x_{\Number - 2},\ldots,x_1,x_0}, \\
       \ket{y} &\equiv \bigotimes_{n = \Number - 1}^{0}\ket{y_n} = \ket{y_{\Number - 1},y_{\Number - 2},\ldots,y_1,y_0},
   \end{aligned}

can then be accomplished by a succession of exactly :math:`\Number` quantum ripple-carry adders. Each of these adders is applied to a different pair of subsystems in the encoded integers' states---the first acts on the least significant qubit (:math:`n = 0`), with the carry qubit from the previous adder being used as input to the next one. An example of this for a :math:`2`-qubit encoding (:math:`\Number = 2`) is depicted in :numref:`fig:circuit_algorithm_adder_ripple`.

.. only:: html

   .. figure:: /figures/output/circuit_algorithm_adder_ripple-dark.png
      :scale: 36 %
      :alt: A quantum circuit diagram of a quantum ripple-carry adder.
      :align: center
      :figwidth: 100 %
      :figclass: only-dark

   .. figure:: /figures/output/circuit_algorithm_adder_ripple-light.png
      :scale: 36 %
      :alt: A quantum circuit diagram of a quantum ripple-carry adder.
      :align: center
      :figwidth: 100 %
      :figclass: only-light

.. figure:: /figures/output/circuit_algorithm_adder_ripple-light.png
   :name: fig:circuit_algorithm_adder_ripple
   :scale: 36 %
   :alt: A quantum circuit diagram of a quantum ripple-carry adder.
   :align: center
   :figwidth: 100 %
   :figclass: light-dark hidden

   A :math:`2`-qubit quantum ripple-carry adder. The CNOT operation between the FULL ADDER subcircuits transfers the value of the previous iteration's carry output to the carry input of the next iteration.

From this circuit, the general output values of the summation qubits can be computed to be

.. math::

   s_i =
       \begin{cases}
           x_0 \oplus y_0 \oplus c_0 & i = 0; \\
           x_i \oplus y_i \oplus c_i \oplus c^\prime_{i - 1} & i > 0; \\
       \end{cases}

while the carry values are

.. math::

   c^\prime_i =
       \begin{cases}
           x_0 y_0 \oplus y_0 c_0 \oplus x_0 c_0 & i = 0; \\
           x_i y_i \oplus (x_i \oplus y_i)(c_i \oplus c^\prime_{i-1}) & i > 0. \\
       \end{cases}

With these, the corresponding states

.. math::
   :label: eq:encoded

   \begin{aligned}
       \ket{s} &\equiv \bigotimes_{n = \Number - 1}^{0}\ket{s_n}, \\
       \ket{c^\prime} &\equiv \bigotimes_{n = \Number - 1}^{0}\ket{c^\prime_n},
   \end{aligned}

can be decoded, using :eq:`eq:decoding`, to be

.. math::
   :label: eq:decoded
   
   \begin{aligned}
       s &= \sum_{n = 0}^{\Number - 1} s_n \Dimension^n, \\
       c^\prime &= \sum_{n = 0}^{\Number - 1} c^\prime_n \Dimension^n.
   \end{aligned}

Implementation
--------------

Due to performance constraints, this example sums two 2-bit integers. Increasing the ``encoding_depth`` *greatly* increases the calculation time as a result of having to perform operations on larger matrices. The decimal ``augend_integer`` and ``addend_integer`` variables can be freely changed, provided their summation is within the encodable range.

.. literalinclude:: /text/examples/algorithms/adder_ripple.py
   :name: code:adder_ripple
   :language: python
   :caption:

Output
------

Diagram
^^^^^^^

.. code:: python

   >>> adder.diagram()

..

   .. raw:: latex
      
      \vspace{1em}
      \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

   .. only:: html

      .. image:: /figures/output/text_examples_algorithms_adder_ripple-dark.png
         :scale: 40 %
         :align: left
         :class: only-dark

   .. only:: html or latex

      .. image:: /figures/output/text_examples_algorithms_adder_ripple-light.png
         :scale: 40 %
         :align: left
         :class: only-light

   .. raw:: latex
      
      \end{mdframed}
      \vspace{1em}

States
^^^^^^

.. code:: python

   >>> augend_state.print()
   |x⟩ = |0,1⟩

.. code:: python

   >>> addend_state.print()
   |y⟩ = |0,1⟩

.. code:: python

   >>> sum_state.print()
   |s⟩ = |1,0⟩

Results
^^^^^^^

.. code:: python

   >>> print(computation)
   Computation: 1 + 1 = 2

.. code:: python

   >>> print(duration)
   Duration: 16.363 seconds

This is of course *extremely* slow, mainly due to the computations involving relatively large matrices in the underlying calculation. Optimization of Qhronology's linear algebra algorithms, particularly the partial trace implementation, should improve both efficiency and speed.

.. raw:: latex
   
   \newpage