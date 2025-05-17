class TrieNode {
    var children: [Character: TrieNode] = [:]
    var isEnd: Bool = false
}

class Trie {
    private let root: TrieNode
    
    init() {
        root = TrieNode()
    }
    
    func insert(_ word: String) {
        var current = root
        for char in word {
            if current.children[char] == nil {
                current.children[char] = TrieNode()
            }
            current = current.children[char]!
        }
        current.isEnd = true
    }
    
    func search(_ word: String) -> Bool {
        guard let node = findNode(word) else {
            return false
        }
        return node.isEnd
    }
    
    func startsWith(_ prefix: String) -> Bool {
        return findNode(prefix) != nil
    }
    
    private func findNode(_ prefix: String) -> TrieNode? {
        var current = root
        for char in prefix {
            guard let next = current.children[char] else {
                return nil
            }
            current = next
        }
        return current
    }
}

