// TC: O(n)
// SC: O(n)
type TreeNode = {
    val: number
    left: TreeNode | null
    right: TreeNode | null
}
function isValidBST(root: TreeNode | null): boolean {
        
    function dfs(node: TreeNode | null, low: number, high: number): boolean {
        if(!node) {
            return true;
        }

        if(node.val <= low || node.val >= high) {
            return false;
        }

        return dfs(node.left, low, node.val) && dfs(node.right, node.val, high)
    }

    return dfs(root, -Infinity, Infinity);
};
