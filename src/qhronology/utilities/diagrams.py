# Project: Qhronology (https://github.com/lgbishop/qhronology)
# Author: lgbishop <lachlanbishop@protonmail.com>
# Copyright: Lachlan G. Bishop 2025
# License: AGPLv3 (non-commercial use), proprietary (commercial use)
# For more details, see the README in the project repository:
# https://github.com/lgbishop/qhronology,
# or visit the website:
# https://qhronology.com.

"""
Classes for the creation of diagrams of quantum states, gates, and circuits.
Not intended to be used directly by the user.
"""

# https://peps.python.org/pep-0649/
# https://peps.python.org/pep-0749/
from __future__ import annotations

import copy
from enum import StrEnum
import math
import statistics
import textwrap

import numpy as np

from qhronology.utilities.helpers import flatten_list


class Families(StrEnum):
    WIRE = "WIRE"
    PUSH = "PUSH"
    GATE = "GATE"
    LSTICK = "LSTICK"
    RSTICK = "RSTICK"
    TARG = "TARG"
    METER = "METER"
    TRACE = "TRACE"
    TERM = "TERM"
    WORMHOLE = "WORMHOLE"
    COMPOSITION = "COMPOSITION"


class Sections(StrEnum):
    INPUTS = "inputs"
    GATES = "gates"
    OUTPUTS = "outputs"


class Styles(StrEnum):
    ASCII = "ascii"
    UNICODE = "unicode"
    SHADED = "shaded"


class Connections(StrEnum):
    NONE = "none"
    CLASSICAL = "classical"
    QUANTUM = "quantum"


class Directions(StrEnum):
    UPPER = "upper"
    LOWER = "lower"
    LEFT = "left"
    RIGHT = "right"


# The central template for constructing every diagram cell.
# Each of these entries is a unique keyword string which is to be assigned a corresponding visualization character (see STYLES below).
CELL_TEMPLATE = np.array(
    [
        [
            "exterior_corner_left_upper",
            "block_connector_left_upper",
            "exterior_horizontal_left_upper",
            "wire_upper_unset",
            "exterior_horizontal_right_upper",
            "block_connector_right_upper",
            "exterior_corner_right_upper",
        ],
        [
            "exterior_vertical_left_upper",
            "edge_corner_left_upper",
            "edge_horizontal_left_upper",
            "edge_connector_upper_unset",
            "edge_horizontal_right_upper",
            "edge_corner_right_upper",
            "exterior_vertical_right_lower",
        ],
        [
            "exterior_vertical_left_upper",
            "edge_vertical_left_upper",
            "pad_corner",
            "pad_upper",
            "pad_corner",
            "edge_vertical_right_upper",
            "exterior_vertical_right_lower",
        ],
        [
            "wire_left_unset",
            "edge_connector_left_unset",
            "pad_left",
            "label",
            "pad_right",
            "edge_connector_right_unset",
            "wire_right_unset",
        ],
        [
            "exterior_vertical_left_lower",
            "edge_vertical_left_lower",
            "pad_corner",
            "pad_lower",
            "pad_corner",
            "edge_vertical_right_lower",
            "exterior_vertical_right_lower",
        ],
        [
            "exterior_vertical_left_lower",
            "edge_corner_left_lower",
            "edge_horizontal_left_lower",
            "edge_connector_lower_unset",
            "edge_horizontal_right_lower",
            "edge_corner_right_lower",
            "exterior_vertical_right_lower",
        ],
        [
            "exterior_corner_left_lower",
            "block_connector_left_lower",
            "exterior_horizontal_left_lower",
            "wire_lower_unset",
            "exterior_horizontal_right_lower",
            "block_connector_right_lower",
            "exterior_corner_right_lower",
        ],
    ],
    dtype="object",
)

