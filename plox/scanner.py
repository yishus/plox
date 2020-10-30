from token import Token
from token_type import TokenType

# Returns a list of tokens
def scan(source):
    tokens = []
    current = 0
    line = 0
    while current < len(source):
        c = source[current]
        if c in ["!", "=", "<", ">"]:
            peek = source[current + 1]
            if peek == "=":
                tokens.append(Token(TokenType(c + peek)))
                current += 2
            else:
                tokens.append(Token(TokenType(c)))
                current += 1
        elif source[current : current + 2] == "//":
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
            current += 1
        elif c == "\n":
            line += 1
            current += 1
        elif c.isalpha():
            word = ""
            while source[current].isalnum() or source[current] == "_":
                word += source[current]
                current += 1
            try:
                tokens.append(Token(TokenType(word)))
            except ValueError:
                tokens.append(Token(TokenType.IDENTIFIER, word))
        elif c.isdigit():
            num_str = ""
            while source[current].isdigit() or source[current] == ".":
                num_str += source[current]
                period_removed = num_str.replace(".", "", 1)
                if not period_removed.isdigit():
                    print("something wrong")
                current += 1
            tokens.append(Token(TokenType.NUMBER, float(num_str)))
        else:
            try:
                tokens.append(Token(TokenType(c)))
            except ValueError:
                pass
            current += 1
