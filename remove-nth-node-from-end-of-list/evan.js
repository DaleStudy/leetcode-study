/**
 * @param {ListNode} head
 * @param {number} n
 * @return {ListNode}
 */
function removeNthFromEnd(head, n) {
  let dummy = new ListNode(0);
  dummy.next = head;
  let first = dummy;
  let second = dummy;

  // Move the first pointer n+1 steps ahead
  for (let i = 0; i <= n; i++) {
    first = first.next;
  }

  // Move both pointers until the first pointer reaches the end
  // Second pointer will be at the (n+1)th node from the end
  while (first !== null) {
    first = first.next;
    second = second.next;
  }

  // Remove the nth node from the end
  second.next = second.next.next;

  return dummy.next;
}

/**
 * Time Complexity: O(n)
 * Space Complexity: O(1)
 */
