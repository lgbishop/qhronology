# Project: Qhronology (https://github.com/lgbishop/qhronology)
# Author: lgbishop <lgbishop@protonmail.com>
# Copyright: Lachlan G. Bishop 2025
# License: AGPLv3 (non-commercial use), proprietary (commercial use)
# For more details, see the README in the project repository:
# https://github.com/lgbishop/qhronology,
# or visit the website:
# https://qhronology.org.

"""
General helper functions.
Not intended to be used directly by the user.
"""

# https://peps.python.org/pep-0649/
# https://peps.python.org/pep-0749/
from __future__ import annotations
import copy
import inspect
import itertools
from typing import Any, Callable

import numpy as np
import sympy as sp
from sympy.physics.quantum import TensorProduct

from qhronology.utilities.classification import (
    Shapes,
    arr,
    count_columns,
    count_rows,
    expr,
    mat,
    matrix_shape,
    num,
    sym,
)


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


def count_systems(matrix: mat | arr, dim: int) -> int:
    """Count the number of :python:`dim`-dimensional subsystems that constitute the (composite) system on which :python:`matrix` resides."""
    return int(np.emath.logn(dim, count_rows(to_density(matrix))))


def count_dims(matrix: mat | arr, num_systems: int) -> int:
    """Compute the dimensionality of the (composite) system on which :python:`matrix` resides."""
    return int((count_rows(to_density(matrix))) ** (1 / num_systems))


def check_systems_conflicts(*subsystems: *tuple[list[int]]) -> bool:
    """Check for conflicts (common element(s)) in the given (unpacked) tuple of lists.
    Returns :python:`True` if any are found, otherwise :python:`False`."""
    subsystems_list = flatten_list([*subsystems])
    subsystems_set = set(subsystems_list)
    return len(subsystems_list) != len(subsystems_set)


def adjust_targets(targets: list[int], removed: list[int]) -> list[int]:
    """Adjust the specified system indices (:python:`targets`) according to those which have been removed (:python:`removed`) from the total set."""
    targets = sorted(list(set(flatten_list([targets]))))
    removed = sorted(list(set(flatten_list([removed]))))

    removed_below = [remove for remove in removed if remove < min(targets, default=0)]

    targets_adjusted = []
    for target in targets:
        targets_adjusted.append(target - len(removed_below))

    return targets_adjusted


def arrange(positions: list[list[int]], items: list[Any]) -> list[Any]:
    """Arranges the elements of :python:`items` the according to the respective locations (e.g., system indices) in :python:`positions`.
    The main use case would be to arrange gates in a multipartite system.
    The lengths of both :python:`positions` and :python:`items` must be the same, and :python:`positions` must not contain any missing system indices.

    Examples
    --------
    >>> arrange([[0, 3], [1, 2]], ["a", "b"])
    ['a', 'b', 'b', 'a']
    """
    if len(positions) != len(items):
        raise ValueError(
            """The number of items in :python:`positions` and :python:`items` do not match."""
        )

    arranged = []
    for n in range(min(flatten_list(positions)), max(flatten_list(positions)) + 1):
        for k in range(0, len(items)):
            if n in positions[k]:
                arranged.append(items[k])

    return arranged


def conjugate_transpose(matrix: mat | arr) -> mat | arr:
    """Compute the conjugate transpose of :python:`matrix`."""
    return matrix.conjugate().transpose()


def dtype(matrix: mat | arr) -> type:
    """Determine the numerical data type (:python:`dtype`) of :python:`matrix`."""
    if isinstance(matrix, mat) is True:
        return object
    elif isinstance(matrix, arr) is True:
        if matrix.dtype == object:
            return object
        elif matrix.dtype == float:
            return float
        elif matrix.dtype == complex:
            return complex
        elif matrix.dtype == int:
            return int
        else:
            raise TypeError("""Unable to determine the matrix's datatype.""")
    else:
        raise TypeError(
            """The given matrix is neither a SymPy matrix or NumPy array."""
        )


