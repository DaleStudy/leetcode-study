import java.util.*;

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
    final int NULL_MARKER = Integer.MIN_VALUE;
    public boolean isSameTree(TreeNode p, TreeNode q) {
        Queue<Integer> OrderP = new ArrayDeque<>();
        Queue<Integer> OrderQ = new ArrayDeque<>();
        trevasalTree(p, OrderP);
        trevasalTree(q, OrderQ);

        if (OrderP.size() != OrderQ.size()) return false;

        while (!OrderP.isEmpty() && !OrderQ.isEmpty()){
            Integer a = OrderP.poll();
            Integer b = OrderQ.poll();
            if (!a.equals(b)) return false;
        }

        return OrderP.isEmpty() && OrderQ.isEmpty();
    }
    public void trevasalTree(TreeNode t, Queue<Integer> queue){
        // System.out.print(t.val+ " ");
        if (t == null){
            queue.add(NULL_MARKER);
            return;
        }
        queue.add(t.val);
        trevasalTree(t.left, queue);
        trevasalTree(t.right, queue);

    }
}

