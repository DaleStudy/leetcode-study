class Trie:

    def __init__(self):
        self.trie = {}

    def insert(self, word: str) -> None:
        level = self.trie
        
        for i in range(len(word)+1):
            if i==len(word):
                level['end'] = 0
                break
            if word[i] not in level:
                level[word[i]] = {}
            level = level[word[i]]
            
    def search(self, word: str) -> bool:
        level = self.trie

        for char in word:
            if i==len(word):
                if 'end' in level:
                    return True
                else:
                    return False
            if word[i] not in level:
                return False
            level = level[word[i]]

    def startsWith(self, prefix: str) -> bool:
        level = self.trie

        for i in range(len(prefix)+1):
            if i==len(prefix):
                return True
            if prefix[i] not in level:
                return False
            level = level[prefix[i]]
    