def to_density(vector: mat | arr) -> mat | arr:
    """Compute the outer product of :python:`vector` with itself, thereby converting any vector state into density matrix form.
    Leaves square matrices unaffected, and raises an error for non-square matrices."""
    if matrix_shape(vector) == Shapes.COLUMN.value:
        return vector * conjugate_transpose(vector)
    elif matrix_shape(vector) == Shapes.ROW.value:
        return conjugate_transpose(vector) * vector
    elif matrix_shape(vector) == Shapes.SQUARE.value:
        return vector
    else:
        raise ValueError(
            """A non-square matrix cannot be converted to a density matrix form."""
        )


def to_column(vector: mat | arr) -> mat | arr:
    """Transpose :python:`vector` into its column form."""
    if matrix_shape(vector) == Shapes.COLUMN.value:
        return vector
    elif matrix_shape(vector) == Shapes.ROW.value:
        return vector.transpose()
    elif matrix_shape(vector) == Shapes.SQUARE.value:
        return vector
    else:
        raise ValueError("""Cannot convert a non-square matrix to a column vector.""")


def to_array(
    matrix: mat | arr | list[list[num | expr | str]], numerical: bool | None = None
) -> arr:
    """Converts :python:`matrix` to a NumPy array."""
    numerical = False if numerical is None else numerical
    if numerical is True:
        if not (
            isinstance(matrix, arr) is True and issubclass(dtype(matrix), num) is True
        ):
            try:
                matrix = np.array(matrix, dtype=complex)
            except:
                # print(
                #     """Warning: The given matrix contains non-floating types.""",
                #     """Falling back to `object` mode.""",
                # )
                matrix = np.array(matrix, dtype=object)
    else:
        if isinstance(matrix, arr) is False:
            matrix = np.array(matrix, dtype=object)
    return matrix


def to_matrix(matrix: mat | arr | list[list[num | expr | str]]) -> mat:
    """Converts :python:`matrix` to a SymPy matrix."""
    return sp.Matrix(matrix).as_mutable()


def cast(
    matrix: mat | arr | list[list[num | expr | str]],
    numerical: bool | None = None,
    array: bool | None = None,
) -> mat | arr:
    """Converts :python:`matrix` to either a NumPy array or SymPy matrix."""
    numerical = False if numerical is None else numerical
    array = False if array is None else array
    if array is True:
        return to_array(matrix, numerical=numerical)
    else:
        return to_matrix(matrix)


def to_numerical(
    expression: num | expr | str, numerical: bool | None = None
) -> num | expr | str:  # TODO
    """Converts :python:`expression` to a numerical value, if possible."""
    numerical = False if numerical is None else numerical
    if numerical is True:
        try:
            expression = np.array([expression], dtype=complex)
        except:
            expression = np.array([expression], dtype=object)
        expression = expression[0]
    return expression


def generate_identity(
    size: int, numerical: bool | None = None, array: bool | None = None
) -> mat | arr:
    """Construct an identity matrix as either a SymPy matrix or NumPy matrix."""
    if numerical is True:
        return cast(np.eye(size), numerical=numerical, array=array)
    else:
        return cast(sp.eye(size), numerical=numerical, array=array)


def generate_zeros(
    size: int, numerical: bool | None = None, array: bool | None = None
) -> mat | arr:
    """Construct a matrix or zeros as either a SymPy matrix or NumPy matrix."""
    if numerical is True:
        return cast(np.zeros((size, size)), numerical=numerical, array=array)
    else:
        return cast(sp.zeros(size), numerical=numerical, array=array)


