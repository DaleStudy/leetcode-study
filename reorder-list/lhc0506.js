/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {void} Do not return anything, modify head in-place instead.
 */
var reorderList = function(head) {
  const nodes = {};
  let currentNode = head;
  let i = 0;
  while (currentNode) {
      nodes[i] = currentNode;
      currentNode = currentNode.next;
      i++;
  }

  i--;

  for (let j = 0; j < (i / 2); j++) {
      nodes[j].next = nodes[i - j];
      nodes[i - j].next = nodes[j + 1];
      console.log(j)
  }

  nodes[Math.ceil(i / 2)].next = null;
};

// 시간 복잡도: O(n)
// 공간 복잡도: O(n)
