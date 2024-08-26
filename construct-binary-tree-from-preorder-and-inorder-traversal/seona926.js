/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {number[]} preorder
 * @param {number[]} inorder
 * @return {TreeNode}
 */
let buildTree = function (preorder, inorder) {
  if (preorder.length === 0 || inorder.length === 0) {
    return null;
  }

  // 중위 순회의 값과 인덱스를 매핑하는 Map 생성
  const inorderIndexMap = new Map();
  inorder.forEach((value, index) => {
    inorderIndexMap.set(value, index);
  });

  // 재귀적 트리 구성 함수
  function build(preStart, preEnd, inStart, inEnd) {
    if (preStart > preEnd || inStart > inEnd) {
      return null;
    }

    // 전위순회 배열에서 루트 노드를 얻기
    const rootVal = preorder[preStart];
    const root = new TreeNode(rootVal);

    // 중위순회 배열에서 루트 노드의 인덱스 찾기
    const rootIndexInInorder = inorderIndexMap.get(rootVal);

    // 왼쪽 서브트리 크기 계산
    const leftSize = rootIndexInInorder - inStart;

    // 재귀적으로 왼쪽과 오른쪽 서브트리를 생성
    root.left = build(
      preStart + 1,
      preStart + leftSize,
      inStart,
      rootIndexInInorder - 1
    );
    root.right = build(
      preStart + leftSize + 1,
      preEnd,
      rootIndexInInorder + 1,
      inEnd
    );

    return root;
  }

  return build(0, preorder.length - 1, 0, inorder.length - 1);
};

/*
  1. 시간복잡도: O(n)
    - 트리의 모든 노드를 한 번씩 처리해야함
  2. 공간복잡도: O(n)
    - map 저장공간, 재귀호출 스택, 트리노드 저장공간 -> O(n)
*/
