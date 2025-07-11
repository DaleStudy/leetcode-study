/**
 * <a href="https://leetcode.com/problems/clone-graph/">week8-3.clone-graph</a>
 * <li>Description: Return a deep copy (clone) of the graph</li>
 * <li>Topics: Hash Table, Depth-First Search, Breadth-First Search, Graph</li>
 * <li>Time Complexity: O(N+E), Runtime 26ms</li>
 * <li>Space Complexity: O(N), Memory 42.77MB</li>
 */

class Solution {
    private Map<Node, Node> map = new HashMap<>();

    public Node cloneGraph(Node node) {
        if(node == null) return null;

        if (map.containsKey(node)) {
            return map.get(node);
        }

        Node clone = new Node(node.val);
        map.put(node, clone);

        for(Node neighbor : node.neighbors) {
            clone.neighbors.add(cloneGraph(neighbor));
        }

        return clone;
    }
}
