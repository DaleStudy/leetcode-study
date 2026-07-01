/**
이진 탐색 트리의 특징은 다음과 같다.
- 부모 노드를 기준으로 left는 부모보다 작은 수
- 부모 노드를 기준으로 right는 부모보다 큰 수
이 문제에서 구하려는 것은 '주어진 트리가 이진 탐색 트리를 만족하는가?'이다
이는 재귀함수를 사용하여 깊이 우선 탐색(DFS)을 통해 해결할 수 있다.
여기서 validate는 'BST'의 특징을 비교하는 함수인데,
validate()는 validate를 반환하면서 깊이 탐색하여 최종 참/거짓을 판별한다.
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
 * @return {boolean}
 */
function isValidBST(root) {
  function validate(p, min, max) {
    if (p === null) return true;

    if (p.val <= min || p.val >= max) return false;

    return validate(p.left, min, p.val) && validate(p.right, p.val, max);
  }

  return validate(root, -Infinity, Infinity);
}
