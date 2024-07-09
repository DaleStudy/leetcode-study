//
//  211. Design Add and Search Words Data Structure
//  https://leetcode.com/problems/design-add-and-search-words-data-structure/description/
//  Dale-Study
//
//  Created by WhiteHyun on 2024/06/28.
//

private final class Node {
  var children: [Character: Node]
  var endOfWord: Bool

  init(
    children: [Character: Node] = [:],
    endOfWord: Bool = false
  ) {
    self.children = children
    self.endOfWord = endOfWord
  }
}

final class WordDictionary {
  private let root: Node

  init() {
    root = Node()
  }

  func addWord(_ word: String) {
    var node = root
    for character in word {
      if node.children[character] == nil {
        node.children[character] = Node()
      }
      node = node.children[character]!
    }
    node.endOfWord = true
  }

  func search(_ word: String) -> Bool {
    let word = Array(word)
    func dfs(index: Int, node: Node) -> Bool {
      guard index < word.count else { return node.endOfWord }

      let character = word[index]
      if character == "." {
        return node.children.values.contains { dfs(index: index + 1, node: $0) }
      } else if let nextNode = node.children[character] {
        return dfs(index: index + 1, node: nextNode)
      }
      return false
    }
    return dfs(index: 0, node: root)
  }
}
