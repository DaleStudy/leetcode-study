# Time Complexity:  O(n) - where n is the length of the word(addWord)
# Space Complexity: O(N) - where N is the total number of characters inserted

class WordDictionary:
    def __init__(self):
        # using a trie (prefix tree) to store all the words
        self.trie = dict()

    def addWord(self, word: str) -> None:
        # start from the root of the trie
        trie = self.trie
        for letter in word:
            # if this letter isn't already in the current trie level, add it
            if letter not in trie:
                trie[letter] = dict()
            # move one level deeper
            trie = trie[letter]
        # mark the end of the word with a special null character
        trie['\0'] = dict()

    def internal_search(self, trie: dict, index: int, word: str) -> bool:
        if index == len(word):
            # check if this path ends a valid word
            return '\0' in trie  

        letter = word[index]
        
        # if hit a '.', gotta try all possible paths from here
        if letter == '.':
            for child in trie.values():
                if self.internal_search(child, index + 1, word):
                    return True
            return False
        else:
            # if the letter exists in the current trie level, keep going
            if letter in trie:
                return self.internal_search(trie[letter], index + 1, word)
            else:
                return False

    def search(self, word: str) -> bool:
        # start the recursive search from index 0 and the root
        return self.internal_search(self.trie, 0, word)
