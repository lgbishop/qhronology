.. _`eg:shor`:

Shor's factorization algorithm
==============================

Description
-----------

*Shor's factorization algorithm* :cite:p:`shor_algorithms_1994, shor_polynomial-time_1997`, often called just *Shor's algorithm*, is an innovative quantum algorithm for the factorization of integers. An instance of the *hidden subgroup problem*, the algorithm's significance lies in its ability to factor large integers in polynomial time, which is exponentially faster than any known classical algorithm.

Shor's algorithm is a notable example of a *hybrid algorithm*, in which both classical and quantum processing are employed in order to obtain the desired outcome. As part of the algorithm, the factorization problem is reduced down to the problem of *order-finding*, a process known as *classical reduction*. Solving the order-finding problem then forms the core of the algorithm, and is the only component which is performed quantum mechanically (via quantum phase estimation---see :numref:`eg:phase_estimation` :ref:`eg:phase_estimation`).

Integer factorization
^^^^^^^^^^^^^^^^^^^^^

Formally, the factorization of an arbitrary positive integer :math:`N` involves determining a pair of positive integers :math:`p, q` such that

.. math:: pq = N.

If either of :math:`p` and :math:`q` is composite, then factorization of the factor itself can occur. Repeatedly decomposing all factors in this manner eventually results in a sequence of prime numbers :math:`(n_k)_k` where their product reconstructs :math:`N`, e.g.,

.. math:: \prod_k n_k = N.

This process is known as *prime factorization*, and by the *prime factorization theorem*, the sequence of prime factors :math:`(n_k)_k` is always unique (up to its order).

Formulating an algorithm to perform factorization on a classical computer is not unobtainable, with a plethora of such algorithms already existing, including *Euclid's algorithm*. However, formulating a factorization algorithm that is sufficiently efficient for large integers is currently an open problem: no classical algorithm which can perform integer factorization in polynomial time (i.e., a time complexity of :math:`\BigO(n^k)` for input of size :math:`n` and some positive constant :math:`k`) have been found to date. Fortunately, Shor's algorithm presents a quantum approach for efficient integer factorization, with significant applications in fields such as cryptography and computational mathematics.

The order-finding problem
^^^^^^^^^^^^^^^^^^^^^^^^^

Given the set of integers :math:`\Integers`, we can, using a positive integer :math:`N \in \IntegersPositive`, define a subset as

.. math:: \Integers_N = \{ n \in \Integers : 0 \leq n \leq N - 1 \}.

If we only include elements in this set which are coprime to :math:`N,` (which necessarily satisfy :math:`\gcd(N, n) = 1`), then we obtain

.. math:: \Integers_N^* = \{ n \in \Integers \, : \, 0 \leq n \leq N - 1, \; \gcd(N, n) = 1 \}.

Under the operation of (modular) multiplication, this set forms a *group*, and is sometimes written as :math:`(\Integers \setminus n\Integers)^\times`.

.. note::

   Suppose :math:`G_m` is a modulo multiplication group with the group operation of multiplication (modulo :math:`m`), and let :math:`1_G \in G_m` denote its multiplicative identity. If :math:`g \in G_m` is an element of the group, then there exists a positive integer :math:`\abs{G}` such that :math:`g^{\abs{G}} = 1_G \; (\mathrm{mod} \; m)`. Here, :math:`\abs{G}` is called the *order* of :math:`G_m`, and :math:`g^{\abs{G}}` denotes the multiplication of :math:`g` by itself exactly :math:`\abs{G}` times.

As :math:`\Integers_N^*` is the multiplicative group of integers modulo :math:`N`, then we can repeatedly multiply any element :math:`a \in \Integers_N^*` by itself and eventually obtain :math:`1`. Mathematically, this means that for each base :math:`a` there exists a finite number of modular multiplications :math:`r` such that

.. math:: a^{r} = 1 \; (\mathrm{mod} \; N).
   :label: eq:multiplicative_order

Note that the value of :math:`r` is specific to that combination of both the element :math:`a` and the modulus :math:`N`.

Of course, if :math:`r` satisfies :eq:`eq:multiplicative_order`, then so will any exponent of the form :math:`r + k`, where :math:`k` is a positive integer. The smallest possible non-zero value of :math:`r` for which this holds true is called the *order* of the element :math:`a`. This can be expressed more eloquently; by defining the *modular exponential function*,

.. math:: f_{N, a}(k) \equiv a^k \; (\mathrm{mod} \; N),
   :label: eq:modular_exponential_function

