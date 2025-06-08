# Project: Qhronology (https://github.com/lgbishop/qhronology)
# Author: lgbishop <lachlanbishop@protonmail.com>
# Copyright: Lachlan G. Bishop 2025
# License: AGPLv3 (non-commercial use), proprietary (commercial use)
# For more details, see the README in the project repository:
# https://github.com/lgbishop/qhronology,
# or visit the website:
# https://qhronology.com.

"""
General helper functions.
Not intended to be used directly by the user.
"""

# https://peps.python.org/pep-0649/
# https://peps.python.org/pep-0749/
from __future__ import annotations

import inspect
import itertools
import copy
from typing import Callable, Any

import numpy as np
import sympy as sp
from sympy.physics.quantum import TensorProduct
from sympy.physics.quantum.dagger import Dagger

from qhronology.utilities.classification import mat, arr, num, sym, Shapes, matrix_shape


def flatten_list(nested_list: list) -> list:
    """Flatten a list of any nesting depth and structure, e.g.:

    Examples
    --------
    >>> flatten_list([1, [2, [3, [4]]]])
    [1, 2, 3, 4]

    >>> flatten_list([[1], [2], [3], [4]])
    [1, 2, 3, 4]
    """
    if isinstance(nested_list, list | tuple) is True:
        flattened_list = sum(map(flatten_list, nested_list), [])
    else:
        flattened_list = [nested_list]
    return flattened_list


def list_depth(nested_list: list) -> int:
    """Compute the depth of a (nested) list."""
    if not isinstance(nested_list, list):
        return 0
    return max(map(list_depth, nested_list), default=0) + 1


def count_systems(matrix: mat, dim: int) -> int:
    """Count the number of ``dim``-dimensional subsystems which constitute the (composite) system
    represented by ``matrix``."""
    return int(np.emath.logn(dim, sp.shape(to_density(matrix))[0]))


def count_dims(matrix: mat, systems: list[int]) -> int:
    """Compute the dimensionality of the (composite) system represented by ``matrix``."""
    return int((sp.shape(to_density(matrix))[0]) ** (1 / len(set(systems))))


def check_systems_conflicts(*subsystems: list[int]) -> bool:
    """Check for conflicts (common element(s)) in the given (unpacked) tuple of lists.
    Returns ``True`` if any are found, otherwise ``False``."""
    subsystems_list = flatten_list([*subsystems])
    subsystems_set = set(subsystems_list)
    return len(subsystems_list) != len(subsystems_set)


def adjust_targets(targets: list[int], removed: list[int]) -> list[int]:
    """Adjust the specified system indices (``targets``) according to those which have been
    removed (``removed``) from the total set."""
    targets = sorted(list(set(flatten_list([targets]))))
    removed = sorted(list(set(flatten_list([removed]))))

    removed_below = [remove for remove in removed if remove < min(targets, default=0)]

    targets_adjusted = []
    for target in targets:
        targets_adjusted.append(target - len(removed_below))

    return targets_adjusted


def arrange(positions: list[list[int]], items: list[Any]) -> list[Any]:
    """Arranges the elements of ``items`` the according to the respective locations
    (e.g., system indices) in ``positions``.
    The main use case would be to arrange gates in a multipartite system.

    The lengths of both ``positions`` and ``items`` must be the same, and ``positions`` must not
    contain any missing system indices.

    Examples
    --------
    >>> arrange([[0, 3], [1, 2]], ["a", "b"])
    ['a', 'b', 'b', 'a']
    """
    if len(positions) != len(items):
        raise ValueError(
            "The number of items in ``positions`` and ``items`` do not match."
        )

    arranged = []
    for n in range(min(flatten_list(positions)), max(flatten_list(positions)) + 1):
        for k in range(0, len(items)):
            if n in positions[k]:
                arranged.append(items[k])

    return arranged


