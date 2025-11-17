/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public var val: Int
 *     public var left: TreeNode?
 *     public var right: TreeNode?
 *     public init(_ val: Int) {
 *         self.val = val
 *         self.left = nil
 *         self.right = nil
 *     }
 * }
 */

class Codec {
    // O(n) time / O(n) space
    func serialize(_ root: TreeNode?) -> String {
        var serializedNodes = [String]()
        var queueNodes = [TreeNode?]()
        queueNodes.append(root)
        var head = 0
        
        while head < queueNodes.count {
            let node = queueNodes[head]
            head += 1
            
            if let node {
                serializedNodes.append("\(node.val)")

                queueNodes.append(node.left)
                queueNodes.append(node.right)
            } else {
                serializedNodes.append("null")
            }
            
        }
        
        return serializedNodes.joined(separator: ",")
    }
    
    // O(n) time / O(n) space
    func deserialize(_ data: String) -> TreeNode? {
        let serializedTree = data
        var nodeVals = serializedTree.split(separator: ",")
        
        guard let first = nodeVals.first,
           let firstVal = Int(first) else {
            return nil
        }
        
        let root = TreeNode(firstVal)
        var queueNodes = [TreeNode]()
        queueNodes.append(root)
        var head = 0
        var isLeft = true
        
        for i in 1..<nodeVals.count {
            let node = queueNodes[head]
            let stringValue = nodeVals[i]
            let val = Int(stringValue)
            
            if isLeft {
                if let val {
                    let leftNode = TreeNode(val)
                    node.left = leftNode
                    queueNodes.append(leftNode)
                } else {
                    node.left = nil
                }
            } else {
                if let val {
                    let rightNode = TreeNode(val)
                    node.right = rightNode
                    queueNodes.append(rightNode)
                } else {
                    node.right = nil
                }
                head += 1
            }
            isLeft.toggle()
        }
        
        return root
    }
}


