/**
 * 시간 복잡도: k번째 수가 가장 큰 수일 때는 최악의 경우이며, 모든 노드를 방문하므로 O(n)
 * 공간 복잡도: 재귀 호출 스택의 깊이는 균형 잡힌 트리의 경우 O(logn), 편향된 트리는 O(n)
 */
/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @param {number} k
 * @return {number}
 */
var kthSmallest = function(root, k) {
  let kth;
  let cnt = k;
  
  const dfs = (node) => {
      if (!node) return;
      dfs(node.left);
      cnt--;
      if(cnt ===0) {
          kth = node.val
          return;
      }
      dfs(node.right);
  }
  dfs(root)
  return kth;
}
