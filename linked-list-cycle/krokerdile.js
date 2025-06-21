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
var hasCycle = function(head) {
    let list = new Set();
    while (head != null) {
        if (list.has(head))
            return true;
        list.add(head);
        head = head.next;
    }

    return false;
};
