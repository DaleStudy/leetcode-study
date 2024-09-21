from unittest import TestCase, main


class Node:

    def __init__(self, key):
        self.key = key
        self.isWordEnd = False
        self.children = {}


class Trie:
    WILD_CARD = '.'

    def __init__(self):
        self.root = Node(None)

    def insert(self, word: str) -> None:
        curr_node = self.root
        for char in word:
            if char not in curr_node.children:
                curr_node.children[char] = Node(char)

            curr_node = curr_node.children[char]
        curr_node.isWordEnd = True

    def search(self, node: Node, word: str, idx: int) -> bool:
        if idx == len(word):
            return node.isWordEnd

        for idx in range(idx, len(word)):
            if word[idx] == self.WILD_CARD:
                for child in node.children.values():
                    if self.search(child, word, idx + 1) is True:
                        return True
                else:
                    return False

            if word[idx] in node.children:
                return self.search(node.children[word[idx]], word, idx + 1)
            else:
                return False


"""
Runtime: 1810 ms (Beats 22.46%)
Time Complexity:
    > addWord: word의 길이만큼 순회하므로 O(L)
    > search:
        - word의 평균 길이를 W이라하면,
        - '.'가 포함되어 있지 않는 경우 O(W), early return 가능하므로 upper bound
        - '.'가 포함되어 있는 경우, 해당 노드의 child만큼 재귀, trie의 평균 자식 수를 C라 하면 O(W) * O(C), early return 가능하므로 upper bound
            - trie의 평균 자식 수는 addWord의 실행횟수 C'에 선형적으로 비레(겹치는 char가 없는 경우 upper bound)
        > O(W) * O(C) ~= O(W) * O(C') ~= O(W * C'), upper bound

Memory: 66.78 MB (Beats 12.26%)
Space Complexity: O(1)
    > addWord: 
        - 삽입한 word의 평균 길이 L만큼 Node가 생성 및 Trie에 추가, O(L)
        - addWord의 실행횟수 C'에 비례, O(C')
        > O(L) * O(C') ~= O(L * C')
    > search:
        > 만들어진 Trie와 패러미터 word, 정수 변수 idx를 사용하므로 O(1)
    
"""
class WordDictionary:

    def __init__(self):
        self.trie = Trie()

    def addWord(self, word: str) -> None:
        self.trie.insert(word)

    def search(self, word: str) -> bool:
        return self.trie.search(self.trie.root, word, 0)


class _LeetCodeTestCases(TestCase):
    def test_1(self):
        wordDictionary = WordDictionary()
        wordDictionary.addWord("at")
        self.assertEqual(wordDictionary.search(".at"), False)


if __name__ == '__main__':
    main()
