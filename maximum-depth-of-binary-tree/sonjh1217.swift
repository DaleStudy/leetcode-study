class Solution {
    func maxDepthStack(_ root: TreeNode?) -> Int {
        guard let root = root else {
            return 0
        }
        var searchStack = [(TreeNode, Int)]()
        searchStack.append((root, 1))
        var maxDepth = 1

        while searchStack.isEmpty == false {
            guard let popped = searchStack.popLast() else {
                break
            }
            maxDepth = max(popped.1, maxDepth)
            
            if let left = popped.0.left {
                searchStack.append((left, popped.1 + 1))
            }
            
            if let right = popped.0.right {
                searchStack.append((right, popped.1 + 1))
            }
        }
        
        return maxDepth
        
        //시간복잡도 O(n)
        //공간복잡도 O(n)
    }
    
    func maxDepthRecursion(_ root: TreeNode?) -> Int {
        guard let root = root else {
            return 0
        }
        
        return max(maxDepth(root.left), maxDepth(root.right)) + 1
        
        //시간복잡도 O(n)
        //공간복잡도 O(n)
    }
}

