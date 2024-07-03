- 문제
  - 유료: https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/
  - 무료: https://neetcode.io/problems/count-connected-components
- 풀이: https://algorithm.jonghoonpark.com/2024/07/03/leetcode-323

```java
public class Solution {
    public int countComponents(int n, int[][] edges) {
        Map<Integer, Vertex> vertexMap = new HashMap<>();
        int lastGroupId = 0;

        for (int[] edge : edges) {
            Vertex v1 = vertexMap.getOrDefault(edge[0], new Vertex(edge[0]));
            Vertex v2 = vertexMap.getOrDefault(edge[1], new Vertex(edge[1]));

            v1.edges.add(v2);
            v2.edges.add(v1);

            vertexMap.put(edge[0], v1);
            vertexMap.put(edge[1], v2);
        }

        for (int i = 0; i < n; i++) {
            Vertex vertex = vertexMap.get(i);
            if (vertex == null) {
                lastGroupId++;
            } else {
                // 0 이 아닐 경우는 이미 탐색한 케이스므로 스킵
                if (vertex.groupId == 0) {
                    lastGroupId++;
                    dfs(vertex, lastGroupId);
                }
            }
        }

        return lastGroupId;
    }

    public void dfs(Vertex vertex, int groupId) {
        vertex.groupId = groupId;
        for (Vertex connected : vertex.edges) {
            if (connected.groupId == 0) {
                dfs(connected, groupId);
            }
        }
    }
}

class Vertex {
    int id;
    int groupId;
    List<Vertex> edges;

    public Vertex(int id) {
        this.id = id;
        this.edges = new ArrayList<>();
    }
}
```

### TC, SC

Vertex 의 수를 V, Edge 의 수를 E 라고 하였을 때,
시간 복잡도는 O(V + E), 공간 복잡도는 O(V + E) 이다.
