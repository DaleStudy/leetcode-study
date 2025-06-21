import leetcode_study.TreeNode;

import java.util.AbstractMap;
import java.util.Map;

/**
 * <a href="https://leetcode.com/problems/same-tree/description/">week12-1. same-tree</a>
 * <li>Description: Given the roots of two binary trees p and q, check if they are the same or not </li>
 * <li>Topics: Tree, Depth-First Search, Breadth-First Search, Binary Tree </li>
 * <li>Time Complexity: O(N), Runtime 0ms     </li>
 * <li>Space Complexity: O(N), Memory 41.14MB </li>
 */
class Solution {
    public boolean isSameTree(TreeNode p, TreeNode q) {
        Queue<Map.Entry<TreeNode, TreeNode>> queue = new LinkedList<>();
        queue.add(new AbstractMap.SimpleEntry<>(p, q));

        while (!queue.isEmpty()) {
            Map.Entry<TreeNode, TreeNode> nodeMap = queue.poll();
            TreeNode nodeP = nodeMap.getKey();
            TreeNode nodeQ = nodeMap.getValue();

            if (nodeP == null && nodeQ == null) {
                continue;
            }
            if (nodeP == null || nodeQ == null || nodeP.val != nodeQ.val) {
                return false;
            }

            queue.add(new AbstractMap.SimpleEntry<>(nodeP.left, nodeQ.left));
            queue.add(new AbstractMap.SimpleEntry<>(nodeP.right, nodeQ.right));
        }

        return true;
    }
}