# "STYLES": assign the actual text characters to each component of the template.
STYLES = {
    "GATE_SINGLE": {
        "block_connector_left_lower": {
            "ascii": "empty",
            "unicode": "empty",
            "unicode_alt": "empty",
        },
        "block_connector_left_upper": {
            "ascii": "empty",
            "unicode": "empty",
            "unicode_alt": "empty",
        },
        "block_connector_right_lower": {
            "ascii": "empty",
            "unicode": "empty",
            "unicode_alt": "empty",
        },
        "block_connector_right_upper": {
            "ascii": "empty",
            "unicode": "empty",
            "unicode_alt": "empty",
        },
        "edge_connector_left_quantum": {
            "ascii": "|",
            "unicode": "┨",
            "unicode_alt": "░",
        },
        "edge_connector_lower_quantum": {
            "ascii": "-",
            "unicode": "┯",
            "unicode_alt": "░",
        },
        "edge_connector_right_quantum": {
            "ascii": "|",
            "unicode": "┠",
            "unicode_alt": "░",
        },
        "edge_connector_upper_quantum": {
            "ascii": "-",
            "unicode": "┷",
            "unicode_alt": "░",
        },
        "edge_connector_left_classical": {
            "ascii": "|",
            "unicode": "╡",
            "unicode_alt": "░",
        },
        "edge_connector_lower_classical": {
            "ascii": "-",
            "unicode": "╥",
            "unicode_alt": "░",
        },
        "edge_connector_right_classical": {
            "ascii": "|",
            "unicode": "╞",
            "unicode_alt": "░",
        },
        "edge_connector_upper_classical": {
            "ascii": "-",
            "unicode": "╨",
            "unicode_alt": "░",
        },
        "edge_connector_left_none": {"ascii": "|", "unicode": "┃", "unicode_alt": "░"},
        "edge_connector_lower_none": {"ascii": "-", "unicode": "━", "unicode_alt": "░"},
        "edge_connector_right_none": {"ascii": "|", "unicode": "┃", "unicode_alt": "░"},
        "edge_connector_upper_none": {"ascii": "-", "unicode": "━", "unicode_alt": "░"},
        "edge_corner_left_lower": {"ascii": "+", "unicode": "┗", "unicode_alt": "░"},
        "edge_corner_left_upper": {"ascii": "+", "unicode": "┏", "unicode_alt": "░"},
        "edge_corner_right_lower": {"ascii": "+", "unicode": "┛", "unicode_alt": "░"},
        "edge_corner_right_upper": {"ascii": "+", "unicode": "┓", "unicode_alt": "░"},
        "edge_horizontal_left_lower": {
            "ascii": "-",
            "unicode": "━",
            "unicode_alt": "░",
        },
        "edge_horizontal_left_upper": {
            "ascii": "-",
            "unicode": "━",
            "unicode_alt": "░",
        },
        "edge_horizontal_right_lower": {
            "ascii": "-",
            "unicode": "━",
            "unicode_alt": "░",
        },
        "edge_horizontal_right_upper": {
            "ascii": "-",
            "unicode": "━",
            "unicode_alt": "░",
        },
        "edge_vertical_left_lower": {"ascii": "|", "unicode": "┃", "unicode_alt": "░"},
        "edge_vertical_left_upper": {"ascii": "|", "unicode": "┃", "unicode_alt": "░"},
        "edge_vertical_right_lower": {"ascii": "|", "unicode": "┃", "unicode_alt": "░"},
        "edge_vertical_right_upper": {"ascii": "|", "unicode": "┃", "unicode_alt": "░"},
        "empty": {"ascii": " ", "unicode": " ", "unicode_alt": " "},
        "exterior_horizontal_left_lower": {
            "ascii": "empty",
            "unicode": "empty",
            "unicode_alt": "empty",
        },
        "exterior_horizontal_left_upper": {
            "ascii": "empty",
            "unicode": "empty",
            "unicode_alt": "empty",
        },
        "exterior_horizontal_right_lower": {
            "ascii": "empty",
            "unicode": "empty",
            "unicode_alt": "empty",
        },
        "exterior_horizontal_right_upper": {
            "ascii": "empty",
            "unicode": "empty",
            "unicode_alt": "empty",
        },
        "exterior_vertical_left_lower": {
            "ascii": "empty",
            "unicode": "empty",
            "unicode_alt": "empty",
        },
        "exterior_vertical_left_upper": {
            "ascii": "empty",
            "unicode": "empty",
            "unicode_alt": "empty",
        },
        "exterior_vertical_right_lower": {
            "ascii": "empty",
            "unicode": "empty",
            "unicode_alt": "empty",
        },
        "exterior_vertical_right_upper": {
            "ascii": "empty",
            "unicode": "empty",
            "unicode_alt": "empty",
        },
        "exterior_corner_left_lower": {
            "ascii": "empty",
            "unicode": "empty",
            "unicode_alt": "empty",
        },
        "exterior_corner_left_upper": {
            "ascii": "empty",
            "unicode": "empty",
            "unicode_alt": "empty",
        },
        "exterior_corner_right_lower": {
            "ascii": "empty",
            "unicode": "empty",
            "unicode_alt": "empty",
        },
        "exterior_corner_right_upper": {
            "ascii": "empty",
            "unicode": "empty",
            "unicode_alt": "empty",
        },
        "label": {"ascii": "label", "unicode": "label", "unicode_alt": "label"},
        "replacement": {"ascii": "empty", "unicode": "empty", "unicode_alt": "░"},
        "pad_corner": {"ascii": "empty", "unicode": "empty", "unicode_alt": "░"},
        "pad_left": {"ascii": "empty", "unicode": "empty", "unicode_alt": "░"},
        "pad_lower": {"ascii": "empty", "unicode": "empty", "unicode_alt": "░"},
        "pad_right": {"ascii": "empty", "unicode": "empty", "unicode_alt": "░"},
        "pad_upper": {"ascii": "empty", "unicode": "empty", "unicode_alt": "░"},
        "wire_left_quantum": {"ascii": "-", "unicode": "─", "unicode_alt": "─"},
        "wire_lower_quantum": {"ascii": "|", "unicode": "│", "unicode_alt": "│"},
        "wire_right_quantum": {"ascii": "-", "unicode": "─", "unicode_alt": "─"},
        "wire_upper_quantum": {"ascii": "|", "unicode": "│", "unicode_alt": "│"},
        "wire_left_classical": {"ascii": "=", "unicode": "═", "unicode_alt": "═"},
        "wire_lower_classical": {"ascii": "#", "unicode": "║", "unicode_alt": "║"},
        "wire_right_classical": {"ascii": "=", "unicode": "═", "unicode_alt": "═"},
        "wire_upper_classical": {"ascii": "#", "unicode": "║", "unicode_alt": "║"},
        "wire_left_none": {
            "ascii": "empty",
            "unicode": "empty",
            "unicode_alt": "empty",
        },
        "wire_lower_none": {
            "ascii": "empty",
            "unicode": "empty",
            "unicode_alt": "empty",
        },
        "wire_right_none": {
            "ascii": "empty",
            "unicode": "empty",
            "unicode_alt": "empty",
        },
        "wire_upper_none": {
            "ascii": "empty",
            "unicode": "empty",
            "unicode_alt": "empty",
        },
        "edge_blend_left": {"ascii": "+", "unicode": "┣", "unicode_alt": "░"},
        "edge_blend_right": {"ascii": "+", "unicode": "┫", "unicode_alt": "░"},
    },
    "PUSH": {
        "block_connector_left_lower": {
            "ascii": "empty",
            "unicode": "empty",
            "unicode_alt": "empty",
        },
        "block_connector_left_upper": {
            "ascii": "empty",
            "unicode": "empty",
            "unicode_alt": "empty",
        },
        "block_connector_right_lower": {
            "ascii": "empty",
            "unicode": "empty",
            "unicode_alt": "empty",
        },
        "block_connector_right_upper": {
            "ascii": "empty",
            "unicode": "empty",
            "unicode_alt": "empty",
        },
        "edge_connector_left_quantum": {
            "ascii": "-",
            "unicode": "─",
            "unicode_alt": "─",
        },
        "edge_connector_lower_quantum": {
            "ascii": "|",
            "unicode": "│",
            "unicode_alt": "│",
        },
        "edge_connector_right_quantum": {
            "ascii": "-",
            "unicode": "─",
            "unicode_alt": "─",
        },
        "edge_connector_upper_quantum": {
            "ascii": "|",
            "unicode": "│",
            "unicode_alt": "│",
        },
        "edge_connector_left_classical": {
            "ascii": "=",
            "unicode": "═",
            "unicode_alt": "═",
        },
        "edge_connector_lower_classical": {
            "ascii": "#",
            "unicode": "║",
            "unicode_alt": "║",
        },
        "edge_connector_right_classical": {
            "ascii": "=",
            "unicode": "═",
            "unicode_alt": "═",
        },
        "edge_connector_upper_classical": {
            "ascii": "#",
            "unicode": "║",
            "unicode_alt": "║",
        },
        "edge_connector_left_none": {
            "ascii": "empty",
            "unicode": "empty",
            "unicode_alt": "empty",
        },
        "edge_connector_lower_none": {
            "ascii": "empty",
            "unicode": "empty",
            "unicode_alt": "empty",
        },
        "edge_connector_right_none": {
            "ascii": "empty",
            "unicode": "empty",
            "unicode_alt": "empty",
        },
        "edge_connector_upper_none": {
            "ascii": "empty",
            "unicode": "empty",
            "unicode_alt": "empty",
        },
        "edge_corner_left_lower": {
            "ascii": "empty",
            "unicode": "empty",
            "unicode_alt": "empty",
        },
        "edge_corner_left_upper": {
            "ascii": "empty",
            "unicode": "empty",
            "unicode_alt": "empty",
        },
        "edge_corner_right_lower": {
            "ascii": "empty",
            "unicode": "empty",
            "unicode_alt": "empty",
        },
        "edge_corner_right_upper": {
            "ascii": "empty",
            "unicode": "empty",
            "unicode_alt": "empty",
        },
        "edge_horizontal_left_lower": {
            "ascii": "empty",
            "unicode": "empty",
            "unicode_alt": "empty",
        },
        "edge_horizontal_left_upper": {
            "ascii": "empty",
            "unicode": "empty",
            "unicode_alt": "empty",
        },
        "edge_horizontal_right_lower": {
            "ascii": "empty",
            "unicode": "empty",
            "unicode_alt": "empty",
        },
        "edge_horizontal_right_upper": {
            "ascii": "empty",
            "unicode": "empty",
            "unicode_alt": "empty",
        },
        "edge_vertical_left_lower": {
            "ascii": "empty",
            "unicode": "empty",
            "unicode_alt": "empty",
        },
        "edge_vertical_left_upper": {
            "ascii": "empty",
            "unicode": "empty",
            "unicode_alt": "empty",
        },
        "edge_vertical_right_lower": {
            "ascii": "empty",
            "unicode": "empty",
            "unicode_alt": "empty",
        },
        "edge_vertical_right_upper": {
            "ascii": "empty",
            "unicode": "empty",
            "unicode_alt": "empty",
        },
        "empty": {"ascii": " ", "unicode": " ", "unicode_alt": " "},
        "exterior_horizontal_left_lower": {
            "ascii": "empty",
            "unicode": "empty",
            "unicode_alt": "empty",
        },
        "exterior_horizontal_left_upper": {
            "ascii": "empty",
            "unicode": "empty",
            "unicode_alt": "empty",
        },
        "exterior_horizontal_right_lower": {
            "ascii": "empty",
            "unicode": "empty",
            "unicode_alt": "empty",
        },
        "exterior_horizontal_right_upper": {
            "ascii": "empty",
            "unicode": "empty",
            "unicode_alt": "empty",
        },
        "exterior_vertical_left_lower": {
            "ascii": "empty",
            "unicode": "empty",
            "unicode_alt": "empty",
        },
        "exterior_vertical_left_upper": {
            "ascii": "empty",
            "unicode": "empty",
            "unicode_alt": "empty",
        },
        "exterior_vertical_right_lower": {
            "ascii": "empty",
            "unicode": "empty",
            "unicode_alt": "empty",
        },
        "exterior_vertical_right_upper": {
            "ascii": "empty",
            "unicode": "empty",
            "unicode_alt": "empty",
        },
        "exterior_corner_left_lower": {
            "ascii": "empty",
            "unicode": "empty",
            "unicode_alt": "empty",
        },
        "exterior_corner_left_upper": {
            "ascii": "empty",
            "unicode": "empty",
            "unicode_alt": "empty",
        },
        "exterior_corner_right_lower": {
            "ascii": "empty",
            "unicode": "empty",
            "unicode_alt": "empty",
        },
        "exterior_corner_right_upper": {
            "ascii": "empty",
            "unicode": "empty",
            "unicode_alt": "empty",
        },
        "label": {"ascii": "label", "unicode": "label", "unicode_alt": "label"},
        "replacement": {"ascii": "empty", "unicode": "empty", "unicode_alt": "empty"},
        "pad_corner": {"ascii": "empty", "unicode": "empty", "unicode_alt": "empty"},
        "pad_left": {
            "ascii": "edge_connector_left_unset",
            "unicode": "edge_connector_left_unset",
            "unicode_alt": "edge_connector_left_unset",
        },
        "pad_lower": {
            "ascii": "edge_connector_lower_unset",
            "unicode": "edge_connector_lower_unset",
            "unicode_alt": "edge_connector_lower_unset",
        },
        "pad_right": {
            "ascii": "edge_connector_right_unset",
            "unicode": "edge_connector_right_unset",
            "unicode_alt": "edge_connector_right_unset",
        },
        "pad_upper": {
            "ascii": "edge_connector_upper_unset",
            "unicode": "edge_connector_upper_unset",
            "unicode_alt": "edge_connector_upper_unset",
        },
        "wire_left_quantum": {"ascii": "-", "unicode": "─", "unicode_alt": "─"},
        "wire_lower_quantum": {"ascii": "|", "unicode": "│", "unicode_alt": "│"},
        "wire_right_quantum": {"ascii": "-", "unicode": "─", "unicode_alt": "─"},
        "wire_upper_quantum": {"ascii": "|", "unicode": "│", "unicode_alt": "│"},
        "wire_left_classical": {"ascii": "=", "unicode": "═", "unicode_alt": "═"},
        "wire_lower_classical": {"ascii": "#", "unicode": "║", "unicode_alt": "║"},
        "wire_right_classical": {"ascii": "=", "unicode": "═", "unicode_alt": "═"},
        "wire_upper_classical": {"ascii": "#", "unicode": "║", "unicode_alt": "║"},
        "wire_left_none": {
            "ascii": "empty",
            "unicode": "empty",
            "unicode_alt": "empty",
        },
        "wire_lower_none": {
            "ascii": "empty",
            "unicode": "empty",
            "unicode_alt": "empty",
        },
        "wire_right_none": {
            "ascii": "empty",
            "unicode": "empty",
            "unicode_alt": "empty",
        },
        "wire_upper_none": {
            "ascii": "empty",
            "unicode": "empty",
            "unicode_alt": "empty",
        },
    },
    "LSTICK_SINGLE": {
        "block_connector_left_lower": {
            "ascii": "empty",
            "unicode": "empty",
            "unicode_alt": "empty",
        },
        "block_connector_left_upper": {
            "ascii": "empty",
            "unicode": "empty",
            "unicode_alt": "empty",
        },
        "block_connector_right_lower": {
            "ascii": "emptyempty",
            "unicode": "emptyempty",
            "unicode_alt": "emptyempty",
        },
        "block_connector_right_upper": {
            "ascii": "emptyempty",
            "unicode": "emptyempty",
            "unicode_alt": "emptyempty",
        },
        "edge_connector_left_quantum": {
            "ascii": "empty",
            "unicode": "empty",
            "unicode_alt": "empty",
        },
        "edge_connector_lower_quantum": {
            "ascii": "empty",
            "unicode": "empty",
            "unicode_alt": "empty",
        },
        "edge_connector_right_quantum": {
            "ascii": "--",
            "unicode": "──",
            "unicode_alt": "──",
        },
        "edge_connector_upper_quantum": {
            "ascii": "empty",
            "unicode": "empty",
            "unicode_alt": "empty",
        },
        "edge_connector_left_classical": {
            "ascii": "empty",
            "unicode": "empty",
            "unicode_alt": "empty",
        },
        "edge_connector_lower_classical": {
            "ascii": "empty",
            "unicode": "empty",
            "unicode_alt": "empty",
        },
        "edge_connector_right_classical": {
            "ascii": "==",
            "unicode": "══",
            "unicode_alt": "══",
        },
        "edge_connector_upper_classical": {
            "ascii": "empty",
            "unicode": "empty",
            "unicode_alt": "empty",
        },
        "edge_connector_left_none": {
            "ascii": "empty",
            "unicode": "empty",
            "unicode_alt": "empty",
        },
        "edge_connector_lower_none": {
            "ascii": "empty",
            "unicode": "empty",
            "unicode_alt": "empty",
        },
        "edge_connector_right_none": {
            "ascii": "empty",
            "unicode": "empty",
            "unicode_alt": "empty",
        },
        "edge_connector_upper_none": {
            "ascii": "empty",
            "unicode": "empty",
            "unicode_alt": "empty",
        },
        "edge_corner_left_lower": {
            "ascii": "empty",
            "unicode": "empty",
            "unicode_alt": "empty",
        },
        "edge_corner_left_upper": {
            "ascii": "empty",
            "unicode": "empty",
            "unicode_alt": "empty",
        },
        "edge_corner_right_lower": {
            "ascii": "emptyempty",
            "unicode": "emptyempty",
            "unicode_alt": "emptyempty",
        },
        "edge_corner_right_upper": {
            "ascii": "emptyempty",
            "unicode": "emptyempty",
            "unicode_alt": "emptyempty",
        },
        "edge_horizontal_left_lower": {
            "ascii": "empty",
            "unicode": "empty",
            "unicode_alt": "empty",
        },
        "edge_horizontal_left_upper": {
            "ascii": "empty",
            "unicode": "empty",
            "unicode_alt": "empty",
        },
        "edge_horizontal_right_lower": {
            "ascii": "empty",
            "unicode": "empty",
            "unicode_alt": "empty",
        },
        "edge_horizontal_right_upper": {
            "ascii": "empty",
            "unicode": "empty",
            "unicode_alt": "empty",
        },
        "edge_vertical_left_lower": {
            "ascii": "empty",
            "unicode": "empty",
            "unicode_alt": "empty",
        },
        "edge_vertical_left_upper": {
            "ascii": "empty",
            "unicode": "empty",
            "unicode_alt": "empty",
        },
        "edge_vertical_right_lower": {
            "ascii": "emptyempty",
            "unicode": "emptyempty",
            "unicode_alt": "emptyempty",
        },
        "edge_vertical_right_upper": {
            "ascii": "emptyempty",
            "unicode": "emptyempty",
            "unicode_alt": "emptyempty",
        },
        "empty": {"ascii": " ", "unicode": " ", "unicode_alt": " "},
        "exterior_horizontal_left_lower": {
            "ascii": "empty",
            "unicode": "empty",
            "unicode_alt": "empty",
        },
        "exterior_horizontal_left_upper": {
            "ascii": "empty",
            "unicode": "empty",
            "unicode_alt": "empty",
        },
        "exterior_horizontal_right_lower": {
            "ascii": "empty",
            "unicode": "empty",
            "unicode_alt": "empty",
        },
        "exterior_horizontal_right_upper": {
            "ascii": "empty",
            "unicode": "empty",
            "unicode_alt": "empty",
        },
        "exterior_vertical_left_lower": {
            "ascii": "empty",
            "unicode": "empty",
            "unicode_alt": "empty",
        },
        "exterior_vertical_left_upper": {
            "ascii": "empty",
            "unicode": "empty",
            "unicode_alt": "empty",
        },
        "exterior_vertical_right_lower": {
            "ascii": "empty",
            "unicode": "empty",
            "unicode_alt": "empty",
        },
        "exterior_vertical_right_upper": {
            "ascii": "empty",
            "unicode": "empty",
            "unicode_alt": "empty",
        },
        "exterior_corner_left_lower": {
            "ascii": "empty",
            "unicode": "empty",
            "unicode_alt": "empty",
        },
        "exterior_corner_left_upper": {
            "ascii": "empty",
            "unicode": "empty",
            "unicode_alt": "empty",
        },
        "exterior_corner_right_lower": {
            "ascii": "empty",
            "unicode": "empty",
            "unicode_alt": "empty",
        },
        "exterior_corner_right_upper": {
            "ascii": "empty",
            "unicode": "empty",
            "unicode_alt": "empty",
        },
        "label": {"ascii": "label", "unicode": "label", "unicode_alt": "label"},
        "replacement": {"ascii": "empty", "unicode": "empty", "unicode_alt": "empty"},
        "pad_corner": {"ascii": "empty", "unicode": "empty", "unicode_alt": "empty"},
        "pad_left": {"ascii": "empty", "unicode": "empty", "unicode_alt": "empty"},
        "pad_lower": {"ascii": "empty", "unicode": "empty", "unicode_alt": "empty"},
        "pad_right": {
            "ascii": "wire_right_unset",
            "unicode": "wire_right_unset",
            "unicode_alt": "wire_right_unset",
        },
        "pad_upper": {"ascii": "empty", "unicode": "empty", "unicode_alt": "empty"},
        "wire_left_quantum": {
            "ascii": "empty",
            "unicode": "empty",
            "unicode_alt": "empty",
        },
        "wire_lower_quantum": {
            "ascii": "empty",
            "unicode": "empty",
            "unicode_alt": "empty",
        },
        "wire_right_quantum": {"ascii": "-", "unicode": "─", "unicode_alt": "─"},
        "wire_upper_quantum": {
            "ascii": "empty",
            "unicode": "empty",
            "unicode_alt": "empty",
        },
        "wire_left_classical": {
            "ascii": "empty",
            "unicode": "empty",
            "unicode_alt": "empty",
        },
        "wire_lower_classical": {
            "ascii": "empty",
            "unicode": "empty",
            "unicode_alt": "empty",
        },
        "wire_right_classical": {"ascii": "=", "unicode": "═", "unicode_alt": "═"},
        "wire_upper_classical": {
            "ascii": "empty",
            "unicode": "empty",
            "unicode_alt": "empty",
        },
        "wire_left_none": {
            "ascii": "empty",
            "unicode": "empty",
            "unicode_alt": "empty",
        },
        "wire_lower_none": {
            "ascii": "empty",
            "unicode": "empty",
            "unicode_alt": "empty",
        },
        "wire_right_none": {
            "ascii": "empty",
            "unicode": "empty",
            "unicode_alt": "empty",
        },
        "wire_upper_none": {
            "ascii": "empty",
            "unicode": "empty",
            "unicode_alt": "empty",
        },
        "label_connector": {"ascii": "empty", "unicode": "╶", "unicode_alt": "╶"},
        "bracket_connector_right_quantum": {
            "ascii": "empty",
            "unicode": "╶",
            "unicode_alt": "╶",
        },
        "bracket_connector_right_classical": {
            "ascii": "wire_right_unset",
            "unicode": "wire_right_unset",
            "unicode_alt": "wire_right_unset",
        },
        "bracket_connector_right_none": {
            "ascii": "wire_right_unset",
            "unicode": "wire_right_unset",
            "unicode_alt": "wire_right_unset",
        },
    },
    "RSTICK_SINGLE": {
        "block_connector_left_lower": {
            "ascii": "emptyempty",
            "unicode": "emptyempty",
            "unicode_alt": "emptyempty",
        },
        "block_connector_left_upper": {
            "ascii": "emptyempty",
            "unicode": "emptyempty",
            "unicode_alt": "emptyempty",
        },
        "block_connector_right_lower": {
            "ascii": "empty",
            "unicode": "empty",
            "unicode_alt": "empty",
        },
        "block_connector_right_upper": {
            "ascii": "empty",
            "unicode": "empty",
            "unicode_alt": "empty",
        },
        "edge_connector_left_quantum": {
            "ascii": "--",
            "unicode": "──",
            "unicode_alt": "──",
        },
        "edge_connector_lower_quantum": {
            "ascii": "empty",
            "unicode": "empty",
            "unicode_alt": "empty",
        },
        "edge_connector_right_quantum": {
            "ascii": "empty",
            "unicode": "empty",
            "unicode_alt": "empty",
        },
        "edge_connector_upper_quantum": {
            "ascii": "empty",
            "unicode": "empty",
            "unicode_alt": "empty",
        },
        "edge_connector_left_classical": {
            "ascii": "==",
            "unicode": "══",
            "unicode_alt": "══",
        },
        "edge_connector_lower_classical": {
            "ascii": "empty",
            "unicode": "empty",
            "unicode_alt": "empty",
        },
        "edge_connector_right_classical": {
            "ascii": "empty",
            "unicode": "empty",
            "unicode_alt": "empty",
        },
        "edge_connector_upper_classical": {
            "ascii": "empty",
            "unicode": "empty",
            "unicode_alt": "empty",
        },
        "edge_connector_left_none": {
            "ascii": "empty",
            "unicode": "empty",
            "unicode_alt": "empty",
        },
        "edge_connector_lower_none": {
            "ascii": "empty",
            "unicode": "empty",
            "unicode_alt": "empty",
        },
        "edge_connector_right_none": {
            "ascii": "empty",
            "unicode": "empty",
            "unicode_alt": "empty",
        },
        "edge_connector_upper_none": {
            "ascii": "empty",
            "unicode": "empty",
            "unicode_alt": "empty",
        },
        "edge_corner_left_lower": {
            "ascii": "emptyempty",
            "unicode": "emptyempty",
            "unicode_alt": "emptyempty",
        },
        "edge_corner_left_upper": {
            "ascii": "emptyempty",
            "unicode": "emptyempty",
            "unicode_alt": "emptyempty",
        },
        "edge_corner_right_lower": {
            "ascii": "empty",
            "unicode": "empty",
            "unicode_alt": "empty",
        },
        "edge_corner_right_upper": {
            "ascii": "empty",
            "unicode": "empty",
            "unicode_alt": "empty",
        },
        "edge_horizontal_left_lower": {
            "ascii": "empty",
            "unicode": "empty",
            "unicode_alt": "empty",
        },
        "edge_horizontal_left_upper": {
            "ascii": "empty",
            "unicode": "empty",
            "unicode_alt": "empty",
        },
        "edge_horizontal_right_lower": {
            "ascii": "empty",
            "unicode": "empty",
            "unicode_alt": "empty",
        },
        "edge_horizontal_right_upper": {
            "ascii": "empty",
            "unicode": "empty",
            "unicode_alt": "empty",
        },
        "edge_vertical_left_lower": {
            "ascii": "emptyempty",
            "unicode": "emptyempty",
            "unicode_alt": "emptyempty",
        },
        "edge_vertical_left_upper": {
            "ascii": "emptyempty",
            "unicode": "emptyempty",
            "unicode_alt": "emptyempty",
        },
        "edge_vertical_right_lower": {
            "ascii": "empty",
            "unicode": "empty",
            "unicode_alt": "empty",
        },
        "edge_vertical_right_upper": {
            "ascii": "empty",
            "unicode": "empty",
            "unicode_alt": "empty",
        },
        "empty": {"ascii": " ", "unicode": " ", "unicode_alt": " "},
        "exterior_horizontal_left_lower": {
            "ascii": "empty",
            "unicode": "empty",
            "unicode_alt": "empty",
        },
        "exterior_horizontal_left_upper": {
            "ascii": "empty",
            "unicode": "empty",
            "unicode_alt": "empty",
        },
        "exterior_horizontal_right_lower": {
            "ascii": "empty",
            "unicode": "empty",
            "unicode_alt": "empty",
        },
        "exterior_horizontal_right_upper": {
            "ascii": "empty",
            "unicode": "empty",
            "unicode_alt": "empty",
        },
        "exterior_vertical_left_lower": {
            "ascii": "empty",
            "unicode": "empty",
            "unicode_alt": "empty",
        },
        "exterior_vertical_left_upper": {
            "ascii": "empty",
            "unicode": "empty",
            "unicode_alt": "empty",
        },
        "exterior_vertical_right_lower": {
            "ascii": "empty",
            "unicode": "empty",
            "unicode_alt": "empty",
        },
        "exterior_vertical_right_upper": {
            "ascii": "empty",
            "unicode": "empty",
            "unicode_alt": "empty",
        },
        "exterior_corner_left_lower": {
            "ascii": "empty",
            "unicode": "empty",
            "unicode_alt": "empty",
        },
        "exterior_corner_left_upper": {
            "ascii": "empty",
            "unicode": "empty",
            "unicode_alt": "empty",
        },
        "exterior_corner_right_lower": {
            "ascii": "empty",
            "unicode": "empty",
            "unicode_alt": "empty",
        },
        "exterior_corner_right_upper": {
            "ascii": "empty",
            "unicode": "empty",
            "unicode_alt": "empty",
        },
        "label": {"ascii": "label", "unicode": "label", "unicode_alt": "label"},
        "replacement": {"ascii": "empty", "unicode": "empty", "unicode_alt": "empty"},
        "pad_corner": {"ascii": "empty", "unicode": "empty", "unicode_alt": "empty"},
        "pad_left": {
            "ascii": "wire_left_unset",
            "unicode": "wire_left_unset",
            "unicode_alt": "wire_left_unset",
        },
        "pad_lower": {"ascii": "empty", "unicode": "empty", "unicode_alt": "empty"},
        "pad_right": {"ascii": "empty", "unicode": "empty", "unicode_alt": "empty"},
        "pad_upper": {"ascii": "empty", "unicode": "empty", "unicode_alt": "empty"},
        "wire_left_quantum": {"ascii": "-", "unicode": "─", "unicode_alt": "─"},
        "wire_lower_quantum": {
            "ascii": "empty",
            "unicode": "empty",
            "unicode_alt": "empty",
        },
        "wire_right_quantum": {
            "ascii": "empty",
            "unicode": "empty",
            "unicode_alt": "empty",
        },
        "wire_upper_quantum": {
            "ascii": "empty",
            "unicode": "empty",
            "unicode_alt": "empty",
        },
        "wire_left_classical": {"ascii": "=", "unicode": "═", "unicode_alt": "═"},
        "wire_lower_classical": {
            "ascii": "empty",
            "unicode": "empty",
            "unicode_alt": "empty",
        },
        "wire_right_classical": {
            "ascii": "empty",
            "unicode": "empty",
            "unicode_alt": "empty",
        },
        "wire_upper_classical": {
            "ascii": "empty",
            "unicode": "empty",
            "unicode_alt": "empty",
        },
        "wire_left_none": {
            "ascii": "empty",
            "unicode": "empty",
            "unicode_alt": "empty",
        },
        "wire_lower_none": {
            "ascii": "empty",
            "unicode": "empty",
            "unicode_alt": "empty",
        },
        "wire_right_none": {
            "ascii": "empty",
            "unicode": "empty",
            "unicode_alt": "empty",
        },
        "wire_upper_none": {
            "ascii": "empty",
            "unicode": "empty",
            "unicode_alt": "empty",
        },
        "label_connector": {"ascii": "empty", "unicode": "╴", "unicode_alt": "╴"},
        "bracket_connector_left_quantum": {
            "ascii": "empty",
            "unicode": "╴",
            "unicode_alt": "╴",
        },
        "bracket_connector_left_classical": {
            "ascii": "wire_left_unset",
            "unicode": "wire_left_unset",
            "unicode_alt": "wire_left_unset",
        },
        "bracket_connector_left_none": {
            "ascii": "wire_left_unset",
            "unicode": "wire_left_unset",
            "unicode_alt": "wire_left_unset",
        },
    },
}

