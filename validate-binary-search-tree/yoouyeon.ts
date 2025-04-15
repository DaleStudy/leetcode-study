// [98] Validate Binary Search Tree

/**
 * [Idea]
 * 부모 트리가 BST가 되려면 왼쪽 자식 트리와 오른쪽 자식 트리가 모두 BST여야 한다.
 * 이 때 왼쪽 자식 트리의 범위는 "하한"은 계속 유지되고 (음의 무한대), "상한"은 부모 노드의 값으로 업데이트되고
 * 오른쪽 자식 트리의 범위는 "상한"은 계속 유지되고 (양의 무한대), "하한"은 부모 노드의 값으로 업데이트된다.
 * (다 푼 뒤에 찾아보니 트리 순회 방식 중 전위순회 방식으로 순회하며 확인하는 것이었다.)
 *
 * [Time Complexity]
 * 모든 노드를 한번씩 확인하므로 O(n)
 *
 * [Space Complexity]
 * 재귀적으로 돌아가는 코드이기 때문에 공간 복잡도는 **재귀 콜 스택**에 의해 결정된다!
 * 재귀 호출은 양쪽 트리로 쪼개져서 호출되기 때문에 (왼쪽 다 하고 오른쪽 검사) 콜 스택의 최대 깊이는 트리의 최대 깊이가 된다.
 * 최악의 경우 (왼쪽이나 오른쪽 노드만 있는 연결 리스트 형태의 트리) 깊이가 n이 되므로
 * 콜 스택의 깊이가 n이 되어 O(n)
 */

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

function isValidBST(root: TreeNode | null): boolean {
  // 노드가 하나만 있는 경우를 먼저 처리해줬다.
  if (root === null || (root.left === null && root.right === null)) {
    return true;
  }

  function checkSubTree(
    currNode: TreeNode | null,
    min: number,
    max: number
  ): boolean {
    if (currNode === null) {
      return true;
    }
    if (currNode.val <= min || currNode.val >= max) {
      return false;
    }

    return (
      checkSubTree(currNode.left, min, currNode.val) &&
      checkSubTree(currNode.right, currNode.val, max)
    );
  }

  return checkSubTree(root, -Infinity, Infinity);
}
