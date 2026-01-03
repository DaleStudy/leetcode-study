import java.util.ArrayList;
import java.util.List;

/**
 * Runtime: 25 ms (Beats 72.12%)
 * Memory: 44.35 MB (Beats 34.32%)
 * Space Complexity: O(N)
 * - 모든 노드 저장 => O(N)
 * - visited로 복사했던 노드 관리 => O(N)
 * > O(N)
 * Time Complexity: O(N)
 * - 루트노드부터 모든 노드까지 한번씩 탐색 => O(N)
 * > O(N)
 * 
 */

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
  public Node cloneGraph(Node node) {
    if (node == null) {
      return node;
    }

    if (node.neighbors == null) {
      Node newNode = new Node(node.val, null);
      return newNode;
    } else if (node.neighbors.isEmpty()) {
      Node newNode = new Node(node.val, new ArrayList<>());
      return newNode;
    }

    Node[] visited = new Node[104];

    Node ans = new Node(node.val, new ArrayList<>(node.neighbors));
    visited[ans.val] = ans;
    dfs(ans, visited);

    return ans;
  }

  /**
   * node의 리스트를 dfs로 변경해간다.
   * 다만, 변경했던 노드는 다시 변경하지 않음
   */
  private void dfs(Node node, Node[] visited) {

    List<Node> neighbors = node.neighbors; // 이전 것

    List<Node> newNeighbors = new ArrayList<>(); // 새 껍질
    // 하나씩 새걸로 바꾸자
    for (Node n : neighbors) {
      if (visited[n.val] != null) {
        newNeighbors.add(visited[n.val]);
        continue;
      }
      Node newN = new Node(n.val, new ArrayList<>(n.neighbors)); // 껍질 만들기
      visited[newN.val] = newN;
      dfs(newN, visited); //
      newNeighbors.add(newN);
    }
    node.neighbors = newNeighbors; // 신규 리스트로 바꿔치기
    // printNode(node);
  }

  private void printNode(Node node) {
    System.out.print("val -> " + node.val);
    System.out.println(" size -> " + node.neighbors.size());
    node.neighbors.forEach(n -> System.out.print(n.val));
    System.out.print('\n');
  }
}
