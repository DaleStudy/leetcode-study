import java.util.*;

// TC: O(V + E)
// SC: O(V)
class Solution {
    public Node cloneGraph(Node node) {
        return deepCopy(node, new HashMap<>());
    }

    private Node deepCopy(Node node, Map<Node, Node> cloned) {
        if (node == null) {
            return null;
        }

        if (cloned.containsKey(node)) {
            return cloned.get(node);
        }

        Node clonedNode = new Node(node.val);
        cloned.put(node, clonedNode);

        for (Node neighbor : node.neighbors) {
            clonedNode.neighbors.add(deepCopy(neighbor, cloned));
        }

        return clonedNode;
    }
}
