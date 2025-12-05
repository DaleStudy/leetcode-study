/**
 * Definition for a binary tree node.
 */
function TreeNode(val, left, right) {
  this.val = (val === undefined ? 0 : val);
  this.left = (left === undefined ? null : left);
  this.right = (right === undefined ? null : right);
}
/*
  이진 트리(Binary Tree)의 root 노드가 주어졌을 때,
  트리의 최대 깊이(maximum depth)를 반환하는 함수.

  최대 깊이란:
    - 루트(root)에서 가장 먼 리프(leaf) 노드까지
      도달하는 경로에 포함된 "노드의 개수"를 의미함.

  Example 1:
    Input:  root = [3,9,20,null,null,15,7]
    Output: 3
    설명:
      트리 구조는 다음과 같으며,
      가장 깊은 경로(3 → 20 → 15 또는 3 → 20 → 7)의 노드 수는 3.

  Example 2:
    Input:  root = [1,null,2]
    Output: 2
    설명:
      트리 구조는 1 → 2 형태이며 노드 수 2가 최대 깊이.

  Constraints:
    - 트리의 노드 개수: 0 ~ 10^4
    - 노드 값 범위: -100 ~ 100
*/

/**
 * @param {TreeNode} root
 * @return {number}
 */
var maxDepth = function(root) {
    
    if (root === null) return 0;

    const left = maxDepth(root.left);
    const right = maxDepth(root.right);

    return 1 + Math.max(left, right);
};

// example1
const example1 = new TreeNode(
  3,
  new TreeNode(9),
  new TreeNode(20,
    new TreeNode(15),
    new TreeNode(7)
  )
);

// example2
const example2 = new TreeNode(
  1,
  null,
  new TreeNode(2)
);


// maxDepth 함수 결과 출력
console.log("Example 1 maxDepth:", maxDepth(example1));
console.log("Example 2 maxDepth:", maxDepth(example2));

