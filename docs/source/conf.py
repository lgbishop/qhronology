# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys

sys.path.append(os.path.relpath("."))
sys.path.insert(0, os.path.abspath("../../src"))  # Source code dir relative to conf.py.

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Qhronology"
copyright = "2025 Lachlan G. Bishop"
author = "Lachlan G. Bishop"
version = "1"
release = "1.0.0"
html_title = "Qhronology"
html_last_updated_fmt = "%b %d, %Y"
language = "en"
root_doc = "index"
latex_doc = "index_latex"
today_fmt = "%b %d, %Y"
today = "June 2025"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# extensions = []
extensions = [  # "sphinx_sitemap",
    # "sphinx_immaterial",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.doctest",
    # "autoapi.extension",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    #'sphinx.ext.extlinks',
    #'sphinx.ext.intersphinx',
    # "sphinx_favicon",
    # "myst_parser",
    "sphinx_design",
    "sphinx_copybutton",
    "sphinx_togglebutton",
    "sphinx.ext.mathjax",
    "sphinxcontrib.bibtex",
]
# "sphinxcontrib.katex",
#'sphinx_toolbox.latex',]
#'sphinx.ext.napoleon']
#'sphinx.ext.linkcode']

include_patterns = [
    "index.rst",
    "index_latex.rst",
    "README.rst",
    "mathematics.rst",
    "text/**.rst",
    "art/output/**.png",
    "figures/output/**",
    "examples/**.py",
]

exclude_patterns = [
    "_build",
    "Thumbs.db",
    ".DS_Store",
    "**appendix.rst",
    "**chapter-*.rst",
    # "figures/**",
    "**.pdf",
    "fonts**",
    "**es5",
]

templates_path = ["_templates"]

default_role = "py:obj"

maximum_signature_line_length = 10

add_module_names = False
autodoc_preserve_defaults = False

napoleon_google_docstring = False
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = False
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = False
napoleon_use_admonition_for_notes = False
napoleon_use_admonition_for_references = False
napoleon_use_ivar = False
napoleon_use_param = True
napoleon_use_rtype = False
napoleon_preprocess_types = False
napoleon_type_aliases = None
napoleon_attr_annotations = True

autosummary_generate = True  # Enable sphinx.ext.autosummary.

doctest_global_setup = """
import sys
sys.path.append('../../src')
from qhronology.quantum.states import *
from qhronology.quantum.gates import *
from qhronology.quantum.circuits import *
from qhronology.quantum.prescriptions import *
from qhronology.mechanics.matrices import *
from qhronology.mechanics.quantities import *
from qhronology.mechanics.operations import *
from qhronology.utilities.classification import *
from qhronology.utilities.helpers import *
from qhronology.utilities.objects import *
from qhronology.utilities.diagrams import *
from qhronology.utilities.symbolics import *
"""
doctest_show_successes = False

# autoapi_type = 'python'
# autoapi_dirs = ['../../package/qhronology']
# autoapi_generate_api_docs = False

viewcode_follow_imported_members = True
viewcode_enable_epub = False
viewcode_line_numbers = False

bibtex_bibfiles = ["references.bib"]
bibtex_reference_style = "label"
bibtex_tooltips = True

# bibtex_cite_id = "cite-{key}"
bibtex_cite_id = "cite-{bibliography_count}-{key}"
bibtex_footcite_id = "footcite-{key}"
bibtex_bibliography_id = "bibliography-{bibliography_count}"
bibtex_footbibliography_id = "footbibliography-{footbibliography_count}"

# bibtex_bibliography_header = ".. rubric:: References"
# bibtex_footbibliography_header = bibtex_bibliography_header

import pybtex.plugin
from pybtex_style_format_phys import PhysStyle

pybtex.plugin.register_plugin("pybtex.style.formatting", "phys", PhysStyle)
bibtex_default_style = "phys"

numfig = True
numfig_format = {
    "code-block": "Listing %s",
    "figure": "Figure %s",
    "section": "Section %s",
    "table": "Table %s",
}
numfig_secnum_depth = 1

pygments_style = "pygments_style.QhronologyLightStyle"

# pygments_style = "borland" # https://pygments.org/styles/
source_suffix = {
    ".rst": "restructuredtext",
    ".txt": "restructuredtext",
    # ".md": "markdown",
}

# rst_prolog = """
# .. |psf| replace:: Python Software Foundation
# """
# rst_epilog = """
# .. |psf| replace:: Python Software Foundation
# """

