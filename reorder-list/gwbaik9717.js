// Time complexity: O(n)
// Space complexity: O(n)

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
var reorderList = function (head) {
  const nodes = [];
  let n = 0;

  {
    let current = head;
    while (current) {
      n++;
      nodes.push(current);
      current = current.next;
    }
  }

  const answer = head;

  {
    let current = answer;
    for (let i = 1; i < n; i++) {
      if (i % 2 !== 0) {
        current.next = nodes.at(n - Math.ceil(i / 2));
      } else {
        current.next = nodes.at(i / 2);
      }

      current = current.next;
    }

    current.next = null;
  }

  return answer;
};
