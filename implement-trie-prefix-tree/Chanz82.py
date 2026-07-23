class Trie:

    def __init__(self):
        self.root_map = dict()

    def insert(self, word: str) -> None:
        idx = 0
        search_map = self.root_map
        while idx < len(word):
            key = ord(word[idx])
            if key not in search_map:
                search_map[key] = dict()
            search_map = search_map[key]
            idx += 1
        search_map['#'] = True

    def search(self, word: str) -> bool:
        idx = 0
        search_map = self.root_map
        while idx < len(word):
            key = ord(word[idx])
            if key not in search_map:
                return False
            search_map = search_map[key]
            idx += 1
        return '#' in search_map


    def startsWith(self, prefix: str) -> bool:
        idx = 0
        search_map = self.root_map
        while idx < len(prefix):
            key = ord(prefix[idx])
            if key not in search_map:
                return False
            search_map = search_map[key]
            idx += 1
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
