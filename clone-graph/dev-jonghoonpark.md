- 문제: https://leetcode.com/problems/clone-graph/
- 풀이: https://algorithm.jonghoonpark.com/2024/02/13/leetcode-133

```java
class Solution {
    public Node cloneGraph(Node node) {
        return cloneGraph(new HashMap<>(), node);
    }

    private Node cloneGraph(Map<Integer, Node> map, Node node) {
        if(node == null) {
            return null;
        }

        if (map.containsKey(node.val)) {
            return map.get(node.val);
        }

        Node copy = new Node(node.val);
        map.put(node.val, copy);

        for (int i = 0; i < node.neighbors.size(); i++) {
            Node neighborNode = node.neighbors.get(i);
            copy.neighbors.add(map.getOrDefault(neighborNode.val, cloneGraph(map, node.neighbors.get(i))));
        }

        return copy;
    }
}
```

### TC, SC

node(vertex)의 수를 `V`, edge의 수를 `E` 라고 하였을 때 각 노드 마다 edge의 수만큼 반복을 해야한다.
시간 복잡도는 `O(V + E)` 이다. 공간 복잡도는 `O(V)`이다.
