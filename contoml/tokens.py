
"""
TOML lexical tokens.
"""

class TokenType:
    """
    A TokenType is a concrete type of a source token along with a defined priority and a higher-order kind.

    The priority will be used in determining the tokenization behaviour of the lexer in the following manner:
    whenever more than one token is recognizable as the next possible token and they are all of equal source
    length, this priority is going to be used to break the tie by favoring the token type of the lowest priority
    value. A TokenType instance is naturally ordered by its priority.
    """

    def __init__(self, name, priority, is_metadata):
        self._priority = priority
        self._name = name
        self._is_metadata = is_metadata

    @property
    def is_metadata(self):
        return self._is_metadata

    @property
    def priority(self):
        return self._priority

    def __repr__(self):
        return "{}-{}".format(self.priority, self._name)

    def __lt__(self, other):
        return isinstance(other, TokenType) and self._priority < other.priority

# Possible types of tokens
TOKEN_TYPE_BOOLEAN = TokenType('boolean', 0, is_metadata=False)
TOKEN_TYPE_INTEGER = TokenType('integer', 0, is_metadata=False)
TOKEN_TYPE_OP_COMMA = TokenType('comma', 0, is_metadata=True)
TOKEN_TYPE_OP_SQUARE_LEFT_BRACKET = TokenType('square_left_bracket', 0, is_metadata=True)
TOKEN_TYPE_OP_SQUARE_RIGHT_BRACKET = TokenType('square_right_bracket', 0, is_metadata=True)
TOKEN_TYPE_OP_CURLY_LEFT_BRACKET = TokenType('curly_left_bracket', 0, is_metadata=True)
TOKEN_TYPE_OP_CURLY_RIGHT_BRACKET = TokenType('curly_right_bracket', 0, is_metadata=True)
TOKEN_TYPE_OP_ASSIGNMENT = TokenType('assignment', 0, is_metadata=True)
TOKEN_TYPE_DOUBLE_SQUARE_LEFT_BRACKET = TokenType('double_square_left_bracket', 0, is_metadata=True)
TOKEN_TYPE_DOUBLE_SQUARE_RIGHT_BRACKET = TokenType('double_square_right_bracket', 0, is_metadata=True)
TOKEN_TYPE_FLOAT = TokenType('float', 1, is_metadata=False)
TOKEN_TYPE_DATE = TokenType('date', 40, is_metadata=False)
TOKEN_TYPE_OPT_DOT = TokenType('dot', 40, is_metadata=True)
TOKEN_TYPE_BARE_STRING = TokenType('bare_string', 50, is_metadata=False)
TOKEN_TYPE_STRING = TokenType('string', 90, is_metadata=False)
TOKEN_TYPE_MULTILINE_STRING = TokenType('multiline_string', 90, is_metadata=False)
TOKEN_TYPE_LITERAL_STRING = TokenType('literal_string', 90, is_metadata=False)
TOKEN_TYPE_MULTILINE_LITERAL_STRING = TokenType('multiline_literal_string', 90, is_metadata=False)
TOKEN_TYPE_NEWLINE = TokenType('newline', 91, is_metadata=True)
TOKEN_TYPE_WHITESPACE = TokenType('whitespace', 93, is_metadata=True)
TOKEN_TYPE_COMMENT = TokenType('comment', 95, is_metadata=True)

class Token:
    """
    A token/lexeme in a TOML source file.

    A Token instance is naturally ordered by its type.
    """

    def __init__(self, _type, source_substring, col=None, row=None):
        self._source_substring = source_substring
        self._type = _type
        self._col = col
        self._row = row

    @property
    def col(self):
        """
        Column number (1-indexed).
        """
        return self._col

    @property
    def row(self):
        """
        Row number (1-indexed).
        """
        return self._row

    @property
    def type(self):
        """
        One of of the TOKEN_TYPE_* constants.
        """
        return self._type

    @property
    def source_substring(self):
        """
        The substring of the initial source file containing this token.
        """
        return self._source_substring

    def __lt__(self, other):
        return isinstance(other, Token) and self.type < other.type

    def __repr__(self):
        return "{}: {}".format(self.type, self.source_substring)