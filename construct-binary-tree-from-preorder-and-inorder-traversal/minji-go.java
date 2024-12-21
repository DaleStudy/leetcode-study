/*
    Problem: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
    Description: Given two integer arrays preorder and inorder, construct and return the binary tree.
    Concept: Array, Hash Table, Divide and Conquer, Tree, Binary Tree
    Time Complexity: O(NM), Runtime 2ms
    Space Complexity: O(N), Memory 45.02MB
*/
import java.util.HashMap;
import java.util.Map;

class Solution {
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        boolean isLeft = true;
        Map<Integer, TreeNode> parents = new HashMap<>();
        TreeNode rootNode = null, parentNode = null;

        for (int pidx=0, iidx=0; pidx<preorder.length; pidx++) {
            int pval = preorder[pidx];
            int ival = inorder[iidx];

            if(pidx==0) {
                rootNode = parentNode = new TreeNode(pval);
            } else if (isLeft) {
                parents.put(pval, parentNode);
                parentNode = parentNode.left = new TreeNode(pval);
            } else {
                isLeft = true;
                parents.put(pval, parentNode);
                parentNode = parentNode.right = new TreeNode(pval);
            }

            if(pval==ival) {
                isLeft = false;
                TreeNode targetNode = parentNode;
                while (iidx<inorder.length-1 && parents.get(parentNode.val)!=null) {
                    if(parentNode.val == inorder[iidx+1]){
                        iidx++;
                        targetNode = parentNode;
                    }
                    parentNode = parents.get(parentNode.val);
                }
                if(iidx<inorder.length-1 && parentNode.val != inorder[iidx+1]){
                    iidx++;
                    parentNode = targetNode;
                } else iidx = iidx+2;
            }
        }

        return rootNode;
    }
}

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
