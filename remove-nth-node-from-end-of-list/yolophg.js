// Time Complexity: O(n)
// Space Complexity: O(1)

var removeNthFromEnd = function (head, n) {
  // calculate the length of the linked list.
  let length = 0;
  let current = head;
  while (current !== null) {
    length++;
    current = current.next;
  }

  // determine the position to remove from the start.
  let removeIndex = length - n;

  // if the node to be removed is the head, return the next node.
  if (removeIndex === 0) {
    return head.next;
  }

  // traverse to the node just before the node to be removed.
  current = head;
  for (let i = 0; i < removeIndex - 1; i++) {
    current = current.next;
  }

  // remove the nth node from the end.
  current.next = current.next.next;

  // return the modified list.
  return head;
};
