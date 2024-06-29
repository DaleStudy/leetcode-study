- 문제: https://leetcode.com/problems/course-schedule/
- 풀이: https://algorithm.jonghoonpark.com/2024/03/01/leetcode-207

```java
public class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        if (prerequisites.length == 0) {
            return true;
        }

        Map<Integer, Node> vertexMap = new HashMap<>();

        for (int[] prerequisite : prerequisites) {
            vertexMap.putIfAbsent(prerequisite[0], new Node(prerequisite[0]));
            vertexMap.putIfAbsent(prerequisite[1], new Node(prerequisite[1]));

            Node vertex1 = vertexMap.get(prerequisite[0]);
            Node vertex2 = vertexMap.get(prerequisite[1]);

            vertex1.edges.add(vertex2);
            vertex2.reversedEdges.add(vertex1);
        }

        Deque<Integer> deque = new LinkedList<>();

        int[] degrees = new int[numCourses];
        for (int i = 0; i < degrees.length; i++) {
            Node vertex = vertexMap.get(i);
            if (vertex != null) {
                degrees[i] = vertex.edges.size();
                if (degrees[i] == 0) {
                    deque.addLast(i);
                }
            }
        }

        while(!deque.isEmpty()) {
            int vertexId = deque.removeFirst();
            Node vertex = vertexMap.get(vertexId);
            for (Node node : vertex.reversedEdges) {
                degrees[node.id]--;
                if (degrees[node.id] == 0) {
                    deque.addLast(node.id);
                }
            }
            vertexMap.remove(vertexId);
        }

        return vertexMap.isEmpty();
    }
}

class Node {
    int id;
    List<Node> edges;
    List<Node> reversedEdges;

    public Node(int id) {
        this.id = id;
        edges = new ArrayList<>();
        reversedEdges = new ArrayList<>();
    }
}
```
