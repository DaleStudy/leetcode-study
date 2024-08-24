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

/**
 * preorder: [root, left, right]
 * inorder: [left, root, right]
 * preorder의 첫번째 값은 root이다. (1. 현재 root 찾기)
 * 모든 node의 val는 unique하기 때문에 이 값을 기준으로 inorder에서 root의 위치를 찾을 수 있다.
 *
 * inorder에서 root의 위치를 찾으면, root를 기준으로 왼쪽은 left subtree, 오른쪽은 right subtree이다. (2. left subtree, right subtree 구분)
 * inorder: [...left, root, ...right]
 * root값은 이미 찾았기 때문에 shift로 제거한다.
 *
 * 남은 preorder에서 첫번째 값은 left subtree의 root이다. (3. left subtree 구성)
 * preorder에서 하나씩 shift하면서 왼쪽 트리를 먼저 구성한다.
 * preorder에서 첫번째 값이 왼쪽 subtree의 root이다. (1. 현재 root 찾기)
 *  inorder에서 root의 위치를 찾아서 왼쪽 subtree를 구성한다. (2. left subtree, right subtree 구분) (3. left subtree 구성)
 * root 기준 왼쪽 subtree 구성이 끝나면 오른쪽 subtree를 구성한다.
 * 위 과정을 재귀적으로 반복하면, 전체 트리를 구성할 수 있다. (1-3 과정 반복)
 */
function buildTree(preorder: number[], inorder: number[]): TreeNode | null {
  // build 함수가 각 노드마다 호출됨(N) * 각 노드마다 shift, indexOf 수행(N) = O(N^2)
  function build(preorder, inorder) {
    if (inorder.length) {
      // TC: O(N)
      const idx = inorder.indexOf(preorder.shift());
      const root = new TreeNode(inorder[idx]);

      root.left = build(preorder, inorder.slice(0, idx));
      root.right = build(preorder, inorder.slice(idx + 1));

      return root;
    }
    return null;
  }

  return build(preorder, inorder);
}

// TC: O(N^2)
// SC: O(N^2)
