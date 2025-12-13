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

function mergeTwoLists(list1: ListNode | null, list2: ListNode | null): ListNode | null {
  if (!list1 || !list2) {
    return list1 ?? list2;
  }
  function merge(node1: ListNode | null, node2: ListNode | null) {
    if (!node1 || !node2) {
      return node1 ?? node2;
    }
    if (node1.val < node2.val) {
      node1.next = merge(node1.next, node2);
    }
    if (node1.val >= node2.val) {
      node2.next = merge(node1, node2.next);
    }

    return node1.val < node2.val ? node1 : node2;
  }
  return merge(list1, list2);
}

class ListNode {
  val: number;
  next: ListNode | null;
  constructor(val?: number, next?: ListNode | null) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
  }
}
