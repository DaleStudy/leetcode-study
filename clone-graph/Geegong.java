import java.util.*;

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
public class Geegong {

    /**
     * dfs 방식으로 풀이
     * visited 로 memoization 하여 방문해서 복사가 된 노드들을 저장
     * 한번 방문했던 노드를 neighbors 탐색을 통해 또 방문하게 되면 visited 에서 꺼내서 return 하도록 한다.
     *
     * time complexity : O(2N) -> O(N)
     * space complexity : O(N)
     * @param node
     * @return
     */
    public Node cloneGraph(Node node) {
        // node에 진입한 순간에 바로 visited 에 넣어서 cloned 된 node 들을 집어넣도록 관리
        Map<Integer, Node> visited = new HashMap<>();

        if (node == null) {
            return null;
        }

        Node result = cloneDeeply(node, visited);
        return result;
    }

    public Node cloneDeeply(Node origin, Map<Integer, Node> visited) {

        // visited 에는 cloned 된 node 들을 저장하고 있어 한번 방문했던 노드라면 복사한 노드를 리턴한다.
        if (visited.containsKey(origin.val)) {
            return visited.get(origin.val);
        }

        Node clonedTarget = new Node(origin.val);
        visited.put(origin.val, clonedTarget);

        for (Node neighbor : origin.neighbors) {
            Node clonedNeighbor = cloneDeeply(neighbor, visited);
            clonedTarget.neighbors.add(clonedNeighbor);
        }

        return clonedTarget;
    }


    // 이미 다른 분들이 Node 클래스를 많이 만들어놓으셔서.. 개인 클래스 안에 이너 클래스로 Node 만듬
    public static class Node {
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
}


