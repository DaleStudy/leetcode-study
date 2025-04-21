/**
 * Definition for singly-linked list.
 * class ListNode {
 *     val: number
 *     next: ListNode | null
 *     constructor(val?: number, next?: ListNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.next = (next===undefined ? null : next)
 *     }
 * }
 */
/**
 * 
 * Time Complexity: O(n + m)
 * Space Complexity: O(n + m)
 */
function mergeTwoLists(list1: ListNode | null, list2: ListNode | null): ListNode | null {
    if (!list1 && !list2) {
        // both lists are empty
        return null
    } else if (!list1) {
        // list1 is empty
        return list2
    } else if (!list2) {
        // list2 is empty
        return list1
    } else if (list1.val <= list2.val) {
        // list1's current node is smaller
        return new ListNode(list1.val, mergeTwoLists(list1.next, list2))
    } else {
        // list2's current node is smaller
        return new ListNode(list2.val, mergeTwoLists(list1, list2.next))
    }
};