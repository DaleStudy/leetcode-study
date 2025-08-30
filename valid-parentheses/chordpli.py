class Solution:
    def isValid(self, s: str) -> bool:
        if not s or len(s) % 2 == 1:
            return False

        open_symbols = ['(', '[', '{']
        open_box = []

        for char in list(s):
            if char in open_symbols:
                open_box.append(char)
            elif char not in open_symbols:
                if not open_box:
                    return False
                open_symbol = open_box.pop()
                if open_symbol == '(' and char == ')':
                    continue
                elif open_symbol == '[' and char == ']':
                    continue
                elif open_symbol == '{' and char == '}':
                    continue
                else:
                    return False

        return len(open_box) == 0
