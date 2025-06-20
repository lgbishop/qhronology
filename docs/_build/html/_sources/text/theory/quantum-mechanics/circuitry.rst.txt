.. include:: /styles.rst

.. _`sec:circuitry`:

*****************
Quantum circuitry
*****************

Anatomy of a quantum circuit
============================

Analogous to how the processing of information inside a classical computer may be represented diagrammatically by wires and logic gates, the *quantum circuitry* picturalism provides a way by which quantum operations can likewise be expressed visually. The formalism is based on the *Penrose graphical notation* (also often called *tensor network diagrams*)---a graphical notation for the visualization of tensors. This diagramming scheme is similar to logic circuit diagrams, in which wires depict the flow of information between logic gates (themselves representing logical operations on their input states).

A quantum circuit diagram is constructed using wires spanning input and output sections, upon which quantum gates are placed, describing manipulations and transformations (e.g., unitary operations) on the quantum states which follow these wires. A circuit's *inputs* (on the left) is a collection of one or more quantum states which, when encoded in an appropriate basis (for qubits this is typically the computational basis), is often called a (quantum) *register*. Oppositely, a circuit's *outputs* (on the right) is the set of quantum state(s) resulting from the transformations performed on the input(s) by the intermediary quantum gate(s). *Quantum computation* is then defined as any (unitary) evolution which takes an initial input state into some final output state. In this regard, it is important to note that, despite the "circuit" nomenclature, quantum circuits are typically not used to depict *closed* loops of state evolution.

One of the first uses of quantum circuit diagrams as we know them today was by Feynman :cite:p:`feynman_quantum_1986`. The construction of these diagrams is described in more detail in :cite:p:`nielsen_quantum_2010,serrano_quantum_2022,moret-bonillo_adventures_2017,williams_explorations_2010,wilde_quantum_2017`. All diagrams here were produced using the excellent LaTeX (TikZ) *Quantikz* package :cite:p:`kay_tutorial_2019`.

Fundamentals
------------

- **Time**: Time advances horizontally from the left to the right. Each vertical slice of the circuit corresponds to a distinct instant of time in the temporal progression. In other words, vertically aligned events occur simultaneously.

- **Wires**: Each (physical) quantum or classical system (Hilbert space) is represented by a *wire* which is aligned with a single horizontal axis. Events at various points in time on these modes (such as state preparation, logical operations, measurement, etc.) are connected by lines (i.e., wires), thus forming a *circuit*.

  - Quantum wires:

   .. raw:: latex
      
      \vspace{1em}
      \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

   .. only:: html

      .. image:: /figures/output/circuitry_wire_quantum_input-dark.png
         :scale: 36 %
         :align: left
         :class: only-dark

   .. only:: html or latex

      .. image:: /figures/output/circuitry_wire_quantum_input-light.png
         :scale: 36 %
         :align: left
         :class: only-light

   .. raw:: html

      </div>
      </blockquote>
      <blockquote>
      <div>

   .. raw:: latex
      
      \end{mdframed}
      \vspace{1em}
      \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

   .. only:: html

      .. image:: /figures/output/circuitry_wire_quantum_output-dark.png
         :scale: 36 %
         :align: left
         :class: only-dark

   .. only:: html or latex

      .. image:: /figures/output/circuitry_wire_quantum_output-light.png
         :scale: 36 %
         :align: left
         :class: only-light

   .. raw:: latex
      
      \end{mdframed}
      \vspace{1em}

  - Classical wires:

   .. raw:: latex
      
      \vspace{1em}
      \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

   .. only:: html

      .. image:: /figures/output/circuitry_wire_classical_input-dark.png
         :scale: 36 %
         :align: left
         :class: only-dark

   .. only:: html or latex

      .. image:: /figures/output/circuitry_wire_classical_input-light.png
         :scale: 36 %
         :align: left
         :class: only-light

   .. raw:: html

      </div>
      </blockquote>
      <blockquote>
      <div>

   .. raw:: latex
      
      \end{mdframed}
      \vspace{1em}
      \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

   .. only:: html

      .. image:: /figures/output/circuitry_wire_classical_output-dark.png
         :scale: 36 %
         :align: left
         :class: only-dark

   .. only:: html or latex

      .. image:: /figures/output/circuitry_wire_classical_output-light.png
         :scale: 36 %
         :align: left
         :class: only-light

   .. raw:: latex
      
      \end{mdframed}
      \vspace{1em}

- **Omission**: Ellipses denote the omission of parts of the circuit. This notation is usually employed only in the context of the subsequent tutorial circuits as a way to give focus to the important parts of each example.

- **Ordering and labels**: For circuits with multiple systems, the order of tensor products (from left-to-right) in its corresponding mathematical expression matches the order of modes (from top-to-bottom) in the circuit. In the case of any ambiguity, the Hilbert spaces in which the states and operators reside are labelled using either superscripts or subscripts (depending on the context). If the systems are not explicitly named, the common convention is to denote them in order (from top-to-bottom) using the integers, starting from :math:`0` (zero, as is customary in computer science) and counting up.

States
------

- State preparation or preselection is represented by:

   .. raw:: latex
      
      \vspace{1em}
      \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

   .. only:: html

      .. image:: /figures/output/circuitry_preselection_singlemode_density-dark.png
         :scale: 36 %
         :align: left
         :class: only-dark

   .. only:: html or latex

      .. image:: /figures/output/circuitry_preselection_singlemode_density-light.png
         :scale: 36 %
         :align: left
         :class: only-light

   .. raw:: latex
      
      \end{mdframed}
      \vspace{1em}

