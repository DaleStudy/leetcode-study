class TreeNode {
  val: number;
  left: TreeNode | null;
  right: TreeNode | null;
  constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
    this.val = val === undefined ? 0 : val;
    this.left = left === undefined ? null : left;
    this.right = right === undefined ? null : right;
  }
}

// 1번풀이
function isValidBST1(root: TreeNode | null): boolean {
  const values: number[] = [];

  // 중위노드 : 왼쪽 자식 -> 부모 노드 -> 오른쪽 자식
  function inorder(node: TreeNode | null) {
    if (!node) return null;
    const { val, left, right } = node;

    inorder(left);
    values.push(val);
    inorder(right);
  }

  inorder(root);

  for (let i = 1; i < values.length; i++) {
    if (values[i] <= values[i - 1]) return false;
  }

  return true;
};

// 2번풀이 (배열 대신 변수 사용)
function isValidBST2(root: TreeNode | null): boolean {
  let prev: number | null = null;
  let isValid = true;

  function inorder(node: TreeNode | null) {
    if (!node || !isValid) return;

    inorder(node.left);

    if (prev !== null && node.val <= prev) {
      isValid = false;
      return;
    }
    prev = node.val;

    inorder(node.right);
  }

  inorder(root);
  return isValid;
};
