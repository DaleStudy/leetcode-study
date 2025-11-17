/**
 * Definition for a binary tree node.
 * class TreeNode {
 *   int val;
 *   TreeNode? left;
 *   TreeNode? right;
 *   TreeNode([this.val = 0, this.left, this.right]);
 * }
 */
class Solution {
  TreeNode? buildTree(List<int> preorder, List<int> inorder) {
    int i = 1, j = 0;
    final root = TreeNode(preorder[0]);
    final stack = [root]; // T(n) = S(n) = O(n)
    while (i != preorder.length) {
        var u = stack.last;
        if (u.val != inorder[j]) {
            u.left = TreeNode(preorder[i++]);
            stack.add(u.left!);
            continue;
        }
        while (! stack.isEmpty && stack.last.val == inorder[j]) {
            u = stack.removeLast();
            j++;
        }
        u.right = TreeNode(preorder[i++]);
        stack.add(u.right!);
    }
    return root;
  }
}
