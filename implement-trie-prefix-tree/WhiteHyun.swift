//  
//  208. Implement Trie (Prefix Tree)
//  https://leetcode.com/problems/implement-trie-prefix-tree/description/
//  Dale-Study
//  
//  Created by WhiteHyun on 2024/06/28.
//  

// MARK: - Node

private class Node {
  var children: [Character: Node]
  let value: Character
  var isEndOfWord: Bool

  init(children: [Character: Node] = [:], value: Character, isEndOfWord: Bool = false) {
    self.children = children
    self.value = value
    self.isEndOfWord = isEndOfWord
  }
}

// MARK: - Trie

class Trie {
  private var root: Node

  init() {
    root = .init(value: "$")
  }

  func insert(_ word: String) {
    var node = root
    for character in word {
      if node.children[character] == nil {
        node.children[character] = Node(value: character)
      }
      node = node.children[character]!
    }
    node.isEndOfWord = true
  }

  func search(_ word: String) -> Bool {
    var node = root
    for character in word {
      if node.children[character] == nil {
        return false
      }
      node = node.children[character]!
    }
    return node.isEndOfWord
  }

  func startsWith(_ prefix: String) -> Bool {
    var node = root
    for character in prefix {
      if node.children[character] == nil {
        return false
      }
      node = node.children[character]!
    }
    return true
  }
}