math_eqref_format = "({number})"
math_number_all = True
math_numfig = True
math_numsep = "."

nitpicky = True
nitpick_ignore = [
    ("py:class", "num"),
    ("py:class", "sym"),
    ("py:class", "mat"),
    ("py:class", "arr"),
    ("py:class", "numbers.Number"),
    ("py:class", "numpy.generic"),
    ("py:class", "sympy.core.basic.Basic"),
    ("py:class", "sympy.matrices.expressions.matexpr.MatrixSymbol"),
    ("py:class", "sympy.matrices.expressions.matexpr.MatrixElement"),
    ("py:class", "sympy.core.symbol.Symbol"),
    ("py:class", "sympy.matrices.dense.MutableDenseMatrix"),
    ("py:class", "numpy.ndarray"),
]

# nitpick_ignore = {
#     ('py:func', 'int'),
#     ('envvar', 'LD_LIBRARY_PATH'),
# }

# Relative to _static.
mathjax_path = "./js/MathJax/es5/tex-chtml.js"
# mathjax_path = "./js/MathJax/tex-mml-chtml.js"

sys.path.append(os.path.relpath("./preamble/"))
from macros_mathjax import mathjax3_config

latex_engine = "pdflatex"
latex_additional_files = ["./preamble/header.tex.txt", "./preamble/macros.tex.txt"]
latex_elements = {
    "papersize": "a4paper",
    "pointsize": "10pt",
    # "pxunit": "0.5bp",
    "figure_align": "H",
    #     'fontpkg': r"""
    # \setmainfont{DejaVu Serif}
    # \setsansfont{DejaVu Sans}
    # \setmonofont{DejaVu Sans Mono}
    # """,
    "maketitle": r"""\newcommand\sphinxbackoftitlepage{

\vspace*{\fill}

\emph{Qhronology}: A Python package for resolving quantum time-travel paradoxes and performing general quantum information processing \& computation.

\textcopyright\enspace 2025 Lachlan G. Bishop

First published in June 2025 as version 1.0.0

Latest documentation PDF version available online:

\texttt{\url{https://github.com/lgbishop/qhronology/blob/latest/docs/_build/latex/Qhronology.pdf}}

Official website:

\texttt{\url{https://qhronology.com}}

Source code available online:

\texttt{\url{https://github.com/lgbishop/qhronology}}

\vspace*{0.2cm}
\hrulefill
\vspace*{0.4cm}

This documentation, including its text and images, is published under the \texttt{CC BY-NC-ND 4.0} license. In accordance with this license, you are free to share (copy and redistribute) the material in any medium or format under the following terms:

\begin{description}
    \item[Attribution] -- You must give appropriate credit, provide a link to the license, and indicate if changes were made. You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or your use.
    \item[NonCommercial] -- You may not use the material for commercial purposes.
    \item[NoDerivatives] -- If you remix, transform, or build upon the material, you may not distribute the modified material.
    \item[No additional restrictions] -- You may not apply legal terms or technological measures that legally restrict others from doing anything the license permits.
\end{description}

For more information, see:

\texttt{\url{https://creativecommons.org/licenses/by-nc-nd/4.0/}}

Read the full license here:

\texttt{\url{https://github.com/lgbishop/qhronology/blob/latest/licenses/CC-BY-NC-ND-4.0.txt}}

}\sphinxmaketitle""",
    "fontenc": r"\usepackage[LGR,T1]{fontenc}",
    "preamble": r"""
\input{header.tex.txt}
\input{macros.tex.txt}

\setcounter{tocdepth}{1}

% \definecolor{accentcolor}{HTML}{224499}
% \definecolor{accentcolor}{HTML}{005AAA}
\definecolor{accentcolor}{HTML}{2266C0}

\hypersetup{
    unicode = true,
    colorlinks = true,
    linkcolor = accentcolor,
    anchorcolor = accentcolor,
    citecolor = accentcolor,
    filecolor = accentcolor,
    menucolor = accentcolor,
    runcolor = accentcolor,
    urlcolor = accentcolor,
}

% \renewcommand{\mathbb}[1]{\mathbb{#1}}
% % \renewcommand{\mathbb}{\mathds}

\pdfimageresolution=128 % Controls the scaling of images. https://github.com/sphinx-doc/sphinx/issues/8253

%%% FONTS:

% \usepackage{tocloft}
% \renewcommand\sphinxtableofcontentshook{}
% \renewcommand{\cftpartfont}{\sffamily\bfseries}
% \renewcommand{\cftchapfont}{\sffamily\bfseries}
% \renewcommand{\cftsecfont}{\rmfamily}
% \renewcommand{\cftsubsecfont}{\rmfamily}

% \renewcommand{\cftpartpagefont}{\rmfamily\bfseries}
% \renewcommand{\cftchappagefont}{\rmfamily\bfseries}
% \renewcommand{\cftsecpagefont}{\rmfamily}
% \renewcommand{\cftsubsecpagefont}{\rmfamily}

% \usepackage[%
%     protrusion=true,
%     expansion=true,
%     spacing=true,
%     tracking=true,
%     kerning=true
% ]{microtype}
% \usepackage{libertinus}

% sffamily (headings)
\usepackage{ClearSans}
%\usepackage[medium]{inter}
%\usepackage{roboto}
%\usepackage{sourcesanspro}

% rmfamily (main text)
\usepackage{mlmodern}

% ttfamily (code, monospace, verbatim)
\usepackage[scaled=0.85]{sourcecodepro}
%\usepackage[scaled=0.85,lining]{FiraMono}
%\usepackage[scaled=0.85]{beramono}
%\usepackage{ascii}

% Make normal (medium) series semi-bold instead for the loaded ttfamily.
\DeclareFontSeriesDefault[tt]{md}{sb}

%%% Fixes for pdflatex being unable to compile when the included code snippets (e.g., the usage examples) contain non-ascii characters (i.e., Greek letters).

\DeclareUnicodeCharacter{0391}{$\Alpha$}
\DeclareUnicodeCharacter{0392}{$\Beta$}
\DeclareUnicodeCharacter{0393}{$\Gamma$}
\DeclareUnicodeCharacter{0394}{$\Delta$}
\DeclareUnicodeCharacter{0395}{$\Epsilon$}
\DeclareUnicodeCharacter{0396}{$\Zeta$}
\DeclareUnicodeCharacter{0397}{$\Eta$}
\DeclareUnicodeCharacter{0398}{$\Theta$}
\DeclareUnicodeCharacter{0399}{$\Iota$}
\DeclareUnicodeCharacter{039A}{$\Kappa$}
\DeclareUnicodeCharacter{039B}{$\Lambda$}
\DeclareUnicodeCharacter{039C}{$\Mu$}
\DeclareUnicodeCharacter{039D}{$\Nu$}
\DeclareUnicodeCharacter{039E}{$\Xi$}
\DeclareUnicodeCharacter{039F}{$\Omicron$}
\DeclareUnicodeCharacter{03A0}{$\Pi$}
\DeclareUnicodeCharacter{03A1}{$\Rho$}
\DeclareUnicodeCharacter{03A3}{$\Sigma$}
\DeclareUnicodeCharacter{03A4}{$\Tau$}
\DeclareUnicodeCharacter{03A5}{$\Upsilon$}
\DeclareUnicodeCharacter{03A6}{$\Phi$}
\DeclareUnicodeCharacter{03A7}{$\Chi$}
\DeclareUnicodeCharacter{03A8}{$\Psi$}
\DeclareUnicodeCharacter{03A9}{$\Omega$}

\DeclareUnicodeCharacter{03B1}{$\alpha$}
\DeclareUnicodeCharacter{03B2}{$\beta$}
\DeclareUnicodeCharacter{03B3}{$\gamma$}
\DeclareUnicodeCharacter{03B4}{$\delta$}
\DeclareUnicodeCharacter{03B5}{$\epsilon$}
\DeclareUnicodeCharacter{03B6}{$\zeta$}
\DeclareUnicodeCharacter{03B7}{$\eta$}
\DeclareUnicodeCharacter{03B8}{$\theta$}
\DeclareUnicodeCharacter{03B9}{$\iota$}
\DeclareUnicodeCharacter{03BA}{$\kappa$}
\DeclareUnicodeCharacter{03BB}{$\lambda$}
\DeclareUnicodeCharacter{03BC}{$\mu$}
\DeclareUnicodeCharacter{03BD}{$\nu$}
\DeclareUnicodeCharacter{03BE}{$\xi$}
\DeclareUnicodeCharacter{03BF}{$\omicron$}
\DeclareUnicodeCharacter{03C0}{$\pi$}
\DeclareUnicodeCharacter{03C1}{$\rho$}
\DeclareUnicodeCharacter{03C2}{$\varsigma$}
\DeclareUnicodeCharacter{03C3}{$\sigma$}
\DeclareUnicodeCharacter{03C4}{$\tau$}
\DeclareUnicodeCharacter{03C5}{$\upsilon$}
\DeclareUnicodeCharacter{03C6}{$\phi$}
\DeclareUnicodeCharacter{03C7}{$\chi$}
\DeclareUnicodeCharacter{03C8}{$\psi$}
\DeclareUnicodeCharacter{03C9}{$\omega$}

\DeclareUnicodeCharacter{03B8}{$\theta$}
\DeclareUnicodeCharacter{03D1}{$\vartheta$}
\DeclareUnicodeCharacter{03D5}{$\phi$}
\DeclareUnicodeCharacter{03D6}{$\varpi$}
\DeclareUnicodeCharacter{03F0}{$\varkappa$}
\DeclareUnicodeCharacter{03F1}{$\varrho$}
\DeclareUnicodeCharacter{03F4}{$\varphi$}
\DeclareUnicodeCharacter{03F5}{$\varpi$}
\DeclareUnicodeCharacter{03F6}{$\varsigma$}
\DeclareUnicodeCharacter{03F7}{$\vartheta$}
\DeclareUnicodeCharacter{03F9}{$\varsigma$}
\DeclareUnicodeCharacter{03FA}{$\vartheta$}
\DeclareUnicodeCharacter{03FB}{$\vartheta$}
\DeclareUnicodeCharacter{03FC}{$\vartheta$}
\DeclareUnicodeCharacter{03FD}{$\vartheta$}
\DeclareUnicodeCharacter{03FE}{$\vartheta$}
\DeclareUnicodeCharacter{03FF}{$\vartheta$}

\DeclareUnicodeCharacter{1F10}{$\alpha$}
\DeclareUnicodeCharacter{1F11}{$\beta$}
\DeclareUnicodeCharacter{1F12}{$\gamma$}
\DeclareUnicodeCharacter{1F13}{$\delta$}
\DeclareUnicodeCharacter{1F14}{$\epsilon$}
\DeclareUnicodeCharacter{1F15}{$\zeta$}
\DeclareUnicodeCharacter{1F16}{$\eta$}
\DeclareUnicodeCharacter{1F17}{$\theta$}
\DeclareUnicodeCharacter{1F18}{$\iota$}
\DeclareUnicodeCharacter{1F19}{$\kappa$}
\DeclareUnicodeCharacter{1F1A}{$\lambda$}
\DeclareUnicodeCharacter{1F1B}{$\mu$}
\DeclareUnicodeCharacter{1F1C}{$\nu$}
\DeclareUnicodeCharacter{1F1D}{$\xi$}
\DeclareUnicodeCharacter{1F1E}{$\omicron$}
\DeclareUnicodeCharacter{1F1F}{$\pi$}
\DeclareUnicodeCharacter{1F20}{$\rho$}
\DeclareUnicodeCharacter{1F21}{$\varsigma$}
\DeclareUnicodeCharacter{1F22}{$\sigma$}
\DeclareUnicodeCharacter{1F23}{$\tau$}
\DeclareUnicodeCharacter{1F24}{$\upsilon$}
\DeclareUnicodeCharacter{1F25}{$\phi$}
\DeclareUnicodeCharacter{1F26}{$\chi$}
\DeclareUnicodeCharacter{1F27}{$\psi$}
\DeclareUnicodeCharacter{1F28}{$\omega$}
\DeclareUnicodeCharacter{1F29}{$\vartheta$}
\DeclareUnicodeCharacter{1F2A}{$\varkappa$}
\DeclareUnicodeCharacter{1F2B}{$\varrho$}
\DeclareUnicodeCharacter{1F2C}{$\varsigma$}
\DeclareUnicodeCharacter{1F2D}{$\varphi$}
\DeclareUnicodeCharacter{1F2E}{$\varpi$}
\DeclareUnicodeCharacter{1F2F}{$\vartheta$}

\DeclareUnicodeCharacter{2295}{$\oplus$}
\DeclareUnicodeCharacter{2296}{$\ominus$}
\DeclareUnicodeCharacter{2297}{$\otimes$}
\DeclareUnicodeCharacter{221A}{$\surd$}

% \usepackage{titlesec}
\titleclass{\part}{top}
\titleformat{\part}[display]{\Huge\sffamily\bfseries\centering}{\partname~\thepart}{0pt}{#1}
\titlespacing*{\part}{0pt}{48pt}{48pt}

\usepackage{calc}
\fboxsep7pt
\definecolor{fontcolor}{HTML}{003989}
% \definecolor{fontcolor}{HTML}{002569}
\titleformat{\chapter}[hang]
{\filcenter}
{\raisebox{-3pt}[0pt][0pt]{%
  \colorbox{fontcolor}{%
    \parbox[b][][b]{\widthof{\LARGE\sffamily\MakeUppercase{\chaptername}} * \real{0.8}}{%
      \color{white}\filcenter\large\sffamily\bfseries\MakeUppercase{\chaptername}\\%
      \fontsize{48pt}{48pt}\selectfont\thechapter\vspace{4pt}}%\enspace%
    }%
  }%
}
{0pt}
{\huge\sffamily\bfseries%\vrule width 1pt height 72pt depth 0pt \enspace%
 \parbox[b][][b]{\textwidth-\widthof{\LARGE\sffamily\MakeUppercase{\chaptername}\enspace} * \real{0.85}}{\filleft \hspace{12pt} $\qquad$ #1}%
}[{\color{fontcolor}\titlerule[2.5pt]}]
\titlespacing*{\chapter}{0pt}{20pt}{12pt}

\titleformat{\section}
{\sffamily\Large\bfseries}{\thesection}{1em}{#1}
\titleformat{\subsection}
{\sffamily\large\bfseries}{\thesubsection}{1em}{#1}
\titleformat{\subsubsection}
{\sffamily\large\bfseries}{\thesubsubsection}{1em}{#1}
\titleformat{\paragraph}[runin]
{\sffamily\large\bfseries}{\theparagraph}{1em}{#1}
\titleformat{\subparagraph}[runin]
{\sffamily\large\bfseries}{\thesubparagraph}{1em}{#1}

\titlespacing*{\section}{0pt}{16pt}{10pt}
\titlespacing*{\subsection}{0pt}{12pt}{8pt}
\titlespacing*{\subsubsection}{0pt}{12pt}{8pt}
\titlespacing*{\paragraph}{0pt}{12pt}{8pt}
\titlespacing*{\subparagraph}{0pt}{12pt}{8pt}

% \renewcommand{\theparagraph}{\S\arabic{paragraph}}
\setcounter{secnumdepth}{4}

\definecolor{header}{RGB}{100,100,100}
\definecolor{bg}{RGB}{0,0,255}
\definecolor{frame}{RGB}{100,100,100}

\usepackage[skins,breakable]{tcolorbox}
\usepackage{adjustbox}

\let\startsig\pysigstartsignatures
\renewcommand{\pysigstartsignatures}{\startsig\fontsize{11}{12}\selectfont\ttfamily}

\let\stopsig\pysigstopsignatures
\renewcommand{\pysigstopsignatures}{\stopsig\normalsize\rmfamily}

\let\lineitem\sphinxlineitem
\renewcommand{\sphinxlineitem}[1]{\lineitem{\textsf{#1}}}

\let\paramitem\sphinxparam
\renewcommand{\sphinxparam}[1]{\paramitem{\texttt{#1}}}

%\let\paramcomma\sphinxparamcomma
%\renewcommand{\sphinxparamcomma}{\paramcomma\newline}

%\let\siglinewithargsret\pysiglinewithargsret
%\renewcommand{\pysiglinewithargsret}[3]{\siglinewithargsret{\textcolor{fontcolor}{#1}}{#2}{\linebreak\texttt{\textcolor{fontcolor}{\bfseries #3}}}}

\let\siglinewithargsret\pysiglinewithargsret
\renewcommand{\pysiglinewithargsret}[3]{\siglinewithargsret{\textcolor{fontcolor}{#1}}{#2}{\texttt{\textcolor{fontcolor}{\bfseries #3}}}}

% \definecolor{color_defaults}{HTML}{BA00EE}
\definecolor{color_defaults}{HTML}{699ADA}
\definecolor{color_keywords}{HTML}{224499}
\definecolor{color_names}{HTML}{002569}
\definecolor{color_operators}{HTML}{000000}
\definecolor{color_punctuation}{HTML}{000000}
\definecolor{color_standard}{HTML}{003989}
\definecolor{color_whitespace}{HTML}{00FF00}
%\definecolor{color_code}{HTML}{224499}
\definecolor{color_code}{HTML}{005AAA}
%\definecolor{color_code}{HTML}{006FD0}
\definecolor{color_bfcode}{HTML}{000000}
% \definecolor{color_arguments}{HTML}{B10061}
\definecolor{color_arguments}{HTML}{224499}
\definecolor{color_types}{HTML}{699ADA}

\usepackage{ifthen}
\makeatletter
\renewcommand*{\DUrole}[2]{%
  \ifcsname DUrole\detokenize{#1}\endcsname
    \csname DUrole\detokenize{#1}\endcsname{#2}%
  \else% backwards compatibility: try \docutilsrole#1{#2}
    \ifcsname docutilsrole\detokenize{#1}\endcsname
      \csname docutilsrole\detokenize{#1}\endcsname{#2}%
    \else% Define colors based on the role
      \ifthenelse{\equal{#1}{default_value}}{\textcolor{color_defaults}{#2}}{% defaults
      \ifthenelse{\equal{#1}{k}}{\textit{\textcolor{color_keywords}{#2}}}{% keywords
      \ifthenelse{\equal{#1}{n}}{\textcolor{color_names}{#2}}{% names
      \ifthenelse{\equal{#1}{o}}{\textcolor{color_operators}{#2}}{% operators
      \ifthenelse{\equal{#1}{p}}{\textcolor{color_punctuation}{#2}}{% punctuation
      \ifthenelse{\equal{#1}{std}}{\textcolor{color_standard}{#2}}{% standard text
      \ifthenelse{\equal{#1}{w}}{#2}{% whitespace
      \textcolor{black}{#2}}}}}}}}% Default color if #1 doesn't match any case
    \fi
  \fi
}
\makeatother

% {\sphinxcode{\sphinxupquote{QuantumState.}}\sphinxbfcode{\sphinxupquote{output}}}

\let\newsphinxcode\sphinxcode
\renewcommand{\sphinxcode}[1]{\newsphinxcode{\textcolor{color_code}{#1}}}

\let\newsphinxbfcode\sphinxbfcode
\renewcommand{\sphinxbfcode}[1]{\newsphinxbfcode{\textcolor{color_bfcode}{#1}}}

\let\newsphinxstyleliteralemphasis\sphinxstyleliteralemphasis
\renewcommand{\sphinxstyleliteralemphasis}[1]{\newsphinxstyleliteralemphasis{\textcolor{color_types}{#1}}}

\let\newsphinxstyleliteralstrong\sphinxstyleliteralstrong
\renewcommand{\sphinxstyleliteralstrong}[1]{\newsphinxstyleliteralstrong{\textcolor{color_arguments}{#1}}}

\setlength{\sphinxsignaturelistskip}{0cm}

\makeatletter
\renewenvironment{sphinxnote}[1]
  {\def\spx@noticetype{note}\begin{sphinxheavybox}\sphinxremovefinalcolon{\sphinxstylenotetitle{\textsf{#1}}}}
  {\end{sphinxheavybox}}
\makeatother

\makeatletter
\def\hrulefillthick{{\color{fontcolor}\leavevmode\leaders\hrule height 0.85pt\hfill\kern\z@}}
\def\hrulefillinvisible{{\color{white}\leavevmode\leaders\hrule height 0.85pt\hfill\kern\z@}}
\makeatother

\usepackage[bottom]{footmisc}

% \setlist[itemize]{leftmargin=0.5cm}

\renewcommand{\labelitemi}{\footnotesize{$\blacktriangleright$}}
\renewcommand{\labelitemii}{\footnotesize{$\bullet$}}
\renewcommand{\labelitemiii}{\footnotesize{$\vartriangleright$}}
\renewcommand{\labelitemiv}{\footnotesize{$\circ$}}

""",
    "passoptionstopackages": r"""
\PassOptionsToPackage{final}{hyperref}
\PassOptionsToPackage{explicit}{titlesec}
""",
    # \PassOptionsToPackage{footskip=0.75cm}{geometry}
    "sphinxsetup": "TitleColor=black, \
    div.note_border-radius=0px, \
    pre_border-radius=0px, \
    noteBorderColor={HTML}{2266C0}, \
    div.note_title-foreground-TeXcolor={HTML}{2266C0}, \
    div.note_title-background-TeXcolor={HTML}{DCE7FC}, \
    verbatimvisiblespace=\\textcolor{color_types}{\\textvisiblespace}, \
    verbatimcontinued=\\makebox[2\\fontcharwd\\font`\\x][r]{\\textcolor{color_types}{\\tiny$\\hookrightarrow$}}",
    "fncychap": r"",
    # "printindex": r'\footnotesize\raggedright\printindex',
}
latex_show_urls = "footnote"
latex_show_pagerefs = True

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "pydata_sphinx_theme"
# html_theme = "sphinx_immaterial"
html_static_path = ["_static"]
html_css_files = [
    "css/custom.css",
    "fonts/ClearSans/ClearSans.css",
    "fonts/DejaVuSansMono/DejaVuSansMono.css",
    "fonts/JuliaMono/JuliaMono.css",
    "fonts/Roboto/Roboto.css",
    "fonts/SourceCodePro/SourceCodePro.css",
    "fonts/SourceSans3/SourceSans3.css",
]
html_js_files = ["backgrounds/three.min.js"]

