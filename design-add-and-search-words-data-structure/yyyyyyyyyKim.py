"""
TrieNode: 한 글자를 담는 노드
- children: 자식노드들 저장하는 딕셔너리
- end: 해당 노드에서 단어가 끝나는지 여부
"""
class TrieNode:
    # Trie 노드 초기화
    def __init__(self):
        self.children = {}  # 자식 노드 저장
        self.end = False    # 단어의 끝인지 표시

"""
Trie(트라이)구조, DFS, 재귀
- addWord : 단어를 Trie에 삽입
- search : 단어가 Trie에 존재하는지 검색
"""
class WordDictionary:

    # Trie 자료구조 초기화(루트 노드 생성)
    def __init__(self):
        # Trie의 시작(빈 루트 노드 생성)
        self.root = TrieNode()        

    def addWord(self, word: str) -> None:
        node = self.root    # 단어 삽입의 시작 위치 = 루트 노드

        # 단어의 글자 하나하나를 Trie에 삽입
        for i in word:
            # 글자가 자식 노드에 없으면 새로운 노드 생성해서 뻗어가기
            if i not in node.children:
                node.children[i] = TrieNode()

            node = node.children[i] # 다음 글자(노드)로 이동

        node.end = True # 단어 삽입 완료, 현재 노드에서 단어의 끝 표시(True)


    def search(self, word: str) -> bool:

        def dfs(node,i):
            # 단어를 다 돌고 마지막 노드가 단어의 끝이면 node.end는 True
            if i == len(word):
                return node.end

            if word[i] == ".":
                # "." 일 경우 모든 자식 노드 대상으로 재귀 탐색
                for j in node.children.values():
                    if dfs(j, i+1):
                        return True
            else:
                # "."이 아닌 경우 자식노드에 있는지 확인. 
                # 있으면 다음 글자 탐색, 없으면 False 리턴
                if word[i] in node.children:
                    return dfs(node.children[word[i]], i+1)
                else:
                    return False
                    
            # 일치하는 단어가 없는 경우에 대비한 예외 처리
            return False

        # DFS시작(루트 노드부터 탐색)
        return dfs(self.root, 0)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
