class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        """
        주어진 문자열 s를 단어 사전 wordDict의 단어들로 분할할 수 있는지 여부를 판단하는 함수.
        N은 문자열 s의 길이, M은 단어 사전의 최대 단어 길이로 가정할 때,
        시간 복잡도: O(N * M)
        공간 복잡도: O(N)

        Args:
            s (str): 주어진 문자열
            wordDict (list[str]): 사용가능한 단어 사전

        Returns:
            bool: 주어진 문자열을 단어 사전의 단어들로 분할할 수 있는지 여부
        """
        word_check = [False] * (len(s) + 1)
        max_len = len(max(wordDict, key=len))
        word_check[0] = True
        for i in range(len(s)):
            if not word_check[i]:
                continue
            for j in range(i + 1, min(len(s), i + max_len) + 1):
                # i까지의 단어가 사전에 있고, i부터 j까지의 단어가 사전에 있으면 모든 단어가 사전에 있는 상태로 판단
                if word_check[i] and s[i:j] in wordDict:
                    word_check[j] = True
        return word_check[-1]
