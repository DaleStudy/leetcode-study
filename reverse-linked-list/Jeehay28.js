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

// Time Complexity: O(n)
// Space Complexity: O(1)

// The algorithm uses a constant amount of extra space: prev, current, and nextTemp.
// No additional data structures (like arrays or new linked lists) are created.
// Hence, the space complexity is O(1).

var reverseList = function (head) {
  let prev = null;
  let current = head;

  while (current) {
    let nextTemp = current.next;

    current.next = prev;
    console.log(current, prev);

    prev = current;
    console.log(current, prev);
    current = nextTemp;
  }

  return prev; // New head of the reversed list
};

// head = [1,2,3,4,5]
// [1] null
// [1] [1]
// [2,1] [1]
// [2,1] [2,1]
// [3,2,1] [2,1]
// [3,2,1] [3,2,1]
// [4,3,2,1] [3,2,1]
// [4,3,2,1] [4,3,2,1]
// [5,4,3,2,1] [5,4,3,2,1]

// my own approach
// Time Complexity: O(n)
// Space Complexity: O(n)
var reverseList = function (head) {
  if (head === null) {
    return null;
  }

  let current = head;
  let arr = [];
  // console.log(head.val)

  // traverse the linked List - TC: O(n)
  while (current) {
    arr.push(current.val);
    current = current.next;
  }

  // reverse the array - TC: O(n)
  arr = arr.reverse();

  let head1 = new ListNode(arr[0]);
  let current1 = head1;

  // rebuild the linked list - TC: O(n)
  for (let i = 1; i < arr.length; i++) {
    current1.next = new ListNode(arr[i]);
    current1 = current1.next;
  }

  return head1;
};


