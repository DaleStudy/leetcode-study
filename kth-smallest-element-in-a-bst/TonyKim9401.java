class Solution {
    private List<Integer> nums = new ArrayList<>();
    public int kthSmallest(TreeNode root, int k) {
        visitTreeNode(root);
        return nums.get(k-1);
    }

    public void visitTreeNode(TreeNode node) {
        if (node == null) return;

        // left < right
        visitTreeNode(node.left);
        nums.add(node.val);
        visitTreeNode(node.right);
    }
    // time complexity: O(n), visit all nodes once
    // space complexity: O(1), used an array list
}