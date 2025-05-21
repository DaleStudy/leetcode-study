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

import java.util.HashMap;
import java.util.Map;

/**
 * 참조 노드는 무방향 그래프에 연결되어있다. 그래프의 deep copy(clone)을 반환하세요.
 */
class Solution {

    // 방문한 노드를 기억할 Map 선언
    Map<Node, Node> visited = new HashMap<>();

    public Node cloneGraph(Node node) {
        return clone(node);
    }

    public Node clone(Node node) {
        if (node == null) {
            return null;
        }

        // 이미 방문했으면 Map에서 꺼내서 반환
        if (visited.containsKey(node)) {
            return visited.get(node);
        }

        // 신규 Node 생성
        Node newNode = new Node(node.val);
        visited.put(node, newNode);

        // 인접 노드 Clone
        if (node.neighbors != null && !node.neighbors.isEmpty()) {
            for (Node neighbor : node.neighbors) {
                newNode.neighbors.add(clone(neighbor));
            }
        }
        return newNode;
    }
}

