/**
 * @description
 * bfs, dfs와 같은 순회 방법과 treeNode 구조에 child가 아닌 parent라는 속성을 부여해 부모찾기를 아이디어로 접근
 * 하지만 모든 노드를 순회해야하고 p와 q가 속한지점과 둘이 포함하는 관계인지를 중점으로 문제에 접근함
 * 그 결과 postOrder를 생각하게 되어 문제 풀이
 *
 * n = length of total treeNode
 * time complexity: O(n)
 * space complexity: O(n)
 */
var lowestCommonAncestor = function (root, p, q) {
  let answer = null;

  const postOrder = (tree) => {
    if (tree === null) return [false, false];

    const [hasLeftP, hasLeftQ] = postOrder(tree.left);
    const [hasRightP, hasRightQ] = postOrder(tree.right);

    const hasP = hasLeftP || hasRightP || tree.val === p.val;
    const hasQ = hasLeftQ || hasRightQ || tree.val === q.val;

    if (hasP && hasQ && answer === null) answer = tree;

    return [hasP, hasQ];
  };

  postOrder(root);

  return answer;
};