- The preparation of pure states is similarly:

   .. raw:: latex

      \vspace{1em}
      \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

   .. only:: html

      .. image:: /figures/output/circuitry_preselection_singlemode_pure-dark.png
         :scale: 36 %
         :align: left
         :class: only-dark

   .. only:: html or latex

      .. image:: /figures/output/circuitry_preselection_singlemode_pure-light.png
         :scale: 36 %
         :align: left
         :class: only-light

   .. raw:: latex

      \end{mdframed}
      \vspace{1em}

- States prepared over several modes are denoted using a brace extending across all of the relevant subsystems:

   .. raw:: latex
      
      \vspace{1em}
      \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

   .. only:: html

      .. image:: /figures/output/circuitry_preselection_multimode_density-dark.png
         :scale: 36 %
         :align: left
         :class: only-dark

   .. only:: html or latex

      .. image:: /figures/output/circuitry_preselection_multimode_density-light.png
         :scale: 36 %
         :align: left
         :class: only-light

   .. raw:: latex
      
      \end{mdframed}
      \vspace{1em}

- The preparation of separable states is:

   .. raw:: latex
      
      \vspace{1em}
      \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

   .. only:: html

      .. image:: /figures/output/circuitry_preselection_multimode_separable-dark.png
         :scale: 36 %
         :align: left
         :class: only-dark

   .. only:: html or latex

      .. image:: /figures/output/circuitry_preselection_multimode_separable-light.png
         :scale: 36 %
         :align: left
         :class: only-light

   .. raw:: latex
      
      \end{mdframed}
      \vspace{1em}

Gates
-----

- Linear operators (usually unitary operators) acting on states are denoted by blocks called *gates*:

   .. raw:: latex
      
      \vspace{1em}
      \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

   .. only:: html

      .. image:: /figures/output/circuitry_operator_singlemode_single-dark.png
         :scale: 36 %
         :align: left
         :class: only-dark

   .. only:: html or latex

      .. image:: /figures/output/circuitry_operator_singlemode_single-light.png
         :scale: 36 %
         :align: left
         :class: only-light

   .. raw:: latex
      
      \end{mdframed}
      \vspace{1em}

- Sequences of single-system operators are represented by sequences of gates:

   .. raw:: latex
      
      \vspace{1em}
      \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

   .. only:: html

      .. image:: /figures/output/circuitry_operator_singlemode_series-dark.png
         :scale: 36 %
         :align: left
         :class: only-dark

   .. only:: html or latex

      .. image:: /figures/output/circuitry_operator_singlemode_series-light.png
         :scale: 36 %
         :align: left
         :class: only-light

   .. raw:: latex
      
      \end{mdframed}
      \vspace{1em}

- Operators which act on different subsystems within composite systems are represented distinctly by parallel gates:

   .. raw:: latex
      
      \vspace{1em}
      \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

   .. only:: html

      .. image:: /figures/output/circuitry_operator_multimode_parallel-dark.png
         :scale: 36 %
         :align: left
         :class: only-dark

   .. only:: html or latex

      .. image:: /figures/output/circuitry_operator_multimode_parallel-light.png
         :scale: 36 %
         :align: left
         :class: only-light

   .. raw:: latex
      
      \end{mdframed}
      \vspace{1em}

- An empty wire (i.e., the absence of a gate on a mode) corresponds to the identity operator:

   .. raw:: latex
      
      \vspace{1em}
      \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

   .. only:: html

      .. image:: /figures/output/circuitry_operator_identity-dark.png
         :scale: 36 %
         :align: left
         :class: only-dark

   .. only:: html or latex

      .. image:: /figures/output/circuitry_operator_identity-light.png
         :scale: 36 %
         :align: left
         :class: only-light

   .. raw:: latex
      
      \end{mdframed}
      \vspace{1em}

- **Groups** of gates may be denoted with a bounding box, e.g.:

   .. raw:: latex
      
      \vspace{1em}
      \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

   .. only:: html

      .. image:: /figures/output/circuitry_operator_group_series-dark.png
         :scale: 36 %
         :align: left
         :class: only-dark

   .. only:: html or latex

      .. image:: /figures/output/circuitry_operator_group_series-light.png
         :scale: 36 %
         :align: left
         :class: only-light

   .. raw:: html

      </div>
      </blockquote>
      <blockquote>
      <div>

   .. raw:: latex
      
      \end{mdframed}
      \vspace{1em}
      \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

   .. only:: html

      .. image:: /figures/output/circuitry_operator_group_parallel-dark.png
         :scale: 36 %
         :align: left
         :class: only-dark

   .. only:: html or latex

      .. image:: /figures/output/circuitry_operator_group_parallel-light.png
         :scale: 36 %
         :align: left
         :class: only-light

   .. raw:: latex
      
      \end{mdframed}
      \vspace{1em}

- Gates acting on different systems at distinct times (i.e., non-simultaneous operators) are separated horizontally. If all other wires in their instant are empty, then they may be combined:

   .. raw:: latex
      
      \vspace{1em}
      \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

   .. only:: html

      .. image:: /figures/output/circuitry_operator_multimode_nonsimultaneous_upper,lower-dark.png
         :scale: 36 %
         :align: left
         :class: only-dark

   .. only:: html or latex

      .. image:: /figures/output/circuitry_operator_multimode_nonsimultaneous_upper,lower-light.png
         :scale: 36 %
         :align: left
         :class: only-light

   .. raw:: html

      </div>
      </blockquote>
      <blockquote>
      <div>

   .. raw:: latex
      
      \end{mdframed}
      \vspace{1em}
      \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

   .. only:: html

      .. image:: /figures/output/circuitry_operator_multimode_nonsimultaneous_lower,upper-dark.png
         :scale: 36 %
         :align: left
         :class: only-dark

   .. only:: html or latex

      .. image:: /figures/output/circuitry_operator_multimode_nonsimultaneous_lower,upper-light.png
         :scale: 36 %
         :align: left
         :class: only-light

   .. raw:: latex
      
      \end{mdframed}
      \vspace{1em}

