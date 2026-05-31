/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */

/**
 * 풀이 1: 재귀 (Recursive)
 * 시간 복잡도: O(n) - 모든 노드를 방문
 * 공간 복잡도: O(n) - 재귀 호출 스택 (최악의 경우 트리 높이만큼)
 *
 * @param {TreeNode} root
 * @return {TreeNode}
 */
const invertTree = (root) => {
  if (!root) return null;

  // 좌우 자식을 재귀적으로 반전하면서 교체
  [root.left, root.right] = [invertTree(root.right), invertTree(root.left)];

  return root;
};

/**
 * 풀이 2: 반복 (Iterative) - 스택 사용
 * 시간 복잡도: O(n) - 모든 노드를 방문
 * 공간 복잡도: O(n) - 스택에 노드 저장
 *
 * @param {TreeNode} root
 * @return {TreeNode}
 */
const invertTreeIterative = (root) => {
  if (!root) return null;

  const stack = [root];

  while (stack.length > 0) {
    const node = stack.pop();

    // 좌우 자식 교체
    [node.left, node.right] = [node.right, node.left];

    // null이 아닌 자식들을 스택에 추가
    if (node.left) stack.push(node.left);
    if (node.right) stack.push(node.right);
  }

  return root;
};
