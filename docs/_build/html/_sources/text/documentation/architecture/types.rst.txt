.. include:: /styles.rst

Types
=====

Qhronology's underlying functionality takes advantage of a few bespoke type aliases, which are summarized in the table below.

.. list-table:: Internal type aliases.
   :widths: 5 12 48
   :header-rows: 1

   * - **Alias**
     - **Description**
     - **Definition**
   * - | :inlinelatex:`\vspace*{-2.00\baselineskip}`
       | :python:`num`
     - | :inlinelatex:`\vspace*{-2.00\baselineskip}`
       | Numerical :inlinelatex:`\linebreak` scalars
       | :inlinelatex:`\vspace*{-1.85\baselineskip}`
     - | :inlinelatex:`\vspace*{-2.00\baselineskip}`
       | :python:`numbers.Number | numpy.generic | sympy.Basic`
   * - | :inlinelatex:`\vspace*{-1.75\baselineskip}`
       | :python:`sym`
     - | :inlinelatex:`\vspace*{-1.75\baselineskip}`
       | SymPy scalar :inlinelatex:`\linebreak` symbols
     - | :inlinelatex:`\vspace*{-1.75\baselineskip}`
       | :python:`sympy.matrices.expressions.matexpr.MatrixSymbol | sympy.matrices.expressions.matexpr.MatrixElement | sympy.core.symbol.Symbol`
       | :inlinelatex:`\vspace*{-1.85\baselineskip}`
   * - | :inlinelatex:`\vspace*{-2.75\baselineskip}`
       | :python:`expr`
     - | :inlinelatex:`\vspace*{-1.75\baselineskip}`
       | SymPy scalar :inlinelatex:`\linebreak` expressions
       | :inlinelatex:`\vspace*{-1.85\baselineskip}`
     - | :inlinelatex:`\vspace*{-1.75\baselineskip}`
       | :python:`sympy.core.expr.Expr`
   * - | :inlinelatex:`\vspace*{-1.75\baselineskip}`
       | :python:`mat`
     - | :inlinelatex:`\vspace*{-1.75\baselineskip}`
       | SymPy dense matrices :inlinelatex:`\linebreak` (mutable)
       | :inlinelatex:`\vspace*{-1.85\baselineskip}`
     - | :inlinelatex:`\vspace*{-1.75\baselineskip}`
       | :python:`sympy.matrices.dense.MutableDenseMatrix`
   * - | :inlinelatex:`\vspace*{-1.75\baselineskip}`
       | :python:`arr`
     - | :inlinelatex:`\vspace*{-1.75\baselineskip}`
       | NumPy :inlinelatex:`\linebreak` arrays
       | :inlinelatex:`\vspace*{-1.85\baselineskip}`
     - | :inlinelatex:`\vspace*{-1.75\baselineskip}`
       | :python:`numpy.ndarray`

It may be useful to know that :python:`sym` is a subtype of :python:`expr`. In other words, the set of all :python:`sym`-type objects is a proper subset of the set of all :python:`expr`-type objects.

.. raw:: latex

   \newpage