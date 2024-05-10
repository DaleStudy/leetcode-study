/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} list1
 * @param {ListNode} list2
 * @return {ListNode}
 */
var mergeTwoLists = function (list1, list2) {
  // Make sure both or one of the list is null
  if (!list1 && !list2) return null;
  if (!list1) return list2;
  if (!list2) return list1;

  // Create dummy listNode
  let dummy = new ListNode(0);
  let head = dummy;
  // Make head of dummy list by using smaller node from list1 and list2
  while (list1 && list2) {
    if (list1.val <= list2.val) {
      dummy.next = list1;
      list1 = list1.next;
    } else {
      dummy.next = list2;
      list2 = list2.next;
    }
    // After choosing with dummy list, head should be moved next
    dummy = dummy.next;
  }
  // Iterate until both of list head is equal to null
  if (list1 !== null) {
    dummy.next = list1;
  } else {
    dummy.next = list2;
  }
  return head.next;
};

// TC: O(m+n)
// SC: O(1)