# Derivative styles

style_GATE_UPPER = dict(STYLES["GATE_SINGLE"])
style_GATE_UPPER["block_connector_left_lower"] = {
    "ascii": "|",
    "unicode": "┃",
    "unicode_alt": "░",
}
style_GATE_UPPER["block_connector_right_lower"] = {
    "ascii": "|",
    "unicode": "┃",
    "unicode_alt": "░",
}
style_GATE_UPPER["edge_connector_lower_quantum"] = {
    "ascii": "empty",
    "unicode": "empty",
    "unicode_alt": "░",
}
style_GATE_UPPER["edge_connector_lower_classical"] = {
    "ascii": "empty",
    "unicode": "empty",
    "unicode_alt": "░",
}
style_GATE_UPPER["edge_connector_lower_none"] = {
    "ascii": "empty",
    "unicode": "empty",
    "unicode_alt": "░",
}
style_GATE_UPPER["edge_corner_left_lower"] = {
    "ascii": "|",
    "unicode": "┃",
    "unicode_alt": "░",
}
style_GATE_UPPER["edge_corner_right_lower"] = {
    "ascii": "|",
    "unicode": "┃",
    "unicode_alt": "░",
}
style_GATE_UPPER["edge_horizontal_left_lower"] = {
    "ascii": "empty",
    "unicode": "empty",
    "unicode_alt": "░",
}
style_GATE_UPPER["edge_horizontal_right_lower"] = {
    "ascii": "empty",
    "unicode": "empty",
    "unicode_alt": "░",
}
style_GATE_UPPER["exterior_horizontal_left_lower"] = {
    "ascii": "empty",
    "unicode": "empty",
    "unicode_alt": "░",
}
style_GATE_UPPER["exterior_horizontal_right_lower"] = {
    "ascii": "empty",
    "unicode": "empty",
    "unicode_alt": "░",
}
style_GATE_UPPER["wire_lower_quantum"] = {
    "ascii": "empty",
    "unicode": "empty",
    "unicode_alt": "░",
}
style_GATE_UPPER["wire_lower_classical"] = {
    "ascii": "empty",
    "unicode": "empty",
    "unicode_alt": "░",
}
style_GATE_UPPER["wire_lower_none"] = {
    "ascii": "empty",
    "unicode": "empty",
    "unicode_alt": "░",
}
STYLES.update({"GATE_UPPER": style_GATE_UPPER})

