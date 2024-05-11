var invertTree = function(root) {
    if (!root) return null;
    
    // swap left and right children.
    let temp = root.left;
    root.left = root.right;
    root.right = temp;
    
    // recursively invert left and right subtrees.
    invertTree(root.left);
    invertTree(root.right);
    
    return root;
};

// Time complexity : O(n)
// Space complexity : O(n)
