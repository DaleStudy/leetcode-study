/**
 * <a href="https://leetcode.com/problems/serialize-and-deserialize-binary-tree/">week12-4. serialize-and-deserialize-binary-tree </a>
 * <li>Description: Design an algorithm to serialize and deserialize a binary tree          </li>
 * <li>Topics: String, Tree, Depth-First Search, Breadth-First Search, Design, Binary Tree  </li>
 * <li>Time Complexity: O(N), Runtime 14ms      </li>
 * <li>Space Complexity: O(N), Memory 45.44MB   </li>
 */
public class Codec {

    public String serialize(TreeNode root) {
        if (root == null) {
            return null;
        }

        Queue<TreeNode> queue = new LinkedList<>();
        queue.add(root);

        StringBuilder sb = new StringBuilder();
        while (!queue.isEmpty()) {
            TreeNode node = queue.poll();
            if (node == null) {
                sb.append("null,");
                continue;
            }
            sb.append(node.val).append(",");
            queue.add(node.left);
            queue.add(node.right);
        }

        return sb.toString();
    }

    public TreeNode deserialize(String data) {
        if (data == null) {
            return null;
        }

        String[] values = data.split(",");

        TreeNode root = new TreeNode(Integer.parseInt(values[0]));
        Queue<TreeNode> queue = new LinkedList<>();
        queue.add(root);

        int i = 1;
        while (!queue.isEmpty()) {
            TreeNode parent = queue.poll();

            if (!values[i].equals("null")) {
                TreeNode left = new TreeNode(Integer.parseInt(values[i]));
                parent.left = left;
                queue.add(left);
            }
            i++;

            if (!values[i].equals("null")) {
                TreeNode right = new TreeNode(Integer.parseInt(values[i]));
                parent.right = right;
                queue.add(right);
            }
            i++;
        }

        return root;
    }
}
