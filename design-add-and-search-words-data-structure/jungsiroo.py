class Node:
    def __init__(self, char=None):
        self.is_end = False
        self.children = {}

class WordDictionary:
    """
    트라이를 활용
    기본 문제와 다른 점은 search 할 때 "." 이 포함되어있는 것

    따라서 . 이라면 해당 노드의 모든 자식을 모두 조회해야됨

    addWord
    w = len(word)
    Tc : O(w)
    Sc : O(w)

    search
    최악의 경우 case : xa, xb, xc, xd, .... xz 로 x의 다음 글자가 a~z일 때
    search("x.") 라면 26개 모두를 찾아봐야됨
    Tc : O(26^w)
    Sc : O(w) (글자 길이만큼 재귀를 호출하기에)

    """
    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        now = self.root

        for ch in word:
            if ch not in now.children:
                now.children[ch] = Node(ch)
            now = now.children[ch] 
        now.is_end = True

    def search(self, word: str) -> bool:
        def _recur_search(node, index):
            if index == len(word):
                return node.is_end
            
            if word[index] == ".":
                for ch in node.children:
                    if _recur_search(node.children[ch], index+1):
                        return True
            
            if word[index] in node.children:
                return _recur_search(node.children[word[index]], index+1)
            return False 
        
        return _recur_search(self.root, 0)
            
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

