// Time complexity: O(n)
// Space complexity: O(1)

/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} n
 * @return {ListNode}
 */
var removeNthFromEnd = function (head, n) {
  const reverse = (head) => {
    let next = null;
    let current = head;

    while (current) {
      const temp = current.next;
      current.next = next;
      next = current;
      current = temp;
    }

    return next;
  };

  // Reverse
  let reversedHead = reverse(head);

  if (n === 1) {
    reversedHead = reversedHead.next;
  } else {
    let prev = null;
    let current = reversedHead;

    for (let i = 1; i < n; i++) {
      prev = current;
      current = current.next;
    }

    prev.next = current.next;
  }

  // Reverse Again
  return reverse(reversedHead);
};
