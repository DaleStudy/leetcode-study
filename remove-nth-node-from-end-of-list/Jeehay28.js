// 🚀 Optimized Approach: Two-Pointer Method (One-Pass)
// ✅ Time Complexity: O(N), where N is the number of nodes
// ✅ Space Complexity: O(1)

/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} n
 * @return {ListNode}
 */
var removeNthFromEnd = function (head, n) {
  let dummy = new ListNode(0, head);
  let fast = dummy;
  let slow = dummy;

  for (let i = 0; i <= n; i++) {
    fast = fast.next;
  }

  while (fast) {
    fast = fast.next;
    slow = slow.next;
  }

  slow.next = slow.next.next;

  return dummy.next;
};

// ✅ Time Complexity: O(N), where N is the number of nodes
// ✅ Space Complexity: O(1)

/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} n
 * @return {ListNode}
 */
// var removeNthFromEnd = function (head, n) {
//   let length = 0;

//   let node = head;

//   // Compute the length of the linked list
//   while (node) {
//     length += 1;
//     node = node.next;
//   }

//   // Create a dummy node pointing to head (helps handle edge cases)
//   let dummy = new ListNode(0, head);
//   node = dummy;

//   // Move to the node just before the one to be removed
//   for (let i = 0; i < length - n; i++) {
//     node = node.next;
//   }

//   // Remove the nth node from the end by updating the next pointer
//   node.next = node.next.next;

//   // Return the modified linked list (excluding the dummy node)
//   return dummy.next;
// };
