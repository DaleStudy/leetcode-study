class Solution {
    // Time O(N^2)
    // Space O(N)
    func buildTree(_ preorder: [Int], _ inorder: [Int]) -> TreeNode? {
        return buildTree(preorder[...], inorder[...])
    }
    
    func buildTree(_ preorder: ArraySlice<Int>, _ inorder: ArraySlice<Int>) -> TreeNode? {
        if preorder.isEmpty {
            return nil
        }
        
        let rootNode = TreeNode(preorder.first!)
        var rootIndex = 0
        
        for (index, value) in inorder.enumerated() {
            if value == rootNode.val {
                rootIndex = index
                break
            }
        }
        rootNode.left = buildTree(preorder[preorder.startIndex + 1..<preorder.startIndex + rootIndex + 1], inorder[inorder.startIndex..<inorder.startIndex + rootIndex])
        rootNode.right = buildTree(preorder[preorder.startIndex + 1 + rootIndex..<preorder.endIndex], inorder[inorder.startIndex + 1 + rootIndex..<inorder.endIndex])
        
        return rootNode
    }
}
 
