// TC: O(n)
// need to visit all nodes
// SC: O(n)
// normally O(log n) required however, O(n) in the worst case
class Solution {
    private List<List<Integer>> output = new ArrayList<>();
    public List<List<Integer>> levelOrder(TreeNode root) {
        dfs(0, root);
        return output;
    }

    private void dfs(int level, TreeNode node) {
        if (node == null) return;

        if (output.size() == level) {
            List<Integer> inside = new ArrayList<>();
            inside.add(node.val);
            output.add(inside);
        } else {
            output.get(level).add(node.val);
        }
        level += 1;
        dfs(level, node.left);
        dfs(level, node.right);
    }
}
