from token import Token
from token_type import TokenType

# Returns a list of tokens
def scan(source):
    tokens = []
    current = 0
    while current < len(source):
        c = source[current]
        if source[current : current + 2] == "//":
            try:
                current = source.index("\n", current) + 1
            except ValueError:
                break
        elif c == '"':
            start = current + 1
            try:
                current = source.index('"', current + 1)
            except ValueError:
                break
            value = source[start:current]
            tokens.append(Token(TokenType.STRING, value))
        elif c.isalpha():
            word = ""
            while source[current].isalnum():
                word += source[current]
                current += 1
            try:
                tokens.append(Token(TokenType(word)))
            except ValueError:
                tokens.append(Token(TokenType.IDENTIFIER, word))
        else:
            # tokens.append(Token(TokenType(c)))
            current += 1
