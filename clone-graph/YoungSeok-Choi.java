import java.util.HashMap;
import java.util.Map;

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
    public Map<Node, Node> nMap = new HashMap<>();

    public Node cloneGraph(Node node) {
        if (node == null)
            return null;

        if (nMap.containsKey(node)) {
            return nMap.get(node);
        }

        Node clone = new Node(node.val);
        nMap.put(node, clone);

        for (Node nei : node.neighbors) {
            clone.neighbors.add(cloneGraph(nei));
        }

        return clone;
    }
}

class WrongSolution {
    public Node graph;
    public Map<Node, Node> nMap = new HashMap<>();

    public Node cloneGraph(Node node) {
        if (node == null)
            return null;

        graph = new Node(node.val);
        nMap.put(node, graph);

        // print(graph);

        return clone(node, graph);
    }

    public Node clone(Node node, Node cur) {
        for (int i = 0; i < node.neighbors.size(); i++) {
            Node adj = node.neighbors.get(i);

            if (nMap.containsKey(adj)) {
                return nMap.get(adj);
            }

            nMap.put(adj, new Node(adj.val));
            cur.neighbors.add(nMap.get(adj));
            clone(adj, nMap.get(adj));
        }

        return cur;
    }

    public void print(Node node) {
        System.out.println("visit " + node.val);

        for (int i = 0; i < node.neighbors.size(); i++) {
            Node adj = node.neighbors.get(i);
            System.out.println("nei " + adj.val);
            print(adj);
        }
    }
}