def to_density(vector: mat) -> mat:
    """Compute the outer product of ``vector`` with itself, thereby converting any vector state
    into density matrix form.
    Leaves square matrices unaffected, and raises an error for non-square matrices."""
    if matrix_shape(vector) == Shapes.COLUMN.value:
        return vector * Dagger(vector)
    elif matrix_shape(vector) == Shapes.ROW.value:
        return Dagger(vector) * vector
    elif matrix_shape(vector) == Shapes.SQUARE.value:
        return vector
    else:
        raise ValueError(
            "A non-square matrix cannot be converted to a density matrix form."
        )


def to_column(vector: mat) -> mat:
    """Transpose ``vector`` into its column form."""
    if matrix_shape(vector) == Shapes.COLUMN.value:
        return vector
    elif matrix_shape(vector) == Shapes.ROW.value:
        return sp.transpose(vector).as_mutable()
    elif matrix_shape(vector) == Shapes.SQUARE.value:
        return vector
    else:
        raise ValueError("Cannot convert a non-square matrix to a column vector.")


def stringify(matrix: mat, dim: int) -> str:
    """Render the mathematical expression (as a string) of the given ``matrix``."""
    num_systems = count_systems(matrix, dim)

    basis = list(itertools.product([n for n in range(0, dim)], repeat=num_systems))
    matrix_strings = []
    for n in range(0, matrix.shape[0]):
        for m in range(0, matrix.shape[1]):
            if matrix[n, m] != 0:
                if matrix_shape(matrix) == Shapes.COLUMN.value:
                    term = (
                        "|"
                        + str(basis[n])
                        .replace("(", "")
                        .replace(")", "")
                        .replace(" ", "")
                        .strip(",")
                        + "⟩"
                    )
                elif matrix_shape(matrix) == Shapes.ROW.value:
                    term = (
                        "⟨"
                        + str(basis[m])
                        .replace("(", "")
                        .replace(")", "")
                        .replace(" ", "")
                        .strip(",")
                        + "|"
                    )
                elif matrix_shape(matrix) == Shapes.SQUARE.value:
                    term = (
                        "|"
                        + str(basis[n])
                        .replace("(", "")
                        .replace(")", "")
                        .replace(" ", "")
                        .strip(",")
                        + "⟩"
                        + "⟨"
                        + str(basis[m])
                        .replace("(", "")
                        .replace(")", "")
                        .replace(" ", "")
                        .strip(",")
                        + "|"
                    )
                else:
                    raise ValueError(
                        "The given matrix must be either a square, a column, or a row."
                    )
                coefficient = matrix[n, m]
                if isinstance(sp.sympify(coefficient), sp.core.add.Add) is True:
                    coefficient = "(" + str(coefficient) + ")"
                if str(coefficient) == "1":
                    coefficient = ""
                matrix_strings.append(str(coefficient) + term)
    return " + ".join(matrix_strings)


def symbolize_expression(
    expression: mat | arr | num | sym | str,
    symbols: dict[sym | str, dict[str, Any]] | list[sym] | None = None,
) -> mat | arr | num | sym:
    """Sympify a numerical, symbolic, or string expression,
    and replace the symbols with given counterparts."""
    symbols = [] if symbols is None else symbols
    if isinstance(symbols, dict) is True:
        symbols_list = []
        for key, value in symbols.items():
            symbol = sp.Symbol(str(key), **value)
            symbols_list.append(symbol)
        symbols = symbols_list

    expressions = expression
    if isinstance(expressions, mat) is False:
        expressions = [expressions]
    for i, expression in enumerate(expressions):
        try:
            expression = sp.sympify(expression)
        except:
            try:
                expression = sp.sympify(str(expression))
            except:
                raise TypeError(
                    "The given ``expression`` cannot be converted to a symbolic representation."
                )

        for symbol in symbols:
            try:
                expression = expression.subs(str(symbol), symbol)
            except:
                try:
                    expression = expression.subs(sp.sympify(str(symbol)), symbol)
                except:
                    raise ValueError("One of more of the given symbols is invalid.")
        expressions[i] = expression
    if isinstance(expressions, list) is True:
        expressions = expressions[0]
    return expressions


