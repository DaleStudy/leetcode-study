"""
Solution:
    Trie 구조에 대해 배워보았습니다.
    TrieNode 는 children과 ending으로 이루어져있습니다.
    1) insert:
        1.1) 문자열의 각 문자를 Trie 구조에 넣습니다.
        1.2) 마지막 문자열에선 ending 을 True 로 set합니다.
    2) search:
        2.1) 문자열의 각 문자가 node.children 에 존재하지 않으면 False 를 반환합니다.
        2.2) 마지막 문자가 ending 인지 판별합니다.
    3) startsWith
        3.1) search 와 동일하게 문자열을 순회합니다. 
        3.2) ending 여부와 무관하게 True 를 반환합니다.
"""


class TrieNode:
    def __init__(self):
        self.children = {}
        self.ending = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.ending = True

    def search(self, word: str) -> bool:
        node = self.root

        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.ending

    def startsWith(self, prefix: str) -> bool:
        node = self.root

        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