def stringify(
    matrix: mat | arr,
    dim: int,
    delimiter: str | None = None,
    product: bool | None = None,
) -> str:
    """Render the mathematical expression (as a string) of the given :python:`matrix`."""
    num_systems = count_systems(matrix, dim)
    delimiter = "," if delimiter is None else delimiter
    product = False if product is None else product

    basis = list(itertools.product([n for n in range(0, dim)], repeat=num_systems))
    matrix_strings = []
    rows = count_rows(matrix)
    columns = count_columns(matrix)
    for n in range(0, rows):
        for m in range(0, columns):
            if matrix[n, m] != 0:
                if matrix_shape(matrix) == Shapes.COLUMN.value:
                    if product is True:
                        term = "⊗".join(["|" + str(value) + "⟩" for value in basis[n]])
                    else:
                        term = (
                            "|"
                            + delimiter.join([str(value) for value in basis[n]])
                            + "⟩"
                        )
                elif matrix_shape(matrix) == Shapes.ROW.value:
                    if product is True:
                        term = "⊗".join(["⟨" + str(value) + "|" for value in basis[m]])
                    else:
                        term = (
                            "⟨"
                            + delimiter.join([str(value) for value in basis[m]])
                            + "|"
                        )
                elif matrix_shape(matrix) == Shapes.SQUARE.value:
                    kets = ["|" + str(value) + "⟩" for value in basis[n]]
                    bras = ["⟨" + str(value) + "|" for value in basis[m]]
                    ketbras = [kets[k] + bras[k] for k in range(0, len(kets))]
                    if product is True:
                        term = "⊗".join(ketbras)
                    else:
                        term = (
                            "|"
                            + delimiter.join([str(value) for value in basis[n]])
                            + "⟩"
                            + "⟨"
                            + delimiter.join([str(value) for value in basis[m]])
                            + "|"
                        )
                else:
                    raise ValueError(
                        """The given matrix must be either a square, a column, or a row."""
                    )
                coefficient = matrix[n, m]
                if isinstance(sp.sympify(coefficient), sp.core.add.Add) is True:
                    coefficient = "(" + str(coefficient) + ")"
                if str(coefficient) == "1":
                    coefficient = ""
                matrix_strings.append(str(coefficient) + term)
    return " + ".join(matrix_strings)


def symbolize_expression(
    expression: mat | arr | num | expr | str,
    symbols: dict[sym | str, dict[str, Any]] | list[sym] | None = None,
) -> mat | arr | num | expr:
    """Sympify a numerical, symbolic, or string expression, and replace the symbols with given counterparts."""
    symbols = [] if symbols is None else symbols
    if isinstance(symbols, dict) is True:
        symbols_list = []
        for key, value in symbols.items():
            symbol = sp.Symbol(str(key), **value)
            symbols_list.append(symbol)
        symbols = symbols_list

    expressions = expression
    if isinstance(expressions, mat | arr) is False:
        expressions = [expressions]
    if not (
        isinstance(expressions, arr) is True
        and issubclass(dtype(expressions), num) is True
    ):
        for i, expression in enumerate(expressions):
            try:
                expression = sp.sympify(expression)
            except:
                try:
                    expression = sp.sympify(str(expression))
                except:
                    raise TypeError(
                        """The given :python:`expression` cannot be converted to a symbolic representation."""
                    )

            for symbol in symbols:
                try:
                    expression = expression.subs(str(symbol), symbol)
                except:
                    try:
                        expression = expression.subs(sp.sympify(str(symbol)), symbol)
                    except:
                        raise ValueError(
                            """One of more of the given symbols is invalid."""
                        )
            expressions[i] = expression

    if isinstance(expressions, list) is True:
        expressions = expressions[0]

    return expressions


def symbolize_conditions(
    conditions: list[tuple[num | expr | str, num | expr | str]], symbols_list: list[sym]
) -> list[tuple[num | expr, num | expr]]:
    """Sympify the numerical, symbolic, or string expression pairs within tuples of the list :python:`conditions` and replace the symbols with given counterparts."""
    for n in range(0, len(conditions)):
        conditions[n] = list(conditions[n])
        conditions[n][0] = symbolize_expression(conditions[n][0], symbols_list)
        conditions[n][1] = symbolize_expression(conditions[n][1], symbols_list)
        conditions[n] = tuple(conditions[n])

    return conditions


