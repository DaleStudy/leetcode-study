class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0

        for i in range(1, len(s)):
            if s[i] == "0":
                if s[i - 1] == "0":
                    return 0
                if s[i - 1] >= "3":
                    return 0

        splited_arr = []

        i = len(s) - 1
        j = len(s)
        while i > 0:
            if s[i - 1] + s[i] >= "27":
                splited_arr.append(s[i:j])
                i -= 1
                j = i + 1
            elif s[i] == "0":
                splited_arr.append(s[i + 1:j])
                i -= 2
                j = i + 1
            else:
                i -= 1

        splited_arr.append(s[:j])

        result = 1
        for s in splited_arr:
            result *= self.count_num(s)

        return result

    def count_num(self, s: str) -> int:
        if len(s) <= 1:
            return 1

        prev2, prev1, cur = 1, 2, 2
        for i in range(2, len(s)):
            cur = prev2 + prev1
            prev2, prev1 = prev1, cur

        return cur
