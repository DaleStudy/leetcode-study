// 시간복잡도: O(n2)
// 공간복잡도: O(n)

var buildTree = function(preorder, inorder) {
    if (!preorder.length || !inorder.length) return null;

    const root = new TreeNode(preorder[0]);
    const mid = inorder.indexOf(root.val);

    root.left = buildTree(preorder.slice(1, mid + 1), inorder.slice(0, mid));
    root.right = buildTree(preorder.slice(mid + 1), inorder.slice(mid + 1));

    return root;
};