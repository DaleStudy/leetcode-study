/**
 * [Idea]
 * preorder는 val -> left -> right
 * inorder는 left -> val -> right
 * 따라서 preorder의 val을 기준으로 inorder 배열을 왼, 오로 나누면 val의 왼쪽 트리, 오른쪽 트리 구조가 된다.
 *
 * node.val = preorder[i]
 * const leftAndRight = inorder.split(preorder[0])
 * node.left = leftAndRight[0]
 * node.right = leftAndRight[1]
 *
 * 구현이 안되어 코드 참고 ...
 * 직접 배열을 나누지 않고, val의 인덱스를 찾아 그 값을 기준으로 slice된 배열을 재귀적으로 buildTree에 넣는다.
 *
 */

var buildTree = function (preorder, inorder) {
  if (preorder.length === 0 || inorder.length === 0) {
    return null;
  }
  const root = new TreeNode(preorder[0]);
  const rootIndex = inorder.indexOf(root.val);
  root.left = buildTree(
    preorder.slice(1, rootIndex + 1),
    inorder.slice(0, rootIndex)
  );
  root.right = buildTree(
    preorder.slice(rootIndex + 1, preorder.length),
    inorder.slice(rootIndex + 1, inorder.length)
  );
  return root;
};