# html_logo = 'logo-text-bold.svg'
html_theme_options = {
    "logo": {
        # "text": "Qhronology documentation",
        "alt_text": "Qhronology documentation - home",
        "image_light": "./art/output/logo-text-bold-light.svg",
        "image_dark": "./art/output/logo-text-bold-dark.svg",
    },
    # "announcement": "Here's a <a href='https://pydata.org'>PyData Announcement!</a>", # Accepts local HTML.
    # "show_version_warning_banner": False,
    "navbar_start": ["navbar-logo"],
    "navbar_center": ["navbar-nav"],
    "navbar_end": ["search-field", "navbar-icon-links"],
    "navbar_persistent": ["theme-switcher"],
    "navbar_align": "content",
    # "external_links": [ # Appear on the navigation bar.
    #     {"name": "link-one-name", "url": "https://<link-one>"},
    #     {"name": "link-two-name", "url": "https://<link-two>"}
    # ],
    "header_links_before_dropdown": 6,
    "icon_links": [
        {
            "name": "Git Repository",
            "url": "https://github.com/lgbishop/qhronology",
            # "icon": "fa-solid fa-code",
            "icon": "fa-brands fa-square-github",
            "type": "fontawesome",
        },
        {
            "name": "PDF Documentation",
            "url": "https://raw.githubusercontent.com/lgbishop/qhronology/latest/docs/_build/latex/Qhronology.pdf",
            "icon": "fa-regular fa-file-pdf",
            # "icon": "fa-solid fa-file-pdf",
            "type": "fontawesome",
        },
    ],
    "icon_links_label": "Quick Links",  # For screen readers?
    "primary_sidebar_end": [],  # "indices.html"
    "secondary_sidebar_items": {
        "**": ["page-toc"],  # "edit-this-page", "sourcelink"
        f"{root_doc}": [],
        "text/theory/part-theory": [],
        "text/documentation/part-documentation": [],
        "text/examples/part-examples": [],
        "text/theory/part-live": [],
        "text/theory/part-appendix": [],
    },
    "use_edit_page_button": False,  # Enables/disables the "edit-this-page" item in the secondary sidebar.
    "article_footer_items": [
        # "breadcrumbs",
        # "copyright",
        # "edit-this-page",
        # "icon-links",
        # "indices",
        # "last-updated",
        # "navbar-icon-links",
        # "navbar-logo",
        # "navbar-nav",
        # "page-toc",
        # "prev-next",
        # "search-button-field",
        # "search-button",
        # "search-field",
        # "searchbox",
        # # "sidebar-nav-bs", # Throws an error with sphinx-build.
        # "sourcelink",
        # "sphinx-version",
        # "theme-switcher",
        # "theme-version",
        # "version-switcher"
    ],
    "content_footer_items": [],
    "footer_start": ["copyright"],
    "footer_center": ["sphinx-version"],
    "footer_end": ["theme-version"],
    "search_bar_text": "Search",
    "show_prev_next": True,
    "back_to_top_button": False,
    "show_nav_level": 1,
    "navigation_depth": 4,
    "collapse_navigation": True,
    "show_toc_level": 4,
    # https://pygments.org/styles/
    "pygments_light_style": "borland",
    "pygments_dark_style": "rrt",
    # "custom_template": "layout.html",
}
html_context = {
    # "github_url": "https://github.com", # or your GitHub Enterprise site
    "github_user": "<your-github-org>",
    "github_repo": "<your-github-repo>",
    "github_version": "<your-branch>",
    "doc_path": "<path-from-root-to-your-docs>",
    "default_mode": "light",
}

