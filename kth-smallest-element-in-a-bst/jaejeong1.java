import java.util.ArrayList;
import java.util.List;

// Definition for a binary tree node.
class TreeNode {
     int val;
     TreeNode left;
     TreeNode right;
     TreeNode() {}
     TreeNode(int val) { this.val = val; }
     TreeNode(int val, TreeNode left, TreeNode right) {
         this.val = val;
         this.left = left;
         this.right = right;
     }
 }
class SolutionKthSmallest {
  public int kthSmallest(TreeNode root, int k) {
    // 이진 검색 트리의 루트와 정수 k가 주어지면 트리에 있는 모든 노드 값 중 k번째로 작은 값(1-인덱스)을 반환합니다.
    // 이진 검색 트리의 특성을 이용해 중위 순회를 하면 노드 값이 오름차순으로 정렬된다.
    // 정렬 후 k번째 값을 반환한다.
    // 시간복잡도: O(N), 공간복잡도: O(N)
    List<Integer> list = new ArrayList<>();
    inorder(root, list);
    return list.get(k - 1);
  }

  private void inorder(TreeNode root, List<Integer> list) {
    if (root == null) {
      return;
    }
    inorder(root.left, list);
    list.add(root.val);
    inorder(root.right, list);
  }
}
