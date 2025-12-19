# prefix 기반으로 탐색할 수 있는 트라이노드 자료구조 활용
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_ending = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                current_node.children[char] = TrieNode()
            current_node = current_node.children[char]
        current_node.is_ending = True

    def search(self, word):
        def dfs(node, index):
            # 단어자리수만큼 왔고, 끝단어인경우 찾기 성공
            if index == len(word):
                return node.is_ending
            # 와일드카드인 경우 자식들 전부 탐색
            if word[index] == ".":
                for child in node.children.values():
                    if dfs(child, index+1):
                        return True
            # 일반적인 경우 다음 자식 탐색
            if word[index] in node.children:
                return dfs(node.children[word[index]], index+1)
            return False
        return dfs(self.root, 0)
        

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)