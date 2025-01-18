# 시간복잡도
## insert, search는 해시 기반 조회로 인해 O(1), startsWith은 O(n * k) 시간이 소요 (n: 저장된 단어수, k: prefix 길이)
# 공간복잡도
## O(n * m) 공간이 필요 (n: 저장된 단어 수, m : 각 단어의 평균 길이)
class Trie:
    def __init__(self):
        self.trie = set()
    
    def insert(self, word: str) -> None:
        self.trie.add(word)

    def search(self, word: str) -> bool:
        return word in self.trie

    def startsWith(self, prefix: str) -> bool:
        return any(item.startswith(prefix) for item in self.trie)