def symbolize_tuples(
    conditions: list[tuple[num | sym | str, num | sym | str]], symbols_list: list[sym]
) -> list[tuple[num | sym, num | sym]]:
    """Sympify the numerical, symbolic, or string expression pairs within tuples of the
    list ``conditions`` and replace the symbols with given counterparts."""
    for n in range(0, len(conditions)):
        conditions[n] = list(conditions[n])
        conditions[n][0] = symbolize_expression(conditions[n][0], symbols_list)
        conditions[n][1] = symbolize_expression(conditions[n][1], symbols_list)
        conditions[n] = tuple(conditions[n])

    return conditions


def recursively_simplify(
    expression: mat | arr | num | sym,
    conditions: list[tuple[num | sym, num | sym]] | None = None,
    limit: int | None = None,
) -> mat | arr | num | sym:
    """Simplify ``expression`` recursively using the substitutions given in ``conditions``.
    Runs until ``expression`` is unchanged from the previous iteration,
    or until the ``limit`` number of iterations is reached."""

    conditions = [] if conditions is None else conditions
    limit = 2 if limit is None else limit

    expressions = expression
    if isinstance(expressions, mat) is False:
        expressions = [expressions]

    for index, item in enumerate(expressions):
        expression_previous = item
        counter = 0
        expression_after = None
        while True:
            expression_before = copy.deepcopy(expression_previous)

            functions = [
                sp.simplify,
                sp.factor,
                sp.expand,
                sp.cancel,
            ]  # + [sp.cos, sp.exp]
            # functions = [sp.simplify]

            # Generate all (sub-)permutations of the list ``functions``
            permutations = []
            for n in range(1, len(functions) + 1):
                permutations += list(itertools.permutations(functions, r=n))

            for permutation in permutations:
                length_before = expression_before.count_ops()
                expression_after = copy.deepcopy(expression_before)

                for function in permutation:
                    expression_after = expression_after.subs(conditions)
                    if function == sp.cos:
                        expression_after = expression_after.rewrite(sp.cos)
                    elif function == sp.exp:
                        expression_after = expression_after.rewrite(sp.exp)
                    elif function == sp.simplify:
                        expression_after = function(expression_after, inverse=True)
                    else:
                        expression_after = function(expression_after)
                expression_after = expression_after.subs(conditions)

                length_after = expression_after.count_ops()
                if length_after < length_before:
                    expression_before = copy.deepcopy(expression_after)

            # Do not try another iteration if no change
            if expression_after == expression_previous:
                break
            counter += 1
            if counter >= limit:
                break
            expression_previous = copy.deepcopy(expression_before)
        expressions[index] = expression_before

    if isinstance(expressions, list) is True:
        expressions = expressions[0]

    return expressions


def extract_matrix(operator: mat | arr | QuantumObject) -> mat:
    """Extract the SymPy matrix from the ``operator`` object."""
    try:
        matrix = operator.output()
    except:
        try:
            matrix = operator.matrix
        except:
            matrix = operator
    try:
        matrix = sp.Matrix(matrix)
    except:
        raise ValueError("A valid SymPy matrix cannot be extracted from ``operator``.")
    return matrix


def extract_conditions(*states) -> list[tuple[num | sym, num | sym]]:
    """Extract any substitution conditions accessible via the ``conditions`` property
    from the objects in ``states``."""
    conditions = []
    symbols_list = []
    for state in states:
        try:
            conditions += state.conditions
            symbols_list += state.symbols_list
        except:
            pass
    symbols_list = list(set(flatten_list(symbols_list)))
    conditions = symbolize_tuples(conditions, symbols_list)
    return conditions