style_GATE_MIDDLE = dict(STYLES["GATE_SINGLE"])
style_GATE_MIDDLE["block_connector_left_lower"] = {
    "ascii": "|",
    "unicode": "┃",
    "unicode_alt": "░",
}
style_GATE_MIDDLE["block_connector_right_lower"] = {
    "ascii": "|",
    "unicode": "┃",
    "unicode_alt": "░",
}
style_GATE_MIDDLE["edge_connector_lower_quantum"] = {
    "ascii": "empty",
    "unicode": "empty",
    "unicode_alt": "░",
}
style_GATE_MIDDLE["edge_connector_lower_classical"] = {
    "ascii": "empty",
    "unicode": "empty",
    "unicode_alt": "░",
}
style_GATE_MIDDLE["edge_connector_lower_none"] = {
    "ascii": "empty",
    "unicode": "empty",
    "unicode_alt": "░",
}
style_GATE_MIDDLE["edge_corner_left_lower"] = {
    "ascii": "|",
    "unicode": "┃",
    "unicode_alt": "░",
}
style_GATE_MIDDLE["edge_corner_right_lower"] = {
    "ascii": "|",
    "unicode": "┃",
    "unicode_alt": "░",
}
style_GATE_MIDDLE["edge_horizontal_left_lower"] = {
    "ascii": "empty",
    "unicode": "empty",
    "unicode_alt": "░",
}
style_GATE_MIDDLE["edge_horizontal_right_lower"] = {
    "ascii": "empty",
    "unicode": "empty",
    "unicode_alt": "░",
}
style_GATE_MIDDLE["wire_lower_quantum"] = {
    "ascii": "empty",
    "unicode": "empty",
    "unicode_alt": "░",
}
style_GATE_MIDDLE["wire_lower_classical"] = {
    "ascii": "empty",
    "unicode": "empty",
    "unicode_alt": "░",
}
style_GATE_MIDDLE["wire_lower_none"] = {
    "ascii": "empty",
    "unicode": "empty",
    "unicode_alt": "░",
}
style_GATE_MIDDLE["block_connector_left_upper"] = {
    "ascii": "|",
    "unicode": "┃",
    "unicode_alt": "░",
}
style_GATE_MIDDLE["block_connector_right_upper"] = {
    "ascii": "|",
    "unicode": "┃",
    "unicode_alt": "░",
}
style_GATE_MIDDLE["edge_connector_upper_quantum"] = {
    "ascii": "empty",
    "unicode": "empty",
    "unicode_alt": "░",
}
style_GATE_MIDDLE["edge_connector_upper_classical"] = {
    "ascii": "empty",
    "unicode": "empty",
    "unicode_alt": "░",
}
style_GATE_MIDDLE["edge_connector_upper_none"] = {
    "ascii": "empty",
    "unicode": "empty",
    "unicode_alt": "░",
}
style_GATE_MIDDLE["edge_corner_left_upper"] = {
    "ascii": "|",
    "unicode": "┃",
    "unicode_alt": "░",
}
style_GATE_MIDDLE["edge_corner_right_upper"] = {
    "ascii": "|",
    "unicode": "┃",
    "unicode_alt": "░",
}
style_GATE_MIDDLE["edge_horizontal_left_upper"] = {
    "ascii": "empty",
    "unicode": "empty",
    "unicode_alt": "░",
}
style_GATE_MIDDLE["edge_horizontal_right_upper"] = {
    "ascii": "empty",
    "unicode": "empty",
    "unicode_alt": "░",
}
style_GATE_MIDDLE["wire_upper_quantum"] = {
    "ascii": "empty",
    "unicode": "empty",
    "unicode_alt": "░",
}
style_GATE_MIDDLE["wire_upper_classical"] = {
    "ascii": "empty",
    "unicode": "empty",
    "unicode_alt": "░",
}
style_GATE_MIDDLE["wire_upper_none"] = {
    "ascii": "empty",
    "unicode": "empty",
    "unicode_alt": "░",
}
style_GATE_MIDDLE["edge_connector_left_quantum"] = {
    "ascii": "|",
    "unicode": "┨",
    "unicode_alt": "░",
}
style_GATE_MIDDLE["edge_connector_right_quantum"] = {
    "ascii": "|",
    "unicode": "┠",
    "unicode_alt": "░",
}
style_GATE_MIDDLE["edge_connector_left_classical"] = {
    "ascii": "|",
    "unicode": "╡",
    "unicode_alt": "░",
}
style_GATE_MIDDLE["edge_connector_right_classical"] = {
    "ascii": "|",
    "unicode": "╞",
    "unicode_alt": "░",
}
style_GATE_MIDDLE["edge_connector_left_none"] = {
    "ascii": "|",
    "unicode": "┃",
    "unicode_alt": "░",
}
style_GATE_MIDDLE["edge_connector_right_none"] = {
    "ascii": "|",
    "unicode": "┃",
    "unicode_alt": "░",
}
style_GATE_MIDDLE["exterior_horizontal_left_lower"] = {
    "ascii": "empty",
    "unicode": "empty",
    "unicode_alt": "░",
}
style_GATE_MIDDLE["exterior_horizontal_right_lower"] = {
    "ascii": "empty",
    "unicode": "empty",
    "unicode_alt": "░",
}
style_GATE_MIDDLE["exterior_horizontal_left_upper"] = {
    "ascii": "empty",
    "unicode": "empty",
    "unicode_alt": "░",
}
style_GATE_MIDDLE["exterior_horizontal_right_upper"] = {
    "ascii": "empty",
    "unicode": "empty",
    "unicode_alt": "░",
}
STYLES.update({"GATE_MIDDLE": style_GATE_MIDDLE})

style_GATE_LOWER = dict(STYLES["GATE_SINGLE"])
style_GATE_LOWER["block_connector_left_upper"] = {
    "ascii": "|",
    "unicode": "┃",
    "unicode_alt": "░",
}
style_GATE_LOWER["block_connector_right_upper"] = {
    "ascii": "|",
    "unicode": "┃",
    "unicode_alt": "░",
}
style_GATE_LOWER["edge_connector_upper_quantum"] = {
    "ascii": "empty",
    "unicode": "empty",
    "unicode_alt": "░",
}
style_GATE_LOWER["edge_connector_upper_classical"] = {
    "ascii": "empty",
    "unicode": "empty",
    "unicode_alt": "░",
}
style_GATE_LOWER["edge_connector_upper_none"] = {
    "ascii": "empty",
    "unicode": "empty",
    "unicode_alt": "░",
}
style_GATE_LOWER["edge_corner_left_upper"] = {
    "ascii": "|",
    "unicode": "┃",
    "unicode_alt": "░",
}
style_GATE_LOWER["edge_corner_right_upper"] = {
    "ascii": "|",
    "unicode": "┃",
    "unicode_alt": "░",
}
style_GATE_LOWER["edge_horizontal_left_upper"] = {
    "ascii": "empty",
    "unicode": "empty",
    "unicode_alt": "░",
}
style_GATE_LOWER["edge_horizontal_right_upper"] = {
    "ascii": "empty",
    "unicode": "empty",
    "unicode_alt": "░",
}
style_GATE_LOWER["exterior_horizontal_left_upper"] = {
    "ascii": "empty",
    "unicode": "empty",
    "unicode_alt": "░",
}
style_GATE_LOWER["exterior_horizontal_right_upper"] = {
    "ascii": "empty",
    "unicode": "empty",
    "unicode_alt": "░",
}
style_GATE_LOWER["wire_upper_quantum"] = {
    "ascii": "empty",
    "unicode": "empty",
    "unicode_alt": "░",
}
style_GATE_LOWER["wire_upper_classical"] = {
    "ascii": "empty",
    "unicode": "empty",
    "unicode_alt": "░",
}
style_GATE_LOWER["wire_upper_none"] = {
    "ascii": "empty",
    "unicode": "empty",
    "unicode_alt": "░",
}
STYLES.update({"GATE_LOWER": style_GATE_LOWER})

style_GATE_SINGLE = dict(STYLES["GATE_SINGLE"])
STYLES.update({"METER_SINGLE": style_GATE_SINGLE})
style_GATE_UPPER = dict(STYLES["GATE_UPPER"])
STYLES.update({"METER_UPPER": style_GATE_UPPER})
style_GATE_MIDDLE = dict(STYLES["GATE_MIDDLE"])
STYLES.update({"METER_MIDDLE": style_GATE_MIDDLE})
style_GATE_LOWER = dict(STYLES["GATE_LOWER"])
STYLES.update({"METER_LOWER": style_GATE_LOWER})

style_LSTICK_UPPER = dict(STYLES["LSTICK_SINGLE"])
style_LSTICK_UPPER["edge_connector_right_quantum"] = {
    "ascii": "{bracket_connector_right_unset",
    "unicode": "⎧bracket_connector_right_unset",
    "unicode_alt": "⎧bracket_connector_right_unset",
}
style_LSTICK_UPPER["edge_connector_right_classical"] = {
    "ascii": "{bracket_connector_right_unset",
    "unicode": "⎧bracket_connector_right_unset",
    "unicode_alt": "⎧bracket_connector_right_unset",
}
style_LSTICK_UPPER["edge_corner_right_lower"] = {
    "ascii": "| ",
    "unicode": "⎪ ",
    "unicode_alt": "⎪ ",
}
style_LSTICK_UPPER["block_connector_right_lower"] = {
    "ascii": "| ",
    "unicode": "⎪ ",
    "unicode_alt": "⎪ ",
}
style_LSTICK_UPPER["edge_vertical_right_lower"] = {
    "ascii": "| ",
    "unicode": "⎪ ",
    "unicode_alt": "⎪ ",
}
style_LSTICK_UPPER["edge_vertical_right_upper"] = {
    "ascii": "|",
    "unicode": " ",
    "unicode_alt": " ",
}
STYLES.update({"LSTICK_UPPER": style_LSTICK_UPPER})

style_LSTICK_MIDDLE = dict(STYLES["LSTICK_SINGLE"])
style_LSTICK_MIDDLE["edge_connector_right_quantum"] = {
    "ascii": "{bracket_connector_right_unset",
    "unicode": "⎨bracket_connector_right_unset",
    "unicode_alt": "⎨bracket_connector_right_unset",
}
style_LSTICK_MIDDLE["edge_connector_right_classical"] = {
    "ascii": "{bracket_connector_right_unset",
    "unicode": "⎨bracket_connector_right_unset",
    "unicode_alt": "⎨bracket_connector_right_unset",
}
style_LSTICK_MIDDLE["edge_connector_right_none"] = {
    "ascii": "|bracket_connector_right_unset",
    "unicode": "⎪bracket_connector_right_unset",
    "unicode_alt": "⎪bracket_connector_right_unset",
}
style_LSTICK_MIDDLE["edge_corner_right_lower"] = {
    "ascii": "| ",
    "unicode": "⎪ ",
    "unicode_alt": "⎪ ",
}
style_LSTICK_MIDDLE["block_connector_right_lower"] = {
    "ascii": "| ",
    "unicode": "⎪ ",
    "unicode_alt": "⎪ ",
}
style_LSTICK_MIDDLE["edge_vertical_right_lower"] = {
    "ascii": "| ",
    "unicode": "⎪ ",
    "unicode_alt": "⎪ ",
}
style_LSTICK_MIDDLE["edge_corner_right_upper"] = {
    "ascii": "| ",
    "unicode": "⎪ ",
    "unicode_alt": "⎪ ",
}
style_LSTICK_MIDDLE["block_connector_right_upper"] = {
    "ascii": "| ",
    "unicode": "⎪ ",
    "unicode_alt": "⎪ ",
}
style_LSTICK_MIDDLE["edge_vertical_right_upper"] = {
    "ascii": "| ",
    "unicode": "⎪ ",
    "unicode_alt": "⎪ ",
}
STYLES.update({"LSTICK_MIDDLE": style_LSTICK_MIDDLE})

style_LSTICK_LOWER = dict(STYLES["LSTICK_SINGLE"])
style_LSTICK_LOWER["edge_connector_right_quantum"] = {
    "ascii": "{bracket_connector_right_unset",
    "unicode": "⎩bracket_connector_right_unset",
    "unicode_alt": "⎩bracket_connector_right_unset",
}
style_LSTICK_LOWER["edge_connector_right_classical"] = {
    "ascii": "{bracket_connector_right_unset",
    "unicode": "⎩bracket_connector_right_unset",
    "unicode_alt": "⎩bracket_connector_right_unset",
}
style_LSTICK_LOWER["edge_corner_right_upper"] = {
    "ascii": "| ",
    "unicode": "⎪ ",
    "unicode_alt": "⎪ ",
}
style_LSTICK_LOWER["block_connector_right_upper"] = {
    "ascii": "| ",
    "unicode": "⎪ ",
    "unicode_alt": "⎪ ",
}
style_LSTICK_LOWER["edge_vertical_right_lower"] = {
    "ascii": "  ",
    "unicode": "  ",
    "unicode_alt": "  ",
}
style_LSTICK_LOWER["edge_vertical_right_upper"] = {
    "ascii": "| ",
    "unicode": "⎪ ",
    "unicode_alt": "⎪ ",
}
STYLES.update({"LSTICK_LOWER": style_LSTICK_LOWER})

