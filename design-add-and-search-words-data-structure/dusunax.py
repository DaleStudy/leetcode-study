'''
# 211. Design Add and Search Words Data Structure

use trie to perform add and search operations on words.
use recursive dfs to search for words with "." wildcards.

## Time and Space Complexity

### addWord

```
TC: O(n)
SC: O(n)
```

### TC is O(n):
- iterating through each character of the word. = O(n)

### SC is O(n):
- storing the word in the trie. = O(n)

### search

```
TC: O(n)
SC: O(n)
```

### TC is O(n):
- dfs iterates through each character of the word. = O(n)
- if char is "."(wildcard) dfs iterates through all children of the current node. = O(n)

> recursion for the wildcard could involve exploring several paths.
> but time complexity is bounded by the length of the word, so it's still O(n).

### SC is O(n):
- length of the word as recursive call stack. = O(n)
'''
class WordDictionary:
    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        node = self.trie
        for char in word: # TC: O(n)
            if char not in node:
                node[char] = {}
            node = node[char] 
        node["$"] = True

    def search(self, word: str) -> bool:
        def dfs(node, i) -> bool:
            if not isinstance(node, dict):
                return False
            if i == len(word):
                return "$" in node if isinstance(node, dict) else False 
            char = word[i]

            if char == ".":
                for child in node.values():
                    if dfs(child, i + 1):
                        return True
                return False
            else:
                return dfs(node[char], i+1) if char in node else False
        
        return dfs(self.trie, 0)
