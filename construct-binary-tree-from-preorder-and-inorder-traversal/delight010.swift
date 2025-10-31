class Solution {
    // Time O(N)
    // Space O(N)
    func buildTree(_ preorder: [Int], _ inorder: [Int]) -> TreeNode? {
        if preorder.isEmpty {
            return nil
        }
        
        let totalCount = preorder.count
        let rootNode = TreeNode(preorder[0])
        var rootIndex = 0
        
        for (index, value) in inorder.enumerated() {
            if value == rootNode.val {
                rootIndex = index
                break
            }
        }
        
        rootNode.left = buildTree(Array(preorder[1..<rootIndex + 1]), Array(inorder[0..<rootIndex + 1]))
        rootNode.right = buildTree(Array(preorder[1 + rootIndex..<totalCount]), Array(inorder[1 + rootIndex..<totalCount]))
        
        return rootNode
    }
}
 
