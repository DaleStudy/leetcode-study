class ListNode {
  val: number;
  next: ListNode | null;
  constructor(val?: number, next?: ListNode | null) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
  }
}

function mergeTwoLists(
  list1: ListNode | null,
  list2: ListNode | null
): ListNode | null {
  const dummy = new ListNode();
  let current = dummy;

  const addNode = (val: number) => {
    current.next = new ListNode(val);
    current = current.next;
  };

  while (list1 !== null && list2 !== null) {
    if (list1.val < list2.val) {
      addNode(list1.val);
      list1 = list1.next;
    } else if (list1.val > list2.val) {
      addNode(list2.val);
      list2 = list2.next;
    } else {
      addNode(list1.val);
      addNode(list2.val);
      list1 = list1.next;
      list2 = list2.next;
    }
  }

  current.next = list1 !== null ? list1 : list2;
  return dummy.next;
};
