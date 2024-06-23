// Time Complexity: O(n)
// Space Complexity: O(n)

var reorderList = function (head) {
  // push all nodes onto a stack.
  let stack = [];
  let current = head;
  while (current) {
    stack.push(current);
    current = current.next;
  }

  // reorder the list.
  let n = stack.length;
  current = head;

  for (let i = 0; i < Math.floor(n / 2); i++) {
    let next = current.next;
    let last = stack.pop();

    current.next = last;
    last.next = next;
    current = next;
  }
  // ensure the last node points to null.
  if (current) current.next = null;
};
