var invertTree = function (root) {
  if (root === null) return null;

  let queue = [root];

  while (queue.length > 0) {
    let node = queue.shift();

    // 왼쪽과 오른쪽 자식을 교환
    [node.left, node.right] = [node.right, node.left];

    if (node.left) queue.push(node.left);
    if (node.right) queue.push(node.right);
  }

  return root;
};
