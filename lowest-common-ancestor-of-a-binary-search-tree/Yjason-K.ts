/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     val: number
 *     left: TreeNode | null
 *     right: TreeNode | null
 *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.left = (left===undefined ? null : left)
 *         this.right = (right===undefined ? null : right)
 *     }
 * }
 */

/**
 * 이진 탐색 트리(BST)에서 두 노드의 최소 공통 조상을 찾는 함수
 *
 * @param {TreeNode | null} root - 이진 탐색 트리의 루트 노드
 * @param {TreeNode | null} p - 비교할 첫 번째 노드
 * @param {TreeNode | null} q - 비교할 두 번째 노드
 * @returns {TreeNode | null} - 두 노드의 최소 공통 조상 (LCA)
 *
 * 시간복잡도: O(n)
 *   - 최대 트리 높이 만큼 노드를 탐색해야 함
 *
 * 공간복잡도: O(1)
 *   - 현재 노드를 저장할 공간 필요
 */
function lowestCommonAncestor(root: TreeNode | null, p: TreeNode | null, q: TreeNode | null): TreeNode | null {
  // 현재 노드를 기준으로 p 와 q를 비교
  let curNode = root;
  while (curNode !== null) {
    // p와 q의 현재 값보다 작으면 왼쪽 서브 트리로 이동
    if (p.val < curNode.val && q.val < curNode.val) {
      curNode = curNode.left;
    } else if (p.val > curNode.val && q.val > curNode.val) {
      // p와 q의 현재 값보다 큰 경우 오른쪽 서브 트리로 이동
      curNode = curNode.right;
    } else {
      // 현재 값이 p와 q 사이에 있는경우
      return curNode;
    }
  }
};

