// TC: O(n)
// -> visit all elements once for each to clone them
// SC: O(n)
// -> all elements are stored in HashMap and values are limited maximum 2
class Solution {
    private Map<Integer, Node> map = new HashMap<>();
    public Node cloneGraph(Node node) {
        if (node == null) return null;
        if (map.containsKey(node.val)) return map.get(node.val);

        Node clone = new Node(node.val);
        map.put(clone.val, clone);

        for (Node neighbor : node.neighbors) {
            clone.neighbors.add(cloneGraph(neighbor));
        }
        return clone;
    }
}
