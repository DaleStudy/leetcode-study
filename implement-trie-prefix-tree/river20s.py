class TrieNode:
    # 트라이 노드
    def __init__(self):
        self.children = {}
        # 단어의 끝을 나타내기 위한 플래그
        self.isEndOfWord = False

class Trie:
    # 트라이
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        # 삽입 연산
        # Time Complexity: O(L) (L은 word의 길이)
        # Space Complexity: O(M) (M은 트라이에 삽입된 모든 단어들의 총 문자 개수 합)
        currentNode = self.root
        
        for char in word:      
            if char not in currentNode.children:
                currentNode.children[char] = TrieNode()
            currentNode = currentNode.children[char]
        currentNode.isEndOfWord = True

    def search(self, word: str) -> bool:
        # 완전 검색 연산
        # Time Complexity: O(L) (L은 word의 길이)
        # Space Complexity: O(M) 
        currentNode = self.root
        for char in word:
            if char not in currentNode.children:
                return False
            currentNode = currentNode.children[char]
        return currentNode.isEndOfWord        

    def startsWith(self, prefix: str) -> bool:
        # 접두사 일치 검사 연산
        # Time Complexity: O(P) (P는 Prefix의 길이)
        # Space Complexity: O(M) 
        currentNode = self.root
        for char in prefix:
            if char not in currentNode.children:
                return False
            currentNode = currentNode.children[char]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
