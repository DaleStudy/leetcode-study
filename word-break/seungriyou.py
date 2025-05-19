# https://leetcode.com/problems/word-break/

from typing import List

class Solution:
    def wordBreak_bfs(self, s: str, wordDict: List[str]) -> bool:
        """
        [Complexity]
            - TC: O(n^3 + m * k) (n = len(s), m = len(wordDict), k = avg(len(word) for word in wordDict))
                - O(n^3): (1) s[start:end] slicing * (2) end * (3) start
                - O(m * k): set(wordDict)
            - SC: O(n + m * k)
                - O(n): seen, q
                - O(m * k): set(wordDict)

        [Approach]
            BFS로 접근할 수 있다.
            이때, queue는 확인할 substring의 시작 index를 기록하면 되며, seen을 이용하여 각 start 당 한 번씩만 확인한다.
        """
        from collections import deque

        n, words = len(s), set(wordDict)

        q = deque([0])  # 확인할 substring의 시작 index
        seen = set()  # 중복 X

        while q:
            start = q.popleft()

            # base condition
            if start == n:
                return True

            # string slicing에서 사용할 끝 index를 순회하며 확인
            for end in range(start + 1, n + 1):
                # (1) 방문하지 않았으며 (2) wordDict에 현재 보고 있는 substring이 있는 경우
                if end not in seen and s[start:end] in words:
                    q.append(end)
                    seen.add(end)

        return False

    def wordBreak_dp(self, s: str, wordDict: List[str]) -> bool:
        """
        [Complexity]
            - TC: O(n^3 + m * k)
                - O(n^3): (1) s[start:end] slicing * (2) end * (3) start
                - O(m * k): set(wordDict)
            - SC: O(n + m * k)
                - O(n): dp
                - O(m * k): set(wordDict)

        [Approach]
            DP로 접근할 수 있다.
            이때, dp[i] = s[i:]가 wordDict의 원소만으로 구성될 수 있는지 여부이다.
            따라서 핵심은 뒤에서부터 확인하는 것이다!
        """

        n, words = len(s), set(wordDict)

        # dp[i] = s[i:]가 wordDict의 원소만으로 구성될 수 있는지 여부
        dp = [False] * (n + 1)
        dp[n] = True

        for start in range(n - 1, -1, -1):
            for end in range(start + 1, n + 1):
                # (1) s[end:]가 wordDict 원소로 구성 가능하고 (2) wordDict에 현재 보고 있는 substring이 있는 경우
                if dp[end] and s[start:end] in words:
                    dp[start] = True
                    break

        return dp[0]

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        [Complexity]
            - TC: O(n^2 + m * k)
                - O(n^2): 루프 수행 (slicing 제거)
                - O(m * k): trie 생성
            - SC: O(n + m * k)
                - O(n): dp list
                - O(m * k): trie

        [Approach]
            trie를 이용하면, dp에서 매 루프마다 s[start:end] slicing으로 O(n)이 소요되던 것을 O(1)로 최적화 할 수 있다.
        """
        from collections import defaultdict

        class TrieNode:
            def __init__(self):
                self.is_word = False
                self.children = defaultdict(TrieNode)

            def add_word(self, word):
                curr = self

                for w in word:
                    curr = curr.children[w]

                curr.is_word = True

        # 1. trie 구성하기
        root = TrieNode()
        for word in wordDict:
            root.add_word(word)

        # 2. dp 준비하기
        n, words = len(s), set(wordDict)
        # dp[i] = s[i:]가 wordDict의 원소만으로 구성될 수 있는지 여부
        dp = [False] * (n + 1)
        dp[n] = True

        # 3. trie를 이용하여 최적화된 dp 수행
        for start in range(n - 1, -1, -1):
            curr = root
            for end in range(start + 1, n + 1):  # -- trie 사용으로 각 단계 O(n) -> O(1)
                w = s[end - 1]

                # 현재 보고 있는 substring의 마지막 문자가 curr.children에 없다면 중단
                if w not in curr.children:
                    break

                # 있다면 타고 내려가기
                curr = curr.children[w]

                # (1) s[end:]가 wordDict 원소로 구성 가능하고 (2) wordDict의 word가 발견되었다면 dp 리스트에 기록 후 중단
                if dp[end] and curr.is_word:
                    dp[start] = True
                    break

        return dp[0]
