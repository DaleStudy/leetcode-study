class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    모르겠어서 해설의 힘을 빌렸어요..ㅠ
    """
    def encode(self, strs: List[str]):
        text = ""
        for str in strs:
            text += f"{len(str)}:{str}"
        return text

    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """
    def decode(self, s: str):
        output = []
        start = 0
        while start < len(s):
            mid = s.find(":", start)
            length = int(s[start:mid])
            output.append(s[mid + 1 : mid + 1 + length])
            start = mid + 1 + length
        return output
