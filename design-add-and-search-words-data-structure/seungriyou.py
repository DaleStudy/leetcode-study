# https://leetcode.com/problems/design-add-and-search-words-data-structure/

from collections import defaultdict, deque

class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children = defaultdict(TrieNode)

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root

        for w in word:
            curr = curr.children[w]

        curr.is_word = True

    def search(self, word: str) -> bool:
        """
        BFS 혹은 DFS를 사용할 수 있다. 핵심은
            - "."을 마주치면 모든 children을 전부 타고 내려간다.
            - "."이 아닌 문자를 확인해야 한다면 해당 문자가 children에 있는지 확인 후 타고 내려간다.
        는 것이다.
        """
        # return self._bfs(word)
        return self._dfs(self.root, word, 0)

    def _dfs(self, curr, word, idx):
        # base condition
        if idx == len(word):
            return curr.is_word

        # recur
        # (1) "."을 마주치면 모든 children에 대해 타고 내려간다.
        if word[idx] == ".":
            for child in curr.children.values():
                if self._dfs(child, word, idx + 1):
                    return True

        # (2) 현재 idx의 문자가 children에 있는지 확인 후에 타고 내려간다.
        if (w := word[idx]) in curr.children:
            return self._dfs(curr.children[w], word, idx + 1)

        # (3) 그 외의 경우, False를 반환한다.
        return False

    def _bfs(self, word):
        q = deque([(self.root, 0)])  # (node, idx)

        while q:
            curr, idx = q.popleft()

            # base condition
            if idx == len(word):
                if curr.is_word:
                    return True

            # iter
            # (1) "."을 마주치면 모든 children에 대해 타고 내려간다.
            elif word[idx] == ".":
                for child in curr.children.values():
                    q.append((child, idx + 1))

            # (2) 현재 idx의 문자가 children에 있는지 확인 후에 타고 내려간다.
            else:
                if (w := word[idx]) in curr.children:
                    q.append((curr.children[w], idx + 1))

        # (3) 그 외의 경우, False를 반환한다.
        return False

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
