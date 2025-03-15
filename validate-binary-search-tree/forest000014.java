/*
# Time Complexity: O(n)
# Space Complexity: O(n)

BST는 inorder traverse를 하면 오름차순으로 방문해야 함을 활용
*/

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
    public boolean isValidBST(TreeNode root) {
        List<Integer> inorder = new ArrayList<>();

        inorderTraverse(root, inorder);

        for (int i = 1; i < inorder.size(); i++) {
            if (inorder.get(i - 1) >= inorder.get(i)) return false;
        }

        return true;
    }

    private void inorderTraverse(TreeNode root, List<Integer> inorder) {
        if (root == null) return;

        inorderTraverse(root.left, inorder);
        inorder.add(root.val);
        inorderTraverse(root.right, inorder);
    }
}
