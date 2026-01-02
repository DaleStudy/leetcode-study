class Trie {
    private let root: TrieNode

    init() {
        self.root = TrieNode()
    }
    
    func insert(_ word: String) {
        var node = root // 루트 노드의 포인터를 가져오고

        // 단어의 각 글자를 순회하며, 이미 있다면 해당 노드로 이동하고,
        // 그렇지 않다면 새로운 노드를 생성하여 연결
        for letter in word {
            if let childNode = node.children[letter] {
                node = childNode
            } else {
                let newNode = TrieNode()
                node.children[letter] = newNode
                node = newNode
            }
        }

        // 단어의 마지막 글자 노드에 isTerminating을 true로 설정
        node.isTerminating = true
    }
    
    func search(_ word: String) -> Bool {
        var node = root

        // 노드 포인터만 제공하여 순회 로직을 수행하고,
        // 마지막 노드가 isTerminating이 true인지 확인
        guard traverse(startsWith: &node, quote: word) else { return false }
        guard node.isTerminating else { return false }

        return true
    }
    
    func startsWith(_ prefix: String) -> Bool {
        var node = root
        // 노드 포인터만 제공하여 순회 로직을 수행하고 그대로 반환
        return traverse(startsWith: &node, quote: prefix)
    }

    // 트리 탐색 로직
    // 노드 포인터를 받아서, 순회 로직을 수행하고 포인터를 교체
    private func traverse(startsWith node: inout TrieNode, quote: String) -> Bool {
        for letter in quote {
            guard let childNode = node.children[letter] else {
                return false
            }

            node = childNode
        }

        return true
    }
}

// 트라이의 각각의 노드 구현
// 자식 노드 딕셔너리와, 이 글자로 끝나는 단어가 있는지 여부를 저장
// 글자 자체는 부모 노드 딕셔너리의 키로 저장되므로 따로 저장하지 않음
// 루트에는 아무 글자도 들어가지 않는다는 Trie의 조건도 자동으로 만족
class TrieNode {
    var children: [Character: TrieNode]
    var isTerminating: Bool

    init(children: [Character: TrieNode] = [:], isTerminating: Bool = false) {
        self.children = children
        self.isTerminating = isTerminating
    }
}

/**
 * Your Trie object will be instantiated and called as such:
 * let obj = Trie()
 * obj.insert(word)
 * let ret_2: Bool = obj.search(word)
 * let ret_3: Bool = obj.startsWith(prefix)
 */
