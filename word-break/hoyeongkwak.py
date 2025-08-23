'''
TrieNode
a : alphabet size
time complexity : O(m)
space complexity : O(m * a)

dp
time complexity : O(n^2)
space complexity : O(n)
'''
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.isEnd = True
    
    def search(self, s, start_idx):
        node = self.root
        endPosition = []

        for i in range(start_idx, len(s)):
            char = s[i]
            if char not in node.children:
                break
            node = node.children[char]
            if node.isEnd:
                endPosition.append(i + 1)
        return endPosition

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        trie = Trie()
        for word in wordDict:
            trie.insert(word)
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(n):
            if not dp[i]:
                continue
            endPositions = trie.search(s, i)

            for endPos in endPositions:
                dp[endPos] = True
        return dp[n]
