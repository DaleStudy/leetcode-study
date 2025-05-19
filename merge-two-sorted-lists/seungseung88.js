/**
 * 시간 복잡도: O(n + m)
 * 공간 복잡도: O(1)
 */
var mergeTwoLists = function (list1, list2) {
  const dummy = new ListNode();
  node = dummy;

  while (list1 && list2) {
    if (list1.val < list2.val) {
      node.next = list1;
      list1 = list1.next;
    } else {
      node.next = list2;
      list2 = list2.next;
    }
    node = node.next;
  }

  node.next = list1 || list2;

  return dummy.next;
};
