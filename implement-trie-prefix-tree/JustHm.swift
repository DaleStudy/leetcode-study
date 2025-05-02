
class Trie {
    var children: [Character: Trie] = [:]
    var isEndOfWord = false

    func insert(_ word: String) {
        guard !word.isEmpty else { return }
        var node = self
        for char in word {
            if node.children[char] == nil {
                node.children[char] = Trie()
            }
            node = node.children[char]!
        }
        node.isEndOfWord = true
    }

    func search(_ word: String) -> Bool {
        guard let node = findNode(word) else { return false }
        return node.isEndOfWord
    }

    func startsWith(_ prefix: String) -> Bool {
        return findNode(prefix) != nil
    }

    private func findNode(_ word: String) -> Trie? {
        var node = self
        for char in word {
            guard let next = node.children[char] else { return nil }
            node = next
        }
        return node
    }
}
