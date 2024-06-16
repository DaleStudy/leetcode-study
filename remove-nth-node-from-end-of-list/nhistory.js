var removeNthFromEnd = function (head, n) {
  // Edge case: If the list is empty
  if (!head) return null;

  // Create a dummy node that points to the head
  let dummy = new ListNode(0);
  dummy.next = head;
  let length = 0,
    curr = head;

  // Calculate the length of the list
  while (curr) {
    length++;
    curr = curr.next;
  }

  // Find the length-n node from the beginning
  length = length - n;
  curr = dummy;
  while (length > 0) {
    length--;
    curr = curr.next;
  }

  // Skip the desired node
  curr.next = curr.next.next;

  // Return the head, which may be a new head if we removed the first node
  return dummy.next;
};

// TC: O(n)
// SC: O(1)