we can write

.. math:: f_{N, a}(r) = 1.
   :label: eq:modular_exponential_function_order

Due to its modularity, :math:`f` is periodic, with :math:`r` serving as its *period*, i.e.,

.. math:: f_{N, a}(k + r) = f_{N, a}(k)

for any positive integer :math:`k`. Determining the smallest possible value(s) of :math:`r` for which any given (univariate) function :math:`f` is periodic, e.g., :math:`f(x + r) = f(x)` (for all :math:`x`), constitutes the problem of *period-finding*. In the special case of the modular exponent function :eq:`eq:modular_exponential_function`, determining such an integer :math:`r` such that :eq:`eq:modular_exponential_function_order` holds true (given positive integers :math:`N` and :math:`a`, with :math:`\gcd(N, a) = 1`) is called *order-finding*.

Factorization by order-finding
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Solving the problem of order-finding is useful because it can be used to factorize an integer. This is achieved by first assigning the number to be factorized :math:`N` as the modulus of the associated multiplicative group of integers. The period :math:`r` is then calculated given an element :math:`a \in \Integers_N^* \setminus \{1\}` (so :math:`N` and :math:`a` are coprime). Since :eq:`eq:multiplicative_order` is satisfied for such values of :math:`a`, then :math:`N` divides :math:`a^{r} - 1`, which is often written as

.. math:: N \divides a^{r} - 1.

This simply means that there exists an integer :math:`z` such that :math:`a^{r} - 1 = zN`. By factorizing this expression algebraically, we obtain the product

.. math:: a^{r} - 1 = (a^{r/2} - 1)(a^{r/2} + 1).

If :math:`r` is odd, then the period should be recomputed using a different value for :math:`a`. When :math:`r` is determined to be even, then :math:`r/2` is an integer, and so :math:`a^{r/2}` is the non-trivial square root of :math:`a^{r}`. Proceeding under this assumption, we have

.. math:: N \divides (a^{r/2} - 1)(a^{r/2} + 1),

which may imply the following two statements:

.. math::

   \begin{aligned}
       \text{(i)} \quad &N \divides a^{r/2} - 1,\\
       \text{(ii)} \quad &N \divides a^{r/2} + 1.
   \end{aligned}

Neither of these statements can be true if the factorization algorithm is to be successful. If (i) holds, then we must have :math:`a^{r/2} = 1 \; (\mathrm{mod} \; N)`. However, this contradicts the fact that :math:`r` is the order of :math:`a`, and so (i) is always false (provided a correct :math:`r` was found). Thus, (i) cannot be true. We subsequently compute the value

.. math:: d = \gcd(N, a^{r/2} - 1).

If :math:`d = 1`, then statement (ii) is true, and the factorization procedure has trivial factor (either :math:`1` or :math:`N`) and should be repeated with a different value for :math:`a` (to attempt to find a non-trivial factor). Alternatively, if :math:`d > 1`, then

.. math::

   \begin{aligned}
       p &= d,\\
       q &= N/d,
   \end{aligned}

are non-trivial factors of :math:`N`, e.g., :math:`N = pq`, with neither value being equal to :math:`1` or :math:`N`.

.. raw:: latex

   \enlargethispage{-2\baselineskip}

Algorithm
---------

