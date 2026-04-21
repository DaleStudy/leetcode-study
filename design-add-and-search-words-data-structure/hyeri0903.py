class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class WordDictionary:
    ''' 너무 어려워숴 풀이 봤어요..ㅠㅠ'''

    def __init__(self):
        self.root = TrieNode() 

    def addWord(self, word: str) -> None:
        node = self.root

        for ch in word:
            #node 에 존재하지 않으면 TrieNode 생성
            if ch not in node.children:
                node.children[ch] = TrieNode()
            #node 에 children 저장
            node = node.children[ch]
        node.is_end = True

    def dfs(self, node, word, i):
        if i == len(word):
            return node.is_end

        #일반 문자일 경우
        ch = word[i]
        if ch != '.':
            if ch not in node.children:
                return False
            return self.dfs(node.children[ch], word, i + 1)
        #.이 포함된 경우 -> 모든 경우 탐색
        for child in node.children.values():
            if self.dfs(child, word, i + 1):
                return True
        return False

    def search(self, word: str) -> bool:
        return self.dfs(self.root, word, 0)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
