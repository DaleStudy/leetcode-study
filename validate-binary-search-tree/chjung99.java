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
    boolean answer = true;
    Deque<Integer> leftStack = new ArrayDeque<>();
    Deque<Integer> rightStack = new ArrayDeque<>();

    public boolean isValidBST(TreeNode root) {
        rightStack.push(root.val);
        dfs(root.left, root, "left");
        rightStack.pop();

        leftStack.push(root.val);
        dfs(root.right, root, "right");
        leftStack.pop();

        return answer;
    }

    public void dfs(TreeNode node, TreeNode parent, String direction) {
        if (node == null) return;

        if (direction.equals("left") && node.val >= parent.val){
            answer = false;
        }
        if (direction.equals("right") && node.val <= parent.val){
            answer = false;
        }
        if (!leftStack.isEmpty() && node.val <= leftStack.peek()) {
            answer = false;
        }
        if (!rightStack.isEmpty() && node.val >= rightStack.peek()) {
            answer = false;
        }

        rightStack.push(node.val);
        dfs(node.left, node, "left");
        rightStack.pop();

        leftStack.push(node.val);
        dfs(node.right, node, "right");
        leftStack.pop();
    }
}


