// Time complexity: O(n)
// Space complexity: O(n)

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
 * @return {number}
 */
var maxPathSum = function (root) {
  let answer = Number.MIN_SAFE_INTEGER;

  const dfs = (current) => {
    const candidates = [current.val];

    if (current.left) {
      dfs(current.left);
      candidates.push(current.left.val + current.val);
    }

    if (current.right) {
      dfs(current.right);
      candidates.push(current.right.val + current.val);
    }

    // 현재 노드가 루트일 경우
    if (current.left && current.right) {
      answer = Math.max(
        answer,
        current.left.val + current.right.val + current.val
      );
    }

    current.val = Math.max(...candidates);
    answer = Math.max(answer, current.val);
  };

  dfs(root);

  return answer;
};
