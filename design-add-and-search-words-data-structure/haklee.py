"""search시: TC: O(n), SC: O(n)

word의 max length가 w, `addWord`를 통해 만들어진 노드 개수가 n개라고 하자.

아이디어:
`implement-trie-prefix-tree` 문제에서 구현한 trie에서 search 부분만 recursive한 dfs 구현으로 수정.

SC:
- trie의 노드 개수 O(n).
- dfs시 스택 깊이는 최대 w. 즉, O(w). 그런데 스택 깊이는 노드 개수보다 클 수 없다. 즉, O(w) < O(n).
- 종합하면, O(n) + O(w) < O(n) + O(n) = O(n).

TC:
- 최악의 경우 모든 노드 순회. O(n).

"""


class WordDictionary:

    def __init__(self):
        self.next: dict[str, WordDictionary] = {}
        self.end: bool = False

    def addWord(self, word: str) -> None:
        cur = self

        for c in word:
            cur.next[c] = cur.next.get(c, WordDictionary())
            cur = cur.next[c]

        cur.end = True

    def search(self, word: str) -> bool:
        cur = self

        return self._search(cur, word, 0)

    def _search(self, trie, word: str, ind: int) -> bool:
        if ind == len(word):
            return trie.end

        c = word[ind]

        if c == ".":
            return any(
                [self._search(node, word, ind + 1) for node in trie.next.values()]
            )

        if c not in trie.next:
            return False

        return self._search(trie.next[c], word, ind + 1)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
