// Time Complexity: O(n)
// Space Complexity: O(n)

const invertTree = (root) => {
    if (!root) return null;

    const left = invertTree(root.left);
    const right = invertTree(root.right);

    root.left = right;
    root.right = left;

    return root;
};