style_RSTICK_UPPER = dict(STYLES["RSTICK_SINGLE"])
style_RSTICK_UPPER["edge_connector_left_quantum"] = {
    "ascii": "bracket_connector_left_unset}",
    "unicode": "bracket_connector_left_unset⎫",
    "unicode_alt": "bracket_connector_left_unset⎫",
}
style_RSTICK_UPPER["edge_connector_left_classical"] = {
    "ascii": "bracket_connector_left_unset}",
    "unicode": "bracket_connector_left_unset⎫",
    "unicode_alt": "bracket_connector_left_unset⎫",
}
style_RSTICK_UPPER["edge_corner_left_lower"] = {
    "ascii": " |",
    "unicode": " ⎪",
    "unicode_alt": " ⎪",
}
style_RSTICK_UPPER["block_connector_left_lower"] = {
    "ascii": " |",
    "unicode": " ⎪",
    "unicode_alt": " ⎪",
}
style_RSTICK_UPPER["edge_vertical_left_lower"] = {
    "ascii": " |",
    "unicode": " ⎪",
    "unicode_alt": " ⎪",
}
style_LSTICK_UPPER["edge_vertical_left_upper"] = {
    "ascii": "  ",
    "unicode": "  ",
    "unicode_alt": "  ",
}
STYLES.update({"RSTICK_UPPER": style_RSTICK_UPPER})

style_RSTICK_MIDDLE = dict(STYLES["RSTICK_SINGLE"])
style_RSTICK_MIDDLE["edge_connector_left_quantum"] = {
    "ascii": "bracket_connector_left_unset}",
    "unicode": "bracket_connector_left_unset⎬",
    "unicode_alt": "bracket_connector_left_unset⎬",
}
style_RSTICK_MIDDLE["edge_connector_left_classical"] = {
    "ascii": "bracket_connector_left_unset}",
    "unicode": "bracket_connector_left_unset⎬",
    "unicode_alt": "bracket_connector_left_unset⎬",
}
style_RSTICK_MIDDLE["edge_connector_left_none"] = {
    "ascii": "bracket_connector_left_unset|",
    "unicode": "bracket_connector_left_unset⎪",
    "unicode_alt": "bracket_connector_left_unset⎪",
}
style_RSTICK_MIDDLE["edge_corner_left_lower"] = {
    "ascii": " |",
    "unicode": " ⎪",
    "unicode_alt": " ⎪",
}
style_RSTICK_MIDDLE["block_connector_left_lower"] = {
    "ascii": " |",
    "unicode": " ⎪",
    "unicode_alt": " ⎪",
}
style_RSTICK_MIDDLE["edge_vertical_left_lower"] = {
    "ascii": " |",
    "unicode": " ⎪",
    "unicode_alt": " ⎪",
}
style_RSTICK_MIDDLE["edge_corner_left_upper"] = {
    "ascii": " |",
    "unicode": " ⎪",
    "unicode_alt": " ⎪",
}
style_RSTICK_MIDDLE["block_connector_left_upper"] = {
    "ascii": " |",
    "unicode": " ⎪",
    "unicode_alt": " ⎪",
}
style_RSTICK_MIDDLE["edge_vertical_left_upper"] = {
    "ascii": " |",
    "unicode": " ⎪",
    "unicode_alt": " ⎪",
}
STYLES.update({"RSTICK_MIDDLE": style_RSTICK_MIDDLE})

style_RSTICK_LOWER = dict(STYLES["RSTICK_SINGLE"])
style_RSTICK_LOWER["edge_connector_left_quantum"] = {
    "ascii": "bracket_connector_left_unset}",
    "unicode": "bracket_connector_left_unset⎭",
    "unicode_alt": "bracket_connector_left_unset⎭",
}
style_RSTICK_LOWER["edge_connector_left_classical"] = {
    "ascii": "bracket_connector_left_unset}",
    "unicode": "bracket_connector_left_unset⎭",
    "unicode_alt": "bracket_connector_left_unset⎭",
}
style_RSTICK_LOWER["edge_corner_left_upper"] = {
    "ascii": " |",
    "unicode": " ⎪",
    "unicode_alt": " ⎪",
}
style_RSTICK_LOWER["block_connector_left_upper"] = {
    "ascii": " |",
    "unicode": " ⎪",
    "unicode_alt": " ⎪",
}
style_RSTICK_LOWER["edge_vertical_left_lower"] = {
    "ascii": "  ",
    "unicode": "  ",
    "unicode_alt": "  ",
}
style_RSTICK_LOWER["edge_vertical_left_upper"] = {
    "ascii": " |",
    "unicode": " ⎪",
    "unicode_alt": " ⎪",
}
STYLES.update({"RSTICK_LOWER": style_RSTICK_LOWER})

style_TARG = dict(STYLES["PUSH"])
style_TARG["label"] = {"ascii": "@", "unicode": "⨁", "unicode_alt": "⨁"}  # ⊕, ⨁
STYLES.update({"TARG": style_TARG})

style_CTRL = dict(STYLES["PUSH"])
style_CTRL["label"] = {"ascii": "*", "unicode": "●", "unicode_alt": "●"}
STYLES.update({"CTRL": style_CTRL})

style_OCTRL = dict(STYLES["PUSH"])
style_OCTRL["label"] = {"ascii": "o", "unicode": "○", "unicode_alt": "○"}
STYLES.update({"OCTRL": style_OCTRL})

style_SWAP = dict(STYLES["PUSH"])
style_SWAP["label"] = {"ascii": "X", "unicode": "╳", "unicode_alt": "╳"}
STYLES.update({"SWAP": style_SWAP})

style_TRACE = dict(STYLES["RSTICK_SINGLE"])
style_TRACE["label_connector_left"] = {"ascii": "!", "unicode": "⏚", "unicode_alt": "⏚"}
STYLES.update({"TRACE": style_TRACE})

style_TERM = dict(STYLES["RSTICK_SINGLE"])
style_TERM["label_connector_left"] = {
    "ascii": "wire_left_unset",
    "unicode": "wire_left_unset",
    "unicode_alt": "wire_left_unset",
}
STYLES.update({"TERM": style_TERM})

style_WORMHOLE_PAST = dict(STYLES["LSTICK_SINGLE"])
style_WORMHOLE_PAST["label_connector_right"] = {
    "ascii": "<",
    "unicode": "◀",
    "unicode_alt": "◀",
}
STYLES.update({"WORMHOLE_PAST": style_WORMHOLE_PAST})

style_WORMHOLE_FUTURE = dict(STYLES["RSTICK_SINGLE"])
style_WORMHOLE_FUTURE["label_connector_left"] = {
    "ascii": ">",
    "unicode": "▶",
    "unicode_alt": "▶",
}
STYLES.update({"WORMHOLE_FUTURE": style_WORMHOLE_FUTURE})

style_WIRE_QN = dict(STYLES["PUSH"])
style_WIRE_QN["label"] = {"ascii": "-", "unicode": "─", "unicode_alt": "─"}
STYLES.update({"WIRE_QN": style_WIRE_QN})

style_WIRE_CN = dict(STYLES["PUSH"])
style_WIRE_CN["label"] = {"ascii": "=", "unicode": "═", "unicode_alt": "═"}
STYLES.update({"WIRE_CN": style_WIRE_CN})

style_WIRE_NQ = dict(STYLES["PUSH"])
style_WIRE_NQ["label"] = {"ascii": "|", "unicode": "│", "unicode_alt": "│"}
STYLES.update({"WIRE_NQ": style_WIRE_NQ})

style_WIRE_NC = dict(STYLES["PUSH"])
style_WIRE_NC["label"] = {"ascii": "#", "unicode": "║", "unicode_alt": "║"}
STYLES.update({"WIRE_NC": style_WIRE_NC})

style_WIRE_QQ = dict(STYLES["PUSH"])
style_WIRE_QQ["label"] = {"ascii": "-", "unicode": "┼", "unicode_alt": "┼"}
STYLES.update({"WIRE_QQ": style_WIRE_QQ})

style_WIRE_QC = dict(STYLES["PUSH"])
style_WIRE_QC["label"] = {"ascii": "-", "unicode": "╫", "unicode_alt": "╫"}
STYLES.update({"WIRE_QC": style_WIRE_QC})

style_WIRE_CQ = dict(STYLES["PUSH"])
style_WIRE_CQ["label"] = {"ascii": "=", "unicode": "╪", "unicode_alt": "╪"}
STYLES.update({"WIRE_CQ": style_WIRE_CQ})

style_WIRE_CC = dict(STYLES["PUSH"])
style_WIRE_CC["label"] = {"ascii": "=", "unicode": "╬", "unicode_alt": "╬"}
STYLES.update({"WIRE_CC": style_WIRE_CC})

# Useful sets for control statements
family_wide_gates = {
    "METER_SINGLE",
    "METER_UPPER",
    "METER_MIDDLE",
    "METER_LOWER",
    "GATE_SINGLE",
    "GATE_UPPER",
    "GATE_MIDDLE",
    "GATE_LOWER",
}
family_wide_sticks = {
    "LSTICK_UPPER",
    "LSTICK_MIDDLE",
    "LSTICK_LOWER",
    "RSTICK_UPPER",
    "RSTICK_MIDDLE",
    "RSTICK_LOWER",
}


def change_wire_family_horizontal(string, replacement):
    string_list = list(string)
    string_list[-2] = replacement
    return "".join(string_list)


def change_wire_family_vertical(string, replacement):
    string_list = list(string)
    string_list[-1] = replacement
    return "".join(string_list)


class VisualizationProperties:
    def __init__(
        self,
        pad: tuple[int, int] | None = None,
        sep: tuple[int, int] | None = None,
        dimensions: tuple[int, int] | None = None,
        style: str | None = None,
    ):
        pad = (0, 0) if pad is None else pad
        sep = {"upper": 1, "lower": 1, "left": 1, "right": 1} if sep is None else sep
        if isinstance(sep, tuple) is True:
            sep = {"upper": sep[1], "lower": sep[1], "left": sep[0], "right": sep[0]}
        dimensions = (0, 0) if dimensions is None else dimensions
        style = "unicode" if style is None else style

        self.pad = pad
        self.sep = sep
        self.dimensions = dimensions
        self.style = style

    @property
    def pad(self):
        return self._pad

    @pad.setter
    def pad(self, pad):
        self._pad = pad

    @property
    def sep(self):
        return self._sep

    @sep.setter
    def sep(self, sep):
        self._sep = sep

    @property
    def dimensions(self):
        return self._dimensions

    @dimensions.setter
    def dimensions(self, dimensions):
        if dimensions[0] is None:
            dimensions = list(dimensions)
            dimensions[0] = 0
            dimensions = tuple(dimensions)
        if dimensions[1] is None:
            dimensions = list(dimensions)
            dimensions[1] = 0
            dimensions = tuple(dimensions)
        self._dimensions = dimensions

    @property
    def style(self):
        return self._style

    @style.setter
    def style(self, style):
        self._style = style


