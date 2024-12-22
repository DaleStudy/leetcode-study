/**
 * 시간 복잡도:
 *   preIdx를 이용하여 중위 순회 배열에서 루트 노드를 기준으로 왼쪽 서브 트리와 오른쪽 서브 트리를 탐색.
 *   각 서브 트리를 재귀적으로 생성하며 모든 노드를 한 번씩 순회하므로, 시간 복잡도는 O(n)
 * 공간 복잡도:
 *   중위 순회 배열의 길이만큼 맵을 생성하므로, 공간 복잡도는 O(n)
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
 * @param {number[]} preorder
 * @param {number[]} inorder
 * @return {TreeNode}
 */
var buildTree = function(preorder, inorder) {
  let preIdx = 0;
  const inorderMap = new Map(inorder.map((e, i) => [e, i]))

  const dfs = (l, r) => {
      if(l > r) {
          return null;
      }
      let root = preorder[preIdx];
      preIdx++;

      let rootIdx = inorderMap.get(root);

      const node = new TreeNode(root);
      node.left = dfs(l, rootIdx - 1);
      node.right = dfs(rootIdx + 1, r);
      return node;
  }
  return dfs(0, inorder.length - 1)
};
