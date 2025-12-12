'''
문제: 특정 명령이 주어졌을 때, 트라이(Trie) 자료구조를 구현하는 코드를 작성하시오.
풀이: 단순히 문자열을 저장하는 리스트를 사용하여 트라이 자료구조의 기능을 구현합니다.
'''


class Trie:

    def __init__(self):
        self.arr = []

    def insert(self, word: str) -> None:
        self.arr.append(word)

    def search(self, word: str) -> bool:
        for i in self.arr:
            if i == word:
                return True
        return False

    def startsWith(self, prefix: str) -> bool:
        n = len(prefix)
        for i in self.arr:
            if i[:n] == prefix:
                return True
        return False


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

