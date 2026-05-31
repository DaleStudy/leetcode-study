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
    public Node cloneGraph(Node node) {
        if (node == null) return node;
        return deepCopy(node);
    }

    public Node deepCopy(Node node) {
        Deque<Node> deque = new ArrayDeque<>();
        Node root = new Node(node.val, new ArrayList<>());
        Map<Integer, Node> visit = new HashMap<>();

        visit.put(1, root);
        deque.add(node);

        while (!deque.isEmpty()) {
            Node cur = deque.poll();
            for (Node next: cur.neighbors) {
                if (!visit.containsKey(next.val)){
                    visit.put(next.val, new Node(next.val, new ArrayList<>()));
                    deque.add(next);
                }
                visit.get(cur.val).neighbors.add(visit.get(next.val));
            }
        }
        return root;
    }
}


