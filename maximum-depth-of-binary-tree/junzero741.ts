class TreeNode {
    val: number
    left: TreeNode | null
    right: TreeNode | null
    constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
        this.val = (val===undefined ? 0 : val)
        this.left = (left===undefined ? null : left)
        this.right = (right===undefined ? null : right)
    }
}

// TC: O(N)
// SC: O(N)
function maxDepth(root: TreeNode | null): number {
    if(!root) {
        return 0;
    }

    let maxLv = 1;

    function dfs(node: TreeNode, lv: number) {
        if(node.left) {
            dfs(node.left, lv+1)
        }
        if(node.right) {
            dfs(node.right, lv+1)
        }
        maxLv = Math.max(maxLv, lv)
    }


    dfs(root, 1);
    

    return maxLv;

    
};