- Multipartite (composite) operators are denoted by gates which span the relevant wires:

   .. raw:: latex

      \vspace{1em}
      \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

   .. only:: html

      .. image:: /figures/output/circuitry_operator_multimode_multipartite_neighbouring-dark.png
         :scale: 36 %
         :align: left
         :class: only-dark

   .. only:: html or latex

      .. image:: /figures/output/circuitry_operator_multimode_multipartite_neighbouring-light.png
         :scale: 36 %
         :align: left
         :class: only-light

   .. raw:: html

      </div>
      </blockquote>
      <blockquote>
      <div>

   .. raw:: latex
      
      \end{mdframed}
      \vspace{1em}
      \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

   .. only:: html

      .. image:: /figures/output/circuitry_operator_multimode_multipartite_absence_lower-dark.png
         :scale: 36 %
         :align: left
         :class: only-dark

   .. only:: html or latex

      .. image:: /figures/output/circuitry_operator_multimode_multipartite_absence_lower-light.png
         :scale: 36 %
         :align: left
         :class: only-light

   .. raw:: html

      </div>
      </blockquote>
      <blockquote>
      <div>

   .. raw:: latex
      
      \end{mdframed}
      \vspace{1em}
      \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

   .. only:: html

      .. image:: /figures/output/circuitry_operator_multimode_multipartite_absence_upper-dark.png
         :scale: 36 %
         :align: left
         :class: only-dark

   .. only:: html or latex

      .. image:: /figures/output/circuitry_operator_multimode_multipartite_absence_upper-light.png
         :scale: 36 %
         :align: left
         :class: only-light

   .. raw:: html

      </div>
      </blockquote>
      <blockquote>
      <div>

   .. raw:: latex
      
      \end{mdframed}
      \vspace{1em}
      \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

   .. only:: html

      .. image:: /figures/output/circuitry_operator_multimode_multipartite_absence_middle-dark.png
         :scale: 36 %
         :align: left
         :class: only-dark

   .. only:: html or latex

      .. image:: /figures/output/circuitry_operator_multimode_multipartite_absence_middle-light.png
         :scale: 36 %
         :align: left
         :class: only-light

   .. raw:: latex
      
      \end{mdframed}
      \vspace{1em}

  - If the system structure of the operators is unambiguous in the context of the circuit, then the (superscript) system labels are usually omitted for the sake of notational brevity.

Other operations
----------------

- The **trace** over a system (i.e., termination of a wire) is denoted by either a grounding symbol or a down arrow on the end of its corresponding mode:

   .. raw:: latex
      
      \vspace{1em}
      \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

   .. only:: html

      .. image:: /figures/output/circuitry_trace-dark.png
         :scale: 36 %
         :align: left
         :class: only-dark

   .. only:: html or latex

      .. image:: /figures/output/circuitry_trace-light.png
         :scale: 36 %
         :align: left
         :class: only-light

   .. raw:: latex
      
      \end{mdframed}
      \vspace{1em}

- This extends neatly to the **partial trace**:

   .. raw:: latex

      \vspace{1em}
      \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

   .. only:: html

      .. image:: /figures/output/circuitry_trace_partial_upper-dark.png
         :scale: 36 %
         :align: left
         :class: only-dark

   .. only:: html or latex

      .. image:: /figures/output/circuitry_trace_partial_upper-light.png
         :scale: 36 %
         :align: left
         :class: only-light

   .. raw:: html

      </div>
      </blockquote>
      <blockquote>
      <div>

   .. raw:: latex
      
      \end{mdframed}
      \vspace{1em}
      \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

   .. only:: html

      .. image:: /figures/output/circuitry_trace_partial_lower-dark.png
         :scale: 36 %
         :align: left
         :class: only-dark

   .. only:: html or latex

      .. image:: /figures/output/circuitry_trace_partial_lower-light.png
         :scale: 36 %
         :align: left
         :class: only-light

   .. raw:: html

      </div>
      </blockquote>
      <blockquote>
      <div>

   .. raw:: latex
      
      \end{mdframed}
      \vspace{1em}
      \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

   .. only:: html

      .. image:: /figures/output/circuitry_trace_partial_both-dark.png
         :scale: 36 %
         :align: left
         :class: only-dark

   .. only:: html or latex

      .. image:: /figures/output/circuitry_trace_partial_both-light.png
         :scale: 36 %
         :align: left
         :class: only-light

   .. raw:: latex
      
      \end{mdframed}
      \vspace{1em}