Before executing Shor's algorithm for a given number :math:`N`, it can be advantageous to perform a few (purely classical) pre-processing checks in order to maximize efficiency. In particular, the complexity of the problem can be greatly reduced for certain classes of integers. First are the even numbers: using Euclid's algorithm, we can efficiently compute the greatest common divisor (GCD) between two integers, meaning that we can check whether :math:`N` is even (in which case 2 is trivially a factor). Then, we can also check whether :math:`N` is a prime power, for which efficient classical factorization algorithms already exist (and so we need not perform Shor's algorithm). The version of Shor's algorithm presented here therefore assumes that the number :math:`N` to be factorized is neither even or a prime power.

.. raw:: latex

   \begin{codetitled}{Shor's algorithm (natural-language pseudocode)}{}

#. Choose, at random, an integer :math:`a \in \Integers_N \setminus \{1\}`.

#. **Classical pre-processing**: Compute :math:`d = \gcd(N, a)`.

   #. If :math:`d > 1`, then factors have been found: output :math:`p = d` and :math:`q = N/d`. *Exit*.

   #. If :math:`d = 1`, then :math:`a` and :math:`N` are coprime (therefore :math:`a \in \Integers_N^*`). *Continue*.

#. **Quantum order-finding**: Find the period :math:`r` such that :math:`a^r \; \mathrm{mod} \; N = 1`.

#. **Classical post-processing**:

   #. If :math:`r` is even, then compute :math:`a^\prime = a^{r/2} - 1 \; \mathrm{mod} \; N` and :math:`d^\prime = \gcd(N, a^\prime)`.

      #. If :math:`d^\prime > 1`, then factors have been found: output :math:`p = d^\prime` and :math:`q = N/d^\prime`. *Exit*.

      #. If :math:`d^\prime = 1`, then the algorithm has failed to factorize :math:`N`. *Exit*.

   #. If :math:`r` is odd, then the algorithm has failed to factorize :math:`N`. *Exit*.

.. raw:: latex

   \end{codetitled}

This is, in essence, a complete description of Shor's algorithm, with the understanding that the order-finding step is performed efficiently via a phase estimation subroutine on a quantum computer (see :numref:`eg:shor_estimation` :ref:`eg:shor_estimation`).

Evidently, as a probabilistic algorithm, there is a chance that it can fail on any given run. This happens in two specific situations:

- The computed period :math:`r` is odd.
- The computed period :math:`r` is even and :math:`\gcd(N, a^{r/2} - 1) = 1`.

For a random choice of :math:`a`, the probability of either of the two failing events occuring is at most :math:`2^{-(s-1)}`, where :math:`s` is the number of distinct prime factors of :math:`N`. The probability of any given run being successful is therefore at least :math:`0.5`, and so executing the algorithm :math:`t` times (each with a randomly chosen :math:`a`) results in a probability of success being bounded from below by :math:`1 - 2^{-t}`. Much of the trial-and-error of the algorithm's probabilistic nature can therefore be eliminated by providing :math:`a` such that it is coprime to :math:`N` (i.e., :math:`a \in \Integers_N^*`), in cases where such knowledge is possible.

.. _`eg:shor_estimation`:

Order-finding via quantum phase estimation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Quantum phase estimation (see :numref:`eg:phase_estimation` :ref:`eg:phase_estimation`) presents an efficient method of order-finding that is unattainable through classical means. This is achieved through using operators that have the action

.. math:: \Unitary_{N,a} \ket{z} = \left|ay \; (\mathrm{mod} \; N)\right\rangle

as the base of the controlled-:math:`\Unitary` gates in the phase estimation algorithm. Note that, given this definition, it is easy to verify that

.. math:: \Unitary_{N,a}^k \ket{z} = |a^ky \; (\mathrm{mod} \; N)\rangle,

and so, in the case of :math:`z = 1`, we have

.. math::

   \begin{aligned}
       \Unitary_{N,a}^k \ket{1} &= |a^k \; (\mathrm{mod} \; N)\rangle \\
       &= |f_{N,a}(k)\rangle.
   \end{aligned}

The phase estimation procedure then simply determines the smallest integer value of :math:`r` (i.e., the period) for which

.. math:: \Unitary_{N,a}^r \ket{1} = \left|1 \; (\mathrm{mod} \; N)\right\rangle,

thereby solving the order-finding problem. This is achieved by using the decoded phase value :math:`\theta`, obtained from the phase estimation itself, to calculate the integer :math:`r` via the relation :math:`\theta = 1/r`. The quantum circuit depicting the phase estimation procedure in Shor's algorithm appears in :numref:`fig:circuit_algorithm_shor`.

.. only:: html

   .. figure:: /figures/output/circuit_algorithm_shor-dark.png
      :scale: 34 %
      :alt: A quantum circuit diagram of Shor's algorithm.
      :align: center
      :figwidth: 100 %
      :figclass: only-dark

   .. figure:: /figures/output/circuit_algorithm_shor-light.png
      :scale: 34 %
      :alt: A quantum circuit diagram of Shor's algorithm.
      :align: center
      :figwidth: 100 %
      :figclass: only-light

.. figure:: /figures/output/circuit_algorithm_shor-light.png
   :name: fig:circuit_algorithm_shor
   :scale: 34 %
   :alt: A quantum circuit diagram of Shor's algorithm.
   :align: center
   :figwidth: 100 %
   :figclass: light-dark hidden

   A quantum circuit of the order-finding step in Shor's algorithm.

.. raw:: latex

   \vspace*{-\baselineskip}

Implementation
--------------

The implementation of Shor's algorithm presented here diverges from typical implementations in two significant ways:

- The modular exponentiation gates are constructed artificially, by generating their corresponding operators' matrix representations from first principles. Decompositions of these gates in terms of CNOTs can then be computed and subsequently employed, depending on the value of the :python:`decompose` (:python:`bool`) variable.
- Instead of repeating the simulation numerous times to obtain a probability distribution of outcomes, we extract the exact probabilities themselves directly via measurement after a single simulation, and use them to determine the (likely) factors. This is far more computationally efficient, though the circuit can be easily adapted if a more faithful recreation of experiment is desired.

Note that in this implementation of Shor's algorithm, the two registers of the quantum phase estimation procedure employ :math:`2n` and :math:`n` qubits, respectively, where :math:`n` is the minimum number of qubits required to encode the number :math:`N`. Analysis shows that :math:`2n` qubits in the estimation (upper) register is the minimum number that is able to provide the precision necessary in order to correctly distinguish between different periods in every case. However, particularly for small :math:`N`, the algorithm can often be successfully executed using just :math:`n` estimation qubits. It is also useful to be aware that versions of the algorithm in the literature often employ certain optimizations with which they can use fewer qubits to achieve the same result.

As evident by the simulation's results that appear below, the number of controlled-:math:`\Unitary` gates need not always be equal to the number of systems in the estimation register. This is because there can be instances (values of :math:`j` given :math:`N` and :math:`a`) where the modular exponentiation gate :math:`\Unitary_{N,a}^{2^j}` is equivalent to the identity gate :math:`\Identity`, and so application of the corresponding controlled-:math:`\Unitary` gate is redundant.

It is also worth mentioning that while this implementation supports any valid (factorizable) positive integer :math:`N` as input (set with the variable :python:`N`), attempting to factorize those larger than 15 (corresponding to more than 12 qubits in total across both registers) can require significant amounts of both memory and time.

.. raw:: latex

   \enlargethispage{-6\baselineskip}

.. raw:: latex

   \begin{codetitled}{Shor's algorithm}{}

.. literalinclude:: /text/examples/algorithms/shor.py
   :name: code:shor
   :language: python
   :caption:

.. raw:: latex

   \end{codetitled}

Output
------

Diagram
^^^^^^^

If :python:`decompose` is :python:`False`:

.. raw:: latex

   \begin{code}

.. code:: python

   >>> shor.diagram(pad=(1, 0), force_separation=True)

.. raw:: latex
   
   \includegraphics[scale=1.25, trim=-0.02cm -0.10cm 0 -0.12cm]{text_examples_algorithms_shor.pdf}
   \vspace{-1\baselineskip}

..

   .. only:: html

      .. image:: /figures/output/text_examples_algorithms_shor-dark.png
         :scale: 36 %
         :align: left
         :class: only-dark

   .. only:: html

      .. image:: /figures/output/text_examples_algorithms_shor-light.png
         :scale: 36 %
         :align: left
         :class: only-light

.. raw:: latex
   
   \end{code}

.. raw:: latex

   \newpage

If :python:`decompose` is :python:`True`:

.. raw:: latex

   \begin{code}

.. code:: python

   >>> shor.diagram(pad=(1, 0), force_separation=True)

.. raw:: latex
   
   \includegraphics[scale=1.25, trim=-0.02cm -0.10cm 0 -0.12cm]{text_examples_algorithms_shor_decomposed.pdf}
   \vspace{-1\baselineskip}

..

   .. only:: html

      .. image:: /figures/output/text_examples_algorithms_shor_decomposed-dark.png
         :scale: 36 %
         :align: left
         :class: only-dark

   .. only:: html

      .. image:: /figures/output/text_examples_algorithms_shor_decomposed-light.png
         :scale: 36 %
         :align: left
         :class: only-light

.. raw:: latex
   
   \end{code}

Results
^^^^^^^

Cumulative output from the various print statements:

.. raw:: latex

   \begin{code}

.. code:: output

   Input number: 15
   Bitstring=00000000, Probability=0.250, Period=1, (period not suitable)
   Bitstring=00000010, Probability=0.250, Period=4, Factors: 3 and 5
   Bitstring=00000001, Probability=0.250, Period=2, Factors: 3 and 5
   Bitstring=00000011, Probability=0.250, Period=4, Factors: 3 and 5

.. raw:: latex

   \end{code}

.. only:: html

   .. rst-class:: bibliography

      .. rubric:: :stylebibliography:`References`

      .. bibliography::
         :filter: docname in docnames

.. raw:: latex
   
   \newpage