public class Codec {
    public String serialize(TreeNode root) {
        if (root == null) {
            return "N";
        }
        String left = serialize(root.left);
        String right = serialize(root.right);
        return root.val + "," + left + "," + right;
    }

    public TreeNode deserialize(String data) {
        Deque<String> values = new ArrayDeque<>(Arrays.asList(data.split(",")));
        return dfs(values);
    }

    private TreeNode dfs(Deque<String> values) {
        String value = values.pollFirst();
        if (value.equals("N")) {
            return null;
        }
        TreeNode node = new TreeNode(Integer.parseInt(value));
        node.left = dfs(values);
        node.right = dfs(values);
        return node;
    }
}