class DiagramCell(VisualizationProperties):
    """A class for visualizing individual "cells" (the smallest indivisible units) of
    quantum circuit diagrams and storing their metadata."""

    def __init__(
        self,
        *args,
        family: str | None = None,
        connections: dict[str, str] | None = None,
        label: str | None = None,
        quantikz_arguments: dict[str, str] | None = None,
        **kwargs,
    ):
        super().__init__(*args, **kwargs)
        family = "GATE_SINGLE" if family is None else family
        connections = (
            {
                "upper": "none",
                "lower": "none",
                "left": "none",
                "right": "none",
            }
            if connections is None
            else connections
        )
        label = " " if label is None else label
        quantikz_arguments = (
            {"compulsory": "TODO", "optional": "TODO"}
            if quantikz_arguments is None
            else quantikz_arguments
        )

        self.family = family
        self.connections = connections
        self.label = label
        if not any(
            family in self.family
            for family in {
                "GATE",
                "METER",
                "LSTICK",
                "RSTICK",
                "WORMHOLE",
                "TRACE",
                "TERM",
            }
        ):
            self.label = " "
        self.quantikz_arguments = quantikz_arguments
        self._styles = copy.deepcopy(STYLES)

    @property
    def family(self):
        return self._family

    @family.setter
    def family(self, family):
        self._family = family

    @property
    def connections(self):
        return self._connections

    @connections.setter
    def connections(self, connections):
        self._connections = connections

    @property
    def quantikz_arguments(self):
        return self._quantikz_arguments

    @quantikz_arguments.setter
    def quantikz_arguments(self, quantikz_arguments):
        self._quantikz_arguments = quantikz_arguments

    @property
    def width(self):
        return self.dimensions[0]

    @width.setter
    def width(self, width):
        self.dimensions[0] = width

    @property
    def width_label(self):
        return math.ceil((len(self.label) - 1) / 2)

    def width_min(self, pad=None):
        pad = self.pad if pad is None else pad
        width_edge = 1
        width_min = max(0, pad[0] + self.width_label + width_edge)
        return width_min

    @property
    def height(self):
        return self.dimensions[1]

    @height.setter
    def height(self, height):
        self.dimensions[1] = height

    def height_min(self, pad=None):
        pad = self.pad if pad is None else pad
        height_edge = 1
        height_min = max(self.height, pad[1] + height_edge)
        return height_min

    def cell(
        self,
        pad: tuple[int, int] | None = None,
        sep: tuple[int, int] | None = None,
        dimensions: tuple[int, int] | None = None,
        style: str | None = None,
    ):
        pad = self.pad if pad is None else pad
        sep = self.sep if sep is None else sep
        if isinstance(sep, tuple) is True:
            sep = {"upper": sep[1], "lower": sep[1], "left": sep[0], "right": sep[0]}
        if dimensions is None:
            width = self.width
            height = self.height
        else:
            width = dimensions[0]
            height = dimensions[1]
        style = self.style if style is None else style

        width = max(width, self.width_min(pad))
        height = max(height, self.height_min(pad))

        cell = copy.deepcopy(CELL_TEMPLATE.copy())
        styles = copy.deepcopy(self._styles)

        unsets = [
            "wire_left_unset",
            "wire_lower_unset",
            "wire_right_unset",
            "wire_upper_unset",
            "edge_connector_left_unset",
            "edge_connector_lower_unset",
            "edge_connector_right_unset",
            "edge_connector_upper_unset",
            "bracket_connector_right_none",
            "bracket_connector_left_none",
        ]

        # Label padding for the *STICK family so that they are left-aligned or right-aligned.
        # This removes the small padding sticks for STICK cells which do not have a label,
        # e.g., the bottom cell (*STICK_LOWER).
        # This also connects any cells with non-empty labels to the circuit with a wire.
        label = self.label
        if "STICK" in self.family:

            # Check for empty labels. For non-labelled *STICK_* variants.
            if label.isspace() is True:

                if "LSTICK" in self.family:
                    styles[self.family]["pad_right"] = {
                        "ascii": "empty",
                        "unicode": "empty",
                        "unicode_alt": "empty",
                    }

                if "RSTICK" in self.family:
                    styles[self.family]["pad_left"] = {
                        "ascii": "empty",
                        "unicode": "empty",
                        "unicode_alt": "empty",
                    }

                styles[self.family]["label_connector"] = {
                    "ascii": "empty",
                    "unicode": "empty",
                    "unicode_alt": "empty",
                }
                styles[self.family]["label_connector"] = {
                    "ascii": "empty",
                    "unicode": "empty",
                    "unicode_alt": "empty",
                }
        if any(family in self.family for family in {"LSTICK"}) is True:
            label = label + styles[self.family]["label_connector"][style]
        if any(family in self.family for family in {"RSTICK"}) is True:
            label = styles[self.family]["label_connector"][style] + label

        if any(family in self.family for family in {"WORMHOLE_PAST"}):
            label = label + styles[self.family]["label_connector_right"][style]
        if any(
            family in self.family for family in {"WORMHOLE_FUTURE", "TRACE", "TERM"}
        ):
            label = styles[self.family]["label_connector_left"][style] + label

        # Replace label if cell should not have a label.
        if (
            any(family in self.family for family in ["GATE", "METER"])
            and self.label.isspace() is True
        ):
            styles[self.family]["label"] = {
                "ascii": "replacement",
                "unicode": "replacement",
                "unicode_alt": "replacement",
            }

        codes = list(set(flatten_list([*styles[self.family].keys()] + [unsets])))

        # Replacement of self-referencing components.
        for n in range(0, cell.shape[0]):
            for m in range(0, cell.shape[1]):
                while True:
                    cell_before = cell[n][m]
                    for code, substitution in styles[self.family].items():
                        cell[n][m] = cell[n][m].replace(code, substitution[style])
                        label = label.replace(code, substitution[style])

                    for position, kind in self.connections.items():
                        cell[n][m] = cell[n][m].replace(
                            f"wire_{position}_unset", f"wire_{position}_{kind}"
                        )
                        cell[n][m] = cell[n][m].replace(
                            f"edge_connector_{position}_unset",
                            f"edge_connector_{position}_{kind}",
                        )
                        cell[n][m] = cell[n][m].replace(
                            f"bracket_connector_{position}_unset",
                            f"bracket_connector_{position}_{kind}",
                        )
                        label = label.replace(
                            f"wire_{position}_unset", f"wire_{position}_{kind}"
                        )
                        label = label.replace(
                            f"edge_connector_{position}_unset",
                            f"edge_connector_{position}_{kind}",
                        )
                        label = label.replace(
                            f"bracket_connector_{position}_unset",
                            f"bracket_connector_{position}_{kind}",
                        )
                    cell_after = cell[n][m]
                    if cell_after == cell_before:
                        break

        for n in range(0, cell.shape[0]):
            for m in range(0, cell.shape[1]):
                for code in codes:
                    if code in styles[self.family].keys():
                        cell[n][m] = cell[n][m].replace(
                            code, styles[self.family][code][style]
                        )
                        label = label.replace(code, styles[self.family][code][style])

        # Horizontal padding
        width_label = max(self.width_label, math.ceil((len(label) - 1) / 2))
        width_desired = width
        width_total = int((cell.shape[1] - 1) / 2) - 2 + width_label + pad[0]

        if width_desired < width_total:
            width_extra = width_total - width_desired
        else:
            width_extra = width_desired - width_total

        columns = [m for m in range(0, cell.shape[1])]
        median = statistics.median(columns)
        columns[columns.index(median - 1)] = [columns[columns.index(median - 1)]] * (
            pad[0] + self.width_label + width_extra
        )
        columns = flatten_list(columns)
        columns[columns.index(median + 1)] = [columns[columns.index(median + 1)]] * (
            pad[0] + self.width_label + width_extra
        )
        columns = flatten_list(columns)
        cell = cell[0 : cell.shape[0], columns]

        # Vertical padding
        height_desired = height
        height_increase_from_label = 0
        height_total = (
            int((cell.shape[0] - 1) / 2) - 2 + height_increase_from_label + pad[1]
        )
        if height is not None:
            height_extra = height_desired - height_total
        else:
            height_extra = 0
        if height_extra < 0:
            raise ValueError(
                "The current cell cannot be as short as the specified height."
            )

        rows = [n for n in range(0, cell.shape[0])]
        median = statistics.median(rows)
        rows[rows.index(median - 1)] = [rows[rows.index(median - 1)]] * (
            pad[1] + height_extra
        )
        rows = flatten_list(rows)
        rows[rows.index(median + 1)] = [rows[rows.index(median + 1)]] * (
            pad[1] + height_extra
        )
        rows = flatten_list(rows)
        cell = cell[rows, 0 : cell.shape[1]]

        # Adjust width
        trim_left = math.ceil((len(label) - 1) / 2)
        trim_right = math.floor((len(label) - 1) / 2)
        if (
            any(
                family in self.family
                for family in {"RSTICK", "TRACE", "TERM", "WORMHOLE_FUTURE"}
            )
            is True
        ):
            trim_left = math.floor((len(label) - 1) / 2)
            trim_right = math.ceil((len(label) - 1) / 2)
        middle_row = int((cell.shape[0] - 1) / 2)
        middle_column = int((cell.shape[1] - 1) / 2)
        for k in range(1, trim_left + 1):
            cell[middle_row][middle_column - k] = ""
        for k in range(1, trim_right + 1):
            cell[middle_row][middle_column + k] = ""

        # Insert label
        for n in range(0, cell.shape[0]):
            for m in range(0, cell.shape[1]):
                cell[n][m] = cell[n][m].replace("label", label)

        # Separations
        for position, length in sep.items():
            if position == "upper":
                rows = [n for n in range(0, cell.shape[0])]
                rows[rows.index(min(rows))] = [rows[rows.index(min(rows))]] * length
                rows = flatten_list(rows)
                cell = cell[rows, 0 : cell.shape[1]]
            elif position == "lower":
                rows = [n for n in range(0, cell.shape[0])]
                rows[rows.index(max(rows))] = [rows[rows.index(max(rows))]] * length
                rows = flatten_list(rows)
                cell = cell[rows, 0 : cell.shape[1]]
            elif position == "left":
                columns = [m for m in range(0, cell.shape[1])]
                columns[columns.index(min(columns))] = [
                    columns[columns.index(min(columns))]
                ] * length
                columns = flatten_list(columns)
                cell = cell[0 : cell.shape[0], columns]
            elif position == "right":
                columns = [m for m in range(0, cell.shape[1])]
                columns[columns.index(max(columns))] = [
                    columns[columns.index(max(columns))]
                ] * length
                columns = flatten_list(columns)
                cell = cell[0 : cell.shape[0], columns]

        return cell

    def visualize(self, **kwargs):
        cell = self.cell(**kwargs)
        visualization = "\n".join(["".join(row) for row in cell])
        visualization = textwrap.dedent(visualization)
        print(visualization)


class DiagramColumn(VisualizationProperties):
    """A class for assembling a collection of ``DiagramCell`` instances into a column."""

    def __init__(
        self, *args, cells: list[DiagramCell], section: str | None = None, **kwargs
    ):
        super().__init__(*args, **kwargs)
        section = Sections.GATES.value if section is None else section
        self.cells = cells
        self.section = section

    @property
    def section(self):
        return self._section

    @section.setter
    def section(self, section):
        self._section = section

    @property
    def cells(self):
        return self._cells

    @cells.setter
    def cells(self, cells):
        self._cells = cells

    @property
    def family(self):
        family = Families.COMPOSITION.value
        for archetype in family:
            family_truths = list(
                set(
                    [
                        (True if archetype in cell.family else False)
                        for cell in self.cells
                    ]
                )
            )
            if len(family_truths) == 1 and family_truths[0] is True:
                family = archetype
        return family

    @property
    def width(self):
        width = 0
        if self.dimensions[0] is not None:
            width = self.dimensions[0]
        return width

    @width.setter
    def width(self, width):
        self.dimensions[0] = width

    def width_min(self, pad=None):
        pad = self.pad if pad is None else pad
        widths = []
        for cell in self.cells:
            widths.append(cell.width_min(pad))
        width_min = max(flatten_list([widths, self.width]))
        return width_min

    @property
    def height(self):
        height = 0
        if self.dimensions[1] is not None:
            height = self.dimensions[1]
        return height

    @height.setter
    def height(self, height):
        self.dimensions[1] = height

    def height_min(self, pad=None):
        pad = self.pad if pad is None else pad
        heights = []
        for cell in self.cells:
            heights.append(cell.height_min(pad))
        height_min = max(flatten_list([heights, self.height]))
        return height_min

    def column(
        self,
        pad: tuple[int, int] | None = None,
        sep: tuple[int, int] | None = None,
        dimensions: tuple[int, int] | None = None,
        style: str | None = None,
        sep_collapse: bool = True,
        sep_trim: dict[str, bool] | None = None,
    ):
        pad = self.pad if pad is None else pad
        sep = self.sep if sep is None else sep
        if isinstance(sep, tuple) is True:
            sep = {"upper": sep[1], "lower": sep[1], "left": sep[0], "right": sep[0]}
        dimensions = self.dimensions if dimensions is None else dimensions
        style = self.style if style is None else style
        sep_trim_default = {
            "upper": False,
            "lower": False,
            "left": False,
            "right": False,
        }
        sep_trim = copy.deepcopy(sep_trim_default) if sep_trim is None else sep_trim
        for position, value in sep_trim_default.items():
            if position not in sep_trim:
                sep_trim[position] = value

        column = []
        # Determine width of column from its individual cells.
        width = 0
        label_width_max = 0
        for cell in self.cells:
            pad_cell = copy.deepcopy(pad)
            pad_cell = cell.pad if pad_cell is None else pad_cell
            width_total = cell.width_label
            width = max(
                width,
                dimensions[0],
                self.width_min(pad_cell),
                cell.width_min(),
                width_total,
            )
            height = dimensions[1]

            label_width_max = max(label_width_max, len(cell.label))

        for k, cell in enumerate(self.cells):

            # Pad label with spaces on relevant side.
            if self.section == Sections.INPUTS.value:
                cell.label = f"{cell.label:{' '}>{label_width_max}}"
            if self.section == Sections.OUTPUTS.value:
                cell.label = f"{cell.label:{' '}<{label_width_max}}"

            pad_cell = copy.deepcopy(pad)
            if pad_cell is None or pad_cell is False:
                pad_cell = cell.pad

            sep_cell = copy.deepcopy(sep)
            if sep is None or sep is False:
                sep_cell = cell.sep

            if sep_collapse is True and k != 0:
                sep_cell["upper"] = 0

            if k == 0 and sep_trim["upper"] is True:
                sep_cell["upper"] = 0
            if k == len(self.cells) - 1 and sep_trim["lower"] is True:
                sep_cell["lower"] = 0
            if sep_trim["left"] is True:
                sep_cell["left"] = 0
            if sep_trim["right"] is True:
                sep_cell["right"] = 0

            style_cell = style
            if style is None or style is False:
                style_cell = cell.style

            cell_string_array = cell.cell(
                pad=pad_cell, sep=sep_cell, dimensions=(width, height), style=style_cell
            )
            column.append(cell_string_array)

        column = np.vstack(tuple(column))

        return column

    def visualize(self, return_string: bool | None = None, **kwargs):

        column = self.column(**kwargs)

        visualization = "\n".join(["".join(row) for row in column])
        visualization = textwrap.dedent(visualization)
        if return_string is True:
            return visualization
        else:
            print(visualization)

    def diagram(
        self,
        sep: tuple[int, int] | None = None,
        return_string: bool | None = None,
        **kwargs,
    ):
        if isinstance(sep, tuple) is True:
            sep = {"upper": sep[1], "lower": sep[1], "left": sep[0], "right": sep[0]}
        return_string = False if return_string is None else return_string
        return self.visualize(sep=sep, return_string=return_string, **kwargs)


