
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

    return dfs(p.left, q.left) && dfs(p.right, q.right);
  }
}
