'''
# 208. Implement Trie (Prefix Tree)

```
- Node structure
{children: {char: {children: { ... }, is_end: False}}, is_end: False}
```

## Time and Space Complexity

```
TC: O(n)
SC: O(n)
```

#### TC is O(n):
- insert, search, startsWith: iterating through the word just once. = O(n)

#### SC is O(n):
- insert, search, startsWith: using a hash map to store the children nodes. = O(n)
'''

class Trie:
    def __init__(self):
        self.root = {"children": {}, "is_end": False}

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node["children"]:
                node["children"][char] = {"children": {}, "is_end": False}
            node = node["children"][char]
        node["is_end"] = True

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node["children"]:
                return False
            node = node["children"][char]
        return node["is_end"]

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node["children"]:
                return False
            node = node["children"][char]
        return True
