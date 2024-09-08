"""
단순한 trie 구현이므로 분석은 생략합니다.
"""


class Trie:
    def __init__(self):
        self.next: dict[str, Trie] = {}
        self.end: bool = False

    def insert(self, word: str) -> None:
        cur = self

        for c in word:
            cur.next[c] = cur.next.get(c, Trie())
            cur = cur.next[c]

        cur.end = True

    def search(self, word: str) -> bool:
        cur = self

        for c in word:
            if c not in cur.next:
                return False
            cur = cur.next[c]

        return cur.end

    def startsWith(self, prefix: str) -> bool:
        cur = self

        for c in prefix:
            if c not in cur.next:
                return False
            cur = cur.next[c]

        return True
