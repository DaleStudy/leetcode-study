class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        res = ''

        for s in strs:
            res += str(len(s)) + '#' + s

        return res

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        res = []

        i = 0
        while i < len(s):
            a = s.find('#', i)
            length = int(s[i:a])
            res.append(s[a + 1:a + 1 + length])
            i = a + 1 + length

        return res

        ## TC: O(n), SC:O(n),n denotes sum of all len(s)
