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

 // time : O(n) 
 // space : O(n)
 // n은 트리 노드 수

 class Solution {

    private int i = 0;
    Map<Integer, Integer> map = new HashMap<>();

    public TreeNode buildTree(int[] preorder, int[] inorder) {

        for(int i = 0; i < inorder.length; i++) {
            map.put(inorder[i], i);
        }
        
        return build(preorder, inorder, 0, inorder.length);

    }

    private TreeNode build(int[] preorder, int[] inorder, int start, int end) {
        if(i >= preorder.length || start >= end) {
            return null;
        }

        int value = preorder[i++];
        int index = map.get(value);

        TreeNode leftTreeNode = build(preorder, inorder, start, index);
        TreeNode rightTreeNode = build(preorder, inorder, index+1, end);

        return new TreeNode(value, leftTreeNode, rightTreeNode);
    }

}
