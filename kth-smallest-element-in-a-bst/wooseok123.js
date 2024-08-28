// TC : O(n log n) | SC : O(n)

let findAllValuesInTree = (root, obj) => {
  obj[root.val] = true;
  if (!root.left && !root.right) return obj;
  if (root.left) findAllValuesInTree(root.left, obj);
  if (root.right) findAllValuesInTree(root.right, obj);

  return obj;
};

var kthSmallest = function (root, k) {
  const obj = findAllValuesInTree(root, {});
  const sortedList = Object.keys(obj)
    .map(Number)
    .sort((a, b) => a - b);

  return sortedList[k - 1];
};
