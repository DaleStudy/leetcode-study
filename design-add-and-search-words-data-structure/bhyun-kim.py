"""
211. Design Add and Search Words Data Structure
https://leetcode.com/problems/design-add-and-search-words-data-structure/

Solution:
    To solve this problem, we can use a trie data structure to store the words.
    We can create a TrieNode class to represent each node in the trie.

    In addWord, we can iterate through each character in the word and create nodes as needed.
    We mark the end of the word by setting is_end_of_word to True.

    In search, we can use a depth-first search (DFS) to explore all possible paths.
    If we encounter a '.', we explore all children of the current node.
    If we find a mismatch or reach the end of the word, we return False.


Time complexity: 
    - addWord: O(m)
        - m is the length of the word.
        - We iterate through each character in the word once.
    - search: O(n * 26^l)
        - n is the number of nodes in the trie.
        - l is the length of the word.
        - We explore all possible paths in the trie.
        - The worst-case time complexity is O(n * 26^l) when all nodes have 26 children.

Space complexity: O(n)
    - n is the number of nodes in the trie.
    - We use a trie data structure to store the words.
"""


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        def dfs(j, node):
            for i in range(j, len(word)):
                char = word[i]
                if char == ".":
                    for child in node.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if char not in node.children:
                        return False
                    node = node.children[char]
            return node.is_end_of_word

        return dfs(0, self.root)
