from __future__ import unicode_literals

import re


class WrongArgumentTypeException(Exception):
    pass


class _Expression(object):
    def __init__(self, expr):
        self._expr = re.sub(r'\s+', ' ', expr.strip())

    @property
    def has_more_tokens(self):
        return self._has_more_tokens

    def next_token(self):
        pass


def calculate(expr):
    if not isinstance(expr, basestring):
        raise WrongArgumentTypeException('Wrong argument type. '
                                         'The expression must be a string')
    result = 0.0
    expr = _Expression(expr)
    while expr.has_more_tokens:
        pass
