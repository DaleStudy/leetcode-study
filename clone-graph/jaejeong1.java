import java.util.ArrayList;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.Queue;

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


class Solution {
  // 풀이: BFS 방식으로 그래프를 순회하면서 현재 노드에 연결된 노드들을 복제 여부에 따라 복제 또는 연결 처리해준다
  // TC: O(N)
  // SC: O(N)
  public Node cloneGraph(Node node) {
    if (node == null) {
      return null;
    }

    Map<Node, Node> cloneMap = new HashMap<>();
    Node clone = new Node(node.val);
    cloneMap.put(node, clone);

    Queue<Node> queue = new LinkedList<>();
    queue.add(node);

    while (!queue.isEmpty()) {
      Node current = queue.poll();

      for (Node neighbor : current.neighbors) {
        if (!cloneMap.containsKey(neighbor)) {
          cloneMap.put(neighbor, new Node(neighbor.val));
          queue.add(neighbor);
        }
        cloneMap.get(current).neighbors.add(cloneMap.get(neighbor));
      }
    }
    return clone;
  }
}
