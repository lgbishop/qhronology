# Project: Qhronology (https://github.com/lgbishop/qhronology)
# Author: lgbishop <lgbishop@protonmail.com>
# Copyright: Lachlan G. Bishop 2025
# License: AGPLv3 (non-commercial use), proprietary (commercial use)
# For more details, see the README in the project repository:
# https://github.com/lgbishop/qhronology,
# or visit the website:
# https://qhronology.org.

"""
A mixin for symbolic algebra.
Not intended to be used directly by the user.
"""

# https://peps.python.org/pep-0649/
# https://peps.python.org/pep-0749/
from __future__ import annotations

from typing import Any

import sympy as sp

from qhronology.utilities.classification import num, sym


class SymbolicsProperties:
    """A mixin for endowing derived classes with algebraic symbolism.

    Not intended to be instantiated itself, but rather indirectly via the constructor
    in its child classes."""

    def __init__(
        self,
        symbols: dict[sym | str, dict[str, Any]] | None = None,
        conditions: list[tuple[num | sym | str, num | sym | str]] | None = None,
    ):
        symbols = {} if symbols is None else symbols
        conditions = [] if conditions is None else conditions
        self.symbols = symbols
        self.conditions = conditions

    @property
    def symbols(self) -> dict[sym | str, dict[str, Any]]:
        """A dictionary in which the keys are individual symbols (contained within the object's
        matrix representation) and the values are dictionaries of their respective SymPy
        keyword-argument :python:`assumptions` ("predicates").
        A full list of currently supported predicates, and their defaults, is as follows:

        - :python:`"algebraic"`: :python:`True`
        - :python:`"commutative"`: :python:`True`
        - :python:`"complex"`: :python:`True`
        - :python:`"extended_negative"`: :python:`False`
        - :python:`"extended_nonnegative"`: :python:`True`
        - :python:`"extended_nonpositive"`: :python:`False`
        - :python:`"extended_nonzero"`: :python:`True`
        - :python:`"extended_positive"`: :python:`True`
        - :python:`"extended_real"`: :python:`True`
        - :python:`"finite"`: :python:`True`
        - :python:`"hermitian"`: :python:`True`
        - :python:`"imaginary"`: :python:`False`
        - :python:`"infinite"`: :python:`False`
        - :python:`"integer"`: :python:`True`
        - :python:`"irrational"`: :python:`False`
        - :python:`"negative"`: :python:`False`
        - :python:`"noninteger"`: :python:`False`
        - :python:`"nonnegative"`: :python:`True`
        - :python:`"nonpositive"`: :python:`False`
        - :python:`"nonzero"`: :python:`True`
        - :python:`"positive"`: :python:`True`
        - :python:`"rational"`: :python:`True`
        - :python:`"real"`: :python:`True`
        - :python:`"transcendental"`: :python:`False`
        - :python:`"zero"`: :python:`False`
        """
        return dict(self._symbols)

    @symbols.setter
    def symbols(self, symbols: dict[sym | str, dict[str, Any]]):
        self._symbols = symbols
        # self.symbols_list = symbols_list

    @property
    def symbols_list(self) -> list[sym]:
        symbols_list = []
        for key, value in self.symbols.items():
            symbol = sp.Symbol(str(key), **value)
            symbols_list.append(symbol)
        return list(symbols_list)

    @property
    def conditions(self) -> list[tuple[num | sym | str, num | sym | str]]:
        """A list of :math:`2`-tuples of conditions to be applied to the object's matrix
        representation."""
        return list(self._conditions)

    @conditions.setter
    def conditions(self, conditions):
        self._conditions = conditions
