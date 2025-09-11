/*
// Definition for a Node.
class Node {
    public int val;
    public List<Node> neighbors;
    public Node() {
        val = 0;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val) {
        val = _val;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val, ArrayList<Node> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
}
*/

class Solution {
    HashMap<Node, Node> nodeMap = new HashMap<>(); // key: original Node, value: copied Node

    public Node cloneGraph(Node node) {
        if (node == null) return null;

        if (nodeMap.containsKey(node)) {
            return nodeMap.get(node);
        }

        Node newNode = new Node(node.val);
        nodeMap.put(node, newNode);

        for (Node neighborNode : node.neighbors) {
            newNode.neighbors.add(cloneGraph(neighborNode));
        }

        return newNode;
    }
}
