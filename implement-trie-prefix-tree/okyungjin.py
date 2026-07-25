class Trie:

    def __init__(self):
        self.word_set = set()
        self.prefix_set = set()
        

    def insert(self, word: str) -> None:
        if word in self.word_set:
            return

        self.word_set.add(word)

        prefix = ''
        for char in word:
            prefix += char
            self.prefix_set.add(prefix)


    def search(self, word: str) -> bool:
        return word in self.word_set
        

    def startsWith(self, prefix: str) -> bool:
        return prefix in self.prefix_set


'''
solution2: TrieNode 자료구조 활용
'''
class TrieNode:
    def __init__(self):
        self.children: dict[str, 'TrieNode'] = {}
        self.is_leaf = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    '''
    시간 복잡도: O(L), L: 단어의 길이
    공간 복잡도: O(L), 겹치는 문자열이 없을 때 TrideNode N개 생성
    '''
    def insert(self, word: str) -> None:
        node = self.root
        
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        
        node.is_leaf = True

    '''
    시간 복잡도: O(L), L: 단어의 길이
    공간 복잡도: O(1) 
    '''
    def search(self, word: str) -> bool:
        node = self.root

        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        
        return node.is_leaf

    '''
    시간 복잡도: O(L), L: 단어의 길이
    공간 복잡도: O(1) 
    '''
    def startsWith(self, prefix: str) -> bool:
        node = self.root

        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        
        return True
