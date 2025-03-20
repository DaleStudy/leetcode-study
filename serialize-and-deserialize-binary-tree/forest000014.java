/*
# Time Complexity: O(n)
# Space Complexity: O(n)
*/
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Codec {

    static int idx;

    // Encodes a tree to a single string.
    public String serialize(TreeNode root) {
        if (root == null) return "";

        return dfs(root);
    }

    private String dfs(TreeNode curr) {
        if (curr == null) {
            return ".";
        }

        return curr.val + "," + dfs(curr.left) + "," + dfs(curr.right);
    }

    // Decodes your encoded data to tree.
    public TreeNode deserialize(String data) {
        if ("".equals(data)) return null;

        String[] values = data.split(",");

        idx = 0;
        return dfs2(values);
    }

    private TreeNode dfs2(String[] values) {
        if (".".equals(values[idx])) {
            idx++;
            return null;
        }

        TreeNode curr = new TreeNode(Integer.parseInt(values[idx]));
        idx++;
        curr.left = dfs2(values);
        curr.right = dfs2(values);

        return curr;
    }
}

// Your Codec object will be instantiated and called as such:
// Codec ser = new Codec();
// Codec deser = new Codec();
// TreeNode ans = deser.deserialize(ser.serialize(root));
