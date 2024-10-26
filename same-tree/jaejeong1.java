
//  Definition for a binary tree node.
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

class Solution {

  public boolean isSameTree(TreeNode p, TreeNode q) {
    // 풀이: 재귀로 left와 right를 비교하면서 같은지 확인한다.
    // TC: O(N)
    // SC: O(N)
    return dfs(p, q);
  }

  private boolean dfs(TreeNode p, TreeNode q) {
    if (p == null || q == null) {
      return p == q; // 둘 다 null이면 true, 하나만 null이면 false
    }

    if (p.val != q.val) { // 값이 다르면 false
      return false;
    }

    if (p.left != null && !dfs(p.left, q.left)) { // 둘 중 하나만 null인 케이스는 위에서 걸러져, p.left 하나만 null 여부를 체크하면 npe 방지할 수 있다
      return false; // 둘다 null이 아닐때만 dfs 값비교를 하고, 결과가 false 라면 false 반환하고 중단
    }

    if (p.right != null && !dfs(p.right, q.right)) {
      return false;
    }

    return true; // 값이 다른 케이스가 없으면 true 반환
  }
}
