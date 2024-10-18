// class ListNode {
//   val: number;
//   next: ListNode | null;
//   constructor(val?: number, next?: ListNode | null) {
//     this.val = val === undefined ? 0 : val;
//     this.next = next === undefined ? null : next;
//   }
// }

/**
 * https://leetcode.com/problems/merge-k-sorted-lists
 * T.C. O(n * k^2) n: average length of list, k: number of lists
 * S.C. O(1)
 */
function mergeKLists(lists: Array<ListNode | null>): ListNode | null {
  if (lists.length === 0) return null;
  if (lists.length === 1) return lists[0];
  return lists.reduce((acc, cur) => mergeTwoLists(acc, cur), null);

  function mergeTwoLists(list1: ListNode | null, list2: ListNode | null): ListNode | null {
    const head = new ListNode();
    let current = head;

    while (list1 && list2) {
      if (list1.val < list2.val) {
        current.next = list1;
        list1 = list1.next;
      } else {
        current.next = list2;
        list2 = list2.next;
      }
      current = current.next;
    }

    current.next = list1 || list2;

    return head.next;
  }
}
