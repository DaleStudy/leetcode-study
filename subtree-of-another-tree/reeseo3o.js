// Time Complexity: O(n*m)
// Space Complexity: O(n+m)

const isSubtree = (root, subRoot) => {
    const isSame = (a, b) => {
      if (!a && !b) return true;
      if (!a || !b) return false;
      if (a.val !== b.val) return false;
      return isSame(a.left, b.left) && isSame(a.right, b.right);
    };
  
    if (!root) return false;
    return (
      isSame(root, subRoot) ||
      isSubtree(root.left, subRoot) ||
      isSubtree(root.right, subRoot)
    );
  };
  