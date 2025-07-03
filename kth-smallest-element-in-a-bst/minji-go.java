/**
 * <a href="https://leetcode.com/problems/kth-smallest-element-in-a-bst/">week13-3. kth-smallest-element-in-a-bst</a>
 * <li>Description: Given the root of a binary search tree, and an integer k, return the kth smallest value</li>
 * <li>Topics: Tree, Depth-First Search, Binary Search Tree, Binary Tree</li>
 * <li>Time Complexity: O(N), Runtime 0ms   </li>
 * <li>Space Complexity: O(H), Memory 44.5MB</li>
 * <li>Note: If the BST is modified often (with frequent insertions or deletions), consider using an Augmented BST, Segment Tree, or TreeMap with additional metadata to efficiently support dynamic updates and k-th smallest queries in logarithmic time. </li>
 */
class Solution {
    public int kthSmallest(TreeNode root, int k) {
        return inorder(root, new AtomicInteger(k));
    }

    public Integer inorder(TreeNode node, AtomicInteger k) {
        if (node == null) {
            return null;
        }

        Integer value = inorder(node.left, k);
        if (value != null) {
            return value;
        }

        if (k.decrementAndGet() == 0) {
            return node.val;
        }

        return inorder(node.right, k);
    }

}