def extract_symbols(*states) -> list[sym]:
    """Extract any SymPy symbols accessible via the ``symbols`` property
    from the objects in ``states``."""
    symbols = dict()
    for state in states:
        try:
            symbols |= state.symbols
        except:
            pass
    return symbols


def apply_function(
    matrix: mat, function: Callable, arguments: list[Any] | None = None
) -> mat:
    """Applies a function to a matrix. This is accomplished using eigendecomposition,
    in which the specified matrix is assumed to be normal
    (i.e., ``matrix * Dagger(matrix) = Dagger(matrix) * matrix``,
    which holds true for density operators)."""
    arguments = [] if arguments is None else arguments
    eigentriple = matrix.eigenvects()
    transformed = sp.zeros(len(eigentriple[0][2][0]))
    for k in range(0, len(eigentriple)):
        eigenvalue = eigentriple[k][0]
        multiplicity = eigentriple[k][1]
        eigenvectors = eigentriple[k][2]
        if function == sp.log and eigenvalue != 0:
            for n in range(0, multiplicity):
                transformed += function(eigenvalue, *arguments) * to_density(
                    eigenvectors[n]
                )
    return transformed


def default_arguments(
    arguments, kwarguments, class_object, arg_pairs: list[tuple[str, Any]]
):
    """Change the default value of an argument in a subclass's constructor.
    ``class_object`` is the class whose ``__init__`` signature is to be targeted.

    """
    arg_strs, arg_defaults = zip(*arg_pairs)
    sig = inspect.signature(class_object.__init__)
    arguments_parent = list(sig.parameters.keys())
    arg_indices = [arguments_parent.index(string) for string in arg_strs]

    arg_pairs, arg_indices = zip(*sorted(zip(arg_pairs, arg_indices)))

    for n in range(0, len(arg_pairs)):
        arg_index = arg_indices[n] - 1
        arg_str = arg_pairs[n][0]
        arg_default = arg_pairs[n][1]
        if len(arguments) > arg_index:
            arguments[arg_index] = (
                arg_default if arguments[arg_index] is None else arguments[arg_index]
            )
        else:
            if arg_str not in kwarguments.keys() or kwarguments[arg_str] is None:
                kwarguments[arg_str] = arg_default

    return arguments, kwarguments


def fix_arguments(
    arguments, kwarguments, class_object, arg_pairs: list[tuple[str, Any]]
):
    """Fix the value of an argument in a subclass's constructor.
    The argument ``class_object`` is the class whose ``__init__`` signature is to be targeted.

    """
    arg_strs, arg_values = zip(*arg_pairs)
    sig = inspect.signature(class_object.__init__)
    arguments_parent = list(sig.parameters.keys())
    arg_indices = [arguments_parent.index(string) for string in arg_strs]

    arg_pairs, arg_indices = zip(*sorted(zip(arg_pairs, arg_indices)))

    shift = 0
    for n in range(0, len(arg_pairs)):
        arg_index = arg_indices[n] - 1
        arg_str = arg_pairs[n][0]
        arg_value = arg_pairs[n][1]
        if len(arguments) + shift > arg_index:
            arguments = list(arguments)
            arguments.insert(arg_index, arg_value)
            arguments = tuple(arguments)
            shift += 1
            if arg_str in kwarguments.keys():
                kwarguments.pop(arg_str)
        else:
            if arg_str not in kwarguments.keys():
                kwarguments[arg_str] = arg_value

    return arguments, kwarguments


def assemble_composition(*pairs: tuple[mat, list[int]]) -> mat:
    """Assemble a composite state from constituent subsystems described by the items in ``pairs``.
    For each pair:
    - the first element is the subsystem's state matrix.
    - the second element is the list of indices of its systems."""
    pairs_sorted = sorted(pairs, key=lambda pair: min(pair[1]))
    state_composition = sp.Matrix(TensorProduct(*[pair[0] for pair in pairs_sorted]))
    return state_composition
