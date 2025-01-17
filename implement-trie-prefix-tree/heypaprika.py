# Big-O 예측
# Time : O(n) (n : 단어 개수)
# Space : O(n) 
class Trie:

    def __init__(self):
        self.trie_dict = {}
        self.trie_dict_list = [{}]

    def insert(self, word: str) -> None:
        self.trie_dict[word] = 1
        for i in range(1, len(word) + 1):
            if i > len(self.trie_dict_list) and i > 1:
                self.trie_dict_list.append({})
            self.trie_dict_list[i-1][word[:i]] = 1

    def search(self, word: str) -> bool:
        return word in self.trie_dict

    def startsWith(self, prefix: str) -> bool:
        if len(prefix) > len(self.trie_dict_list):
            return False
        return prefix in self.trie_dict_list[len(prefix)-1]


# Your Trie object will be instantiated and called as such:
trie = Trie()
trie.insert("apple")
trie.search("apple")
trie.search("app")
trie.startsWith("app")
trie.insert("app")
trie.search("app")

# param_2 = trie.search(word)
# param_3 = trie.startsWith(prefix)

