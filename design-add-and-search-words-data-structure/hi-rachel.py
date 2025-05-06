class WordDictionary:

    def __init__(self):
        self.root = {"$": True}
        

    # TC: O(W),  SC: O(W)
    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node:  # 글자가 node에 없으면
                node[ch] = {"$": False}  # 아직 끝이 아님 표시
            node = node[ch]  # 자식 노드로 변경
        node["$"] = True  # 단어 끝 표시


    # TC: O(26^W) => 최악의 경우 영어 알파벳 26개가 각 노드에서 다음 글자가 됨 * 글자수의 비례해서 호출 스택 깊어짐,  SC: O(W)
    def search(self, word: str) -> bool:
        def dfs(node, idx):
            if idx == len(word):
                return node["$"]
            
            ch = word[idx]
            if ch in node:
                return dfs(node[ch], idx + 1)
            if ch == ".":  # 글자가 .이라면
                # 노드의 모든 자식 노드 호출 (어느 경로에서 글자가 일치할지 모르기 때문)
                if any(dfs(node[k], idx + 1) for k in node if k != '$'): 
                    return True
            return False
        
        return dfs(self.root, 0) # 최상위 노드, 최초 idx
        

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
