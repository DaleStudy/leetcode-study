/**
 *@link https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
 *
 * 접근 방법 :
 *  - BST니까 p,q 노드를 root 노드와 비교해서 탐색 범위 좁히기
 *  - root.val보다 작은 경우 왼쪽 하위 트리 탐색
 *  - root.vale보다 큰 경우 오른쪽 하위 트리 탐색
 *  - 그 외의 경우는 값이 같으니까 root 노드 리턴
 *
 * 시간복잡도 : O(n)
 *  - 균형 잡힌 BST의 경우 O(logn)
 *  - 한쪽으로 치우친 트리의 경우 O(n)
 *
 * 공간복잡도 :  O(n)
 *  - 재귀 호출 스택 크기가 트리 깊이에 비례
 *  - 균형 잡힌 BST의 경우 O(logn)
 *  - 한쪽으로 치우친 트리의 경우 O(n)
 */
class TreeNode {
  val: number;
  left: TreeNode | null;
  right: TreeNode | null;
  constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
    this.val = val === undefined ? 0 : val;
    this.left = left === undefined ? null : left;
    this.right = right === undefined ? null : right;
  }
}

function lowestCommonAncestor(
  root: TreeNode | null,
  p: TreeNode | null,
  q: TreeNode | null
): TreeNode | null {
  if (!root || !p || !q) return null;

  if (p.val < root.val && q.val < root.val)
    return lowestCommonAncestor(root.left, p, q);
  else if (p.val > root.val && q.val > root.val)
    return lowestCommonAncestor(root.right, p, q);
  else return root;
}