- **Postselection** against a state is simply the mirror of state preparation/preselection. This is indicated with either:

  - The postselection state (explicitly in the dual Hilbert space, e.g., :math:`\bra{\StateVector}` and :math:`\StateDensity^\dagger`) at the termination of the wire.

  - A round cap at the termination of the wire, followed by the postselection state.

   .. raw:: latex
      
      \vspace{1em}
      \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

   .. only:: html

      .. image:: /figures/output/circuitry_postselection_singlemode_pure-dark.png
         :scale: 36 %
         :align: left
         :class: only-dark

   .. only:: html or latex

      .. image:: /figures/output/circuitry_postselection_singlemode_pure-light.png
         :scale: 36 %
         :align: left
         :class: only-light

   .. raw:: html

      </div>
      </blockquote>
      <blockquote>
      <div>

   .. raw:: latex
      
      \end{mdframed}
      \vspace{1em}
      \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

   .. only:: html

      .. image:: /figures/output/circuitry_postselection_singlemode_density-dark.png
         :scale: 36 %
         :align: left
         :class: only-dark

   .. only:: html or latex

      .. image:: /figures/output/circuitry_postselection_singlemode_density-light.png
         :scale: 36 %
         :align: left
         :class: only-light

   .. raw:: html

      </div>
      </blockquote>
      <blockquote>
      <div>

   .. raw:: latex
      
      \end{mdframed}
      \vspace{1em}
      \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

   .. only:: html

      .. image:: /figures/output/circuitry_postselection_multimode_single-dark.png
         :scale: 36 %
         :align: left
         :class: only-dark

   .. only:: html or latex

      .. image:: /figures/output/circuitry_postselection_multimode_single-light.png
         :scale: 36 %
         :align: left
         :class: only-light

   .. raw:: html

      </div>
      </blockquote>
      <blockquote>
      <div>

   .. raw:: latex
      
      \end{mdframed}
      \vspace{1em}
      \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

   .. only:: html

      .. image:: /figures/output/circuitry_postselection_multimode_upper-dark.png
         :scale: 36 %
         :align: left
         :class: only-dark

   .. only:: html or latex

      .. image:: /figures/output/circuitry_postselection_multimode_upper-light.png
         :scale: 36 %
         :align: left
         :class: only-light

   .. raw:: html

      </div>
      </blockquote>
      <blockquote>
      <div>

   .. raw:: latex
      
      \end{mdframed}
      \vspace{1em}
      \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

   .. only:: html

      .. image:: /figures/output/circuitry_postselection_multimode_lower-dark.png
         :scale: 36 %
         :align: left
         :class: only-dark

   .. only:: html or latex

      .. image:: /figures/output/circuitry_postselection_multimode_lower-light.png
         :scale: 36 %
         :align: left
         :class: only-light

   .. raw:: html

      </div>
      </blockquote>
      <blockquote>
      <div>

   .. raw:: latex
      
      \end{mdframed}
      \vspace{1em}
      \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

   .. only:: html

      .. image:: /figures/output/circuitry_postselection_multimode_both-dark.png
         :scale: 36 %
         :align: left
         :class: only-dark

   .. only:: html or latex

      .. image:: /figures/output/circuitry_postselection_multimode_both-light.png
         :scale: 36 %
         :align: left
         :class: only-light

   .. raw:: latex
      
      \end{mdframed}
      \vspace{1em}

  - Note that in most cases, the cap notation will be omitted for simplicity. This is particularly true when the postselection state is pre-defined (i.e., not unknown), and so the associated postselection is unambiguous.

- The **measurement** of a system with respect to a particular basis is represented by the termination of its wire with a meter:

   .. raw:: latex
      
      \vspace{1em}
      \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

   .. only:: html

      .. image:: /figures/output/circuitry_measurement_singlemode_pure-dark.png
         :scale: 36 %
         :align: left
         :class: only-dark

   .. only:: html or latex

      .. image:: /figures/output/circuitry_measurement_singlemode_pure-light.png
         :scale: 36 %
         :align: left
         :class: only-light

   .. raw:: html

      </div>
      </blockquote>
      <blockquote>
      <div>

   .. raw:: latex
      
      \end{mdframed}
      \vspace{1em}
      \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

   .. only:: html

      .. image:: /figures/output/circuitry_measurement_singlemode_density-dark.png
         :scale: 36 %
         :align: left
         :class: only-dark

   .. only:: html or latex

      .. image:: /figures/output/circuitry_measurement_singlemode_density-light.png
         :scale: 36 %
         :align: left
         :class: only-light

   .. raw:: html

      </div>
      </blockquote>
      <blockquote>
      <div>

   .. raw:: latex
      
      \end{mdframed}
      \vspace{1em}
      \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]      

   .. only:: html

      .. image:: /figures/output/circuitry_measurement_multimode_single-dark.png
         :scale: 36 %
         :align: left
         :class: only-dark

   .. only:: html or latex

      .. image:: /figures/output/circuitry_measurement_multimode_single-light.png
         :scale: 36 %
         :align: left
         :class: only-light

   .. raw:: latex
      
      \end{mdframed}
      \vspace{1em}

- Performing a measurement on a system returns a set of probabilities associated with the particular set of states against which the system was measured. In a circuit where measurement is not performed on every system, the measurement statistics are obtained by simply discarding (tracing out) all systems which do not undergo measurement:

   .. raw:: latex

      \vspace{1em}
      \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

   .. only:: html

      .. image:: /figures/output/circuitry_measurement_multimode_upper-dark.png
         :scale: 36 %
         :align: left
         :class: only-dark

   .. only:: html or latex

      .. image:: /figures/output/circuitry_measurement_multimode_upper-light.png
         :scale: 36 %
         :align: left
         :class: only-light

   .. raw:: html

      </div>
      </blockquote>
      <blockquote>
      <div>

   .. raw:: latex
      
      \end{mdframed}
      \vspace{1em}
      \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

   .. only:: html

      .. image:: /figures/output/circuitry_measurement_multimode_lower-dark.png
         :scale: 36 %
         :align: left
         :class: only-dark

   .. only:: html or latex

      .. image:: /figures/output/circuitry_measurement_multimode_lower-light.png
         :scale: 36 %
         :align: left
         :class: only-light

   .. raw:: latex
      
      \end{mdframed}
      \vspace{1em}

  - Note however that the output of the circuit still remains as the composite product of all unmeasured systems.

- Multiple measurements simply indicate that multiple sets of probabilities will be obtained, each corresponding to the independent measurement of their respective system, e.g.,

   .. raw:: latex
      
      \vspace{1em}
      \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

   .. only:: html

      .. image:: /figures/output/circuitry_measurement_multimode_both-dark.png
         :scale: 36 %
         :align: left
         :class: only-dark

   .. only:: html or latex

      .. image:: /figures/output/circuitry_measurement_multimode_both-light.png
         :scale: 36 %
         :align: left
         :class: only-light

   .. raw:: latex
      
      \end{mdframed}
      \vspace{1em}

