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
  const middleNode = findMiddleNode(head);
  let reversedHalf = reverseList(middleNode.next);
  middleNode.next = null;

  let half = head;

  while (reversedHalf) {
    const nextForward = half.next;
    const nextBackward = reversedHalf.next;

    half.next = reversedHalf;
    reversedHalf.next = nextForward;

    reversedHalf = nextBackward;
    half = nextForward;
  }
};
/**
 * Time Complexity: O(n)
 * - Finding the middle node takes O(n).
 * - Reversing the second half takes O(n).
 * - Merging the two halves takes O(n).
 * - Overall, the time complexity is O(n) + O(n) + O(n) = O(n).
 *
 * Space Complexity: O(1)
 * - We only use a constant amount of extra space (pointers),
 *   so the space complexity is O(1).
 */

/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var reverseList = function (head) {
  let currentNode = head;
  let previousNode = null;

  while (currentNode !== null) {
    const nextNode = currentNode.next;

    currentNode.next = previousNode;
    previousNode = currentNode;
    currentNode = nextNode;
  }

  return previousNode;
};

/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var findMiddleNode = function (head) {
  if (!head) return null;

  let slow = head;
  let fast = head;

  while (fast !== null && fast.next !== null) {
    slow = slow.next;
    fast = fast.next.next;
  }

  return slow;
};
