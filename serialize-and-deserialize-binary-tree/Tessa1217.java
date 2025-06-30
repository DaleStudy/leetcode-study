import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;

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

    private StringBuilder sb = new StringBuilder();

    // Encodes a tree to a single string.
    public String serialize(TreeNode root) {
        serializeNode(root);
        return sb.toString();
    }

    private void serializeNode(TreeNode node) {
        // null인 경우 구분 위해 null 문자열 삽입
        if (node == null) {
            sb.append("null,");
            return;
        }
        sb.append(node.val).append(",");
        serializeNode(node.left);
        serializeNode(node.right);
    }

    // Decodes your encoded data to tree.
    public TreeNode deserialize(String data) {
        String[] dataArr = data.split(",");
        Queue<String> queue = new LinkedList<>(Arrays.asList(dataArr));
        return buildTree(queue);
    }

    private TreeNode buildTree(Queue<String> queue) {
        String val = queue.poll();
        if (val.equals("null")) {
            return null;
        }
        TreeNode node = new TreeNode(Integer.parseInt(val));
        node.left = buildTree(queue);
        node.right = buildTree(queue);

        return node;

    }
}

// Your Codec object will be instantiated and called as such:
// Codec ser = new Codec();
// Codec deser = new Codec();
// TreeNode ans = deser.deserialize(ser.serialize(root));

