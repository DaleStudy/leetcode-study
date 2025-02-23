// Depth-First Search (DFS) with recursion

// 🕒 Time Complexity: O(n) — where n is the number of nodes in the binary tree.
// 🗂️ Space Complexity: O(h) — where h is the height of the tree.
// ⚙️ How It Works (Example Walkthrough):
// For root = [3,9,20,null,null,15,7]:
// maxDepth(root) = Math.max(maxDepth(9), maxDepth(20)) + 1 = Math.max(1, 2) + 1 = 3
// maxDepth(9) = Math.max(maxDepth(null), maxDepth(null)) + 1 = 1
// maxDepth(20) = Math.max(maxDepth(15), maxDepth(7)) + 1 = Math.max(1, 1) + 1 = 2
// maxDepth(15) = Math.max(maxDepth(null), maxDepth(null)) + 1 = 1
// maxDepth(7) = Math.max(maxDepth(null), maxDepth(null)) + 1 = 1
// So the final result: 3

/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = val === undefined ? 0 : val;
 *     this.next = next === undefined ? null : next;
 * }
 */
/**
 * @param {ListNode[]} lists
 * @return {ListNode}
 */

// For maximum depth, the presence of one child doesn't matter much because we are looking for the deepest path from the root to any leaf. 
var maxDepth = function (root) {
    // Base case: if the node is null, the depth is 0
    if (root === null) return 0;

    // Recursively calculate the depth of the left and right subtrees
    let leftDepth = maxDepth(root.left);
    let rightDepth = maxDepth(root.right);

    // Return the maximum of the two depths plus 1 for the current node
    return Math.max(leftDepth, rightDepth) + 1;
};