class DiagramCircuit(VisualizationProperties):
    """A class for assembling ``DiagramColumn`` instances together into a grid."""

    def __init__(self, *args, columns: list, **kwargs):
        super().__init__(*args, **kwargs)
        self.columns = columns

    @property
    def columns(self):
        return self._columns

    @columns.setter
    def columns(self, columns):
        self._columns = columns

    @property
    def num_columns(self):
        return len(self.columns)

    @property
    def num_rows(self):
        num_rows = []
        for column in self.columns:
            num_rows.append(len(column.cells))
        num_rows = list(set(num_rows))
        if len(num_rows) != 1:
            raise ValueError("The provided columns have an unequal number of rows.")
        return num_rows[0]

    def height_min(self, row_num):
        heights = []
        for column in self.columns:
            heights.append(column.height_min())
        return max(heights)

    def width_min(self, column_num):
        return self.columns[column_num].width_min()

    @property
    def cells(self):
        cells = [[] for k in range(0, self.num_columns)]
        for index, column in enumerate(self.columns):
            for cell in column.cells:
                cells[index].append(cell)
        return cells

    def grid(
        self,
        pad: tuple[int, int] | None = None,
        sep: tuple[int, int] | None = None,
        dimensions: tuple[int, int] | None = None,
        style: str | None = None,
        uniform_spacing: bool | None = None,
        force_separation: bool | None = None,
    ):
        pad = self.pad if pad is None else pad
        sep = self.sep if sep is None else sep
        if isinstance(sep, tuple) is True:
            sep = {"upper": sep[1], "lower": sep[1], "left": sep[0], "right": sep[0]}
        dimensions = self.dimensions if dimensions is None else dimensions
        style = self.style if style is None else style
        uniform_spacing = False if uniform_spacing is None else uniform_spacing
        force_separation = False if force_separation is None else force_separation

        # Set wire types.
        for index_column, column in enumerate(self.cells):
            for index_row, cell in enumerate(column):
                if (
                    index_column > 0
                    and self.cells[index_column - 1][index_row].connections["right"]
                    == "classical"
                ):
                    self.cells[index_column][index_row].connections[
                        "left"
                    ] = "classical"
                    if "WIRE" in self.cells[index_column][index_row].family:
                        old_wire_family = self.cells[index_column][index_row].family
                        new_wire_family = change_wire_family_horizontal(
                            old_wire_family, "C"
                        )
                        self.cells[index_column][index_row].family = new_wire_family
                    self.cells[index_column][index_row].connections[
                        "right"
                    ] = "classical"

        grid = [[] for k in range(0, self.num_columns)]

        # Determine width of columns from their individual cells.
        width = 0
        height = 0
        label_widths_max = []
        for index_column, column in enumerate(self.cells):
            label_width_max = 0
            for index_row, cell in enumerate(column):
                pad_cell = copy.deepcopy(pad)
                pad_cell = cell.pad if pad_cell is None else pad_cell
                height = max(
                    height,
                    dimensions[1],
                    self.height_min(index_row),
                    self.columns[index_column].height_min(pad_cell),
                    cell.height_min(),
                )
                label_width_max = max(label_width_max, len(cell.label))
            label_widths_max.append(label_width_max)

        # Pad label with spaces on relevant side.
        for index, column in enumerate(self.columns):
            if column.section == Sections.INPUTS.value:
                for cell in column.cells:
                    cell.label = f"{cell.label:{' '}>{label_widths_max[index]}}"
            if column.section == Sections.OUTPUTS.value:
                for cell in column.cells:
                    cell.label = f"{cell.label:{' '}<{label_widths_max[index]}}"

        for index_column, column in enumerate(self.cells):
            for index_row, cell in enumerate(column):
                pad_cell = copy.deepcopy(pad)

                if pad_cell is None or pad_cell is False:
                    pad_cell = cell.pad
                width = max(
                    0,
                    dimensions[0],
                    self.width_min(index_column),
                    self.columns[index_column].width_min(pad_cell),
                    cell.width_min(),
                )

                sep_cell = copy.deepcopy(sep)
                if sep_cell is None or sep_cell is False:
                    sep_cell = cell.sep

                if sep_cell["lower"] == sep_cell["upper"]:
                    sep_cell["upper"] = math.ceil((sep_cell["upper"] - 1) / 2)
                    sep_cell["lower"] = math.floor((sep_cell["lower"] - 1) / 2)

                column_family_previous = []
                column_family_next = []
                if len(self.columns) > 1:
                    column_family_previous = [
                        cell.family for cell in self.columns[index_column - 1].cells
                    ]
                    if index_column == 0:
                        column_family_previous = [
                            "PUSH" for cell in self.columns[index_column - 1].cells
                        ]
                column_family_current = [
                    cell.family for cell in self.columns[index_column].cells
                ]

                pad_cell_original = pad_cell[0]
                if self.columns[index_column].section == Sections.INPUTS.value:
                    sep_cell["right"] += pad_cell[0] + 1
                    pad_cell = list(pad_cell)
                    pad_cell[0] = 1
                    pad_cell = tuple(pad_cell)
                if self.columns[index_column].section == Sections.OUTPUTS.value:
                    sep_cell["left"] += pad_cell[0] + 1
                    pad_cell = list(pad_cell)
                    pad_cell[0] = 1
                    pad_cell = tuple(pad_cell)

                style_cell = copy.deepcopy(style)
                if style is None or style is False:
                    style_cell = cell.style

                cell_string_array = cell.cell(
                    pad=pad_cell,
                    sep=sep_cell,
                    dimensions=(width, height),
                    style=style_cell,
                )

                cell_family_previous = (
                    self.columns[index_column].cells[index_row - 1].family
                )

                if (
                    len(self.columns[index_column].cells) != 1
                    and sep["lower"] == sep["upper"]
                ):
                    if "STICK" not in cell.family or "WORMHOLE" not in cell.family:
                        if "LOWER" not in cell.family or "SINGLE" not in cell.family:
                            if index_row + 1 != self.num_rows:
                                if index_row == 0:
                                    if (
                                        "LOWER" not in cell.family
                                        and "SINGLE" not in cell.family
                                    ):
                                        cell_string_array = np.delete(
                                            cell_string_array, (-1), axis=0
                                        )
                                else:
                                    if (
                                        "LOWER" not in cell.family
                                        and "SINGLE" not in cell.family
                                    ):
                                        cell_string_array = np.delete(
                                            cell_string_array, (-1), axis=0
                                        )
                                    if (
                                        "LOWER" in cell_family_previous
                                        or "SINGLE" in cell_family_previous
                                    ):
                                        cell_string_array = np.delete(
                                            cell_string_array, (0), axis=0
                                        )
                            else:
                                if (
                                    "LOWER" in cell_family_previous
                                    or "SINGLE" in cell_family_previous
                                ):
                                    cell_string_array = np.delete(
                                        cell_string_array, (0), axis=0
                                    )
                    else:
                        if index_row + 1 != self.num_rows:
                            cell_string_array = np.delete(
                                cell_string_array, (-1), axis=0
                            )

                # Split array entries up in cases of multi-character strings.
                cell_string_array = np.array(
                    [
                        [char for string in row for char in string]
                        for row in cell_string_array
                    ]
                )

                # Trimming
                trim_left = 0
                trim_right = 0

                if index_column != max(range(0, self.num_columns)):
                    column_family_next = [
                        cell.family for cell in self.columns[index_column + 1].cells
                    ]

                # Account for the padding difference between singlemode and multimode LSTICKs and RSTICK.
                if self.columns[index_column].section == Sections.INPUTS.value:
                    if (
                        any(
                            family in family_wide_sticks
                            for family in column_family_current
                        )
                        is False
                    ):
                        trim_right += 3
                if self.columns[index_column].section == Sections.OUTPUTS.value:
                    if (
                        any(
                            family in family_wide_sticks
                            for family in column_family_current
                        )
                        is False
                    ):
                        trim_left += 3

                # Trim extra spacing to the left of the inputs and to the right of the outputs.
                if self.columns[index_column].section == Sections.INPUTS.value:
                    trim_left += sep["left"] + max(1, pad_cell_original - 1)
                if self.columns[index_column].section == Sections.OUTPUTS.value:
                    trim_right += sep["right"] + max(2, pad_cell_original - 1) - 1

                # Make spacing equal to horizontal separation (not double).
                if self.columns[index_column].section == Sections.GATES.value:
                    if index_column != min(range(0, self.num_columns)):
                        trim_left += math.ceil(sep["left"] / 2)
                    if index_column != max(range(0, self.num_columns)):
                        trim_right += math.floor(sep["right"] / 2)

                # Trim inputs and outputs when no gates
                if self.columns[index_column].section == Sections.INPUTS.value:
                    if (
                        index_column != max(range(0, self.num_columns))
                        and self.columns[index_column + 1].section
                        == Sections.OUTPUTS.value
                    ):
                        trim_right += math.ceil((sep["right"] + 1) / 2) + math.ceil(
                            (pad_cell_original) / 2
                        )
                if self.columns[index_column].section == Sections.OUTPUTS.value:
                    if (
                        index_column != min(range(0, self.num_columns))
                        and self.columns[index_column - 1].section
                        == Sections.INPUTS.value
                    ):
                        trim_left += (
                            math.floor((sep["left"] + 1) / 2)
                            + 1
                            + math.floor((pad_cell_original) / 2)
                        )

                # Trim the spacing between the end gates if either has a neighbouring *STICK.
                if self.columns[index_column].section == Sections.GATES.value:
                    if (
                        index_column != min(range(0, self.num_columns))
                        and self.columns[index_column - 1].section
                        == Sections.INPUTS.value
                    ):
                        trim_left += math.ceil((sep["left"] + 1) / 2) - 1
                    if (
                        index_column != max(range(0, self.num_columns))
                        and self.columns[index_column + 1].section
                        == Sections.OUTPUTS.value
                    ):
                        trim_right += math.floor((sep["right"] + 1) / 2)

                # ``force_separation`` argument
                if force_separation is True:
                    uniform_spacing = True
                    if self.columns[index_column].section == Sections.GATES.value:
                        if (
                            any(
                                family in family_wide_gates
                                for family in column_family_current
                            )
                            is False
                        ):
                            # +1 accounts for edge of block gate:
                            trim_left += pad_cell[0] + 1
                            trim_right += pad_cell[0] + 1
                    if self.columns[index_column].section == Sections.INPUTS.value:
                        trim_right += pad_cell_original + 1
                        if (
                            index_column != max(range(0, self.num_columns))
                            and self.columns[index_column + 1].section
                            == Sections.OUTPUTS.value
                        ):
                            trim_right -= pad_cell_original + 1
                    if self.columns[index_column].section == Sections.OUTPUTS.value:
                        trim_left += pad_cell_original + 1
                        if (
                            index_column != min(range(0, self.num_columns))
                            and self.columns[index_column - 1].section
                            == Sections.INPUTS.value
                        ):
                            trim_left -= pad_cell_original + 1
                        else:
                            if (
                                any(
                                    family in family_wide_gates
                                    for family in column_family_current
                                )
                                is False
                            ):
                                trim_left += max(pad_cell_original - 2, 0)

                else:
                    if (
                        self.columns[index_column].section == Sections.GATES.value
                        and any(
                            family in family_wide_gates
                            for family in column_family_current
                        )
                        is False
                    ):
                        if (
                            index_column != max(range(0, self.num_columns))
                            and self.columns[index_column + 1].section
                            == Sections.OUTPUTS.value
                        ):
                            trim_right += 1

                if uniform_spacing is False:
                    if (
                        self.columns[index_column].section == Sections.GATES.value
                        and len(self.columns) > 1
                    ):
                        if (
                            any(
                                family in family_wide_gates
                                for family in column_family_current
                            )
                            is False
                            and any(
                                family in family_wide_gates
                                for family in column_family_next
                            )
                            is False
                        ):
                            trim_right += math.floor(pad_cell[0] / 2)
                        if (
                            any(
                                family in family_wide_gates
                                for family in column_family_previous
                            )
                            is False
                            and any(
                                family in family_wide_gates
                                for family in column_family_current
                            )
                            is False
                        ):
                            # +1 accounts for edge of block gate:
                            trim_left += math.ceil(pad_cell[0] / 2) + 1

                for k in range(0, trim_left):
                    cell_string_array = np.delete(cell_string_array, (0), axis=1)
                for k in range(0, trim_right):
                    cell_string_array = np.delete(cell_string_array, (-1), axis=1)

                grid[index_column].append(cell_string_array)

        columns = []
        for k in range(0, self.num_columns):
            columns.append(np.vstack(tuple(grid[k])))

        grid = np.hstack(tuple(columns))

        styles = copy.deepcopy(STYLES)

        # Blending and other hacky fixes
        # (Ideally should be fixed properly elsewhere in future).
        if style != "ascii":  # Blending not needed for ASCII
            blend_targets_left = {
                styles["GATE_SINGLE"]["edge_connector_left_classical"][style],
                styles["GATE_SINGLE"]["edge_connector_left_quantum"][style],
                styles["GATE_SINGLE"]["edge_connector_left_none"][style],
                styles["GATE_SINGLE"]["edge_vertical_left_upper"][style],
            }
            blend_targets_right = {
                styles["GATE_SINGLE"]["edge_connector_right_classical"][style],
                styles["GATE_SINGLE"]["edge_connector_right_quantum"][style],
                styles["GATE_SINGLE"]["edge_connector_right_none"][style],
                styles["GATE_SINGLE"]["edge_vertical_right_upper"][style],
            }
            for n in range(0, grid.shape[0]):
                for m in range(0, grid.shape[1]):
                    # Vertically separated block gates together if they are overlapping
                    if (
                        grid[n, m]
                        == styles["GATE_SINGLE"]["edge_corner_left_lower"][style]
                        and n + 1 != grid.shape[0]
                    ):
                        if grid[n + 1, m] in blend_targets_left:
                            grid[n, m] = styles["GATE_SINGLE"]["edge_blend_left"][style]
                    if (
                        grid[n, m]
                        == styles["GATE_SINGLE"]["edge_corner_right_lower"][style]
                        and n + 1 != grid.shape[0]
                    ):
                        if grid[n + 1, m] in blend_targets_right:
                            grid[n, m] = styles["GATE_SINGLE"]["edge_blend_right"][
                                style
                            ]

                    # LSTICK and RSTICK smoothing when no label
                    if (
                        grid[n, m]
                        == styles["LSTICK_MIDDLE"]["edge_connector_right_quantum"][
                            style
                        ][0]
                        or grid[n, m]
                        == styles["LSTICK_MIDDLE"]["edge_connector_right_classical"][
                            style
                        ][0]
                    ):
                        if m - 1 >= 0 and grid[n, m - 1] == " ":
                            grid[n, m] = styles["LSTICK_MIDDLE"][
                                "edge_connector_right_none"
                            ][style][0]
                    if (
                        grid[n, m]
                        == styles["RSTICK_MIDDLE"]["edge_connector_left_quantum"][
                            style
                        ][-1]
                        or grid[n, m]
                        == styles["RSTICK_MIDDLE"]["edge_connector_left_classical"][
                            style
                        ][-1]
                    ):
                        if m + 1 <= grid.shape[1] and grid[n, m + 1] == " ":
                            grid[n, m] = styles["RSTICK_MIDDLE"][
                                "edge_connector_left_none"
                            ][style][-1]

        return grid

    def visualize(self, return_string: bool | None = None, **kwargs):
        return_string = False if return_string is None else return_string

        grid = self.grid(**kwargs)

        # Trim empty rows at top and bottom of the entire grid.
        while grid.shape[0] > 0 and np.all(len(set(grid[0])) == 1 and grid[0] == " "):
            grid = grid[1:]
        while grid.shape[0] > 0 and np.all(len(set(grid[-1])) == 1 and grid[-1] == " "):
            grid = grid[:-1]

        visualization = "\n".join(["".join(row) for row in grid])
        visualization = textwrap.dedent(visualization)
        if return_string is True:
            return visualization
        else:
            print(visualization)

    def diagram(self, sep: tuple[int, int], **kwargs):
        if isinstance(sep, tuple) is True:
            sep = {"upper": sep[1], "lower": sep[1], "left": sep[0], "right": sep[0]}
        return self.visualize(sep=sep, **kwargs)


