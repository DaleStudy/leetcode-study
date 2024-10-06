class Solution:
    # 시간복잡도: O(A*B)
    # 공간복잡도: O(A*B)
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        a = len(text1)
        b = len(text2)

        lcs = [[0]*(b+1) for _ in range(a+1)]

        for i in range(1, a+1):
            for j in range(1, b+1):
                if text1[i-1] == text2[j-1]:
                    lcs[i][j] = lcs[i-1][j-1] + 1
                lcs[i][j] = max(lcs[i][j], lcs[i-1][j], lcs[i][j-1])

        return lcs[a][b]

    # 시간복잡도: O(A*B)
    # 공간복잡도: O(A)
    def longestCommonSubsequence2(self, text1: str, text2: str) -> int:
        n = len(text1)
        lcs = [0]*n
        longest = 0
        for ch in text2:
            cur = 0
            for i in range(n):
                if cur < lcs[i]:
                    cur = lcs[i]
                elif ch == text1[i]:
                    lcs[i] = cur + 1
                    longest = max(longest, cur+1)

        return longest
