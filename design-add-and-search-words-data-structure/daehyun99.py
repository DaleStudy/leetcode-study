class WordDictionary:

    def __init__(self):
        self.root = {}
        
    def addWord(self, word: str) -> None:
        pointer = self.root
        for char in word:
            if char in pointer:
                pointer = pointer[char]
            else:
                pointer[char] = {}
                pointer = pointer[char]
        pointer["0"]={}

    def search(self, word: str) -> bool:
        from collections import deque
        pointer = self.root
        que = deque()
        que.append(pointer)

        for char in word:
            for i in range(len(que)):
                pointer = que.popleft()
                if char in pointer:
                    que.append(pointer[char])
                elif char == ".":
                    for key in pointer.keys():
                        que.append(pointer[key])
        while len(que) > 0:
            pointer = que.popleft()
            if "0" in pointer:
                return True
        return False

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
