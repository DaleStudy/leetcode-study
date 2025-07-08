class TreeNode(var `val`: Int = 0) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}


class Solution {

    // TC: O(H) - H: height of BST
    // SC: O(1) - while loop: X stack
    fun lowestCommonAncestor(root: TreeNode?, p: TreeNode?, q: TreeNode?): TreeNode? {

        if (root == null || p == null || q == null) return null
    
        // BST: left < parent < right
        var current = root
        while(current != null){ 
            if(current.`val` < p.`val` && current.`val` < q.`val`){
                current = current.right
            }
            else if(current.`val` > p.`val` && current.`val` > q.`val`){
                current = current.left
            }
            else return current
        }
        
        return null
    }
   
}
