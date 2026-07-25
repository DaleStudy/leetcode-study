# 1) Tried to come up with the Trie data structure first and then imlement TrieNode. Key factor here is each TrieNode has children array and is_end to connect to its child nodes and end flag. 
# TC: insert, search O(N) where N is len(word), prefix O(L) where L is len(prefix)
# SC: insert O(N) where N is len(word), search/startsWith O(1)
class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.is_end = False

class Trie:

    def __init__(self):
        self.root = TrieNode()     

    # apple
    def insert(self, word: str) -> None:
        cur = self.root

        for c in word:
            idx = ord(c) - ord('a')
            if not cur.children[idx]: 
                cur.children[idx] = TrieNode()
            cur = cur.children[idx]
            
        cur.is_end = True

    # apple
    def search(self, word: str) -> bool:
        cur = self.root

        for c in word:
            idx = ord(c) - ord('a')
            if cur.children[idx]: cur = cur.children[idx]
            else:
                return False
        
        return cur.is_end

    def startsWith(self, prefix: str) -> bool:
        cur = self.root

        for c in prefix:
            idx = ord(c) - ord('a')
            if cur.children[idx]: cur = cur.children[idx]
            else: return False
        
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