html_favicon = "./art/output/icon.svg"
html_sidebars = {
    f"{root_doc}": [],
    "README": [],
    "text/live/part-live": [],
    #'**': ["globaltoc"] # "sidebar-nav-bs"
    "**": [
        "sidebar-nav-bs",
    ],
}
html_show_copyright = True
html_show_sphinx = True
html_show_sourcelink = True
html_secnumber_suffix = ". "

# import sphinxcontrib.katex as katex
# macros_path = "./preamble/macros.tex.txt"

# with open(macros_path, 'r') as file:
#     lines = file.readlines()
#     macros_string = ''.join(lines)

# # Translate LaTeX macros to KaTeX and add to options for HTML builder
# katex_macros = katex.latex_defs_to_katex_macros(macros_string)

sys.path.append(os.path.relpath("./preamble/"))
from macros_katex import katex_macros

katex_options = "displayMode: true," + " macros: " + str(katex_macros) + ""

# Add LaTeX macros for LATEX builder
# latex_elements = {'preamble': latex_macros}


katex_css_path = "https://cdn.jsdelivr.net/npm/katex@0.16.10/dist/katex.min.css"
katex_js_path = "katex.min.js"
katex_autorender_path = "auto-render.min.js"
katex_inline = [r"\(", r"\)"]
katex_display = [r"\[", r"\]"]
katex_prerender = False  # Set "True" to prerender all mathematics on server (requires NodeJS to be installed)
# katex_options = r'''{
#     displayMode: true,
#     macros: {
#         "\\RR": "\\mathbb{R}"
#     }
# }'''
# from macros import katex_options