def recursively_simplify(
    expression: mat | arr | num | expr,
    conditions: list[tuple[num | expr, num | expr]] | None = None,
    limit: int | None = None,
    comprehensive: bool | None = None,
) -> mat | arr | num | expr:
    """Simplify :python:`expression` recursively using the substitutions given in :python:`conditions`.
    Runs until :python:`expression` is unchanged from the previous iteration, or until the :python:`limit` number of iterations is reached.
    If :python:`comprehensive` is :python:`False`, the algorithm uses a relatively efficient subset of simplifying operations, otherwise it uses a larger, more powerful (but slower) set.
    """
    conditions = [] if conditions is None else conditions
    limit = 2 if limit is None else limit
    comprehensive = False if comprehensive is None else comprehensive

    expressions = expression
    scalar = False
    if isinstance(expressions, mat | arr) is False:
        scalar = True
        expressions = to_matrix([expressions])

    if not (
        isinstance(expressions, arr) is True
        and issubclass(dtype(expressions), num) is True
    ):
        for index, item in np.ndenumerate(expressions):
            if isinstance(item, expr) is True:
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
                    ]
                    if comprehensive is True:
                        functions += [sp.cos, sp.exp]
                    # functions = [sp.simplify] # Simple version for testing/comparison.

                    # Generate all (sub-)permutations of the list :python:`functions`.
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
                                expression_after = function(
                                    expression_after, inverse=True
                                )
                            else:
                                expression_after = function(expression_after)
                        expression_after = expression_after.subs(conditions)

                        length_after = expression_after.count_ops()
                        if length_after < length_before:
                            expression_before = copy.deepcopy(expression_after)

                    # Do not try another iteration if no change.
                    if expression_after == expression_previous:
                        break
                    counter += 1
                    if counter >= limit:
                        break
                    expression_previous = copy.deepcopy(expression_before)
                expressions[index] = expression_before

    if scalar is True:
        expressions = expressions[0]

    return expressions


def apply_conditions(
    matrix: mat | arr,
    conditions: list[tuple[num | expr | str, num | expr | str]],
) -> mat | arr:
    """Make the substitutions as specified in :python:`conditions` to the given :python:`matrix`."""
    if isinstance(matrix, mat) is True:
        matrix.subs(conditions)
    elif issubclass(dtype(matrix), num) is False:
        for index, value in np.ndenumerate(matrix):
            try:
                matrix[index] = value.subs(conditions)
            except:
                pass
    return matrix


def extract_matrix(operator: mat | arr | QuantumObject) -> mat:
    """Extract the SymPy matrix from the :python:`operator` object."""
    try:
        matrix = operator.output()
    except:
        try:
            matrix = operator.matrix()
        except:
            matrix = operator
    if isinstance(matrix, mat) is False:
        try:
            matrix = to_matrix(matrix)
        except:
            raise ValueError(
                """A valid matrix cannot be extracted from :python:`operator`."""
            )
    return matrix


def extract_array(operator: mat | arr | QuantumObject) -> arr:
    """Extract the NumPy array from the :python:`operator` object."""
    try:
        matrix = operator.output()
    except:
        try:
            matrix = operator.matrix()
        except:
            matrix = operator
    if isinstance(matrix, arr) is False:
        try:
            matrix = to_array(matrix, numerical=False)
        except:
            raise ValueError(
                """A valid array cannot be extracted from :python:`operator`."""
            )
    return matrix


def extract_representation(operator: mat | arr | QuantumObject) -> mat | arr:
    """Extract the matrix representation from the :python:`operator` object."""
    if isinstance(operator, mat | arr) is False:
        matrix = extract_array(operator)  # Prefer NumPy arrays for performance.
    else:
        matrix = operator
    return matrix


