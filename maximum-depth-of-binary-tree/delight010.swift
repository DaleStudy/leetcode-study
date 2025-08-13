class Solution {
    func maxDepth(_ root: TreeNode?) -> Int {
        if root == nil {
            return 0
        }
        
        var level = 0
        var stack: [(TreeNode?, Int)] = [(root, 1)]
        
        while !stack.isEmpty {
            let (current, count) = stack.removeLast()
            if current?.left == nil && current?.right == nil {
                level = max(level, count)
            }
            if let right = current?.right {
                stack.append((right, count + 1))
            }
            if let left = current?.left {
                stack.append((left, count + 1))
            }
        }
        
        return level
    }
}
 
