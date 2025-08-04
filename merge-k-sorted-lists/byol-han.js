/**
 * https://leetcode.com/problems/merge-k-sorted-lists/description/
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode[]} lists
 * @return {ListNode}
 */
var mergeKLists = function (lists) {
  if (lists.length === 0) {
    return null;
  }

  while (lists.length > 1) {
    const merged = [];
    const size = lists.length;

    for (let i = 0; i < size; i += 2) {
      const l1 = lists[i];
      const l2 = i + 1 < lists.length ? lists[i + 1] : null;
      merged.push(mergeLists(l1, l2));
    }

    lists = merged;
  }

  return lists[0];
};

function mergeLists(l1, l2) {
  const head = new ListNode(0);
  let cur = head;
  while (l1 !== null && l2 !== null) {
    if (l1.val < l2.val) {
      cur.next = l1;
      l1 = l1.next;
    } else {
      cur.next = l2;
      l2 = l2.next;
    }
    cur = cur.next;
  }
  cur.next = l1 === null ? l2 : l1;
  return head.next;
}
