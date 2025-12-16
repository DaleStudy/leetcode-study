class WordDictionary:

    def __init__(self):
        self.trie = {}
        

    def addWord(self, word: str) -> None:
        level = self.trie

        for i in range(len(word)):
            if word[i] not in level:
                level[word[i]] = {}
            level = level[word[i]]
        level['end'] = True
    def search(self, word: str) -> bool:
        def dfs(idx, word, level):
            if idx == len(word):
                if 'end' in level:
                    return True
                else:
                    return False
            if word[idx] == '.':
                for i in level.keys():
                    if i != 'end' and dfs(idx+1, word, level[i]):
                        return True
                return False
            else:
                if word[idx] in level:
                    return dfs(idx+1, word, level[word[idx]])
                else:
                    return False
        return dfs(0, word, self.trie)
    
