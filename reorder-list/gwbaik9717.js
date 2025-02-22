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
 * @return {void} Do not return anything, modify head in-place instead.
 */
var reorderList = function (head) {
  // middle 찾기
  let slow = head;
  let fast = slow;

  while (fast && fast.next) {
    fast = fast.next.next;
    slow = slow.next;
  }

  const middle = slow;

  // 후반부 뒤집기 (middle 부터)
  let next = null;
  let current = middle;

  while (current) {
    const temp = current.next;
    current.next = next;
    next = current;
    current = temp;
  }

  // 합치기
  let back = next;
  let reordered = head;

  while (reordered && back) {
    const temp = reordered.next;

    reordered.next = back;
    back = back.next;
    reordered = reordered.next;

    reordered.next = temp;
    reordered = reordered.next;
  }

  if (reordered) {
    reordered.next = null;
  }
};
