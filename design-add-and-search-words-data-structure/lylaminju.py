'''
* L: 단어의 길이
시간복잡도: O(1)
- addWord(word): O(L), 최대 단어 길이가 25로 제한되므로 이 작업은 상수 시간에 가깝습니다.
- search(word): O(L * 26^d), 여기서 26은 알파벳 소문자의 개수를 의미합니다. d는 단어 내 '.'의 개수인데, 2로 제한되므로 상수 시간에 가깝습니다.
공간복잡도:
- Trie 구조에 저장되는 문자의 수에 비례합니다. 단어의 총 길이를 T라고 하면 공간복잡도는 O(T) 입니다.
'''


class Trie:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class WordDictionary:

    def __init__(self):
        # Trie의 루트 노드 초기화
        self.root = Trie()

    def addWord(self, word: str) -> None:
        current = self.root

        for char in word:
            if char not in current.children:
                current.children[char] = Trie()
            
            current = current.children[char]
        
        current.is_end_of_word = True

    def search(self, word: str) -> bool:
        def dfs(node, i):
            if i == len(word):
                return node.is_end_of_word

            char = word[i]
            if char == '.':
                # '.'인 경우 모든 자식 노드에 대해 탐색
                for child in node.children.values():
                    if dfs(child, i + 1):
                        return True
                return False
            
            if char not in node.children:
                return False
            
            return dfs(node.children[char], i + 1)
        
        return dfs(self.root, 0)



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
