# Based on the "unsrt" style:
# https://bitbucket.org/pybtex-devs/pybtex/src/master/pybtex/style/formatting/unsrt.py
# With help from:
# https://github.com/cproctor/pybtex-apa7-style/blob/master/formatting/apa.py

from __future__ import unicode_literals

import re

from pybtex.richtext import Symbol, Text
from pybtex.style.formatting import BaseStyle, toplevel
from pybtex.style.template import (
    field, first_of, href, join, names, optional, optional_field, sentence,
    tag, together, words, node, FieldIsMissing
)

@node
def phys_names(children, context, role, **kwargs):
    """
    Returns formatted names in the biblatex "phys" style.
    """
    assert not children

    try:
        persons = context['entry'].persons[role]
    except KeyError:
        raise FieldIsMissing(role, context['entry'])

    style = context['style']
    style.abbreviate_names = True # Force abbreviation of names

    if len(persons) > 20:
        formatted_names = [style.format_name(
            person, style.abbreviate_names) for person in persons[:20]]
        formatted_names += [richtext.Text("et al.")]
        return join(sep=', ')[formatted_names].format_data(context)
    else:
        formatted_names = [style.format_name(
            person, style.abbreviate_names) for person in persons]
        return join(sep=', ', sep2=' and ', last_sep=', and ')[
            formatted_names].format_data(context)

def dashify(text):
    dash_re = re.compile(r'-+')
    return Text(Symbol('ndash')).join(text.split(dash_re))


pages = field('pages', apply_func=dashify)

date = words [optional_field('month'), field('year')]


