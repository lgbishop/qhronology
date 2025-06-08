"""
    Custom styles for the Qhronology project.
"""

from pygments.style import Style
from pygments.token import Keyword, Name, Comment, String, Error, \
     Number, Operator, Generic, Whitespace

class QhronologyLightStyle(Style):
    """
    A custom light-theme style for the Qhronology project.
    """
    name = 'qhronology-light'

    styles = {
        Whitespace:             '#bbbbbb',

        Comment:                'italic #699ADA', # #66AAF0
        # Comment.Preproc:        'noitalic #008080',
        # Comment.Special:        'noitalic bold',

        # String:                 '#9933CC',
        # String:                 '#2266C0',
        # String:                 '#A000CC',
        # String:                 '#00AAAC',
        # String:                 '#009999',
        # String:                 '#00a1bb',
        String:                 '#008A8A',
        # String.Char:            '#800080',
        String.Doc:             "#2266C0",
        # String.Interpol:        "bold #BB6688",
        # String.Escape:          "bold #BB6622",
        # String.Regex:           "#BB6688",
        # String.Symbol:          "#B8860B",
        # String.Other:           "#008000",
        Number:                 '#B10061',
        Keyword:                'bold #224499',
        # Keyword.Pseudo:         "nobold",
        # Keyword.Type:           "bold #00BB00",
        # Operator:               "#666666",
        Operator.Word:          'bold #002569',
        Name.Tag:               'bold #002569',
        Name.Attribute:         '#FF0000',
        # Name.Builtin:           "#AA22FF",
        # Name.Function:          "#00A000",
        Name.Class:             'bold #FF2550',
        Name.Namespace:         "bold #0066C0",
        # Name.Exception:         "bold #D2413A",
        # Name.Variable:          "#B8860B",
        # Name.Constant:          "#880000",
        # Name.Label:             "#A0A000",
        # Name.Entity:            "bold #999999",
        # Name.Attribute:         "#BB4444",
        # Name.Tag:               "bold #008000",
        Name.Decorator:         "italic #9933CC",

        Generic.Heading:        '#999999',
        Generic.Subheading:     '#aaaaaa',
        Generic.Deleted:        'bg:#ffdddd #000000',
        Generic.Inserted:       'bg:#ddffdd #000000',
        Generic.Error:          '#aa0000',
        Generic.Emph:           'italic',
        Generic.Strong:         'bold',
        Generic.EmphStrong:     'bold italic',
        Generic.Prompt:         'bold #0066C0',
        Generic.Output:         '#224499',
        Generic.Traceback:      '#aa0000',

        Error:                  'bg:#e3d2d2 #a61717'
    }