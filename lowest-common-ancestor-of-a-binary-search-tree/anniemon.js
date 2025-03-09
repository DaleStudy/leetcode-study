/**
 * 시간 복잡도: 트리의 한쪽 경로를 선택하면서 탐색하므로, 트리의 높이가 h면 O(h)
 * 공간 복잡도: 재귀 호출 스택의 깊이는 균형 잡힌 트리의 경우 O(logn), 편향된 트리는 O(n) ==> O(h)
 */
/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {TreeNode}
 */
var lowestCommonAncestor = function(root, p, q) {
  const dfs = (node, p, q) => {
    if(node.val > p.val && node.val > q.val) {
        return dfs(node.left, p, q);
    }
    if(node.val < p.val && node.val < q.val) {
        return dfs(node.right, p, q);
    }
    return node;
  }
  return dfs(root, p, q);
};