- A measurement for which the outcome is discarded (or forgotten) leaves the measured system in a superposition of all post-measurement states corresponding to all measurement operators :math:`\{\StateDensity_i\}`. As this characteristically destroys purity, the post-gate wire of such a discarded measurement operation is visualized using a classical wire:

   .. raw:: latex
      
      \vspace{1em}
      \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

   .. only:: html

      .. image:: /figures/output/circuitry_measurement_singlemode_discarded-dark.png
         :scale: 36 %
         :align: left
         :class: only-dark

   .. only:: html or latex

      .. image:: /figures/output/circuitry_measurement_singlemode_discarded-light.png
         :scale: 36 %
         :align: left
         :class: only-light

   .. raw:: latex
      
      \end{mdframed}
      \vspace{1em}

- Usage of the measurement outcomes as the (classical) control of a gate is denoted by the connection of the meter and the gate with a classical wire:

   .. raw:: latex
      
      \vspace{1em}
      \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

   .. only:: html

      .. image:: /figures/output/circuitry_measurement_control_equation-dark.png
         :scale: 36 %
         :align: left
         :class: only-dark

   .. only:: html or latex

      .. image:: /figures/output/circuitry_measurement_control_equation-light.png
         :scale: 36 %
         :align: left
         :class: only-light

   .. raw:: latex
      
      \end{mdframed}
      \vspace{1em}

  - Note that a terminating post-measurement system like this is equivalent to a discarded measurement operation followed by a (partial) trace, and that a classical control wire is merely a device used to indicate the conveyance of classical information (and is in fact completely equivalent to a quantum control wire). This means we have the equivalence:

   .. raw:: latex
      
      \vspace{1em}
      \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

   .. only:: html

      .. image:: /figures/output/circuitry_measurement_control_equivalence-dark.png
         :scale: 36 %
         :align: left
         :class: only-dark

   .. only:: html or latex

      .. image:: /figures/output/circuitry_measurement_control_equivalence-light.png
         :scale: 36 %
         :align: left
         :class: only-light

   .. raw:: latex
      
      \end{mdframed}
      \vspace{1em}

  - The *principle of deferred measurement* states that measurement operations commute with control operations. Depicted visually, this is the equivalence:

   .. raw:: latex
      
      \vspace{1em}
      \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

   .. only:: html

      .. image:: /figures/output/circuitry_measurement_control_deferred-dark.png
         :scale: 36 %
         :align: left
         :class: only-dark

   .. only:: html or latex

      .. image:: /figures/output/circuitry_measurement_control_deferred-light.png
         :scale: 36 %
         :align: left
         :class: only-light

   .. raw:: latex
      
      \end{mdframed}
      \vspace{1em}

- The closed and timelike nature of the paths of chronology-violating systems (i.e., those which correspond to quantum states propagating along closed timelike curves) is captured by the use of triangular caps at the ends of the associated wires:

  - Future connection:

   .. raw:: latex
      
      \vspace{1em}
      \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

   .. only:: html

      .. image:: /figures/output/circuitry_ctc_future-dark.png
         :scale: 36 %
         :align: left
         :class: only-dark

   .. only:: html or latex

      .. image:: /figures/output/circuitry_ctc_future-light.png
         :scale: 36 %
         :align: left
         :class: only-light

   .. raw:: latex
      
      \end{mdframed}
      \vspace{1em}

  - Past connection:

   .. raw:: latex
      
      \vspace{1em}
      \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

   .. only:: html

      .. image:: /figures/output/circuitry_ctc_past-dark.png
         :scale: 36 %
         :align: left
         :class: only-dark

   .. only:: html or latex

      .. image:: /figures/output/circuitry_ctc_past-light.png
         :scale: 36 %
         :align: left
         :class: only-light

   .. raw:: latex
      
      \end{mdframed}
      \vspace{1em}

  - These constructs can be thought of as the "mouths" of a wormhole, and so represent a instantaneous physical connection ("portals") between the past and the future such that any quantum state which propagates into the future mouth immediately emerges from the corresponding past mouth. Note however that of course not every chronology-violating system is associated with a *wormhole-based* time machine, and so these connections should be taken as representing closed timelike curves in the most general, abstract sense.

List of special gates
=====================

Note that in these examples, :math:`\Dimension` is the dimensionality of the relevant linear operator's underlying Hilbert space.

- X (Pauli-X):

   .. raw:: latex
      
      \vspace{1em}
      \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

   .. only:: html

      .. image:: /figures/output/circuitry_gate_pauli_x-dark.png
         :scale: 36 %
         :align: left
         :class: only-dark

   .. only:: html or latex

      .. image:: /figures/output/circuitry_gate_pauli_x-light.png
         :scale: 36 %
         :align: left
         :class: only-light

   .. raw:: latex
      
      \end{mdframed}
      \vspace{1em}

- Y (Pauli-Y):

   .. raw:: latex
      
      \vspace{1em}
      \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

   .. only:: html

      .. image:: /figures/output/circuitry_gate_pauli_y-dark.png
         :scale: 36 %
         :align: left
         :class: only-dark

   .. only:: html or latex

      .. image:: /figures/output/circuitry_gate_pauli_y-light.png
         :scale: 36 %
         :align: left
         :class: only-light

   .. raw:: latex
      
      \end{mdframed}
      \vspace{1em}

- Z (Pauli-Z):

   .. raw:: latex
      
      \vspace{1em}
      \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

   .. only:: html

      .. image:: /figures/output/circuitry_gate_pauli_z-dark.png
         :scale: 36 %
         :align: left
         :class: only-dark

   .. only:: html or latex

      .. image:: /figures/output/circuitry_gate_pauli_z-light.png
         :scale: 36 %
         :align: left
         :class: only-light

   .. raw:: latex
      
      \end{mdframed}
      \vspace{1em}

