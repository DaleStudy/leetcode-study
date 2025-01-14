"""
Solution: 
    1) encode: 각 글자의 앞에 글자수와 # 라는 delimiter 를 붙여 stringify 한다.
    2) decode: length 를 참고삼아 word를 따내어 result 배열을 만든다.

Time: O(n)
Space: O(n)
"""


class Codec:

    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string."""
        result = ""
        for word in strs:
            result += str(len(word))
            result += "#"
            result += word
        return result

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings."""
        i = 0
        result = []
        length = ""
        while i < len(s):
            # find number
            length = ""
            while s[i] is not "#":
                length += s[i]
                i += 1
            # find #
            i += 1
            # find word
            result.append(s[i : i + int(length)])
            i += int(length)

        return result


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
