class WordDictionary {
    let root: TrieNode

    init() {
        root = TrieNode()
    }
    
    func addWord(_ word: String) {
        let spread = Array(word)
        var node = root

        for letter in spread {
            if let child = node.children[letter] {
                node = child
            } else {
                let newNode = TrieNode()
                node.children[letter] = newNode
                node = newNode
            }
        }

        node.isTerminating = true
    }
    
    func search(_ word: String) -> Bool {
        return traverse(root, Array(word), 0)
    }

    private func traverse(_ node: TrieNode, _ quote: [Character], _ starting: Int) -> Bool {
        if starting == quote.count {
            return node.isTerminating
        }

        let letter = quote[starting]

        if letter == "." {
            var result = false

            for key in node.children.keys {
                if let child = node.children[key] {
                    result = result || traverse(child, quote, starting + 1)
                }
            }

            return result
        } else {
            guard let child = node.children[letter] else {
                return false
            }

            return traverse(child, quote, starting + 1)
        }
    }
}

class TrieNode {
    var isTerminating: Bool
    var children: [Character: TrieNode]

    init(isTerminating: Bool = false, children: [Character: TrieNode] = [:]) {
        self.isTerminating = isTerminating
        self.children = children
    }
}

/**
 * Your WordDictionary object will be instantiated and called as such:
 * let obj = WordDictionary()
 * obj.addWord(word)
 * let ret_2: Bool = obj.search(word)
 */
