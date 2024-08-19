//  
//  102. Binary Tree Level Order Traversal
//  https://leetcode.com/problems/binary-tree-level-order-traversal/description/
//  Dale-Study
//  
//  Created by WhiteHyun on 2024/06/12.
//  

// MARK: - Node

private class Node<T> {
  let element: T
  var next: Node<T>?

  init(element: T, next: Node<T>? = nil) {
    self.element = element
    self.next = next
  }
}

// MARK: - Queue

final class Queue<T> {
  private var head: Node<T>?
  private var tail: Node<T>?
  private var count: Int = 0

  var isEmpty: Bool {
    count == 0
  }

  func enqueue(_ element: T) {
    let newNode = Node(element: element)

    if let tailNode = tail {
      tailNode.next = newNode
    } else {
      head = newNode
    }

    tail = newNode
    count += 1
  }

  func dequeue() -> T? {
    guard let headNode = head
    else {
      return nil
    }

    let element = headNode.element
    head = headNode.next

    if head == nil {
      tail = nil
    }

    count -= 1
    return element
  }

  func peek() -> T? {
    head?.element
  }

  func clear() {
    head = nil
    tail = nil
    count = 0
  }
}

// MARK: ExpressibleByArrayLiteral

extension Queue: ExpressibleByArrayLiteral {
  convenience init(arrayLiteral elements: T...) {
    self.init()
    for element in elements {
      enqueue(element)
    }
  }
}

class Solution {
  func levelOrder(_ root: TreeNode?) -> [[Int]] {
    guard let root else { return [] }
    var array: [[Int]] = []
    let queue: Queue<(node: TreeNode, layer: Int)> = [(root, 0)]

    while let (node, layer) = queue.dequeue() {
      // array index 범위에 layer가 들어있지 않으면, 마지막 요소에 빈 배열 추가
      if (array.indices ~= layer) == false {
        array.append([])
      }
      array[layer].append(node.val)

      if node.left != nil {
        queue.enqueue((node.left!, layer + 1))
      }
      if node.right != nil {
        queue.enqueue((node.right!, layer + 1))
      }
    }

    return array
  }
}
