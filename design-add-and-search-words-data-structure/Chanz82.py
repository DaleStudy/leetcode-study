class WordDictionary:

    def __init__(self):
        self.word_tree = {}

    def addWord(self, word: str) -> None:
        curr_branch = self.word_tree
        for ch in word:
            if not curr_branch.get(ch, None):
                curr_branch[ch] = {}
            curr_branch = curr_branch[ch]
        curr_branch["#"] = {} # end of word

    def search(self, word: str) -> bool:
        curr_branch = self.word_tree

        def nested_search(start_branch: dict, word: str) -> bool:
            
            for idx, ch in enumerate(word):
                if ch in start_branch:
                    start_branch = start_branch[ch]
                elif ch == ".":
                    for branch in start_branch.values():
                        if nested_search(branch, word[idx+1:]):
                            return True
                    return False
                else:
                    return False

            if "#" in start_branch:
                return True

            return False

        return nested_search(curr_branch, word)        

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
