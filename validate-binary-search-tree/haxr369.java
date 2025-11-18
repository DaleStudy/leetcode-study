/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
/***
 * dfs로 내려가면서 node와 자녀 노드의 값을 비교하기
 * 다만, 자녀노드는 주어진 범위 내에 있어야한다.
 * sml < childNpde < lrg
 * 
 */
class Solution {
  public boolean isValidBST(TreeNode root) {
    return dfs(root, null, null);
  }

  /**
   * 1. node의 자녀 노드는 sml <= val <= lrg를 항상 만족해야한다.
   * 2. sml, lrg가 null이면 상관 없음
   * 3. node의 val과도 맞게 유지해야한다.
   * 
   * Runtime: 0 ms (Beats 100.00%)
   * Memory: 45.1 MB (Beats 13.09%)
   * Space Complexity: O(N)
   * - 총 노드의 개수를 N이라고 할 때, dfs로 모든 노드 수만큼 스택을 쌓기 때문에
   * > O(N)
   * Time Complexity: O(N)
   * - dfs로 모든 노드를 1회 탐색 O(N)
   * > O(N)
   */
  private boolean dfs(TreeNode node, Integer sml, Integer lrg) {
    TreeNode lN = node.left;
    TreeNode rN = node.right;
    boolean rslt = true;
    // System.out.println("node.val->"+node.val+" sml->"+sml+" lrg->"+lrg+"====IN");
    if (lN != null) {
      // 1. 범위 체크
      if ((sml != null && sml >= lN.val)
          || (lrg != null && lrg <= lN.val)) {
        return false;
      }

      // 2. node와 left 자녀 값 비교
      if (node.val <= lN.val) {
        return false;
      }
      // System.out.println(". lN->"+lN.val);
      // 3. 범위 지정. 앞으로 모든 노드는 node.val 보다 작아야한다.
      rslt = dfs(lN, sml, node.val);
      if (!rslt) {
        return rslt;
      }
    }

    if (rN != null) {
      // 1. 범위 체크
      if ((sml != null && sml >= rN.val)
          || (lrg != null && lrg <= rN.val)) {
        return false;
      }
      // 2. node와 left 자녀 값 비교
      if (node.val >= rN.val) {
        return false;
      }
      // System.out.println(". rN->"+rN.val);
      // 3. 범위 지정. 앞으로 모든 노드는 node.val 보다 커야한다.
      rslt = dfs(rN, node.val, lrg);
      if (!rslt) {
        return rslt;
      }
    }
    // System.out.println("node.val->"+node.val+" sml->"+sml+"
    // lrg->"+lrg+"====OUT");
    return rslt;
  }
}