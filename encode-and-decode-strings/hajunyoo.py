class Solution1:
    # time complexity: O(n)
    # space complexity: O(1)
    def encode(self, strs):
        return ":;".join(strs)

    # time complexity: O(n)
    # space complexity: O(1)
    def decode(self, str):
        return str.split(":;")

class Solution2:
    # time complexity: O(n)
    # space complexity: O(1)
    def encode(self, strs):
        txt = ""
        for s in strs:
            txt += str(len(s)) + ":" + s
        return txt

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