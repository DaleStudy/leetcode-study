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
            1. understanding
            - preorder: mid -> left -> right
            - inorder: left -> mid -> right
            - so, first element of the preorder array is always mid node.
            - if the idx of inorder's 1st depth mid node is k, then inorder[0:k-1] is the left tree part array. And also, preorder[k:] is the right tree part.
            2. strategy
            - find the inorder's mid node idx, and then split left tree part and right part, buildTree with each preorder and inorder part.

            3. complexity
            - time: O(N^2) 
            - space: O(N^2)
        */
        if (preorder.length == 0) return null;
        if (preorder.length == 1) return new TreeNode(preorder[0]);
        int i = 0;
        List<Integer> leftPreorder = new ArrayList<>(); // O(N)
        List<Integer> leftInorder = new ArrayList<>(); // O(N)
        List<Integer> rightPreorder = new ArrayList<>(); // O(N)
        List<Integer> rightInorder = new ArrayList<>(); // O(N)
        for (; i < inorder.length; i++) { // O(N)
            if (inorder[i] == preorder[0]) break;
            leftPreorder.add(preorder[i+1]);
            leftInorder.add(inorder[i]);
        }
        for (int idx = i+1; idx < inorder.length; idx++) { // O(N)
            rightPreorder.add(preorder[idx]);
            rightInorder.add(inorder[idx]);
        }

        return new TreeNode(preorder[0], buildTree(leftPreorder.stream().mapToInt(Integer::intValue).toArray(), leftInorder.stream().mapToInt(Integer::intValue).toArray()), buildTree(rightPreorder.stream().mapToInt(Integer::intValue).toArray(), rightInorder.stream().mapToInt(Integer::intValue).toArray()));
    }
}