def partition_systems(systems, boundaries):
    systems = list(set(systems))
    boundaries = list(set(boundaries))
    partitions = []
    boundaries[-1] = max(max(systems), max(boundaries))
    boundaries.sort()
    for n in boundaries:
        remaining = list(systems)
        current = []
        for m in remaining:
            if m <= n:
                current.append(m)
                systems.remove(m)
        current.sort()
        partitions.append(current)

    return partitions


def assign_family(family, systems, targets, controls, anticontrols, boundaries):
    systems_occupied = list(set(targets + controls + anticontrols))
    partitions = partition_systems(systems, boundaries)
    family_list = [None for k in systems]
    family = flatten_list([family])

    for k, partition in enumerate(partitions):
        partition_occupied = list(set(partition) & set(systems_occupied))
        partition_targets = list(set(partition) & set(targets))
        partitions_controls = list(set(partition) & set(controls))
        partitions_anticontrols = list(set(partition) & set(anticontrols))
        for n in partition:
            if n in partition_targets:
                if family[k] in {"GATE", "METER"}:
                    if (
                        n - 1 not in partition_targets
                        and n + 1 not in partition_targets
                    ):
                        family_list[n] = family[k] + "_SINGLE"
                    elif n - 1 not in partition_targets and n + 1 in partition_targets:
                        family_list[n] = family[k] + "_UPPER"
                    elif n - 1 in partition_targets and n + 1 not in partition_targets:
                        family_list[n] = family[k] + "_LOWER"
                    else:
                        family_list[n] = family[k] + "_MIDDLE"
                elif family[k] in {"LSTICK", "RSTICK"}:
                    if len(partition_targets) == 1:
                        family_list[n] = family[k] + "_SINGLE"
                    elif n == min(partition_targets):
                        family_list[n] = family[k] + "_UPPER"
                    elif n == max(partition_targets):
                        family_list[n] = family[k] + "_LOWER"
                    else:
                        family_list[n] = family[k] + "_MIDDLE"
                else:
                    family_list[n] = family[k]
            elif n in partitions_controls:
                family_list[n] = "CTRL"
            elif n in partitions_anticontrols:
                family_list[n] = "OCTRL"
            else:
                family_list[n] = "WIRE_QN"
            if (
                n in range(min(partition_occupied), max(partition_occupied) + 1)
                and n not in partition_occupied
            ):
                family_list[n] = "WIRE_QQ"

    return family_list


def assign_connections(systems, targets, controls, anticontrols, boundaries):
    systems_occupied = list(set(targets + controls + anticontrols))
    partitions = partition_systems(systems, boundaries)
    connections_list = [
        {"upper": "none", "lower": "none", "left": "quantum", "right": "quantum"}
        for k in systems
    ]

    for k, partition in enumerate(partitions):
        partition_occupied = list(set(partition) & set(systems_occupied))
        for n in partition:
            if n in range(min(partition_occupied), max(partition_occupied) + 1):
                if n != min(partition_occupied):
                    connections_list[n]["upper"] = "quantum"
                if n != max(partition_occupied):
                    connections_list[n]["lower"] = "quantum"

    return connections_list


class VisualizationMixin:
    """A mixin for endowing classes derived from the base class
    :py:class:`~qhronology.utilities.objects.QuantumObject` the ability to be visualized as
    quantum circuit diagram elements."""

    def diagram_column(
        self,
        pad: tuple[int, int] | None = None,
        sep: tuple[int, int] | None = None,
        style: str | None = None,
    ) -> DiagramColumn:
        label_list = [None for k in self.systems]
        sep_list = [sep for k in self.systems]
        style_list = [style for k in self.systems]
        family = flatten_list([self.family])
        labels = flatten_list([self.labels])
        family = flatten_list(
            [
                x
                for _, x in sorted(
                    zip(self.boundaries, family), key=lambda pair: pair[0]
                )
            ]
        )
        labels = flatten_list(
            [
                x
                for _, x in sorted(
                    zip(self.boundaries, labels), key=lambda pair: pair[0]
                )
            ]
        )

        family_list = assign_family(
            family=family,
            systems=self.systems,
            targets=self.targets,
            controls=self.controls,
            anticontrols=self.anticontrols,
            boundaries=self.boundaries,
        )

        connections_list = assign_connections(
            systems=self.systems,
            targets=self.targets,
            controls=self.controls,
            anticontrols=self.anticontrols,
            boundaries=self.boundaries,
        )

        for k, connections in enumerate(connections_list):
            if "METER" in family and k in self.targets:
                connections_list[k]["right"] = "classical"

        partitions = partition_systems(self.systems, self.boundaries)
        for k, partition in enumerate(partitions):
            partition_targets = list(set(partition) & set(self.targets))
            partition_target_middle_index = math.floor((len(partition_targets) - 1) / 2)
            label_list[partition_targets[partition_target_middle_index]] = labels[k]

        cells_list = []
        for k in self.systems:
            cells_list.append(
                DiagramCell(
                    family=family_list[k],
                    connections=connections_list[k],
                    label=label_list[k],
                    quantikz_arguments={"compulsory": "TODO", "optional": "TODO"},
                    pad=pad,
                    sep=sep_list[k],
                    dimensions=None,
                    style=style_list[k],
                )
            )
        return DiagramColumn(cells=cells_list)

    def diagram(
        self,
        pad: tuple[int, int] | None = None,
        sep: tuple[int, int] | None = None,
        style: str | None = None,
        return_string: bool | None = None,
    ) -> None | str:
        """Print or return a string diagram of the quantum object as a multiline string.

        Arguments
        ---------
        pad : tuple[int, int]
            A two-tuple describing the horizontal and vertical interior paddings between the content
            at the centre of the object (e.g., its label) and its outer edge (e.g., block border).
            Both integers must be non-negative.
            Defaults to ``(0, 0)``.
        sep : tuple[int, int]
            A two-tuple describing the horizontal and vertical exterior separation distances
            at the object's edges.
            Both integers must be non-negative.
            Defaults to ``(1, 1)``.
        style : str
            A string specifying the style for the circuit visualization to take.
            Can be any of ``"ascii"``, ``"unicode"``, or ``"unicode_alt"``.
            Defaults to ``"unicode"``.
        return_string : bool
            Whether to return the assembled diagram as a multiline string.
            Defaults to ``False``.

        Returns
        -------
        None
            Returned only if ``return_string`` is ``False``.
        str
            The rendered circuit diagram. Returned only if ``return_string`` is ``True``.

        Note
        ----
        The quality of the visualization depends greatly on the output's configuration.
        For best results, the terminal should have a monospace font with good Unicode coverage.

        """
        pad = (1, 0) if pad is None else pad
        sep = (1, 1) if sep is None else sep
        style = "unicode" if style is None else style
        return_string = False if return_string is None else return_string

        uniform_spacing = False
        force_separation = True

        section = Sections.GATES.value
        if "STICK" in self.family:
            section = Sections.INPUTS.value
        pad_sections = {Sections.INPUTS.value: (2, 0), Sections.GATES.value: (0, 0)}
        cells = [*self.diagram_column(pad=pad, sep=sep, style=style).cells]
        column = DiagramColumn(
            cells=flatten_list(cells), pad=pad_sections[section], section=section
        )

        grid = DiagramCircuit(columns=flatten_list([column]))
        grid.diagram(
            pad=pad,
            sep=sep,
            style=style,
            uniform_spacing=uniform_spacing,
            force_separation=force_separation,
            return_string=return_string,
        )