- NOT (bit-flip), equivalent to the Pauli-X gate for qubits:

   .. raw:: latex
      
      \vspace{1em}
      \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

   .. only:: html

      .. image:: /figures/output/circuitry_gate_not-dark.png
         :scale: 36 %
         :align: left
         :class: only-dark

   .. only:: html or latex

      .. image:: /figures/output/circuitry_gate_not-light.png
         :scale: 36 %
         :align: left
         :class: only-light

   .. raw:: latex
      
      \end{mdframed}
      \vspace{1em}

- SUM (summation), a parameter-dependent :math:`\Dimension`-dimensional generalization of the NOT gate:

   .. raw:: latex
      
      \vspace{1em}
      \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

   .. only:: html

      .. image:: /figures/output/circuitry_gate_sum-dark.png
         :scale: 36 %
         :align: left
         :class: only-dark

   .. only:: html or latex

      .. image:: /figures/output/circuitry_gate_sum-light.png
         :scale: 36 %
         :align: left
         :class: only-light

   .. raw:: latex
      
      \end{mdframed}
      \vspace{1em}

- P (phase):

   .. raw:: latex
      
      \vspace{1em}
      \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

   .. only:: html

      .. image:: /figures/output/circuitry_gate_phase-dark.png
         :scale: 36 %
         :align: left
         :class: only-dark

   .. only:: html or latex

      .. image:: /figures/output/circuitry_gate_phase-light.png
         :scale: 36 %
         :align: left
         :class: only-light

   .. raw:: latex
      
      \end{mdframed}
      \vspace{1em}

- R (rotation):

   .. raw:: latex
      
      \vspace{1em}
      \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

   .. only:: html

      .. image:: /figures/output/circuitry_gate_rotation-dark.png
         :scale: 36 %
         :align: left
         :class: only-dark

   .. only:: html or latex

      .. image:: /figures/output/circuitry_gate_rotation-light.png
         :scale: 36 %
         :align: left
         :class: only-light

   .. raw:: latex
      
      \end{mdframed}
      \vspace{1em}


- SWAP (exchange):

   .. raw:: latex
      
      \vspace{1em}
      \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

   .. only:: html

      .. image:: /figures/output/circuitry_gate_swap-dark.png
         :scale: 36 %
         :align: left
         :class: only-dark

   .. only:: html or latex

      .. image:: /figures/output/circuitry_gate_swap-light.png
         :scale: 36 %
         :align: left
         :class: only-light

   .. raw:: latex
      
      \end{mdframed}
      \vspace{1em}

- PSWAP (power-SWAP):

   .. raw:: latex
      
      \vspace{1em}
      \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

   .. only:: html

      .. image:: /figures/output/circuitry_gate_swap_power-dark.png
         :scale: 36 %
         :align: left
         :class: only-dark

   .. only:: html or latex

      .. image:: /figures/output/circuitry_gate_swap_power-light.png
         :scale: 36 %
         :align: left
         :class: only-light

   .. raw:: latex
      
      \end{mdframed}
      \vspace{1em}

- PERM (permutation):

   .. raw:: latex
      
      \vspace{1em}
      \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

   .. only:: html

      .. image:: /figures/output/circuitry_gate_permute-dark.png
         :scale: 36 %
         :align: left
         :class: only-dark

   .. only:: html or latex

      .. image:: /figures/output/circuitry_gate_permute-light.png
         :scale: 36 %
         :align: left
         :class: only-light

   .. raw:: latex
      
      \end{mdframed}
      \vspace{1em}

- HAD (Hadamard):

   .. raw:: latex
      
      \vspace{1em}
      \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

   .. only:: html

      .. image:: /figures/output/circuitry_gate_hadamard-dark.png
         :scale: 36 %
         :align: left
         :class: only-dark

   .. only:: html or latex

      .. image:: /figures/output/circuitry_gate_hadamard-light.png
         :scale: 36 %
         :align: left
         :class: only-light

   .. raw:: latex
      
      \end{mdframed}
      \vspace{1em}

- QFT (quantum Fourier transform):

   .. raw:: latex
      
      \vspace{1em}
      \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

   .. only:: html

      .. image:: /figures/output/circuitry_gate_fourier-dark.png
         :scale: 36 %
         :align: left
         :class: only-dark

   .. only:: html or latex

      .. image:: /figures/output/circuitry_gate_fourier-light.png
         :scale: 36 %
         :align: left
         :class: only-light

   .. raw:: latex
      
      \end{mdframed}
      \vspace{1em}

- controlled-:math:`\Unitary`:

   .. raw:: latex
      
      \vspace{1em}
      \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

   .. only:: html

      .. image:: /figures/output/circuitry_gate_controlled_unitary-dark.png
         :scale: 36 %
         :align: left
         :class: only-dark

   .. only:: html or latex

      .. image:: /figures/output/circuitry_gate_controlled_unitary-light.png
         :scale: 36 %
         :align: left
         :class: only-light

   .. raw:: latex
      
      \end{mdframed}
      \vspace{1em}

- controlled-:math:`\Unitary` (inverted):

   .. raw:: latex
      
      \vspace{1em}
      \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

   .. only:: html

      .. image:: /figures/output/circuitry_gate_controlled_unitary_inverted-dark.png
         :scale: 36 %
         :align: left
         :class: only-dark

   .. only:: html or latex

      .. image:: /figures/output/circuitry_gate_controlled_unitary_inverted-light.png
         :scale: 36 %
         :align: left
         :class: only-light

   .. raw:: latex
      
      \end{mdframed}
      \vspace{1em}

