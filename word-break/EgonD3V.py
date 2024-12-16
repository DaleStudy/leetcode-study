from typing import List
from unittest import TestCase, main


class Node:
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}


class Trie:

    def __init__(self):
        self.root = Node(None)

    def insert(self, word: str) -> None:
        curr_node = self.root
        for char in word:
            if char not in curr_node.children:
                curr_node.children[char] = Node(char)

            curr_node = curr_node.children[char]

        curr_node.data = word

    def search(self, word: str) -> bool:
        curr_node = self.root
        for char in word:
            if char in curr_node.children:
                curr_node = curr_node.children[char]
            else:
                return False

        return curr_node.data == word

    def startsWith(self, prefix: str) -> bool:
        curr_node = self.root
        for char in prefix:
            if char in curr_node.children:
                curr_node = curr_node.children[char]
            else:
                return False
        else:
            return True


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        return self.solveWithTrieDFSMemo(s, wordDict)

    """
    Runtime: 38 ms (Beats 70.76%)
    Time Complexity: O(n * L + s^2)
        - s의 길이를 S, wordDict의 길이를 L, word의 최대 길이를 W라 하면
            - trie에 insert하는데 O(W * L), upper bound
            - DFS에서 curr_s의 모든 문자 조회에 최대 O(S), 접두사를 제거하는 curr_s.removeprefix에서 최대 O(S)
        > O(W * L) + O(S) * O(S) = O(W * L + S^2) upper bound

    Memory: 17.70 MB (Beats 5.25%)
    Space Complexity:
         - trie 생성 및 갱신에 O(W * L)
         - visited는 최악의 경우 s의 모든 부분 문자열을 저장하므로 O(S^2) upper bound
         > O(W * L) + O(S^2) = O(W * L + S^2) upper bound
    """
    def solveWithTrieDFSMemo(self, s: str, wordDict: List[str]) -> bool:
        trie = Trie()
        for word in wordDict:
            trie.insert(word)

        stack = [s]
        visited = set()
        while stack:
            curr_s = stack.pop()
            if curr_s in visited:
                continue

            curr_node = trie.root
            for char in curr_s:
                if char in curr_node.children:
                    curr_node = curr_node.children[char]
                    if curr_node.data is not None:
                        post_s = curr_s.removeprefix(curr_node.data)
                        if not post_s:
                            return True
                        else:
                            stack.append(post_s)
                else:
                    visited.add(curr_s)
                    break

        return False


class _LeetCodeTestCases(TestCase):
    def test_1(self):
        s = "leetcode"
        wordDict = ["leet","code"]
        output = True
        self.assertEqual(Solution.wordBreak(Solution(), s, wordDict), output)

    def test_2(self):
        s = "applepenapple"
        wordDict = ["apple","pen"]
        output = True
        self.assertEqual(Solution.wordBreak(Solution(), s, wordDict), output)

    def test_3(self):
        s = "catsandog"
        wordDict = ["cats","dog","sand","and","cat"]
        output = False
        self.assertEqual(Solution.wordBreak(Solution(), s, wordDict), output)

    def test_4(self):
        s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
        wordDict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
        output = False
        self.assertEqual(Solution.wordBreak(Solution(), s, wordDict), output)


if __name__ == '__main__':
    main()
