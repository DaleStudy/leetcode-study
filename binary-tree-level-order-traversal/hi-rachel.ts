/**
 * python의 len(queue)는 반복 시작 전에 계산된 값, 즉 고정된 횟수만큼 반복
 * JS의 queue.length는 반복마다 실시간으로 다시 계산하므로 고정 사이즈 size 변수 사용
 */

/**
 * Definition for a binary tree node.
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

function levelOrder(root: TreeNode | null): number[][] {
  if (!root) return [];

  const queue: TreeNode[] = [root];
  const output: number[][] = [];

  while (queue.length > 0) {
    const level: number[] = [];
    for (let node of queue) {
      level.push(node.val);
    }
    output.push(level);
    const size = queue.length;

    for (let i = 0; i < size; i++) {
      const node = queue.shift();
      if (node && node.left) {
        queue.push(node.left);
      }
      if (node && node.right) {
        queue.push(node.right);
      }
    }
  }
  return output;
}
