// class TreeNode {
//     val: number
//     left: TreeNode | null
//     right: TreeNode | null
//     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
//         this.val = (val===undefined ? 0 : val)
//         this.left = (left===undefined ? null : left)
//         this.right = (right===undefined ? null : right)
//     }
// }

/**
 * 전위 순회(preorder)와 중위 순회(inorder) 배열을 이용해 이진 트리를 재구성하는 함수.
 *
 * @param {number[]} preorder - 트리의 전위 순회 배열 (루트 → 왼쪽 → 오른쪽 순서).
 * @param {number[]} inorder - 트리의 중위 순회 배열 (왼쪽 → 루트 → 오른쪽 순서).
 * @returns {TreeNode | null} - 재구성된 이진 트리의 루트 노드, 만약 트리가 비어있다면 null.
 *
 * 시간 복잡도: O(n)
 * - 각 노드를 한 번씩 처리함.
 *
 * 공간 복잡도: O(n)
 * - 재귀 호출 스택과 중위 순회 값-인덱스 해시맵 저장 공간 포함.
 */
function buildTree(preorder: number[], inorder: number[]): TreeNode | null {
  // 중위 순회 배열의 각 값과 해당 인덱스를 저장
  const inorderIndexMap = new Map<number, number>();
  inorder.forEach((value, index) => inorderIndexMap.set(value, index));

  // 처리할 노드의 인덱스를 추적
  let preorderIndex = 0;

  // 재귀적으로 서브트리를 재구성하는 함수
  const helper = (left: number, right: number): TreeNode | null => {
      // 현재 서브트리의 범위가 유효하지 않은 경우
      if (left > right) return null;

      // 전위 순회 배열에서 현재 노드 값을 가져와 루트로 사용하고 인덱스 증가
      const rootVal = preorder[preorderIndex++];
      // 새로운 TreeNode 객체 생성
      const root = new TreeNode(rootVal);

      // 해시맵에서 현재 루트 값의 인덱스를 찾아 중위 순회 배열 내에서의 위치 확인
      const rootIndex = inorderIndexMap.get(rootVal)!;

      // 중위 순회 배열에서 왼쪽 서브트리 범위 (left ~ rootIndex - 1)를 재귀 호출로 구성
      root.left = helper(left, rootIndex - 1);
      // 중위 순회 배열에서 오른쪽 서브트리 범위 (rootIndex + 1 ~ right)를 재귀 호출로 구성
      root.right = helper(rootIndex + 1, right);

      // 현재 서브트리의 루트 노드를 반환
      return root;
  };

  // 전체 트리를 재구성하기 위해 중위 순회 배열의 전체 범위(0 ~ inorder.length - 1)를 헬퍼 함수에 전달
  return helper(0, inorder.length - 1);
}

