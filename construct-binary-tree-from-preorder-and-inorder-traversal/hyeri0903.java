/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        /**
        1.preorder, inorder array를 기반으로 binary tree return
        2.constraints
        - 모두 unique values
        - length min = 1, max = 3000
        3.solutions
        - Root node = preorder[0] 
        - inorder 에서 root node 위치 찾기 -> root node 위치 left/right node 
        - inorder 에서 구한 left/right node 수로 preorder array 에서 left/right 나눔

         */

         return buildTree(preorder, 0, preorder.length - 1,
         inorder, 0, inorder.length - 1);
      
    }
    private TreeNode buildTree(int[] preorder, int preStart, int preEnd, 
    int[] inorder, int inStart, int inEnd) {
        if(preStart > preEnd || inStart > inEnd) return null;

        //preorder 첫번째 값 = root node value
        int rootVal = preorder[preStart];
        TreeNode root = new TreeNode(rootVal);

        //inorder 에서 root 찾기
        int rootIndex = 0;
        for(int i = 0; i<inorder.length; i++) {
            if(inorder[i] == rootVal) {
                rootIndex = i;
                break;
            }
        }
        //num of left subtree node
        int leftSize = rootIndex - inStart;
        root.left = buildTree(preorder, preStart+1, preStart + leftSize,
        inorder, inStart, rootIndex - 1);

        root.right = buildTree(preorder, preStart+leftSize+1, preEnd, 
        inorder, rootIndex + 1, inEnd);

        return root;
    }
}
