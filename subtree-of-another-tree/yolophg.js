// Time complexity : O(m * n)
// Space complexity : O(h)

// fuunction to check if two trees are identical.
var isIdentical = function(root1, root2) {
    // if they are both empty, return true.
    if (!root1 && !root2) return true;
    // if either one of them is null and the other is not, return false.
    if (!root1 || !root2) return false;

    // if the right subtrees are identical, return true only if all conditions are met.
    return root1.val === root2.val &&
           isIdentical(root1.left, root2.left) &&
           isIdentical(root1.right, root2.right);
}

var isSubtree = function(root, subRoot) {
    // if the root is empty, return false
    if (!root) return false;
    // if the subtree rooted at subRoot is identical, return true.
    if (isIdentical(root, subRoot)) return true;
    
    // if find the subtree in either the left or right subtree, return true. otherwise, return false.
    return isSubtree(root.left, subRoot) || isSubtree(root.right, subRoot);  
};
