// 문제 의도를 잘 모르겠음. 깊은 복사가 된 Node를 만들면 된다.
// DFS로 풀면 되고, BFS도 가능하겠지만 BFS는 까딱 잘못하면 타임아웃이 나서 그냥 DFS로 해결
class Solution {
    private Map<Node, Node> visited = new HashMap<>();

    public Node cloneGraph(Node node) {
        if (node == null) return null;

        if (visited.containsKey(node)) {
            return visited.get(node);
        }

        Node cloneNode = new Node(node.val);
        visited.put(node, cloneNode);

        for (Node neighbor : node.neighbors) {
            cloneNode.neighbors.add(cloneGraph(neighbor));
        }

        return cloneNode;
    }
}
