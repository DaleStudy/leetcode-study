'''
solution1: dfs + @cache
'''
from typing import List
from functools import cache

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        size = len(s)
        word_set = set(wordDict)

        @cache
        def dfs(start: int) -> bool:
            if start == size:
                return True
                
            for end in range(start + 1, size + 1):
                word = s[start:end] # O(N)

                if word in word_set and dfs(end):
                    return True
                        
            return False

        return dfs(0)

'''
solution2: dfs + memo
'''
class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        size = len(s)
        word_set = set(wordDict)
        failed: set[int] = set() # 탐색에 실패한 인덱스 기록
        
        def dfs(start: int) -> bool:
            if start == size:
                return True
            
            if start in failed:
                return False
            
            for end in range(start + 1, size + 1):
                word = s[start:end]

                if word in word_set and dfs(end):
                    return True

            failed.add(start)
            return False

        return dfs(0)

'''
solution3: bfs
'''
from collections import deque

class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        size = len(s)
        word_set = set(wordDict)
        queue = deque([0])
        visited = set([0])

        while queue:
            start = queue.popleft()
            
            for end in range(start + 1, size + 1):
                word = s[start:end]

                if end not in visited and word in word_set:
                    if end == size:
                        return True
                    
                    queue.append(end)
                    visited.add(end)
                    
        return False

'''
solution4: dp
'''
class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        size = len(s)
        word_set = set(wordDict)
        dp = [False] * (size + 1)
        dp[0] = True
        
        for end in range(1, size + 1):
            for start in range(end):
                word = s[start:end]

                if dp[start] and word in word_set:
                    dp[end] = True
                    break
                    
        return dp[-1]

'''
solution5: trie 자료구조 활용

Trie 자료구조로 노드를 만들어서 탐색한다
Examples3: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]

[Root]
  ├── 'c' ── 'a' ── 't'(leaf) ── 's'(leaf)
  ├── 'd' ── 'o' ── 'g'(leaf)
  ├── 's' ── 'a' ── 'n' ── 'd'(leaf)
  └── 'a' ── 'n' ── 'd'(leaf)
'''
class TrieNode:
    def __init__(self):
        self.children: dict[int, 'TrieNode'] = {}
        self.is_leaf = False

class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        root = self._build_trie(wordDict)
        
        size = len(s)
        dp = [False] * (size + 1)
        dp[0] = True
        
        for start in range(size):
            if not dp[start]:
                continue
            
            node = root
            for end in range(start + 1, size + 1):
                char = s[end - 1]
                # trie에 없으면 바로 종료
                if char not in node.children:
                    break
                node = node.children[char]
                
                if node.is_leaf:
                    dp[end] = True
                    
        return dp[-1]

    # wordDict로 trie 자료구조 생성
    def _build_trie(self, wordDict: list[str]) -> TrieNode:
        root = TrieNode()

        for word in wordDict:
            node = root

            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.is_leaf = True

        return root
