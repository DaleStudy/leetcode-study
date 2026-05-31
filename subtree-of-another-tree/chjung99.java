// time: O(N^2)
// space: O(N)

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
    public boolean isSubtree(TreeNode root, TreeNode subRoot) {
        Deque<TreeNode> deque = new ArrayDeque<>();
        deque.add(root);

        while (!deque.isEmpty()){
            TreeNode cur = deque.poll();

            if (isEqual(cur, subRoot)) {
                return true;
            }

            if (cur.left != null) deque.add(cur.left);
            if (cur.right != null) deque.add(cur.right);
        }
        return false;
    }

    public boolean isEqual(TreeNode x, TreeNode y){
        Deque<TreeNode> dequeX = new ArrayDeque<>();
        Deque<TreeNode> dequeY = new ArrayDeque<>();

        dequeX.add(x);
        dequeY.add(y);

        while (!dequeX.isEmpty()||!dequeY.isEmpty()){
            TreeNode curX = dequeX.poll();
            TreeNode curY = dequeY.poll();

            if (curX.val != curY.val) return false;

            if (curX.left != null && curY.left != null){
                dequeX.add(curX.left);
                dequeY.add(curY.left);
            } else if (curX.left == null && curY.left == null){
                ;
            } else{
                return false;
            }
            if (curX.right != null && curY.right != null){
                dequeX.add(curX.right);
                dequeY.add(curY.right);
            } else if (curX.right == null && curY.right == null){
                ;
            } else{
                return false;
            }
        }
        return (dequeX.isEmpty() && dequeY.isEmpty());
    }
}

