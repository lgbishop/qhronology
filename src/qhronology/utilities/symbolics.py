# Project: Qhronology (https://github.com/lgbishop/qhronology)
# Author: lgbishop <lachlanbishop@protonmail.com>
# Copyright: Lachlan G. Bishop 2025
# License: AGPLv3 (non-commercial use), proprietary (commercial use)
# For more details, see the README in the project repository:
# https://github.com/lgbishop/qhronology,
# or visit the website:
# https://qhronology.com.

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
        keyword-argument ``assumptions`` ("predicates").
        A full list of currently supported predicates, and their defaults, is as follows:

        - ``"algebraic"``: ``True``
        - ``"commutative"``: ``True``
        - ``"complex"``: ``True``
        - ``"extended_negative"``: ``False``
        - ``"extended_nonnegative"``: ``True``
        - ``"extended_nonpositive"``: ``False``
        - ``"extended_nonzero"``: ``True``
        - ``"extended_positive"``: ``True``
        - ``"extended_real"``: ``True``
        - ``"finite"``: ``True``
        - ``"hermitian"``: ``True``
        - ``"imaginary"``: ``False``
        - ``"infinite"``: ``False``
        - ``"integer"``: ``True``
        - ``"irrational"``: ``False``
        - ``"negative"``: ``False``
        - ``"noninteger"``: ``False``
        - ``"nonnegative"``: ``True``
        - ``"nonpositive"``: ``False``
        - ``"nonzero"``: ``True``
        - ``"positive"``: ``True``
        - ``"rational"``: ``True``
        - ``"real"``: ``True``
        - ``"transcendental"``: ``False``
        - ``"zero"``: ``False``
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
