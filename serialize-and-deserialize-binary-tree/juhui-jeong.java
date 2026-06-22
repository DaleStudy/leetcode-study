
public class Codec {
    private int index;

    // Encodes a tree to a single string.(직렬화)
    public String serialize(TreeNode root) {
        StringBuilder sb = new StringBuilder();
        dfsSerialize(root, sb);
        return sb.toString();
    }

    private void dfsSerialize(TreeNode node, StringBuilder sb) {
        if (node == null) {
            sb.append("null").append(",");
            return;
        }
        sb.append(node.val).append(",");
        
        dfsSerialize(node.left, sb);
        dfsSerialize(node.right, sb);        
    }

    // Decodes your encoded data to tree.(역직렬화)
    public TreeNode deserialize(String data) {
        String[] arr = data.split(",");
        index = 0;
        return dfsDeserialize(arr);
    }

    private TreeNode dfsDeserialize(String[] arr) {
        String value = arr[index++];

        if (value.equals("null")) {
            return null;
        }

        TreeNode node = new TreeNode(Integer.parseInt(value));

        node.left = dfsDeserialize(arr);
        node.right = dfsDeserialize(arr);
        return node;
    }
}
