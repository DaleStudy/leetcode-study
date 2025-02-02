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
    Map<Integer, Node> nodeMap = new HashMap<>();
    if(node == null) return null;
    boolean[] visited = new boolean[101];
    dfsHelper(nodeMap, node, visited);
    return nodeMap.get(1);
  }

  private void dfsHelper(Map<Integer, Node> map, Node node, boolean[] visited) {
    if(!map.containsKey(node.val)) {
      map.put(node.val, new Node(node.val));
    }
    visited[node.val] = true;
    Node cur = map.get(node.val);
    for(Node adjacent : node.neighbors) {
      map.putIfAbsent(adjacent.val, new Node(adjacent.val));
      cur.neighbors.add(map.get(adjacent.val));
      if(!visited[adjacent.val]) dfsHelper(map, adjacent, visited);
    }
  }
}
