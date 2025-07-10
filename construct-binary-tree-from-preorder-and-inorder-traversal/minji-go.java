/**
 * <a href="https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/">week15-2. construct-binary-tree-from-preorder-and-inorder-traversal</a>
 * <li>Description: Given two integer arrays preorder and inorder, construct and return the binary tree</li>
 * <li>Topics: Array, Hash Table, Divide and Conquer, Tree, Binary Tree</li>
 * <li>Time Complexity: O(N), Runtime 2ms   </li>
 * <li>Space Complexity: O(N), Memory 44.41MB</li>
 */

class Solution {
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        Map<Integer, Integer> inorderMap = new HashMap<>();
        for (int i = 0; i < inorder.length; i++) {
            inorderMap.put(inorder[i], i);
        }
        return buildTree(preorder, new AtomicInteger(0), inorderMap, 0, inorder.length - 1);
    }

    public TreeNode buildTree(int[] preorder, AtomicInteger index, Map<Integer, Integer> inorderMap, int start, int end) {
        if (start > end) return null;

        int nodeValue = preorder[index.getAndIncrement()];
        TreeNode node = new TreeNode(nodeValue);

        int nodeIndex = inorderMap.get(nodeValue);

        node.left = buildTree(preorder, index, inorderMap, start, nodeIndex - 1);
        node.right = buildTree(preorder, index, inorderMap, nodeIndex + 1, end);

        return node;
    }
}
