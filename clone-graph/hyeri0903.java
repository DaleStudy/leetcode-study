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
    //key: original node, value: clone node
    private Map<Node, Node> map = new HashMap<>();

    public Node cloneGraph(Node node) {
        if(node == null) {
            return null;
        }
        //이미 존재하면 return
        if(map.containsKey(node)) {
            return map.get(node);
        }

        //현재 노드 복제
        Node clone = new Node(node.val);
        map.put(node, clone);

        //이웃 노드들 복제해서 연결
        for(Node neighbor: node.neighbors) {
            clone.neighbors.add(cloneGraph(neighbor));
        }
        return clone;
    }
}
