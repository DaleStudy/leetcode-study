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
 * @return {ListNode}
 */
var reverseList = function (head) {
  const stack = [];

  let temp = head;
  while (temp) {
    stack.push(temp.val);
    temp = temp.next;
  }

  if (!stack.length) {
    return null;
  }

  const popped = stack.pop();
  const answer = new ListNode(popped);

  temp = answer;
  while (stack.length > 0) {
    const popped = stack.pop();

    temp.next = new ListNode(popped);
    temp = temp.next;
  }

  return answer;
};
