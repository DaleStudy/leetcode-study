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
// runtime: 1ms
// memory: 58.22MB

function mergeTwoLists(list1: ListNode | null, list2: ListNode | null): ListNode | null {
    // 1. if next exists
    if(!list1 && !list2)
    return null
    else if(!list1) return list2
    else if(!list2) return list1
    // 2. compare value and link node
    else if(list1.val <= list2.val) return new ListNode(list1.val, mergeTwoLists(list1.next, list2))
    else return new ListNode(list2.val, mergeTwoLists(list1, list2.next))

};
