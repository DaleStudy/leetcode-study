
// Definition for a Node.

import java.util.ArrayList;
import java.util.Map;

/* 
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

    // <원본, 복제본>
    public Map<Node,Node> map = new HashMap<>();

    public Node cloneGraph(Node node) {
    
      if (node == null) {
        return null;
      }

      return dfs(node);
    }

    public Node dfs(Node origin) {
        if (map.containsKey(origin)) {
            return map.get(origin);
        }

        if (origin == null) {
            return null;
        }

        Node copied = new Node(origin.val);
        map.put(origin, copied);
        
        for (Node n : origin.neighbors) {
            Node neighbor = dfs(n);
            copied.neighbors.add(neighbor);
        }

        return copied;
    }
}