class PhysStyle(BaseStyle):

    def format_names(self, role, as_sentence=True):
        formatted_names = phys_names(role)
        if as_sentence:
            return sentence(capfirst=False,add_period=False)[formatted_names]
        else:
            return formatted_names

    def format_author_or_editor_and_date(self, e):
        if 'author' in e.persons and 'editor' in e.persons:
            return sentence(sep=' ')[
                self.format_names('author'), 
                self.format_date(e),
                self.format_editor(e, as_sentence=False)
            ]
        elif 'author' in e.persons:
            return sentence(sep=' ')[
                self.format_names('author'), 
                self.format_date(e),
            ]
        else:
            return sentence(sep=' ')[
                self.format_editor(e, as_sentence=False),
                self.format_date(e),
            ]

    def format_author_or_editor(self, e):
        return first_of [
            optional[ self.format_names('author') ],
            self.format_editor(e),
        ]

    def format_editor(self, e, as_sentence=False):
        editors = self.format_names('editor', as_sentence=False)
        if 'editor' not in e.persons:
            # when parsing the template, a FieldIsMissing exception
            # will be thrown anyway; no need to do anything now,
            # just return the template that will throw the exception
            return editors
        if len(e.persons['editor']) > 1:
            word = '(editors)'
        else:
            word = '(editor)'
        # result = join(sep=', ') [editors, word]
        result = join(sep=' ') [editors, word]
        if as_sentence:
            return sentence [result]
        else:
            return result

    def format_volume_and_series(self, e, as_sentence=False):
        volume_and_series = optional [
            words [
                together ['Volume' if as_sentence else 'volume', field('volume')], optional [
                    words ['of', field('series')]
                ]
            ]
        ]
        number_and_series = optional [
            words [
                join(sep=Symbol('nbsp')) ['Number' if as_sentence else 'number', field('number')],
                optional [
                    words ['in', field('series')]
                ]
            ]
        ]
        series = optional_field('series')
        result = first_of [
            volume_and_series,
            number_and_series,
            series,
        ]
        # result = join[result,","]
        if as_sentence:
            return sentence(capfirst=True) [result]
        else:
            return result

    def format_chapter_and_pages(self, e):
        return join(sep=', ') [
            optional [together ['chapter', field('chapter')]],
            optional [together ['pages', pages]],
        ]

    def format_edition(self, e):
        return optional [
            words [
                field('edition', apply_func=lambda x: x.lower()),
                'edition',
            ]
        ]

    def format_title(self, e, which_field, as_sentence=True):
        formatted_title = field(
            which_field, apply_func=lambda text: text.capitalize()
        )
        if as_sentence:
            return join['“',sentence(add_period=False) [ formatted_title ],'”']
        else:
            return formatted_title

    def format_btitle(self, e, which_field, as_sentence=False):
        formatted_title = tag('em') [ field(which_field) ]
        if as_sentence:
            return sentence[ formatted_title ]
        else:
            # return join[formatted_title,","]
            return formatted_title

    def format_address_organization_publisher_date(
        self, e, include_organization=True):
        """Format address, organization, publisher, and date.
        Everything is optional, except the date.
        """
        # small difference from unsrt.bst here: unsrt.bst
        # starts a new sentence only if the address is missing;
        # for simplicity here we always start a new sentence
        if include_organization:
            organization = optional_field('organization')
        else:
            organization = None
        return first_of[
            # this will be rendered if there is an address
            optional [
                join(sep=' ') [
                    sentence[
                        field('address'),
                        date,
                        organization,
                        optional_field('publisher'),
                    ],
                ],
            ],
            # if there is no address then we have this
            sentence[
                organization,
                optional_field('publisher'),
                date,
            ],
        ]

    def format_web_refs(self, e):
        # based on urlbst output.web.refs
        return sentence(add_period=False) [
            optional [ self.format_url(e) ],
                       # optional [ ' (visited on ', field('urldate'), ')' ] ],
            optional [ self.format_eprint(e) ],
            optional [ self.format_pubmed(e) ],
            optional [ self.format_doi(e) ],
            ]

    def format_url(self, e):
        return words[
            # 'URL:',
            href[
                field('url', raw=True),
                field('url', raw=True)
            ]
        ]

    def format_pubmed(self, e):
        return href[
            join[
                'https://www.ncbi.nlm.nih.gov/pubmed/',
                field('pubmed', raw=True)
            ],
            join[
                # 'PMID:',
                field('pubmed', raw=True)
            ]
        ]

    def format_doi(self, e):
        return href[
            join[
                'https://doi.org/',
                field('doi', raw=True)
            ],
            join[
                'doi:',
                field('doi', raw=True)
            ]
        ]

    def format_eprint(self, e):
        return href[
            join[
                'https://arxiv.org/abs/',
                field('eprint', raw=True)
            ],
            join[
                'arXiv:',
                field('eprint', raw=True)
            ]
        ]

    def format_isbn(self, e):
        return join(sep=' ') [
            'ISBN',
            field('isbn')
        ]

    def get_article_template(self, e):
        volume_and_pages = first_of [
            # volume and pages, with optional issue number
            optional [
                join [
                    field('volume'),
                    optional['(', field('number'),')'],
                    ':', pages
                ],
            ],
            # pages only
            words ['pages', pages],
        ]
        template = toplevel [
            sentence [
                self.format_names('author'),
                self.format_title(e, 'title'),
                tag('em') [optional_field('journal')],
                optional[ volume_and_pages ],
                date],
            # sentence [ optional_field('note') ],
            self.format_web_refs(e),
        ]
        return template

    def get_book_template(self, e):
        template = toplevel [
            sentence [
                self.format_author_or_editor(e),
                self.format_btitle(e, 'title'),
                optional[ self.format_volume_and_series(e) ],
                field('publisher'),
                optional_field('address'),
                self.format_edition(e),
                date
            ],
            # optional[ sentence [ self.format_isbn(e) ] ],
            # sentence [ optional_field('note') ],
            # self.format_web_refs(e),
        ]
        return template

    def get_booklet_template(self, e):
        template = toplevel [
            sentence [
                self.format_names('author'),
                self.format_title(e, 'title'),
                optional_field('howpublished'),
                optional_field('address'),
                date,
                # optional_field('note'),
            ],
            self.format_web_refs(e),
        ]
        return template

    def get_inbook_template(self, e):
        template = toplevel [
            self.format_author_or_editor(e),
            self.format_btitle(e, 'title', as_sentence=False),
            self.format_chapter_and_pages(e),
            self.format_volume_and_series(e),
            sentence [
                field('publisher'),
                optional_field('address'),
                optional [
                    words [field('edition'), 'edition']
                ],
                date,
                # optional_field('note'),
            ],
            self.format_web_refs(e),
        ]
        return template

    def get_incollection_template(self, e):
        template = toplevel [
            sentence [
                self.format_names('author'),
                self.format_title(e, 'title'),
                optional[ self.format_editor(e, as_sentence=False) ],
                self.format_btitle(e, 'booktitle', as_sentence=False),
                self.format_volume_and_series(e, as_sentence=False),
                self.format_chapter_and_pages(e),
                optional_field('publisher'),
                optional_field('address'),
                self.format_edition(e),
                date,
            ],
            self.format_web_refs(e),
        ]
        return template

    def get_inproceedings_template(self, e):
        template = toplevel [
            sentence [
                self.format_names('author'),
                self.format_title(e, 'title'),
                optional[ self.format_editor(e, as_sentence=False) ],
                self.format_btitle(e, 'booktitle', as_sentence=False),
                self.format_volume_and_series(e, as_sentence=False),
                optional[ self.format_chapter_and_pages(e)],
                self.format_address_organization_publisher_date(e),
            ],
            # sentence [ optional_field('note') ],
            self.format_web_refs(e),
        ]
        return template

    def get_manual_template(self, e):
        # TODO this only corresponds to the bst style if author is non-empty
        # for empty author we should put the organization first
        template = toplevel [
            sentence [
                optional [ sentence [ self.format_names('author') ] ],
                self.format_btitle(e, 'title'),
                optional_field('organization'),
                optional_field('address'),
                self.format_edition(e),
                optional[ date ],
            ],
            # sentence [ optional_field('note') ],
            self.format_web_refs(e),
        ]
        return template

    def get_mastersthesis_template(self, e):
        template = toplevel [
            sentence[
                self.format_names('author'),
                self.format_title(e, 'title'),
                "Master's thesis",
                field('school'),
                optional_field('address'),
                date,
            ],
            sentence [ optional_field('note') ],
            self.format_web_refs(e),
        ]
        return template

    def get_online_template(self, e):
        return self.get_misc_template(e)

    def get_phdthesis_template(self, e):
        template = toplevel [
            sentence[
                self.format_names('author'),
                self.format_btitle(e, 'title'),
                first_of [
                    optional_field('type'),
                    'PhD thesis',
                ],
                field('school'),
                optional_field('address'),
                date,
            ],
            # sentence [ optional_field('note') ],
            self.format_web_refs(e),
        ]
        return template

    def get_proceedings_template(self, e):
        if 'editor' in e.persons:
            main_part = [
                sentence [
                    self.format_editor(e),
                    self.format_btitle(e, 'title', as_sentence=False),
                    self.format_volume_and_series(e, as_sentence=False),
                    self.format_address_organization_publisher_date(e),
                ],
            ]
        else:
            main_part = [
                sentence [
                    optional [ sentence [ field('organization') ] ],
                    self.format_btitle(e, 'title', as_sentence=False),
                    self.format_volume_and_series(e, as_sentence=False),
                    self.format_address_organization_publisher_date(
                        e, include_organization=False),
                ],
            ]
        template = toplevel [
            main_part + [
                # sentence [ optional_field('note') ],
                self.format_web_refs(e),
            ]
        ]
        return template

    def get_techreport_template(self, e):
        template = toplevel [
            sentence [
                self.format_names('author'),
                self.format_title(e, 'title'),
                words[
                    first_of [
                        optional_field('type'),
                        'Technical Report',
                    ],
                    optional_field('number'),
                ],
                field('institution'),
                optional_field('address'),
                date,
            ],
            # sentence [ optional_field('note') ],
            self.format_web_refs(e),
        ]
        return template

    def get_misc_template(self, e):
        template = toplevel [
            sentence[
                optional[ self.format_names('author') ],
                optional[ self.format_title(e, 'title') ],
                optional[ field('howpublished') ],
                optional[ date ],
            ],
            # sentence [ optional_field('note') ],
            self.format_web_refs(e),
        ]
        return template

    def get_unpublished_template(self, e):
        template = toplevel [
            sentence [
                self.format_names('author'),
                self.format_title(e, 'title'),
                field('note'),
                optional[ date ]
            ],
            self.format_web_refs(e),
        ]
        return template