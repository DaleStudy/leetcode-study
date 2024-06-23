/**
 * time: O(N)
 * space: O(N)
 */
class Solution {

    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        int curVal = root.val;
        int pVal = p.val;
        int qVal = q.val;

        if (pVal > curVal && qVal > curVal) {
            return lowestCommonAncestor(root.right, p, q);
        } else if (pVal < curVal && qVal < curVal) {
            return lowestCommonAncestor(root.left, p, q);
        } else {
            return root;
        }
    }
}
