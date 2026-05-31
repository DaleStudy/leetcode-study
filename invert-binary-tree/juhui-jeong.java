/*
이전 풀이
 * 시간 복잡도: O(n)
 * 공간 복잡도: O(n)
 */
public class Solution {
    public TreeNode invertTree(TreeNode root) {
        if (root == null) {
            return null;
        }

        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);

        while (!queue.isEmpty()) {
            TreeNode cur = queue.poll();

            TreeNode temp = cur.left;
            cur.left = cur.right;
            cur.right = temp;

            if (cur.left != null) {
                queue.offer(cur.left);
            }

            if (cur.right != null) {
                queue.offer(cur.right);
            }
        }

        return root;
    }
}

/**
 * 시간 복잡도: O(n)
 * 공간 복잡도: O(n)
 * DFS 풀이
 */
class Solution {
    public TreeNode invertTree(TreeNode root) {
        if (root == null) return null;

        Deque<TreeNode> stack = new ArrayDeque<>();
        stack.push(root);

        while(!stack.isEmpty()) {
            TreeNode cur = stack.pop();
            
            TreeNode temp = cur.left;
            cur.left = cur.right;
            cur.right = temp;
 
            if (cur.left != null) stack.push(cur.left);

            if (cur.right != null) stack.push(cur.right);
        }
        return root;
    }
}
