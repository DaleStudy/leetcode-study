class Solution:

    # 시간복잡도: O(N)
    # 공간복잡도: O(1)
    def encode(self, strs):
        res = ""
        for str in strs:
            size = len(str)
            res += str(size)
            res += str

        return res

    # 시간복잡도: O(N)
    # 공간복잡도: O(N)
    def decode(self, str):
        idx = 0
        limit = len(str)
        res = []

        while idx < limit:
            num = str[idx]
            text = ""
            for _ in range(num):
                text += str[idx]
                idx+=1
            res.append(text)

        return res
