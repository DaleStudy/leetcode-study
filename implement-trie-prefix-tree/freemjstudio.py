# 트리이 자체의 시간 복잡도는 O(n) 이다. n 은 단어의 길이이다.

class Trie:

    def __init__(self):
        self.children = {} # 다음 문자(key) : 다음 문자에 해당하는 노드(value)
        self.is_end = False # 현재 문자가 단어의 마지막인지 여부

    def insert(self, word: str) -> None:
        node = self
        for char in word:
            if char not in node.children:
                node.children[char] = Trie() # 새로운 노드를 생성
            node = node.children[char]
        # 현재 마지막 노드를 가리키고 있으므로 is_end 를 True 로 바꾼다.
        node.is_end = True


    def search(self, word: str) -> bool:
        node = self
        for char in word:
            if char in node.children:
                node = node.children[char]
            else: # 더 이상 그 문자가 없다는 의미이므로 false
                return False

        if node.is_end:
            return True
        return False


    def startsWith(self, prefix: str) -> bool:
        node = self
        for char in prefix:
            if char in node.children:
                node = node.children[char]
            else: # 더 이상 그 문자가 없다는 의미이므로 false
                return False

        return True



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
