import java.util.*;
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


    //기존 node, 복사한 node
    Map<Node, Node> visited = new HashMap<>();
    public Node cloneGraph(Node node) {
        if (node==null) return null;

        if (visited.containsKey(node)){
            return visited.get(node);
        }

        //없는 경우
        Node newClone= new Node(node.val);
        visited.put(node, newClone);

        //이웃 복사
        for(Node target : node.neighbors){
            newClone.neighbors.add(cloneGraph(target));
        }

        return newClone;

    }
}


