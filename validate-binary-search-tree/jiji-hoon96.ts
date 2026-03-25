class TreeNode {
	val: number;
	left: TreeNode | null;
	right: TreeNode | null;
	constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
		this.val = val === undefined ? 0 : val;
		this.left = left === undefined ? null : left;
		this.right = right === undefined ? null : right;
	}
}

function isValidBST(root: TreeNode | null): boolean {
	function dfs(node: TreeNode | null, min: number, max: number) {
		if (node === null) return true;

		if (node.val <= min || node.val >= max) {
			return false;
		}

		return dfs(node.left, min, node.val) && dfs(node.right, node.val, max);
	}

	return dfs(root, Number.NEGATIVE_INFINITY, Number.POSITIVE_INFINITY);
}

isValidBST([2, 1, 3]); // true
isValidBST([5, 1, 4, null, null, 3, 6]); // false
