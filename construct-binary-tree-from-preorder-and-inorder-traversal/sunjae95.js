/**
 * @description
 * time complexity: O(n^2)
 * space complexity: O(n)
 *
 * brainstorming:
 * stack, Drawing a graph
 *
 * strategy:
 * discover the rules
 * leftStack = left create , rightStack = right create
 */
var buildTree = function (preorder, inorder) {
  let answer = null;
  let pointer = 0;

  const leftStack = [];
  const rightStack = [];

  preorder.forEach((val, i) => {
    const node = new TreeNode(val);

    if (i === 0) answer = node;

    const leftLen = leftStack.length;
    const rightLen = rightStack.length;

    if (leftLen && rightLen) {
      if (leftStack[leftLen - 1].left) rightStack[rightLen - 1].right = node;
      else leftStack[leftLen - 1].left = node;
    }
    if (leftLen && !rightLen) leftStack[leftLen - 1].left = node;
    if (!leftLen && rightLen) rightStack[rightLen - 1].right = node;

    leftStack.push(node);

    while (leftStack.length && pointer < inorder.length) {
      if (leftStack[leftStack.length - 1].val !== inorder[pointer]) break;
      rightStack.push(leftStack.pop());
      pointer++;
    }
  });

  return answer;
};
