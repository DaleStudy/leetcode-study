public class TreeNode {
    public var val: Int
    public var left: TreeNode?
    public var right: TreeNode?
    public init() { self.val = 0; self.left = nil; self.right = nil; }
    public init( val: Int) { self.val = val; self.left = nil; self.right = nil; }
    public init( val: Int, * left: TreeNode?, * right: TreeNode?) {
        self.val = val
        self.left = left
        self.right = right
    }
}

class Solution {
    // Time O(n)
    // Space O(n)
    func invertTree(_ root: TreeNode?) -> TreeNode? {
        guard let root = root else {
            return nil
        }

        var queue: [TreeNode] = [root]

        while queue.isEmpty == false {
            let current = queue.removeFirst()

            if let left = current.left {
                queue.append(left)
            }

            if let right = current.right {
                queue.append(right)
            }

            (current.left, current.right) = (current.right, current.left)
        }

        return root
    }
}
 
