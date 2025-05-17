class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class Trie:
    # Init Structure
    def __init__(self):
        self.root = TrieNode()        

    # Time Complexity: O(n), n = len(word)
    # Space Complexity: O(n)
    def insert(self, word: str) -> None:
        current = self.root
        for c in word:
            if c not in current.children:
                current.children[c] = TrieNode()
            current = current.children[c]
        current.isEnd = True        

    # Time Complexity: O(n), n = len(word)
    # Space Complexity: O(1)
    def search(self, word: str) -> bool:
        current = self.root
        for c in word:
            if c not in current.children:
                return False
            current = current.children[c]       
        return current.isEnd    # Check whole characters were matched

    # Time Complexity: O(n), n = len(prefix)
    # Space Complexity: O(1)
    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for c in prefix:
            if c not in current.children:
                return False
            current = current.children[c]       
        return True
        

tc = [
    ("insert", "apple", None),
    ("search", "apple", True),
    ("search", "app", False),
    ("startsWith", "app", True),
    ("insert", "app", None),
    ("search", "app", True),
    ("insert", "banana", None),
    ("search", "banana", True),
    ("search", "bananas", False),
    ("startsWith", "ban", True),
    ("startsWith", "baz", False),
    ("search", "", False),
    ("startsWith", "", True)
]

trie = Trie()
for i, (op, value, expected) in enumerate(tc, 1):
    if op == "insert":
        result = trie.insert(value)
    elif op == "search":
        result = trie.search(value)
    elif op == "startsWith":
        result = trie.startsWith(value)
    else:
        result = None  # unknown operation

    if result == expected:
        print(f"TC {i} is Passed!")
    else:
        print(f"TC {i} is Failed! - Op: {op}('{value}'), Expected: {expected}, Result: {result}")
