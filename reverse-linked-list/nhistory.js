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

// Declare linked list
function ListNode(val) {
  this.val = val;
  this.next = null;
}

var reverseList = function (head) {
  let prev = null;
  let curr = head;
  let next;

  while (curr !== null) {
    next = curr.next;
    curr.next = prev;
    prev = curr;
    curr = next;
  }
  return prev;
};

// Create liked list nodes
const node1 = new ListNode(1);
const node2 = new ListNode(2);
const node3 = new ListNode(3);
const node4 = new ListNode(4);
const node5 = new ListNode(5);

node1.next = node2;
node2.next = node3;
node3.next = node4;
node4.next = node5;

// Print out linked list
let current = node1;
while (current !== null) {
  console.log(current.val);
  current = current.next;
}

// Reversed linked list
const reversedHead = reverseList(node1);

// Print out reversed linked list
current = reversedHead;
while (current !== null) {
  console.log(current.val);
  current = current.next;
}

// TC: O(n)
// SC: O(1)
