/**
 * @description
 * time complexity: O(N)
 * space complexity: O(N)
 *
 * brainstorming:
 * 1. BFS, DFS
 * 2. Brute force
 *
 * strategy:
 * inOrder search
 *
 * reason:
 * tree features
 */
var kthSmallest = function (root, k) {
  let answer = 0;

  inOrder(root, (value) => {
    k -= 1;
    if (k > 0) return false;
    if (k === 0) answer = value;
    return true;
  });

  return answer;
};

function inOrder(tree, isEnd) {
  if (tree.left) inOrder(tree.left, isEnd);
  if (isEnd(tree.val)) return;
  if (tree.right) inOrder(tree.right, isEnd);
}