html_math_renderer = "mathjax"
# html_math_renderer = "katex"

# copybutton_image_svg = """
# <svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-copy" width="44" height="44" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" fill="none" stroke-linecap="square" stroke-linejoin="miter">
#   <path stroke="none" d="M0 0h24v24H0z" fill="none"/>
#   <rect x="8" y="8" width="12" height="12" rx="0"/>
#   <path d="M16 8v-2a2 2 0 0 0 -2 -2h-8a2 2 0 0 0 -2 2v8a2 2 0 0 0 2 2h2"/>
# </svg>
# """

# copybutton_image_svg = """
# <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><title>content-copy</title><path fill="currentColor" d="M19,21H8V7H19M19,5H8A2,2 0 0,0 6,7V21A2,2 0 0,0 8,23H19A2,2 0 0,0 21,21V7A2,2 0 0,0 19,5M16,1H4A2,2 0 0,0 2,3V17H4V3H16V1Z" /></svg>
# """

# copybutton_image_svg = """
# <svg
#   width="24"
#   height="24"
#   viewBox="0 0 24 24"
#   fill="none"
#   xmlns="http://www.w3.org/2000/svg"
# >
#   <path d="M13 7H7V5H13V7Z" fill="currentColor" />
#   <path d="M13 11H7V9H13V11Z" fill="currentColor" />
#   <path d="M7 15H13V13H7V15Z" fill="currentColor" />
#   <path
#     fill-rule="evenodd"
#     clip-rule="evenodd"
#     d="M3 19V1H17V5H21V23H7V19H3ZM15 17V3H5V17H15ZM17 7V19H9V21H19V7H17Z"
#     fill="currentColor"
#   />
# </svg>
# """

copybutton_image_svg = """
<svg width="800px" height="800px" viewBox="0 0 24 24" class="icon icon-tabler icon-tabler-copy" xmlns="http://www.w3.org/2000/svg" stroke="currentColor" stroke-width="1" stroke-linecap="square" stroke-linejoin="miter" fill="none" color="currentColor"><rect width="12" height="14" x="8" y="7"/> <polyline points="16 3 4 3 4 17"/> </svg>
"""
copybutton_prompt_text = r">>> |\.\.\. |\$ |In \[\d*\]: | {2,5}\.\.\.: | {5,8}: "
copybutton_prompt_is_regexp = True
copybutton_remove_prompts = True
copybutton_only_copy_prompt_lines = True
copybutton_copy_empty_lines = True
copybutton_line_continuation_character = "\\"
