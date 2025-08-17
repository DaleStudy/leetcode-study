var maxDepth = function (root) {
  let res = 0;

  if (!root) return res; // root 자체가 없을 경우만 0

  function check(node, depth) {
    if (!node.left && !node.right) {
      res = Math.max(res, depth);
      return;
    }

    if (node.left) {
      check(node.left, depth + 1);
    }
    if (node.right) {
      check(node.right, depth + 1);
    }
  }

  check(root, 1); // 루트부터 시작
  return res;
};
