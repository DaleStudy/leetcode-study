'''
이 문제는 단어를 추가하고, 검색할 때 .을 와일드 카드로 사용할 수 있는 자료구조를 구현해야 함
Trie 자료구조를 사용하여 .이 나오면 모든 자식 노드를 탐색해야 함(재귀적 검색) 

시간 복잡도: 
    addWord: O(L) (L = 단어 길이)
    search: 최악의 경우 O(26^M) (M = 단어 길이, .이 연속된 경우)
            *검색할 단어가 모두 .로 구성된 경우 (예: ....) 
             각 .에서 26개의 자식 노드를 모두 탐색해야 하므로

공간 복잡도: O(N) (N = 모든 단어의 총 문자 수)

'''

class TrieNode:
    def __init__(self):
        self.children = {}  # 문자 -> 자식 노드에 저장
        self.is_end = False  # 단어 끝 표시

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    # 단어를 문자별로 트라이에 추가
    def addWord(self, word: str):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        
        # 단어 끝 표시
        node.is_end = True

    # 깊이 우선 탐색(dfs)함수로 재귀적 탐색.
    def search(self, word: str):
        def dfs(node, index):
            if index == len(word):
                return node.is_end
            char = word[index]
            # .이면 모든 자식 노드 탐색
            if char != '.':
                return char in node.children and dfs(node.children[char], index+1)
            else:
                for child in node.children.values():
                    if dfs(child, index+1):
                        return True
                return False
        
        return dfs(self.root, 0)


