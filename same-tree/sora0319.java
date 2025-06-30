public class Solution {
    public boolean isSameTree(TreeNode p, TreeNode q) {
        Stack<TreeNode[]> stack = new Stack<>();
        stack.push(new TreeNode[]{p, q});

        while (!stack.isEmpty()) {
            TreeNode[] nodes = stack.pop();
            TreeNode n1 = nodes[0];
            TreeNode n2 = nodes[1];

            if (n1 == null && n2 == null) {
                continue;
            }
            if (n1 == null || n2 == null) {
                return false;
            }
            if (n1.val != n2.val) {
                return false;
            }
            stack.push(new TreeNode[]{n1.left, n2.left});
            stack.push(new TreeNode[]{n1.right, n2.right});
        }
        return true;
    }
}

