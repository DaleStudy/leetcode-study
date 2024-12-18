export class TreeNode {
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
 *
 * 접근 방법
 *  - preorder는 root -> left -> right 순서로 진행되니까 첫 번째 요소가 root노드 값인 점을 이용
 *  - preorder에서 root 노드 값 파악
 *  - inorder(left -> root -> right)에서 head 노드 기준으로 왼쪽 서브 트리, 오른쪽 하위 서브 나누기
 *  - inorder의 왼쪽 트리 노드 개수 활용해서 preorder도 왼쪽, 오른쪽 나누기
 *  - 재귀 함수를 통해서 위 과정 반복하기
 *  - 재귀 함수 기저 조건으로 빈 배열이 들어오는 경우 null처리
 *
 * 시간복잡도 : O(n)
 *  - forEach문으로 map에 값 초기화하니까 O(n)
 *  - dfs가 각 노드 방문해서 노드 개수 n만큼 호출하니까 O(n)
 *
 * 공간복잡도 : O(n)
 *  - indexMap - n이 노드의 개수일 때 map에 노드의 인덱스 모두 저장하니까 O(n)
 *  - 최악의 경우 한쪽으로 치우친 트리의 경우 재귀 호출 O(n)
 *
 */
function buildTree(preorder: number[], inorder: number[]): TreeNode | null {
  // index 미리 map에 저장해두기
  const indexMap = new Map<number, number>();
  inorder.forEach((number, index) => indexMap.set(number, index));

  // preorder index, inorder range를 전달하기
  const dfs = (
    preorderIndex: number,
    inorderStartIndex: number,
    inorderEndIndex: number
  ): TreeNode | null => {
    // 기저 조건
    if (
      !(preorderIndex < preorder.length && inorderStartIndex <= inorderEndIndex)
    )
      return null;

    const rootValue = preorder[preorderIndex];
    const inorderRootIndex = indexMap.get(rootValue) as number;

    // 왼쪽 하위 트리 범위 = inorder 배열의 start부터 root인덱스 이전까지
    const left = dfs(
      preorderIndex + 1,
      inorderStartIndex,
      inorderRootIndex - 1
    );
    // 오른쪽 하위 트리 범위 = root인덱스 다음부터 끝까지
    const right = dfs(
      preorderIndex + 1 + (inorderRootIndex - inorderStartIndex),
      inorderRootIndex + 1,
      inorderEndIndex
    );

    return new TreeNode(rootValue, left, right);
  };

  return dfs(0, 0, inorder.length - 1);
}