- anticontrolled-:math:`\Unitary`:

   .. raw:: latex
      
      \vspace{1em}
      \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

   .. only:: html

      .. image:: /figures/output/circuitry_gate_controlled_unitary_anti-dark.png
         :scale: 36 %
         :align: left
         :class: only-dark

   .. only:: html or latex

      .. image:: /figures/output/circuitry_gate_controlled_unitary_anti-light.png
         :scale: 36 %
         :align: left
         :class: only-light

   .. raw:: latex
      
      \end{mdframed}
      \vspace{1em}

- multiply-controlled-:math:`\Unitary`:

   .. raw:: latex
      
      \vspace{1em}
      \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

   .. only:: html

      .. image:: /figures/output/circuitry_gate_controlled_unitary_multiple-dark.png
         :scale: 36 %
         :align: left
         :class: only-dark

   .. only:: html or latex

      .. image:: /figures/output/circuitry_gate_controlled_unitary_multiple-light.png
         :scale: 36 %
         :align: left
         :class: only-light

   .. raw:: latex
      
      \end{mdframed}
      \vspace{1em}

- controlled-anticontrolled-:math:`\Unitary`:

   .. raw:: latex
      
      \vspace{1em}
      \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

   .. only:: html

      .. image:: /figures/output/circuitry_gate_controlled_unitary_mixed-dark.png
         :scale: 36 %
         :align: left
         :class: only-dark

   .. only:: html or latex

      .. image:: /figures/output/circuitry_gate_controlled_unitary_mixed-light.png
         :scale: 36 %
         :align: left
         :class: only-light

   .. raw:: latex
      
      \end{mdframed}
      \vspace{1em}

- CNOT (controlled-NOT):

   .. raw:: latex
      
      \vspace{1em}
      \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

   .. only:: html

      .. image:: /figures/output/circuitry_gate_controlled_not-dark.png
         :scale: 36 %
         :align: left
         :class: only-dark

   .. only:: html or latex

      .. image:: /figures/output/circuitry_gate_controlled_not-light.png
         :scale: 36 %
         :align: left
         :class: only-light

   .. raw:: latex
      
      \end{mdframed}
      \vspace{1em}

- CCNOT (controlled-controlled-NOT gate, doubly-controlled-NOT gate, also known as the *Toffoli* gate):

   .. raw:: latex
      
      \vspace{1em}
      \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

   .. only:: html

      .. image:: /figures/output/circuitry_gate_controlled_cnot-dark.png
         :scale: 36 %
         :align: left
         :class: only-dark

   .. only:: html or latex

      .. image:: /figures/output/circuitry_gate_controlled_cnot-light.png
         :scale: 36 %
         :align: left
         :class: only-light

   .. raw:: latex
      
      \end{mdframed}
      \vspace{1em}

- CSUM (controlled-SUM):

   .. raw:: latex
      
      \vspace{1em}
      \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

   .. only:: html

      .. image:: /figures/output/circuitry_gate_controlled_sum-dark.png
         :scale: 36 %
         :align: left
         :class: only-dark

   .. only:: html or latex

      .. image:: /figures/output/circuitry_gate_controlled_sum-light.png
         :scale: 36 %
         :align: left
         :class: only-light

   .. raw:: latex
      
      \end{mdframed}
      \vspace{1em}

- CSWAP (controlled-SWAP, also known as the *Fredkin* gate):

   .. raw:: latex
      
      \vspace{1em}
      \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

   .. only:: html

      .. image:: /figures/output/circuitry_gate_controlled_swap-dark.png
         :scale: 36 %
         :align: left
         :class: only-dark

   .. only:: html or latex

      .. image:: /figures/output/circuitry_gate_controlled_swap-light.png
         :scale: 36 %
         :align: left
         :class: only-light

   .. raw:: latex
      
      \end{mdframed}
      \vspace{1em}

Examples
========

A better understanding of quantum circuitry notation can be gained by studying a few basic examples. Perhaps the simplest complete quantum circuit that we can construct consists of just a unipartite quantum state :math:`\StateDensity` which evolves into the future along a single quantum wire, subsequently becoming the output state :math:`\StateDensity^\prime`:

   .. raw:: latex
      
      \vspace{1em}
      \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

   .. only:: html

      .. image:: /figures/output/circuitry_example_singlemode_simplest-dark.png
         :scale: 36 %
         :align: left
         :class: only-dark

   .. only:: html or latex

      .. image:: /figures/output/circuitry_example_singlemode_simplest-light.png
         :scale: 36 %
         :align: left
         :class: only-light

   .. raw:: latex
      
      \end{mdframed}
      \vspace{1em}

As there are no operations (such as gates or measurements) on the wire, the explicitly labelled output state :math:`\StateDensity^\prime` is identically equal to the input state :math:`\StateDensity` (since the quantum wire directly connects the two).

If we were to place a gate corresponding to an arbitrary unitary operator :math:`\Unitary` upon the intermediary wire, the action from the resulting operation is the standard transformation of a matrix by a linear operator:

   .. raw:: latex
      
      \vspace{1em}
      \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

   .. only:: html

      .. image:: /figures/output/circuitry_example_singlemode_density-dark.png
         :scale: 36 %
         :align: left
         :class: only-dark

   .. only:: html or latex

      .. image:: /figures/output/circuitry_example_singlemode_density-light.png
         :scale: 36 %
         :align: left
         :class: only-light

   .. raw:: latex
      
      \end{mdframed}
      \vspace{1em}

In the case of a pure (vector) input state, the circuit is simply:

   .. raw:: latex
      
      \vspace{1em}
      \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

   .. only:: html

      .. image:: /figures/output/circuitry_example_singlemode_pure-dark.png
         :scale: 36 %
         :align: left
         :class: only-dark

   .. only:: html or latex

      .. image:: /figures/output/circuitry_example_singlemode_pure-light.png
         :scale: 36 %
         :align: left
         :class: only-light

   .. raw:: latex
      
      \end{mdframed}
      \vspace{1em}

