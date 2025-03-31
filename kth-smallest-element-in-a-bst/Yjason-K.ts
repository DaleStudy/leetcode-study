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
 * 이진 탐색 트리(BST)에서 k번째로 작은 값을 찾는 함수
 * @param {TreeNode | null} root - 이진 탐색 트리의 루트 노드
 * @param {number} k - 찾고자 하는 k번째 값
 * @returns {number} - k번째로 작은 값
 *
 * 시간복잡도 : O(n)
 *   - 최악의 경우 트리의 모든 노드를 방문해야 하므로 모든 노드를 탐색
 *
 * 공간복잡도 : O(n)
 *   - dfs 탐색을 하며 최대 O(n) 공간이 사용될 수 있음.
 */
function kthSmallest(root: TreeNode | null, k: number): number {
  // dfs 탐색을 통해 오름차순으로 tree 값들이 저장될 배열
  const values: number[] = [];

  // dfs 탐색 하면 tree 값 추가
  const dfs = (tree: TreeNode | null): void => {
      if (!tree) return;
      
      // 왼쪽 서브트리 탐색
      dfs(tree.left);
      // 현재 노드의 값 저장
      values.push(tree.val);
      // 오른쪽 서브트리 탐색
      dfs(tree.right);
  };

  // 탐색하며 오름차순 정렬
  dfs(root);

  // 정렬된 배열에서 k-1 번째 값 반환
  return values[k - 1];
}

