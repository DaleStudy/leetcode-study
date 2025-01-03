/**
 * 21. Merge Two Sorted Lists
 * You are given the heads of two sorted linked lists list1 and list2.
 * Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
 * Return the head of the merged linked list.
 *
 * https://leetcode.com/problems/merge-two-sorted-lists/description/
 */

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

// O(n + m) time
// O(n + m) space
function mergeTwoLists(
  list1: ListNode | null,
  list2: ListNode | null
): ListNode | null {
  if (!list1) return list2;
  if (!list2) return list1;

  let mergedListNode: ListNode;
  const val1 = list1.val;
  const val2 = list2.val;
  if (val1 > val2) {
    mergedListNode = new ListNode(val2);
    mergedListNode.next = mergeTwoLists(list1, list2.next);
  } else {
    mergedListNode = new ListNode(val1);
    mergedListNode.next = mergeTwoLists(list1.next, list2);
  }

  return mergedListNode;
}

class ListNode {
  val: number;
  next: ListNode | null;
  constructor(val?: number, next?: ListNode | null) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
  }
}
