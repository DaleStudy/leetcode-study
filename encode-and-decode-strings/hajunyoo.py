class Solution1:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    # time complexity: O(n)
    # space complexity: O(1)
    def encode(self, strs):
        return ":;".join(strs)

    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """
    # time complexity: O(n)
    # space complexity: O(1)
    def decode(self, str):
        return str.split(":;")

class Solution2:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    # time complexity: O(n)
    # space complexity: O(1)
    def encode(self, strs):
        txt = ""
        for s in strs:
            txt += str(len(s)) + ":" + s
        return txt

    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """
    # time complexity: O(n)
    # space complexity: O(1)
    def decode(self, str):
        res = []
        i = 0
        while i < len(str):
            colon = str.find(":", i)
            length = int(str[i:colon])
            res.append(str[colon + 1:colon + 1 + length])
            i = colon + 1 + length
        return res