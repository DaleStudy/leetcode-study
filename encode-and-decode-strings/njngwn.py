class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ''

        for s in strs:
            encoded += str(len(s)) + '#' + s

        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []

        i = 0
        while i < len(s):
            j = i  # j is a pointer for beginning of string
            # find '#' in string
            while s[j] != '#':
                j += 1

            length = int(s[i:j])
            word = s[j + 1:j + length + 1]
            decoded.append(word)
            i = j + length + 1

        return decoded
