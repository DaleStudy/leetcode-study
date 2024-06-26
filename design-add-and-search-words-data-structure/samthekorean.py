# n: number of words | m: length of the word
# TC: O(n*m)
# SC: O(n*m)


class TrieNode:
    def __init__(self):
        self.children = {}  # Dictionary to store child TrieNodes
        self.is_word = False  # Flag to indicate if a word ends at this node


class WordDictionary:
    def __init__(self):
        # Initialize WordDictionary with a root TrieNode.
        self.root = TrieNode()

    def addWord(self, word):
        # Add a word to the Trie.
        current_node = self.root

        # Traverse each character in the word
        for character in word:
            # Create a new TrieNode if the character doesn't exist in children
            current_node = current_node.children.setdefault(character, TrieNode())

        # Mark the end of the word at the last character's node
        current_node.is_word = True

    def search(self, word):

        def dfs(node, index):
            if index == len(word):
                # If reached end of the word, check if current node marks the end of a word
                return node.is_word

            if word[index] == ".":
                # Handle wildcard character '.': Try all possible children
                for child in node.children.values():
                    if dfs(child, index + 1):
                        return True
            elif word[index] in node.children:
                # Regular character: Move to the next node
                return dfs(node.children[word[index]], index + 1)

            # If no match found, return False
            return False

        # Start DFS from the root of the Trie
        return dfs(self.root, 0)
