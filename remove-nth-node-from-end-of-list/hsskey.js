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
var removeNthFromEnd = function(head, n) {
    const dummy = new ListNode(0, head);
    let left = dummy;
    let right = head;

    // advance right pointer n steps ahead
    while (n > 0 && right) {
        right = right.next;
        n--;
    }

    // move both pointers until right reaches the end
    while (right) {
        left = left.next;
        right = right.next;
    }

    // delete the nth node from end
    left.next = left.next.next;

    return dummy.next;
};

