class Solution {
    public List<List<Integer>> levelOrder(TreeNode root) {
        if(root == null) {
            return new ArrayList<>();
        }
        List<List<Integer>> list = new ArrayList<>();
        dfs(root, 0, list);
        return list;
    }

    public void dfs(TreeNode node, int depth, List<List<Integer>> list) {
        if(list.size() == depth) {
            list.add(new ArrayList<>());
        }

        List<Integer> dest = list.get(depth);
        dest.add(node.val);

        if(node.left != null) {
            dfs(node.left, depth + 1, list);
        }

        if(node.right != null) {
            dfs(node.right, depth + 1, list);
        }
    }
}
