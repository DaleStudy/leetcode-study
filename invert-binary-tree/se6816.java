class Solution {
    public TreeNode invertTree(TreeNode root) {
        if(root == null) return root;
        Queue<TreeNode> que = new ArrayDeque<>();
        que.add(root);

        while(!que.isEmpty()) {
            TreeNode node = que.poll();
            TreeNode tempNode = node.left;
            node.left = node.right;
            node.right = tempNode;
            if(node.left != null) {
                que.add(node.left);
            }
            if(node.right != null) {
                que.add(node.right);
            }
        }
        return root;
    }
}
