var kthSmallest = function (root, k) {
  let arr = [];
  inOrder(root, arr);

  for (let i = 0; i < arr.length; i++) {
    if (i === k - 1) return arr[i];
  }
};

const inOrder = (root, arr) => {
  if (!root) return;

  inOrder(root.left, arr);
  arr.push(root.val);
  inOrder(root.right, arr);
};

// TC: O(n)
// SC: O(n)
