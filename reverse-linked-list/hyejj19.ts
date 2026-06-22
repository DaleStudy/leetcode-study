/*
time complexity : O(n)
space complexity : O(1)
*/
function reverseList(head: ListNode | null): ListNode | null {
  let prev = null;
  let cur = head;
  let next = null;

  while (cur !== null) {
    next = cur.next;
    cur.next = prev;
    prev = cur;
    cur = next;
  }

  return prev;
}
