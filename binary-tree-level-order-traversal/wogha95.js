/**
 * 2차
 * 각 level의 node 수만큼 끊어서 순회하기
 *
 * TC: O(N)
 * SC: O(N)
 * N: total of nodes
 */

/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number[][]}
 */
var levelOrder = function (root) {
  if (!root) {
    return [];
  }

  const result = [];
  const queue = [root];

  while (queue.length > 0) {
    const level = queue.length;
    const currentLevelValList = [];

    for (let i = 0; i < level; i++) {
      const current = queue.shift();

      currentLevelValList.push(current.val);

      if (current.left) {
        queue.push(current.left);
      }

      if (current.right) {
        queue.push(current.right);
      }
    }

    result.push(currentLevelValList);
  }

  return result;
};

/**
 * 1차
 * level과 노드를 queue에 추가해서 정답만들기
 *
 * TC: O(N)
 * SC: O(N)
 * N: total of nodes
 */

/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number[][]}
 */
var levelOrder = function (root) {
  const result = [];

  const queue = [
    {
      level: 0,
      current: root,
    },
  ];

  while (queue.length > 0) {
    const { level, current } = queue.shift();

    if (!current) {
      continue;
    }

    if (result[level]) {
      result[level].push(current.val);
    } else {
      result[level] = [current.val];
    }

    if (current.left) {
      queue.push({
        level: level + 1,
        current: current.left,
      });
    }

    if (current.right) {
      queue.push({
        level: level + 1,
        current: current.right,
      });
    }
  }

  return result;
};
