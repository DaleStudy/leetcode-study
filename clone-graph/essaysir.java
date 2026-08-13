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
        if ( node == null ) return null;
        // 똑같은 그래프를 만드는 게 목적
        // node.val -> 숫자( id 로 생각 )
        // neighbors -> 인접한 id 들

        Map<Integer, Node> cloned = new HashMap<>();
        cloned.put(node.val, new Node(node.val));

        Queue<Node> queue = new ArrayDeque<>();
        queue.offer(node);

        while( !queue.isEmpty()){
            Node curNode = queue.poll();
            Node cloneNode = cloned.get(curNode.val);

            for ( Node nei : curNode.neighbors ){
                List<Node> curs = nei.neighbors;

                if (!cloned.containsKey(nei.val)) {
                    cloned.put(nei.val, new Node(nei.val));
                    queue.offer(nei);
                }

                cloneNode.neighbors.add(cloned.get(nei.val));
            }
        }

        return cloned.get(node.val);
    }
}
