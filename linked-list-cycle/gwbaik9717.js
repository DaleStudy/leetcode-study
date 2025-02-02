// Time complexity: O(n)
// Space complexity: O(1)

/**
 * @param {ListNode} head
 * @return {boolean}
 */
var hasCycle = function (head) {
  let turtle = head;
  let rabbit = head;

  while (turtle && rabbit && rabbit.next) {
    turtle = turtle.next;
    rabbit = rabbit.next.next;

    if (turtle === rabbit) {
      return true;
    }
  }

  return false;
};