def extract_conditions(*states) -> list[tuple[num | expr, num | expr]]:
    """Extract any substitution conditions accessible via the :python:`conditions` property from the objects in :python:`states`."""
    conditions = []
    symbols_list = []
    for state in states:
        try:
            conditions += state.conditions
            symbols_list += state.symbols_list
        except:
            pass
    symbols_list = list(set(flatten_list(symbols_list)))
    conditions = symbolize_conditions(conditions, symbols_list)
    return conditions


def extract_symbols(*states) -> list[sym]:
    """Extract any SymPy symbols accessible via the :python:`symbols` property from the objects in :python:`states`."""
    symbols = dict()
    for state in states:
        try:
            symbols |= state.symbols
        except:
            pass
    return symbols


def apply_function(
    matrix: mat | arr, function: Callable, arguments: list[Any] | None = None
) -> mat | arr:
    """Applies a function to a matrix. This is accomplished using eigendecomposition, in which the specified matrix is assumed to be normal (i.e., :python:`matrix * conjugate_transpose(matrix) = conjugate_transpose(matrix) * matrix`, which holds true for density operators)."""
    arguments = [] if arguments is None else arguments
    transformed = matrix
    if isinstance(matrix, arr) is True and dtype(matrix) is not object:
        eigenvalues, eigenvectors = np.linalg.eig(matrix)
        transformed = np.zeros(
            (len(eigenvalues), len(eigenvalues)), dtype=dtype(matrix)
        )
        for k in range(0, len(eigenvalues)):
            eigenvalue = eigenvalues[k]
            eigenvector = eigenvectors[:, k]
            try:
                coefficient = function(eigenvalue, *arguments)
            except:
                coefficient = 0
            finally:
                transformed += coefficient * to_density(eigenvector)
    else:
        eigentriple = to_matrix(matrix).eigenvects()
        transformed = sp.zeros(len(eigentriple[0][2][0]))
        for k in range(0, len(eigentriple)):
            eigenvalue = eigentriple[k][0]
            multiplicity = eigentriple[k][1]
            eigenvectors = eigentriple[k][2]
            try:
                coefficient = function(eigenvalue, *arguments)
                if function == sp.log and eigenvalue == 0:
                    coefficient = 0
            except:
                coefficient = 0
            finally:
                for n in range(0, multiplicity):
                    transformed += coefficient * to_density(eigenvectors[n])
        if isinstance(matrix, arr) is True:
            transformed = to_array(transformed, numerical=False)
    return transformed


def default_arguments(
    arguments, kwarguments, class_object, arg_pairs: list[tuple[str, Any]]
):
    """Change the default value of an argument in a subclass's constructor.
    The argument :python:`class_object` is the class whose :python:`__init__` signature is to be targeted.
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
    The argument :python:`class_object` is the class whose :python:`__init__` signature is to be targeted.
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


def tensor_product(*matrices: *tuple[mat | arr]) -> mat | arr:
    """Compute the tensor (or Kronecker) product of the items in :python:`matrices`."""
    if isinstance(matrices[0], arr) is True:
        product = np.ones(1, dtype=dtype(matrices[0]))
        for k in range(0, len(matrices)):
            product = np.kron(product, matrices[k])
    else:
        product = TensorProduct(*matrices)
    return product


def assemble_composition(*pairs: *tuple[mat | arr, list[int]]) -> mat | arr:
    """Assemble a composite state from constituent subsystems described by the items in :python:`pairs`.
    For each pair:
    - The first element is the subsystem's state matrix.
    - The second element is the list of indices of its systems."""
    pairs_sorted = sorted(pairs, key=lambda pair: min(pair[1]))
    return tensor_product(*[pair[0] for pair in pairs_sorted])


def matrix_multiplication(*matrices: *tuple[mat | arr]):
    types = list(set([type(matrix) for matrix in matrices]))
    if len(types) != 1:
        if all(issubclass(value, mat) for value in types) is False:
            raise TypeError("""The input matrices have more than one type.""")
    if isinstance(matrices[0], arr) is True:
        return np.linalg.multi_dot(matrices)
    else:
        return sp.MatMul(*matrices, evaluate=True).as_mutable()
