// 시간 복잡도 O(n) - n은 트리의 노드 개수
// 공간 복잡도 O(h) - h는 트리의 높이 (재귀 호출 스택 공간)
public class TreeNode{
  int val;
  TreeNode left;
  TreeNode right;

  TreeNode(int x) {
    val = x;
  }
}
class Solution{
  public boolean isValidBST(TreeNode root) {
    return isValidBSTHelper(root, Long.MIN_VALUE, Long.MAX_VALUE);
  }
  private boolean isValidBSTHelper(TreeNode node, long min, long max) {
    if (node == null) {
      return true;
    }
    if (node.val <= min || node.val >= max) {
      return false;
    }
    return isValidBSTHelper(node.left, min, node.val) && isValidBSTHelper(node.right, node.val, max);
  }
}
