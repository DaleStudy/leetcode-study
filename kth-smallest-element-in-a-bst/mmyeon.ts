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
 *@link https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/
 *
 * 접근 방법 :
 *  - 작은 수대로 정렬해야 하니까 중위순회로 트리 순회
 *  - 왼쪽 모드 끝까지 방문 -> 중간 노드 -> 오른쪽 끝까지 방문 으로 진행
 *  - k번째 노드 체크하기 위해서 노드 방문할 때마다 count 업데이트
 *
 * 시간복잡도 : O(n)
 *  - n = 노드의 개수,
 *  - 최악의 경우 전체 트리 탐색
 *
 * 공간복잡도 : O(n)
 *  - 재귀 호출이 트리 깊이만큼 스택 쌓임.
 * - 기울어진 트리의 경우 O(n)
 */
function kthSmallest(root: TreeNode | null, k: number): number {
  let count = 0;
  let result: number | null = null;

  const inOrderTraverse = (node: TreeNode | null) => {
    if (!node) return null;

    inOrderTraverse(node.left);

    count++;
    if (count === k) {
      result = node.val;
      return;
    }

    inOrderTraverse(node.right);
  };

  inOrderTraverse(root);

  return result!;
}
