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

/*
 * time: O(N+M), where N is the number of nodes and M is the number of edges.
 * space: O(N), N is the space for the `visited` hash map.
 */
class Solution {
    private Map<Node, Node> visited = new HashMap<>();

    public Node cloneGraph(Node node) {
        if (node == null) {
            return node;
        }

        if (visited.containsKey(node)) {
            return visited.get(node);
        }

        Node cloned = new Node(node.val, new ArrayList());
        visited.put(node, cloned);

        for (Node neighbor : node.neighbors) {
            cloned.neighbors.add(cloneGraph(neighbor));
        }
        return cloned;
    }
}