In this case, we could, without loss of generality, denote the output state with a vector state (such as :math:`\ket{\StateVector^\prime} = \Unitary\ket{\StateVector}`, equivalent to :math:`\StateDensity^\prime = \ket{\StateVector^\prime}\bra{\StateVector^\prime}`), since the action of the (linear transformation) unitary gate preserves the purity of the systems on which it acts. Note that this is not true in general for all circuits; (non-unitary) operations like the (partial) trace do not necessarily preserve the purity of a particular system, and so the output states cannot always be denoted by vector states even if the input states are pure.

More interesting cases are those of multipartite systems. For instance, the evolution of a bipartite input state under a composite unitary gate is:

   .. raw:: latex
      
      \vspace{1em}
      \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

   .. only:: html

      .. image:: /figures/output/circuitry_example_multimode_nonseparable_single-dark.png
         :scale: 36 %
         :align: left
         :class: only-dark

   .. only:: html or latex

      .. image:: /figures/output/circuitry_example_multimode_nonseparable_single-light.png
         :scale: 36 %
         :align: left
         :class: only-light

   .. raw:: latex
      
      \end{mdframed}
      \vspace{1em}

The evolution of the same state under parallel operations appears as:

   .. raw:: latex
      
      \vspace{1em}
      \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

   .. only:: html

      .. image:: /figures/output/circuitry_example_multimode_nonseparable_parallel-dark.png
         :scale: 36 %
         :align: left
         :class: only-dark

   .. only:: html or latex

      .. image:: /figures/output/circuitry_example_multimode_nonseparable_parallel-light.png
         :scale: 36 %
         :align: left
         :class: only-light

   .. raw:: latex
      
      \end{mdframed}
      \vspace{1em}

In the case where the input state is explicitly separable, we write:

   .. raw:: latex
      
      \vspace{1em}
      \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

   .. only:: html

      .. image:: /figures/output/circuitry_example_multimode_separable_single-dark.png
         :scale: 36 %
         :align: left
         :class: only-dark

   .. only:: html or latex

      .. image:: /figures/output/circuitry_example_multimode_separable_single-light.png
         :scale: 36 %
         :align: left
         :class: only-light

   .. raw:: latex
      
      \end{mdframed}
      \vspace{1em}

Due to the input state's separability, the mathematics corresponding to parallel operations on these systems may be greatly simplified:

   .. raw:: latex
      
      \vspace{1em}
      \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

   .. only:: html

      .. image:: /figures/output/circuitry_example_multimode_separable_parallel-dark.png
         :scale: 36 %
         :align: left
         :class: only-dark

   .. only:: html or latex

      .. image:: /figures/output/circuitry_example_multimode_separable_parallel-light.png
         :scale: 36 %
         :align: left
         :class: only-light

   .. raw:: latex
      
      \end{mdframed}
      \vspace{1em}

This is, of course, simply equivalent to two distinct subcircuits with the outputs :math:`\StateDensity^\prime_A = \Unitary_A \StateDensity_A \Unitary_A^\dagger` and :math:`\StateDensity^\prime_B = \Unitary_B \StateDensity_B \Unitary_B^\dagger`, respectively.

.. note:: For more examples, see the :ref:`Examples <part:examples>` section.

Remarks
=======

Matrix vs. vector circuits
--------------------------

Note that our description of quantum circuits thus far has considered quantum processes involving both matrix states (such as mixed states and matrix representations of pure states) and vector states. Traditionally however, quantum circuit diagrams were used exclusively to visualize completely vector processes: all inputs are vector states, all intermediate operations are linear transformations, and so accordingly all outputs are vectors (up until any non-linear operations such as measurement). In such a paradigm, the mathematics corresponding to any given quantum circuit is necessarily always expressible as (linear and unitary) operations on *vectors*. It is therefore not necessary to express the circuit output using density matrices (such as outer products like :math:`\ket{\StateVector^\prime}\bra{\StateVector^\prime}`) in the case of exclusively purity-preserving operations. For example, we may write

   .. raw:: latex
      
      \vspace{1em}
      \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

   .. only:: html

      .. image:: /figures/output/circuitry_example_vector-dark.png
         :scale: 36 %
         :align: left
         :class: only-dark

   .. only:: html or latex

      .. image:: /figures/output/circuitry_example_vector-light.png
         :scale: 36 %
         :align: left
         :class: only-light

   .. raw:: latex
      
      \end{mdframed}
      \vspace{1em}

which is purely a vector description. In our combined matrix and vector formalism, we can equivalently express the above circuit as

   .. raw:: latex
      
      \vspace{1em}
      \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

   .. only:: html

      .. image:: /figures/output/circuitry_example_matrix-dark.png
         :scale: 36 %
         :align: left
         :class: only-dark

   .. only:: html or latex

      .. image:: /figures/output/circuitry_example_matrix-light.png
         :scale: 36 %
         :align: left
         :class: only-light

   .. raw:: latex
      
      \end{mdframed}
      \vspace{1em}

where, despite the vector input and linear transformation, the output is given as a (density) matrix. The circuit formalism presented here is thus a more general one, such that the quantum circuits describe operations on (density) *matrix* states, not just vector states. This additionally means that both purity-preserving and purity-non-preserving operations (such as the partial trace) are completely captured by our methodology. Note however that in cases where a pure state output is obtained, it is often useful to specify such output in vector form (this being the most compact way of expressing pure states).

.. only:: html

   .. rst-class:: bibliography

      .. rubric:: :stylebibliography:`References`

      .. bibliography::
         :filter: docname in docnames
