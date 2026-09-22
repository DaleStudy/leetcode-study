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

// TC: O(n + m) / SC: O(1)
var mergeTwoLists = function (list1, list2) {
  let mergeHead = null;
  let mergePointer = null;

  let head1 = list1;
  let head2 = list2;

  const mergeNode = node => {
    const temp = node.next;
    if (!mergeHead) {
      mergeHead = node;
      mergePointer = node;
    } else {
      mergePointer.next = node;
      mergePointer = mergePointer.next;
    }
    return temp;
  };

  while (head1 && head2) {
    if (head1.val <= head2.val) {
      head1 = mergeNode(head1);
    } else {
      head2 = mergeNode(head2);
    }
  }

  if (head1) mergeNode(head1);
  if (head2) mergeNode(head2);

  return mergeHead;
};
