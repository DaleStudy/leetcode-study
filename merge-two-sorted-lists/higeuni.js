/**
 * @param {ListNode} list1
 * @param {ListNode} list2
 * @return {ListNode}
 * 
 * complexity
 * time: O(n + m)
 * space: O(1)
 */

var mergeTwoLists = function(list1, list2) {
  let dummy = new ListNode();
  let current = dummy;

  while (list1 !== null && list2 !== null) {
      if (list1.val < list2.val) {
          current.next = list1;
          list1 = list1.next;
      } else {
          current.next = list2;
          list2 = list2.next;
      }
      current = current.next;
  }

  if (list1 !== null) {
      current.next = list1;
  } else if (list2 !== null) {
      current.next = list2;
  }

  return dummy.next;
};

