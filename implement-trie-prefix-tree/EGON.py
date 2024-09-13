from unittest import TestCase, main


"""
Runtime: 136 ms (Beats 33.86%)
Time Complexity:
    > insert: word의 각 문자마다 조회하므로 O(L)
    > search: 최대 word의 모든 문자를 조회하므로 O(L), upper bound
    > startsWith: 최대 prefix의 모든 문자를 조회하므로 O(L'), upper bound

Memory: 32.60 MB (Beats 16.08%)
Space Complexity: O(n * L), upper bound
    - 최악의 경우 삽입하는 모든 word가 공통점이 하나도 없는 경우를 상정해보면, 삽입하는 word의 갯수를 n, word의 최대 길이를 L
    > O(n * L), upper bound
"""


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


class _LeetCodeTestCases(TestCase):
    def test_1(self):
        # commands = ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
        # words = [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
        # output = [None, None, True, False, True, None, True]

        trie = Trie()
        trie.insert("apple")
        self.assertEqual(trie.search("apple"), True)
        self.assertEqual(trie.search("app"), False)
        self.assertEqual(trie.startsWith("app"), True)
        trie.insert("app")
        self.assertEqual(trie.search("app"), True)


if __name__ == '__main__':
    main()
