function TreeNode(val, left, right) {
  this.val = val === undefined ? 0 : val;
  this.left = left === undefined ? null : left;
  this.right = right === undefined ? null : right;
}

/**
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {boolean}
 */
var isSameTree = function (p, q) {
  if (!p && !q) {
    return true;
  }

  if (!p || !q || p.val !== q.val) {
    return false;
  }

  return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
};

/**
 * @param {TreeNode} root
 * @param {TreeNode} subRoot
 * @return {boolean}
 */
var isSubtree = function (root, subRoot) {
  if (subRoot === null) {
    return true;
  }

  if (root === null && subRoot !== null) {
    return false;
  }

  if (isSameTree(root, subRoot)) {
    return true;
  }

  return isSubtree(root.left, subRoot) || isSubtree(root.right, subRoot);
};

/**
 * Time Complexity: O(n * m), n: number of nodes in tree `subRoot`, m: number of nodes in tree `root`
 * Reason:
 *   The `isSameTree` function is called at every node of tree `root`.
 *   The time complexity of the `isSameTree` function is O(n) since it compares all nodes of the two trees,
 *   where n is the number of nodes in tree `subRoot`.
 *
 *   Since `isSameTree` is called at every node of tree `root`,
 *   the worst-case time complexity is O(n * m),
 *   where m is the number of nodes in tree `root`.
 */

/**
 * Space Complexity: O(h), where h is the height of tree `root`
 * Reason:
 *   The space complexity is determined by the depth of the recursion stack.
 *   In the worst case, the recursion will reach the maximum depth of tree `root`, which is its height h.
 *   Therefore, the space complexity is O(h).
 */
