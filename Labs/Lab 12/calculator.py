from sly import Lexer, Parser

class CalcLexer(Lexer):
    tokens = { NAME, NUMBER, PLUS, MINUS, MULTIPLY, DIVIDE, ASSIGN, LPAREN, RPAREN, POWER, FACTORIAL }
    ignore = ' \t'

    # Tokens
    NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'
    NUMBER = r'\d+'

    # Special symbols
    PLUS = r'\+'
    MINUS = r'-'
    MULTIPLY = r'\*'
    DIVIDE = r'/'
    ASSIGN = r'='
    LPAREN = r'\('
    RPAREN = r'\)'
    POWER = r'\^'
    FACTORIAL = r'!'

    # Ignored pattern
    ignore_newline = r'\n+'

    # Extra action for newlines
    def ignore_newline(self, t):
        self.lineno += t.value.count('\n')

    def error(self, t):
        print("Illegal character '%s'" % t.value[0])
        self.index += 1

class CalcParser(Parser):
    tokens = CalcLexer.tokens

    def __init__(self):
        self.names = { }

    @_('NAME ASSIGN expr')
    def statement(self, p):
        self.names[p.NAME] = p.expr

    @_('expr')
    def statement(self, p):
        print(p.expr)

    @_('expr PLUS expr')
    def expr(self, p):
        return p.expr0 + p.expr1

    @_('expr MINUS expr')
    def expr(self, p):
        return p.expr0 - p.expr1

    @_('expr MULTIPLY expr')
    def expr(self, p):
        return p.expr0 * p.expr1

    @_('expr DIVIDE expr')
    def expr(self, p):
        if p.expr1 == 0:
            print("Division by zero error")
            return 0
        return p.expr0 / p.expr1

    @_('expr POWER expr')
    def expr(self, p):
        return p.expr0 ** p.expr1

    @_('NUMBER FACTORIAL')
    def expr(self, p):
        n = int(p.NUMBER)
        if n < 0:
            print("Factorial of negative number is undefined")
            return 0
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

    @_('LPAREN expr RPAREN')
    def expr(self, p):
        return p.expr

    @_('NUMBER')
    def expr(self, p):
        return int(p.NUMBER)

    @_('NAME')
    def expr(self, p):
        try:
            return self.names[p.NAME]
        except LookupError:
            print(f'Undefined name {p.NAME!r}')
            return 0

if __name__ == '__main__':
    lexer = CalcLexer()
    parser = CalcParser()
    while True:
        try:
            text = input('calc > ')
        except EOFError:
            break
        if text:
            parser.parse(lexer.tokenize(text))
