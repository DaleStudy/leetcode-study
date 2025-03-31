/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/**
 * @param {ListNode} head
 * @return {boolean}
 */

// Time Complexity: O(n)
// Space Complexity: O(1)

// - In the worst case, we might traverse the entire linked list, but because the fast pointer moves at twice the speed of the slow pointer, they will meet within O(N) steps if a cycle exists.
// - If there is no cycle, the fast pointer reaches the end in O(N) steps.
// - Only two pointers (slow and fast) are used, which require O(1) extra space.
// - No additional data structures (like arrays or hash sets) are used.

var hasCycle = function (head) {
  // If there is a cycle in the linked list, Floyd's Tortoise and Hare algorithm guarantees
  // that the fast and slow pointers will eventually meet.
  let fast = head;
  let slow = head;

  while (fast && fast.next) {
    slow = slow.next; // Move slow pointer one step.
    fast = fast.next.next; // Move fast pointer two steps.

    if (slow === fast) {
      return true; // Cycle detected.
    }
  }

  return false;
};

